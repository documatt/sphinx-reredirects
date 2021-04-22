.. |project| replace:: sphinx-reredirects

#########
|project|
#########

.. image:: logo.png
   :align: right

|project| is the extension for `Sphinx documentation <https://https://www.sphinx-doc.org/>`_ projects that handles redirects for moved pages. Based on the its configuration, the extension generates HTML pages with meta refresh redirects to the new page location to prevent 404 errors if you rename or move your documents.

Good URLs are never changing URLs. But if you must, |project| helps you manage redirects with ease and from the single place in project's ``conf.py``.  For example, if you rename document ``start`` to ``intro``, you configure this redirect, the extension generate HTML page ``start.html`` with ``<meta http-equiv="refresh" content="0; url=intro.html">``. |project| supports wildcards and moving to different domain too.

* docs: https://documatt.gitlab.io/sphinx-reredirects
* code: https://gitlab.com/documatt/sphinx-reredirects where issues and contributions are welcome

*****
About
*****

|project| started from the urge to manage redirects for all documents during moving our *Tech writer at work blog* to the new domain https://techwriter.documatt.com.

*****
Legal
*****

Forward Arrow icon by `Icons8 <https://icons8.com/icon/74159/forward-arrow>`_.

|project| is licensed under BSD3.