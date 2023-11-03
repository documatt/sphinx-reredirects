##################
sphinx-reredirects
##################

.. image:: logo.png
   :align: right

sphinx-reredirects is the extension for `Sphinx documentation <https://https://www.sphinx-doc.org/>`_ projects that handles redirects for moved pages. It generates HTML pages with meta refresh redirects to the new page location to prevent 404 errors if you rename or move your documents.

* docs: https://documatt.gitlab.io/sphinx-reredirects
* code: https://gitlab.com/documatt/sphinx-reredirects where issues and contributions are welcome

Good URLs are never changing URLs. But if you must, sphinx-reredirects helps you manage redirects with ease and from the single place in project's ``conf.py``.  For example, if you rename document ``start`` to ``intro``, and tell it to sphinx-reredirects, it will generate HTML page ``start.html`` with ``<meta http-equiv="refresh" content="0; url=intro.html">``. The extension supports wildcards and moving to different domain too.

*****
About
*****

sphinx-reredirects started from the urge to manage redirects for all documents during moving our *Tech writer at work blog* to the new domain https://techwriter.documatt.com.

*****
Legal
*****

Forward Arrow icon by `Icons8 <https://icons8.com/icon/74159/forward-arrow>`_.

sphinx-reredirects is licensed under BSD3.