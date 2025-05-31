Changelog
#########

1.0.0 (2025-05-31)
******************

A maintenance release with no new features, but with important code clean-up, dependency update, and modernization.

- require Python >= 3.11
- require Sphinx >= 7.4
- change license from BSD3 to MIT
- migrate from pip to uv
- migrate from tox to nox
- migrate from Build/Twine to Flit

0.1.6 (2025-03-22)
******************

- feature: preserve URL fragments in redirects (the ``#foo`` in ``https://example.com/docs#foo``) (`issue #11 <https://github.com/documatt/sphinx-reredirects/issues/11>`_ by `David Ekete <https://github.com/davidekete>`_).
- chore: force lint, format, and test with pre-commit hooks

0.1.5 (2024-07-12)
******************

- feature: check redirect to external URLs for invalid or non-existing addresses with standard linkcheck builder (`issue #3 <https://github.com/documatt/sphinx-reredirects/issues/3>`_ fixed by `Jean Abou Samra <https://github.com/jeanas>`_).
- chore: requires Sphinx 7.1+

0.1.4 (2024-06-21)
******************

- fix ``EncodingWarning: 'encoding' argument not specified`` (`issue #5 <https://github.com/documatt/sphinx-reredirects/issues/5>`_ fixed by `Anderson Bravalheri <https://github.com/abravalheri>`_).

0.1.3 (2023-11-03)
******************

- No new features, maintenance release. Contains only fixed URLs because `the project lives now GitHub <https://github.com/documatt/sphinx-reredirects/>`_.

0.1.2 (2023-05-18)
******************

- be explicit about parallel reads (by `Feanil Patel <https://gitlab.com/documatt/sphinx-reredirects/-/merge_requests/10>`__)
- docs: fix URL in README (by `Angus Hollands <https://gitlab.com/documatt/sphinx-reredirects/-/merge_requests/9>`__ `T <https://twitter.com/agoose77>`__)
- docs: fix name of redirect template option (by `Angus Hollands <https://gitlab.com/documatt/sphinx-reredirects/-/merge_requests/8>`__ `T <https://twitter.com/agoose77>`__)

0.1.1 (2022-06-04)
******************

- add more tests
- add tox.ini
- bugfix failure for non-HTML-based Sphinx builders (by Lynn Root `W <http://roguelynn.com/>`__ `T <https://twitter.com/roguelynn>`__)
- use suffix for redirect HTML file from html_file_suffix config parameter (by Robbert Schreuder Hes `W <https://gitlab.com/mollierobbert>`__)
- add type hints (by Daniël van Noord `W <https://gitlab.com/DanielNoord>`__)
- improve docs with comment that redirects are relative (by Daniël van Noord `W <https://gitlab.com/DanielNoord>`__)
- include LICENCE in sdist

0.0.1 (2021-04-26)
******************

(In Git tagged as v0.1.0.)

- bugfix wildcard/non-wildcard implementation and code clean-up
- migrate README to Sphinx docs
- rewrite Usage article in docs

0.0.0 (2020-09-09)
******************

Initial release.
