##################
sphinx-reredirects
##################

.. image:: https://raw.githubusercontent.com/documatt/sphinx-reredirects/main/logo.png
   :align: right

.. image:: https://github.com/documatt/sphinx-reredirects/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/documatt/sphinx-reredirects/actions/workflows/tests.yml

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/pypi/v/sphinx-reredirects
   :target: https://pypi.org/project/sphinx-reredirects/

sphinx-reredirects is the extension for `Sphinx documentation <https://www.sphinx-doc.org/>`_ projects that handles redirects for moved pages. It generates HTML pages with meta refresh redirects to the new page location to prevent 404 errors if you rename or move your documents.

* docs: https://documatt.com/sphinx-reredirects
* code: https://github.com/documatt/sphinx-reredirects where issues and contributions are welcome

Good URLs are never changing URLs. But if you must, sphinx-reredirects helps you manage redirects with ease and from the single place in project's ``conf.py``.  For example, if you rename document ``start`` to ``intro``, and tell it to sphinx-reredirects, it will generate HTML page ``start.html`` with ``<meta http-equiv="refresh" content="0; url=intro.html">``. The extension supports wildcards and moving to different domain too.

*****
About
*****

sphinx-reredirects started from the urge to manage redirects for all documents during moving our *Tech writer at work blog* to the new address at https://documatt.com/blog/.

*****
Legal
*****

sphinx-reredirects is licensed under BSD3.

Forward Arrow icon by `Icons8 <https://icons8.com>`_.