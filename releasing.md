# How to release new version

1. Choose a version value. git-cliff also calculate new version number based on Git history.

1. Create branch `release/v<version>`.

1. Update `CHANGELOG.md`. Either manually or with git-cliff tool (e.g., `git-cliff --prepend CHANGELOG.md --bump --unreleased`)

1. Fine tune `CHANGELOG.md`. Reorder, fix typos, reword, etc.

1. Set new version to `__version__` variable in `<package>/__init__.py`.

1. Create "release commit" containing changes to `<package>/__init__.py` with message `chore: release v<version>`. Release commit may contain other changes too, like to `CHANGELOG.md` and so on.

1. Create PR for branch. Wait for tests, linters. Do a code review.

1. To publish to Test PyPI `uv run nox -s publish_to_test_pypi`. See https://test.pypi.org/project/sphinx-reredirects/#history.

1. Merge to main branch.

1. To publish to real PyPI `uv run nox -s publish_to_real_pypi`. See https://pypi.org/project/sphinx-reredirects/#history.

1. If successful, tag commit with `v<version>`.
