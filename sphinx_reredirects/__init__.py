import re
from fnmatch import fnmatch
from pathlib import Path
from string import Template
from typing import Dict, Mapping, Optional, Sequence

from sphinx.application import Sphinx
from sphinx.util import logging

OPTION_REDIRECTS = "redirects"
OPTION_REDIRECTS_DEFAULT: Dict[str, str] = {}

OPTION_TEMPLATE_FILE = "redirect_html_template_file"
OPTION_TEMPLATE_FILE_DEFAULT = None

REDIRECT_FILE_DEFAULT_TEMPLATE = '<html><head><meta http-equiv="refresh" content="0; url=${to_uri}"></head></html>'  # noqa: E501

logger = logging.getLogger(__name__)

wildcard_pattern = re.compile(r"[\*\?\[\]]")


def setup(app: Sphinx) -> None:
    """
    Extension setup, called by Sphinx
    """
    app.connect("html-collect-pages", init)
    app.add_config_value(OPTION_REDIRECTS, OPTION_REDIRECTS_DEFAULT, "env")
    app.add_config_value(OPTION_TEMPLATE_FILE, OPTION_TEMPLATE_FILE_DEFAULT, "env")


def init(app: Sphinx) -> Optional[Sequence]:
    if not app.config[OPTION_REDIRECTS]:
        logger.debug("No redirects configured")
        return []

    rr = Reredirects(app)
    to_be_redirected = rr.grab_redirects()
    rr.create_redirects(to_be_redirected)

    # html-collect-pages requires to return iterable of pages to write,
    # we have no additional pages to write
    return []


class Reredirects:
    def __init__(self, app: Sphinx) -> None:
        self.app = app
        self.redirects_option: Dict[str, str] = getattr(app.config, OPTION_REDIRECTS)
        self.template_file_option: str = getattr(app.config, OPTION_TEMPLATE_FILE)

    def grab_redirects(self) -> Mapping[str, str]:
        """Inspect redirects option in conf.py and returns dict mapping \
        docname to target (with expanded placeholder)."""
        # docname-target dict
        to_be_redirected = {}

        # For each source-target redirect pair in conf.py
        for source, target in self.redirects_option.items():
            # no wildcard, append source as-is
            if not self._contains_wildcard(source):
                to_be_redirected[source] = target
                continue

            assert self.app.env

            # wildcarded source, expand to docnames
            expanded_docs = [
                doc for doc in self.app.env.found_docs if fnmatch(doc, source)
            ]

            if not expanded_docs:
                logger.warning(f"No documents match to '{source}' redirect.")
                continue

            for doc in expanded_docs:
                new_target = self._apply_placeholders(doc, target)
                to_be_redirected[doc] = new_target

        return to_be_redirected

    def create_redirects(self, to_be_redirected: Mapping[str, str]) -> None:
        """Create actual redirect file for each pair in passed mapping of \
        docnames to targets."""
        if self.app.config.html_file_suffix is not None:
            suffix = self.app.config.html_file_suffix
        else:
            suffix = ".html"

        for doc, target in to_be_redirected.items():
            redirect_file_abs = Path(self.app.outdir).joinpath(doc).with_suffix(suffix)
            redirect_file_rel = redirect_file_abs.relative_to(self.app.outdir)

            if redirect_file_abs.exists():
                logger.info(
                    f"Creating redirect file '{redirect_file_rel}' "
                    f"pointing to '{target}' that replaces "
                    f"document '{doc}'."
                )
            else:
                logger.info(
                    f"Creating redirect file '{redirect_file_rel}' "
                    f"pointing to '{target}'."
                )

            self._create_redirect_file(redirect_file_abs, target)

    @staticmethod
    def _contains_wildcard(text: str) -> bool:
        """Tells whether passed argument contains wildcard characters."""
        return bool(wildcard_pattern.search(text))

    @staticmethod
    def _apply_placeholders(source: str, target: str) -> str:
        """Expand "source" placeholder in target and return it"""
        return Template(target).substitute({"source": source})

    def _create_redirect_file(self, at_path: Path, to_uri: str) -> None:
        """Actually create a redirect file according to redirect template"""

        content = self._render_redirect_template(to_uri)

        # create any missing parent folders
        at_path.parent.mkdir(parents=True, exist_ok=True)

        at_path.write_text(content)

    def _render_redirect_template(self, to_uri: str) -> str:
        # HTML used as redirect file content
        redirect_template = REDIRECT_FILE_DEFAULT_TEMPLATE
        if self.template_file_option:
            redirect_file_abs = Path(self.app.srcdir, self.template_file_option)
            redirect_template = redirect_file_abs.read_text()

        content = Template(redirect_template).substitute({"to_uri": to_uri})

        return content
