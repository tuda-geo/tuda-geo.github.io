import time

extensions = [
    'sphinx_design',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
source_suffix = '.rst'

description = 'tuda-geo: TU Delft - Data Assimilation for Geosciences'
project = 'tuda-geo'
author = 'Femke Vossepoel et al.'
copyright = f'2021-{time.strftime("%Y")}, {author}'

pygments_style = 'friendly'
html_theme = 'pydata_sphinx_theme'

html_static_path = ['_static']
html_logo = '_static/tuda-logo.png'
# html_favicon = '_static/favicon.ico'
html_theme_options = {
    "github_url": "https://github.com/tuda-geo",
    "external_links": [
        {"name": "resmda", "url": "https://tuda-geo.github.io/resmda"},
    ],
    # "navbar_start": ["navbar-logo"],
    # "navbar_center": ["navbar-nav"],
    # "navbar_end": ["navbar-icon-links"],
    # "footer_items": ["copyright", "sphinx-version"],
    "secondary_sidebar_items": [],
}
html_file_suffix = '.html'
html_sidebars = {
    "**": [],
}
html_css_files = [
    # "style.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
]
