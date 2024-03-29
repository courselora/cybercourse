# Configuration file for the Sphinx documentation builder.

# -- Project information
project = 'Cybercourse'
copyright = '2021-2022, Dağhan Tınaztepe'
author = 'Dağhan Tınaztepe'

# release = '0.1'
# version = '0.1.0'

# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_logo = "logo.png"
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- HTML Theme options
html_theme_options = {
    'analytics_id': 'G-P67XEQEL8H',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'display_version': False,
    'logo_only': True,
}