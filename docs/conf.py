# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "sphinx-reredirects"
author = "Documatt.com, s.r.o. and contributors"
version = "0.1.0"
copyright = f"%Y, {author}"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # builtin
    # "sphinx.ext.todo",
    # 3rd party
    "myst_parser",
    # "sphinx_design",
    # "sphinxcontrib.mermaid",
    "sphinx_reredirects",
    "sphinx_sitemap",
    "sphinx_copybutton",
]

nitpicky = True

highlight_language = "none"

exclude_patterns = [
    # Hide files beginning with a dot
    "[.]*",
    # List remaining to exclude from the build
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

suppress_warnings = ["myst.strikethrough"]


# -- Options for internationalisation ----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalisation

language = "en"
# Due to sphinx-intl issue, we need to explicitly set the locale_dirs to its default value
# https://github.com/sphinx-doc/sphinx-intl/issues/116
locale_dirs = ["locales/"]
gettext_compact = False
translation_progress_classes = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = project

html_baseurl = "https://documatt.com/sphinx-reredirects"
if not html_baseurl.endswith("/"):
    html_baseurl += "/"

html_permalinks_icon = "#"
html_copy_source = False
html_logo = html_favicon = "_static/logo.svg"
html_static_path = ["_static"]
html_extra_path = ["robots.txt"]

html_theme = "sphinx_documattcom_theme"
html_theme_options = {
    "hero_title": project,
    "hero_subtitle": 'The extension for <a href="https://www.sphinx-doc.org/">Sphinx documentation</a> projects that handles redirects for moved pages. It generates HTML pages with client-side redirects to the new page location to prevent 404 errors if you rename or move your documents.',
}

templates_path = ["_templates"]


# -- Options for Markdown ----------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    "attrs_inline",
    "attrs_block",
    "deflist",
    "tasklist",
    "linkify",
    "substitution",
    "html_image",
    "colon_fence",
    "strikethrough",
]

# Auto-generated heading anchors
# Allows
#       See settings's [HOME option](../ref/settings.md#HOME).
myst_heading_anchors = 6

# Linky only those that begin with a schema (http://, etc.). Now `documatt.com` will not be converted to a link.
myst_linkify_fuzzy_links = False


# -- Substitutions ----------------------------------------------------------

myst_substitutions = {
    "project": project,
    "author": author,
    "version": version,
}

rst_epilog = f"""
.. |project| replace:: {project}
.. |author| replace:: {author}
.. |version| replace:: {version}
"""


# -- Options for Mermaid ----------------------------------------------------
# https://pypi.org/project/sphinxcontrib-mermaid/

mermaid_version = "11.0.1"

# -- Options for sitemap ----------------------------------------------------
# https://sphinx-sitemap.readthedocs.io/

# Turn off language alternatives in sitemap
# https://github.com/documatt/sphinx-doc-template/issues/1
sitemap_locales = [None]

# Default is {lang}{version}{link}, but version is not used in URLs in this project
sitemap_url_scheme = "{link}"

sitemap_excludes = [
    "search/",
    "genindex/",
]

# -- Options for reredirects ------------------------------------------------
# https://documatt.com/sphinx-reredirects/
redirects = {
    "install.html": "https://documatt.com/sphinx-reredirects/install/",
    "usage.html": "https://documatt.com/sphinx-reredirects/usage/",
    "faq.html": "https://documatt.com/sphinx-reredirects/faq/",
    "rn.html": "https://documatt.com/sphinx-reredirects/changelog/",
}
