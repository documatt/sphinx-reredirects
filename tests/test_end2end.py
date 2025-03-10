import re
from io import StringIO
from string import Template

import pytest
from sphinx.application import Sphinx
from sphinx.errors import ExtensionError

from sphinx_reredirects import REDIRECT_FILE_DEFAULT_TEMPLATE


def _build_redirect_html(to_uri: str) -> str:
    return Template(REDIRECT_FILE_DEFAULT_TEMPLATE).substitute({"to_uri": to_uri})


@pytest.mark.sphinx(
    "html",
    testroot="redirects",
    freshenv=True,
    confoverrides={
        "redirects": {
            "faq/*": "https://new.com/$source.html",
            "*all": "go-to-${source}",
            "setup": "install.html",
            "install/requirements": "https://web.com/docs/requirements.html",
        }
    },
)
def test_ext(app: Sphinx, status, warning):
    app.build()
    status = status.getvalue()

    assert (app.outdir / "faq/one.html").read_text(
        encoding="utf-8"
    ) == _build_redirect_html("https://new.com/faq/one.html")  # noqa: E501

    assert (
        """Overwriting 'faq/one.html' with redirect to 'https://new.com/faq/one.html'."""  # noqa: E501
        in status
    )

    assert (app.outdir / "faq/two.html").read_text(
        encoding="utf-8"
    ) == _build_redirect_html("https://new.com/faq/two.html")  # noqa: E501

    assert (
        """Overwriting 'faq/two.html' with redirect to 'https://new.com/faq/two.html'."""  # noqa: E501
        in status
    )

    assert (app.outdir / "install.html").read_text(
        encoding="utf-8"
    ) == _build_redirect_html("go-to-install")  # noqa: E501

    assert (
        """Overwriting 'install.html' with redirect to 'go-to-install'."""  # noqa: E501
        in status
    )

    assert (app.outdir / "setup.html").read_text(
        encoding="utf-8"
    ) == _build_redirect_html("install.html")  # noqa: E501

    assert """Creating redirect 'setup.html' to 'install.html'.""" in status

    assert (app.outdir / "install/requirements.html").read_text(
        encoding="utf-8"
    ) == _build_redirect_html("https://web.com/docs/requirements.html")  # noqa: E501

    assert (
        """Creating redirect 'install/requirements.html' to 'https://web.com/docs/requirements.html'."""  # noqa: E501
        in status
    )


@pytest.mark.sphinx(
    "dirhtml",
    testroot="dirhtml",
    freshenv=True,
    confoverrides={
        "redirects": {
            "index.html": "/newindex/",
            "index": "http://new.com/index",
            "install": "/installing/trailingslash",
            "install/": "/installing/trailingslash",
            "install/index": "/installing",
            "install/index.html": "/installing.html",
        }
    },
)
def test_dirhtml(app: Sphinx, status, warning):
    app.build()
    status = status.getvalue()

    assert (app.outdir / "index.html").read_text(
        encoding="utf-8"
    ) == _build_redirect_html("http://new.com/index")  # noqa: E501

    assert (
        """Overwriting 'index.html' with redirect to '/newindex/'."""  # noqa: E501
        in status
    )

    assert (
        """Overwriting 'index.html' with redirect to 'http://new.com/index'."""  # noqa: E501
        in status
    )

    assert (app.outdir / "install/index.html").read_text(
        encoding="utf-8"
    ) == _build_redirect_html("/installing.html")  # noqa: E501

    assert (
        """Creating redirect 'install/index.html' to '/installing/trailingslash'."""  # noqa: E501
        in status
    )

    assert (
        """Overwriting 'install/index.html' with redirect to '/installing/trailingslash'."""  # noqa: E501
        in status
    )

    assert (
        """Overwriting 'install/index.html' with redirect to '/installing'."""  # noqa: E501
        in status
    )

    assert (
        """Overwriting 'install/index.html' with redirect to '/installing.html'."""  # noqa: E501
        in status
    )


# Redirect sources starting with a slash are not allowed, use relative URIs
@pytest.mark.sphinx(
    "html",
    testroot="redirects",
    freshenv=True,
    confoverrides={
        "redirects": {
            "/index": "http://new.com/faq/",
        }
    },
)
def test_invalid_uri(app: Sphinx, status, warning):
    with pytest.raises(ExtensionError) as excinfo:
        app.build()

    assert "for event 'html-collect-pages' threw an exception" in str(excinfo.value)  # noqa: E501
    assert any(
        [
            # Newer python versions:
            "exception: '/index.html' is not in the subpath of" in str(excinfo.value),
            # Older python versions:
            "'/index.html' does not start with" in str(excinfo.value),
        ]
    )


@pytest.mark.sphinx("linkcheck", testroot="linkcheck", freshenv=True)
def test_linkcheck(app: Sphinx, status: StringIO, warning: StringIO):
    app.build()

    # strip out ANSI escape sequences
    status_str = re.sub(r"\x1B\[[0-9;]*[ABCDEFGHJKSTfmnsulh]", "", status.getvalue())

    # fmt: off
    assert "(         install: line   -1) ok        https://documatt.com" in status_str
    assert "(         faq/one: line   -1) broken    https://documatt.com/faq/one - 404 Client Error: Not Found for url: https://documatt.com/faq/one" in status_str
    assert "(         faq/two: line   -1) broken    https://documatt.com/faq/two - 404 Client Error: Not Found for url: https://documatt.com/faq/two" in status_str
    assert "(           index: line    6) ok        https://documatt.com/sphinx-reredirects" in status_str
    assert "(           index: line    7) ok        https://github.com/documatt/sphinx-reredirects" in status_str
    # fmt: on
