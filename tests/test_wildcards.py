from sphinx_reredirects import Reredirects
from unittest.mock import Mock


def test_wildcard_expansion():
    sphinx_mock = Mock()
    sphinx_mock.config = {
            "redirects": {
                "faq/*": "http://new.com/faq/",
                "welcome": "intro.html"
            },
            "redirect_html_template_file": None
        }
    sphinx_mock.env.found_docs = ["faq/one", "faq/two", "intro"]
    actual = Reredirects(sphinx_mock).grab_redirects()
    expected = {
        "faq/one": "http://new.com/faq/",
        "faq/two": "http://new.com/faq/",
        "welcome": "intro.html"
    }

    assert actual == expected
