from setuptools import setup

setup(
    name='sphinx_reredirects',
    version='0.0.0',
    url='https://gitlab.com/documatt/sphinx-reredirects',
    license='BSD3',
    author='Matt from Documatt',
    author_email='matt@documatt.com',
    description='Handles redirects for moved pages in Sphinx documentation projects',
    long_description=open('README.rst', encoding='utf-8').read(),
    packages=['sphinx_reredirects'],
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points={
        'sphinx.html_themes': [
            'sphinx_documatt_theme = sphinx_documatt_theme',
        ]
    },
    install_requires=[
        'sphinx'
    ],
    setup_requires = [
        'wheel'
    ],
    classifiers=[
         'Development Status :: 5 - Production/Stable',
         'Environment :: Console',
         'Environment :: Web Environment',
         'Framework :: Sphinx :: Extension',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: BSD License',
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Programming Language :: Python :: 3'
         'Topic :: Documentation',
         'Topic :: Documentation :: Sphinx',
         'Topic :: Utilities',
    ],
)
