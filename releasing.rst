How to release new version
##########################

Part 1: Git release
*******************

#. Choose version.

   $ export VERSION=0.0.1

#. Describe new version in ``docs/rn.rst``.

#. Create commit with message "release $VERSION".

#. Run local tests

   $ tox

#. Push

   $ git push origin HEAD

#. Wait for CI.

#. If they CI passed, stay on master branch, tag just released commit.

   $ git tag -a $VERSION
   $ git push origin HEAD

Part 2: PyPI release
********************

#. If no errors so far, build with

   $ tox -e release

   that creates sdist and wheel in dist/.

#. Upload to TestPyPI

   $ tox -e publish

   and go to https://....

#. If you are happy with it, upload to PyPI.

   $ tox -e publish -- --repository pypi