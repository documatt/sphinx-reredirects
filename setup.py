from setuptools import setup

setup(
    name='sphinx_reredirects',
    version='0.0.1',
    url='https://gitlab.com/documatt/sphinx-reredirects',
    license='BSD3',
    author='Matt from Documatt',
    author_email='matt@documatt.com',
    description='Handles redirects for moved pages in Sphinx documentation '
    'projects',
    long_description=open('README.rst', encoding='utf-8').read(),
    long_description_content_type='text/x-rst',
    packages=['sphinx_reredirects'],
    install_requires=[
        'sphinx'
    ],
    setup_requires=[
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
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Utilities',
    ],
)
