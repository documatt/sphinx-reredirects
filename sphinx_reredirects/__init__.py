import re
from fnmatch import fnmatch
from pathlib import Path
from string import Template

from sphinx.application import Sphinx
from sphinx.util import logging

OPTION_REDIRECTS = "redirects"
OPTION_REDIRECTS_DEFAULT = {}

OPTION_TEMPLATE_FILE = "redirect_html_template_file"
OPTION_TEMPLATE_FILE_DEFAULT = None

REDIRECT_FILE_DEFAULT_TEMPLATE = '<html><head><meta http-equiv="refresh" content="0; url=${to_uri}"></head></html>'     # noqa: E501

logger = logging.getLogger(__name__)

wildcard_pattern = re.compile(r"[\*\?\[\]]")


def setup(app: Sphinx):
    """
    Extension setup, called by Sphinx
    """
    app.connect("build-finished", init)
    app.add_config_value(OPTION_REDIRECTS, OPTION_REDIRECTS_DEFAULT, "env")
    app.add_config_value(OPTION_TEMPLATE_FILE,
                         OPTION_TEMPLATE_FILE_DEFAULT, "env")


def init(app: Sphinx, exception):
    redirects: dict = app.config[OPTION_REDIRECTS]
    template_file: str = app.config[OPTION_TEMPLATE_FILE]

    if not redirects:
        logger.debug('No redirects configured')
        return

    # HTML used as redirect file content
    redirect_template = REDIRECT_FILE_DEFAULT_TEMPLATE
    if template_file:
        redirect_file_abs = Path(app.srcdir, template_file)
        redirect_template = redirect_file_abs.read_text()

    # For each source-target redirect pair in conf.py
    for source, target in redirects.items():
        to_be_redirected = []
        # if wildcarded source, expand pattern to existing docs
        if contains_wildcard(source):
            for doc in app.env.found_docs:
                if fnmatch(doc, source):
                    to_be_redirected.append(doc)
            if not to_be_redirected:
                logger.warning(f"No documents match to '{source}' redirect.")
        else:
            # append source as-is
            to_be_redirected.append(source)

        for doc in to_be_redirected:
            #  apply placeholder, create redirect file
            new_target = apply_placeholders(doc, target)
            redirect_file_abs = Path(app.outdir).joinpath(
                doc).with_suffix(".html")
            redirect_file_rel = redirect_file_abs.relative_to(app.outdir)

            if redirect_file_abs.exists():
                logger.info(f"Creating redirect file '{redirect_file_rel}' "
                            "pointing to '{new_target}' that replaces "
                            "'{doc}'.")
            else:
                logger.info(f"Creating redirect file '{redirect_file_rel}' "
                            "pointing to '{new_target}'.")

            create_redirect_file(
                redirect_template, redirect_file_abs, new_target)


def contains_wildcard(text):
    """Tells whether passed argument contains wildcard characters."""
    return bool(wildcard_pattern.search(text))


def apply_placeholders(source: str, target: str) -> str:
    return Template(target).substitute({"source": source})


def create_redirect_file(template: str, at_path: Path, to_uri: str) -> None:
    content = Template(template).substitute({"to_uri": to_uri})

    # create any missing parent folders
    at_path.parent.mkdir(parents=True, exist_ok=True)

    at_path.write_text(content)
