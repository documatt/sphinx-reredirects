from unittest.mock import Mock

import pytest

from sphinx_reredirects import Reredirects


def test_placeholder1():
    actual = Reredirects._apply_placeholders(
        "features/one", "https://elsewhere/$source.html"
    )
    expected = "https://elsewhere/features/one.html"
    assert actual == expected


def test_placeholder2():
    actual = Reredirects._apply_placeholders(
        "features", "https://elsewhere/$source.html"
    )
    expected = "https://elsewhere/features.html"
    assert actual == expected


def test_no_placeholder():
    actual = Reredirects._apply_placeholders(
        "features", "https://elsewhere/features.html"
    )
    expected = "https://elsewhere/features.html"
    assert actual == expected


@pytest.mark.xfail(
    reason="To be fixed. Reported in https://github.com/documatt/sphinx-reredirects/issues/2"  # noqa: E501
)
def test_source_placeholder_returns_just_matched_part():
    sphinx_mock = Mock()
    sphinx_mock.config = {
        "redirects": {"faq/*": "http://new.com/$source.html"},
        "redirect_html_template_file": None,
    }
    sphinx_mock.env.found_docs = ["faq/one", "faq/two"]

    actual = Reredirects(sphinx_mock).grab_redirects()
    expected = {
        "faq/one": "http://new.com/one.html",
        "faq/two": "http://new.com/two.html",
    }
    assert actual == expected
