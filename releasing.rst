How to release new version
##########################

Part 1: Git release
*******************

#. Choose version.

#. Describe new version in ``docs/rn.rst``.

#. Increment version in setup.py.

#. Create commit with message "release <version>".

#. Run local tests

   $ tox

#. Push

   $ git push origin HEAD

#. Wait for CI.

#. If they CI passed, stay on master branch, tag just released commit as "vX.Y.Z"

   $ git tag -a vX.Y.Z
   $ git push origin HEAD

Part 2: PyPI release
********************

#. If no errors so far, build with

   $ tox -e build

   that creates sdist and wheel in dist/.

#. Upload to TestPyPI

   $ tox -e publish

   and go to https://test.pypi.org/project/sphinx-reredirects/<version>/

#. If you are happy with it, upload to PyPI.

   $ tox -e publish -- --repository pypi