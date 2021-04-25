# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from datetime import date


# -- Project information -----------------------------------------------------

project = 'sphinx-reredirects'
copyright = f'{date.today().year}, Documatt'
author = 'Matt'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

rst_epilog = f'''
.. |project| replace:: {project}
'''

highlight_language = 'none'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_logo = 'logo.png'

html_theme = 'sphinx_documatt_theme'
html_theme_options = {
    'motto': f'{project} is the extension for <a href="https://www.sphinx-doc.org/">Sphinx documentation</a> projects that handles redirects for moved pages. It generates HTML pages with meta refresh redirects to the new page location to prevent 404 errors if you rename or move your documents.',
    'header_text': project,
    'header_logo_style': 'height: 3em',
    'footer_logo_style': 'height: 3em',
}