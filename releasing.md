# How to release new version

## Part 1: Git release

1. Choose a version value. git-cliff also calculate new version number based on Git history.

1. Create branch `release/v<version>`.

1. Update `CHANGELOG.md`. Either manually or with git-cliff tool (e.g., `git-cliff --prepend CHANGELOG.md --bump --unreleased`)

1. Fine tune `CHANGELOG.md`. Reorder, fix typos, reword, etc.

1. Set new version to `__version__` variable in `<package>/__init__.py`.

1. Create "release commit" containing changes to `<package>/__init__.py` with message `chore: release vX.Y.Z`. Release commit may contain other changes too, like to `CHANGELOG.md` and so on.

1. Create PR for branch. Wait for tests, linters. Do a code review. Merge to main branch.

1. Create tag `vX.Y.Z` on release commit.

   ```sh
   git tag -a vX.Y.Z
   git push origin HEAD
   ```

## Part 2: PyPI release

1. Upload to TestPyPI.

   ```sh
   uv run nox -s publish_to_test_pypi
   ```

   and go to https://test.pypi.org/project/sphinx-reredirects/<version>/

1. If you are happy with it, upload to real PyPI.

   ```sh
   uv run nox -s publish_to_real_pypi
   ```
