Usage
#####

This document explains how to use the |project| extension to manage redirects in your Sphinx documentation. The extension provides flexible options for defining redirects, including support for wildcards and placeholders.

Introduction
************

The extension relies on the ``redirects`` configuration option in ``conf.py``. ``redirects`` option maps a *source* to a *target*.

.. highlight:: python3

::

   redirects = {
        "<source>": "<target>"
   }

By default, ``redirects`` is empty (i.e. generates no redirect files).

*Source* (the key in ``redirects`` map) is a *docname*, i.e. document path without a suffix (an extension). Most Sphinx projects use ``.rst`` as extension. For example, a docname for the file ``index.rst`` is ``index``, for ``agents/intro.rst`` is ``agents/intro``, etc.

Source may be non-existing document or existing document. If source does not exist, |project| creates new redirect .html file. For existing document, document's .html file will be overwritten with redirect file. To select multiple existing documents, a `source wildcards <Wildcard syntax_>`_ can be used.

*Target* (the value in ``redirects`` map) is an URL that will be used in the HTML redirecting file. It may be specified using the placeholder to reuse source docname (see `Target placeholders`_).

Target value must correspond to the output file naming of chosen Sphinx builder. For example, html builder creates ``docname.html``, while dirhtml ``docname/index.html``.

.. important:: The extension works only for HTML-based builders like html and dirhtml. When building to other outputs (linkcheck, latex), it does nothing.

The redirect is relative to the current page. So, if you want to redirect ``guides/index.html`` to ``index.html`` use:

.. highlight:: python3

::

   redirects = {
        "guides/index": "../index.html"
   }

Redirect old documents
**********************

The basic usage is to redirect document you delete or rename to a new file within the same project. For example, if you rename ``setup.rst`` to ``install.rst``::

    redirects = {
        "setup": "install.html",
    }

Newly created ``setup.html`` will contain ``<meta http-equiv="refresh" content="0; url=install.html">``.

Or, if you output to dirhtml, target must be a folder::

    redirects = {
        "setup": "install/",
    }

.. rubric:: Absolute URLs

The target maybe any value. For example, if particular page is now on the different website::

    redirects = {
        "install/requirements": "https://anotherwebsite.com/docs/requirements.html",
    }

It will create ``install`` folder (if it does not exist) and ``requirements.html`` containing ``<meta http-equiv="refresh" content="0; url=https://anotherwebsite.com/docs/requirements.html">``.

Redirect existing documents
***************************

Source (the key in the ``redirects`` option) may be specified with wildcards. If wildcard is used, it means that you want to expand it against existing documents. |project| creates redirect .html file that will overwrite original document's html file.

For example, if all FAQ documents in ``faq/`` folder should be redirected to dedicated forum website, but you don't want to delete them in your documentation::

    redirects = {
        "faq/*": "https://website.com/forum/faq",
    }

Now, html files originally produced by documents in ``faq/`` like ``supported-os.html``, ``licencing.html``, etc., are all replaced with body ``<meta http-equiv="refresh" content="0; url=https://website.com/forum/faq">``

Wildcard syntax
===============

Wildcards for selecting existing source documents know only ``*``, ``?``, ``[seq]`` and ``[!seq]`` patterns.

* ``*`` matches everything, while ``?`` any single character.
* ``[seq]`` matches any character in the seq, ``[!seq]`` any character not in seq.

(If you are curious, matching is using Python3 `fnmatch() <https://docs.python.org/3/library/fnmatch.html>`_.)

.. important:: In other words, for example ``**`` used as "recursive" has no meaning here.

Target placeholders
*******************

Matched document in the source, is available in the target as ``$source`` or ``${source}`` placeholder. Because source notation (a docname) is without suffix, you may need to append ``.html`` or ``/`` suffix after the placeholder.

For example, if all FAQ documents in ``faq/`` folder should be redirected to dedicated forum website with the identical filenames in URL, but you don't want to delete them in your documentation::

    redirects = {
        "faq/*": "https://website.com/forum/faq/$source",
    }

Now, html files originally produced by documents in ``faq/`` like ``supported-os.html``, ``licencing.html``, etc., have replaced bodies like ``<meta http-equiv="refresh" content="0; url=https://website.com/forum/faq/supported-os">``, etc.

Redirect everything
*******************

Occasionally, you have to move complete documentation to a new home. It's easy with wildcard and placeholder::

   redirects = {
       "*": "https://anotherwebsite.com/docs/$source.html"
   }

.. tip:: To help search engines to understand the transfer, update (or set) `html_baseurl <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_baseurl>`_ option to the new website, too.


Checking your redirects
***********************

Sphinx has a linkcheck_ builder for finding broken links in your
documentation.  This extension cooperates with it so that redirects to
external websites will be checked too.

.. _linkcheck: https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.linkcheck.CheckExternalLinksBuilder

.. NOTE:: Checking redirects to another page in the same documentation is not supported yet.

Invoke link checker as usual:

.. code-block:: none

    sphinx-build -M linkcheck source build

The output will contains checked links that appear in the documents itself, but also redirects to external URLs (those with line -1):

.. code-block:: none

    (         install: line   -1) ok        https://documatt.com
    (         faq/two: line   -1) broken    https://documatt.com/faq/two - 404 Client Error: Not Found for url: https://documatt.com/faq/two
    (         faq/one: line   -1) broken    https://documatt.com/faq/one - 404 Client Error: Not Found for url: https://documatt.com/faq/one
    (           index: line    6) ok        https://documatt.com/sphinx-reredirects
    (           index: line    7) ok        https://github.com/documatt/sphinx-reredirects