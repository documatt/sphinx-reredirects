Usage
#####

The extension relies on the ``redirects`` configuration option in ``conf.py``. By default is empty (generates no redirect files). ``redirects`` option is a map of docnames to new targets.

Source (the key in ``redirects`` map) is docname, i.e. document path *without a suffix* (an extension). Most Sphinx projects use ``.rst`` as extension. For example, a docname for the file ``index.rst`` is ``index``, for ``agents/intro.rst`` is ``agents/intro``, etc.

Target (the value in ``redirects`` map) is a URL that will be used in HTML redirecting file. It may be specified using the placeholder to reuse docname in the target (`see bellow <Placeholders_>`_).

Relative URIs
*************

Basic usage is to redirect a document to another document within the same project::

    redirects = {
        "agents/intro": "agents/getting-started.html",
    }

Or, if you output to dirhtml::

    redirects = {
        "agents/*": "agents/getting-started/",
    }

Absolute URIs
*************

However, target URI maybe any value. For example, if particular page is now on the different website::

    redirects = {
        "agents/intro": "https://anotherwebsite.com/docs/agents/intro.html",
    }

Wildcards
*********

Source URI (the key in the ``redirects`` option) may be specified with wildcards.

Wildcards know only ``*``, ``?``, ``[seq]`` and ``[!seq]`` patterns. ``*`` matches everything, while ``?`` any single character. ``[seq]`` matches any character in the seq, ``[!seq]`` any character not in seq.

.. important:: In other words, for example ``**`` used as "recursive" has no meaning here.

Placeholders
************

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

Caveats and limitations
***********************

The |project| extension runs after the Sphinx build has finished. It works by creating files in build output directory (usually ``build/html``, ``_build/html``, etc.). If you instruct |project| to create redirect file at the path of existing HTML file produced by Sphinx, it will be overwritten without warning.