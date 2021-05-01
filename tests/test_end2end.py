import pytest
from sphinx.application import Sphinx


@pytest.mark.sphinx('html',
                    testroot='redirects',
                    freshenv=True,
                    confoverrides={
                        "redirects": {
                            "faq/*":
                            "https://new.com/$source.html",
                            "*all":
                            "go-to-${source}",
                            "setup":
                            "install.html",
                            "install/requirements":
                            "https://web.com/docs/requirements.html"
                        }
                    })
def test_ext(app: Sphinx, status, warning):
    app.build()
    status = status.getvalue()

    assert (app.outdir / 'faq/one.html').read_text(
    ) == '<html><head><meta http-equiv="refresh" content="0; url=https://new.com/faq/one.html"></head></html>'  # noqa: E501

    assert '''Creating redirect file 'faq/one.html' pointing to 'https://new.com/faq/one.html' that replaces document 'faq/one'.'''  # noqa: E501

    assert (app.outdir / 'faq/two.html').read_text(
    ) == '<html><head><meta http-equiv="refresh" content="0; url=https://new.com/faq/two.html"></head></html>'  # noqa: E501

    assert '''Creating redirect file 'faq/two.html' pointing to 'https://new.com/faq/two.html' that replaces document 'faq/two'.''' in status  # noqa: E501

    assert (app.outdir / 'install.html').read_text(
    ) == '<html><head><meta http-equiv="refresh" content="0; url=go-to-install"></head></html>'  # noqa: E501

    assert '''Creating redirect file 'install.html' pointing to 'go-to-install' that replaces document 'install'.''' in status  # noqa: E501

    assert (app.outdir / 'setup.html').read_text(
    ) == '<html><head><meta http-equiv="refresh" content="0; url=install.html"></head></html>'  # noqa: E501

    assert '''Creating redirect file 'setup.html' pointing to 'install.html'.''' in status  # noqa: E501

    assert (app.outdir / 'install/requirements.html').read_text(
    ) == '<html><head><meta http-equiv="refresh" content="0; url=https://web.com/docs/requirements.html"></head></html>'  # noqa: E501

    assert '''Creating redirect file 'install/requirements.html' pointing to 'https://web.com/docs/requirements.html'.''' in status  # noqa: E501
