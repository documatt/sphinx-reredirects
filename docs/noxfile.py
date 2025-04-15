import os
from pathlib import Path

import nox

# *****************************************************************************
# *** Settings ***
# *****************************************************************************

INDIR = "."
OUTDIR = "_build"

DEFAULT_SPHINX_OPTS = [
    # Speed up the build by using multiple cores
    "-j",
    "auto",
    # Print traceback
    "-T",
    # Be quiet
    "-q",
]
SPHINX_AUTOBUILD_OPTS = []

DEFAULT_BUILDER = "dirhtml"
BUILDERS = [DEFAULT_BUILDER] + []

DEFAULT_LANGUAGE = "en"
LANGUAGES = [DEFAULT_LANGUAGE] + []

# Speed up builds by reusing virtualenvs
nox.options.reuse_existing_virtualenvs = True

# No default sessions when "nox" is run (explicit is better than implicit)
nox.options.sessions = []

# Massively speed up the build by using uv
nox.options.default_venv_backend = "uv"


# *****************************************************************************
# *** Helpers ***
# *****************************************************************************


def get_outdir_path(builder: str, lang: str) -> str:
    """Constructs the output path."""
    return os.path.join(OUTDIR, builder, lang)


def get_sphinx_opts(lang: str) -> list[str]:
    """Generate a default list of Sphinx options for a given language."""
    return DEFAULT_SPHINX_OPTS + [
        # Set lang
        "-D",
        f"language={lang}",
        # Add the tag for including based on a language
        # https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#including-content-based-on-tags
        "-t",
        f"language_{lang}",
    ]


def get_builder_language(session) -> tuple[str, str]:
    """Get builder and language. Either defaults or from commandline."""
    if session.posargs:
        return session.posargs[0], session.posargs[1]
    else:
        return DEFAULT_BUILDER, DEFAULT_LANGUAGE


def run_sphinx_builder(session, builder, language):
    """Single place for invoking Sphinx builder. Called from all build-related sessions."""
    session.run(
        "sphinx-build",
        "-b",
        builder,
        INDIR,
        get_outdir_path(builder, language),
        *get_sphinx_opts(language),
        # Warning as error
        "-W",
    )


def install_dependencies(session):
    """Install project dependencies (including dev dependencies)."""
    session.run_install(
        "uv", "sync", env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location}
    )


# *****************************************************************************
# *** Nox sessions ***
# *****************************************************************************
# To invoke session(s), use "nox -s <name1>" or "nox -s <name1> <name2>"


@nox.session
@nox.parametrize("builder", BUILDERS)
@nox.parametrize("language", LANGUAGES)
def build_all(session, builder, language):
    """Build documentation for all builders/languages."""
    install_dependencies(session)

    run_sphinx_builder(session, builder, language)


@nox.session
@nox.parametrize("builder", BUILDERS)
def redirect(session, builder):
    """Create a redirect from the root to the default language."""
    Path(OUTDIR, builder, "index.html").write_text(
        f'<html><head><meta http-equiv="refresh" content="0; url={DEFAULT_LANGUAGE}/index.html"></head></html>'
    )


@nox.session
def build(session):
    """Build documentation for a builder/language."""
    install_dependencies(session)

    builder, language = get_builder_language(session)
    run_sphinx_builder(session, builder, language)


@nox.session
def clean(session):
    """Clean the build directory."""
    session.run("rm", "-rf", OUTDIR, external=True)


@nox.session
def preview(session):
    """Build and serve the docs with automatic reload on change."""
    install_dependencies(session)

    # Build sample and serve
    builder, language = get_builder_language(session)
    session.run(
        "sphinx-autobuild",
        "-b",
        builder,
        INDIR,
        get_outdir_path(builder, language),
        *get_sphinx_opts(language),
        *SPHINX_AUTOBUILD_OPTS,
    )


@nox.session
def gettext(session):
    """Generate .pot files and update .po files."""
    if LANGUAGES == [DEFAULT_LANGUAGE]:
        session.error("No additional languages to generate .pot files for.")

    install_dependencies(session)

    gettext_outdir = os.path.join(OUTDIR, "gettext")

    # Generate .pot files from Sphinx
    session.run(
        "sphinx-build",
        "-b",
        "gettext",
        INDIR,
        gettext_outdir,
        *DEFAULT_SPHINX_OPTS,
    )

    # Prepare "-l" param for sphinx-intl but exclude default lang
    l_params = []
    langs_without_default = LANGUAGES.copy()
    langs_without_default.remove(DEFAULT_LANGUAGE)
    for lang in langs_without_default:
        l_params.append("-l")
        l_params.append(lang)

    # Update .po from .pot templates
    session.run(
        "sphinx-intl",
        # Read locale_dirs to place .po files from conf.py
        "-c",
        os.path.join(INDIR, "conf.py"),
        # update .po files
        "update",
        # from .pot files at
        "-p",
        gettext_outdir,
        # for supported languages
        *l_params,
        # no line wrapping
        "-w",
        "0",
    )
