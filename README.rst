.. |project| replace:: sphinx-reredirects

#########
|project|
#########

.. image:: https://img.icons8.com/wired/64/000000/forward-arrow--v1.png
   :align: right

|project| is the extension for `Sphinx documentation <https://https://www.sphinx-doc.org/>`_ projects that handles redirects for moved pages. Based on the its configuration, the extension generates HTML pages with meta refresh redirects to the new page location to prevent 404 errors if you rename or move your documents.

Good URLs are never changing URLs. But if you must, |project| helps you manage redirects with ease and from the single place in project's ``conf.py``.  For example, if you rename document ``start`` to ``intro``, you configure this redirect, the extension generate HTML page ``start.html`` with ``<meta http-equiv="refresh" content="0; url=intro.html">``. |project| supports wildcards and moving to different domain too.

*******
Install
*******

::

    pip3 install sphinx-reredirects

*****
Setup
*****

Open your ``conf.py`` and append ``sphinx_reredirects`` to the ``extensions`` list::

    extensions = [
        ...
        'sphinx_reredirects'
    ]

*****
Usage
*****

The extension relies on the ``redirects`` configuration option in ``conf.py``. By default is empty (generates no redirect files). ``redirects`` option is a map of docnames to new targets.

Source (the key in ``redirects`` map) is docname, i.e. document path *without a suffix* (an extension). Most Sphinx projects use ``.rst`` as extension. For example, a docname for the file ``index.rst`` is ``index``, for ``agents/intro.rst`` is ``agents/intro``, etc.

Target (the value in ``redirects`` map) is a URL that will be used in HTML redirecting file. It may be specified using the placeholder to reuse docname in the target (`see bellow <Placeholders_>`_).

Relative URIs
=============

Basic usage is to redirect a document to another document within the same project::

    redirects = {
        "agents/intro": "agents/getting-started.html",
    }

Or, if you output to dirhtml::

    redirects = {
        "agents/*": "agents/getting-started/",
    }

Absolute URIs
=============

However, target URI maybe any value. For example, if particular page is now on the different website::

    redirects = {
        "agents/intro": "https://anotherwebsite.com/docs/agents/intro.html",
    }

Wildcards
=========

Source URI (the key in the ``redirects`` option) may be specified with wildcards.

Wildcards know only ``*``, ``?``, ``[seq]`` and ``[!seq]`` patterns. ``*`` matches everything, while ``?`` any single character. ``[seq]`` matches any character in the seq, ``[!seq]`` any character not in seq.

.. important:: In other words, for example ``**`` used as "recursive" has no meaning here.

Placeholders
============

Matched part in the source URI, is available in the target URI as ``$source`` or ``${source}`` placeholder. Because source notation (a docname) is without suffix, you may need to append ``.html`` or ``/`` suffix after the placeholder.

For example, if you move all documents from ``agents/`` to ``operators/`` folder::

    redirects = {
        "agents/*": "operators/$source.html",
    }

Or, if you output to dirhtml::

    redirects = {
        "agents/*": "operators/$source/",
    }

Occasionally, you have to move complete documentation to the new home. It's easy with wildcard and placeholder::

    redirects = {
        "*": ""https://anotherwebsite.com/docs/$source.html"
    }

.. tip:: To help search engines to understand the transfer, update (or set) `html_baseurl <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_baseurl>`_ option to the new website, too.

***********************
Caveats and limitations
***********************

The |project| extension runs after the Sphinx build has finished. It works by creating files in build output directory (usually ``build/html``, ``_build/html``, etc.). If you instruct |project| to create redirect file at the path of existing HTML file produced by Sphinx, it will be overwritten without warning.

***
FAQ
***

Isn't 301 redirects better?
===========================

|project| extension was created for tech writers who can't manage redirects with server-side 301 redirects. Generally, SEO consultants recommend server-side redirects created with ``.htaccess`` and similar files. However, many documentation is hosted as on static website hosting which doesn't support server-side redirects.

However, client-side redirects with meta refresh are okay for search engines, even the most ancient browsers, and users too. Also, it is easier if you can manage redirects in documentation, instead of telling about page URL change to the administrators.

I know better how to write HTML redirect file
=============================================

By default, created HTML redirect files contains ``<html><head><meta http-equiv="refresh" content="0; url=${to_uri}"></head></html>``.

If you want JavaScript redirection instead, wait longer, or whatever, set ``redirect_html_template`` option. This option should points to file inside source dir (directory containing ``conf.py``). For example::

    redirect_html_template = "redirect.html.template"

Actual target URI requested in configuration is available under ``${to_uri}`` placeholder.

Why name "reredirects"?
=======================

Because the name "redirects" is already taken by `another <https://github.com/sphinx-contrib/redirects>`_ extension. Unfortunately, it doesn't fulfil our requirements (the most notable it doesn't support wildcards). These were reasons why we decided to craft new extension.

***************
About and legal
***************

|project| started from the urge to manage redirects for all documents during moving our *Tech writer at work blog* to the new domain https://techwriter.documatt.com.

Feel free to raise issue with support question, found bug, or enhancement.

| Matt from Documatt.com
| https://techwriter.documatt.com

Legal
=====

Forward Arrow icon by `Icons8 <https://icons8.com/icon/74159/forward-arrow>`_.

|project| is licensed under BSD3.
