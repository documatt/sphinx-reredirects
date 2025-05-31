import nox

# *****************************************************************************
# *** Settings ***
# *****************************************************************************

# Speed up builds by reusing virtualenvs
nox.options.reuse_existing_virtualenvs = True

# No default sessions when "nox" is run (explicit is better than implicit)
nox.options.sessions = []

# Massively speed up the build by using uv
nox.options.default_venv_backend = "uv"

SUPPORTED_PYTHONS = ["3.11", "3.12", "3.13"]
SUPPORTED_SPHINX_VERSIONS = [
    # ~= is "compatible operator" allowing for patch version updates
    "~=7.4.0",
    "~=8.0.0",
    "~=8.1.0",
    "~=8.2.0",
]


# *****************************************************************************
# *** Helpers ***
# *****************************************************************************


def install_dependencies(session: nox.Session, *args, **kwargs) -> None:
    """Install dependencies for the session."""
    session.run_install(
        "uv",
        "sync",
        *args,
        **kwargs,
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )


# *****************************************************************************
# *** Nox sessions ***
# *****************************************************************************
# To invoke session(s), use "nox -s <name1>" or "nox -s <name1> <name2>"


@nox.session(python=SUPPORTED_PYTHONS, tags=["test"])
@nox.parametrize("sphinx", SUPPORTED_SPHINX_VERSIONS)
def test(session, sphinx):
    """Run tests with different Python and Sphinx versions."""
    install_dependencies(session, "--only-dev")

    # -U is "upgrade" to ensure installing latest path version
    session.install("-U", f"sphinx{sphinx}")
    session.run("pytest")


@nox.session(tags=["lint"])
def mypy(session: nox.Session) -> None:
    """Run mypy."""
    install_dependencies(session)
    session.run("mypy", "sphinx_reredirects")


@nox.session(tags=["lint"])
def ruff_check(session: nox.Session) -> None:
    """Run Ruff check."""
    install_dependencies(session, "--only-dev")
    session.run("ruff", "check")


@nox.session()
def publish_to_test_pypi(session: nox.Session) -> None:
    """Build and publish the package to test PyPI. You will be asked for token. See `docs/releasing.md` for full instructions."""
    install_dependencies(session, "--only-dev")

    session.run(
        "flit",
        "publish",
        env={
            "FLIT_INDEX_URL": "https://test.pypi.org/legacy/",
            "FLIT_USERNAME": "__token__",
        },
    )


@nox.session()
def publish_to_real_pypi(session: nox.Session) -> None:
    """Build and publish the package to real PyPI. You will be asked for token. See `docs/releasing.md` for full instructions."""
    install_dependencies(session, "--only-dev")

    session.run(
        "flit",
        "publish",
        env={
            "FLIT_INDEX_URL": "https://upload.pypi.org/legacy/",
            "FLIT_USERNAME": "__token__",
        },
    )
