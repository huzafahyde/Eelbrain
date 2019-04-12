# -*- coding: utf-8 -*-
#
# Eelbrain documentation build configuration file, created by
# sphinx-quickstart on Tue Mar 29 23:16:11 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from datetime import datetime
import os
from pathlib import Path
from warnings import filterwarnings

import mne
import eelbrain.plot._brain_object  # make sure that Brain is available
import eelbrain


# docutils 0.14
filterwarnings('ignore', category=DeprecationWarning)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

autoclass_content = 'class'  # 'both'

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.4.3'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.autosummary',  # default
    'sphinx.ext.todo', 'sphinx.ext.imgmath',  # default
    'sphinx.ext.intersphinx',  # http://sphinx.pocoo.org/ext/intersphinx.html
    'numpydoc',  # https://github.com/numpy/numpy/tree/master/doc/sphinxext
    'sphinxcontrib.bibtex',  # https://sphinxcontrib-bibtex.readthedocs.io
    'sphinx_gallery.gen_gallery',  # https://sphinx-gallery.github.io
]
# enable to  have all methods documented on the same page as a class:
# autodoc_default_flags=['inherited-members']
autosummary_generate = True
numpydoc_show_class_members = False


def use_pyplot(gallery_conf, fname):
    eelbrain.configure(frame=False)


sphinx_gallery_conf = {
    'examples_dirs': '../examples',   # path to example scripts
    'gallery_dirs': 'auto_examples',  # path where to save gallery generated examples
    'filename_pattern': rf'{os.sep}\w',
    'default_thumb_file': Path(__file__).parent / 'images' / 'eelbrain.png',
    'min_reported_time': 4,
    'download_all_examples': False,
    'reset_modules': ('matplotlib', use_pyplot),
    'reference_url': {'eelbrain': None},
    'first_notebook_cell': (
        "from eelbrain import configure\n"
        "configure(frame=False)\n"  # avoid wxPython dependency
        "%matplotlib inline\n"  # sphinx-gallery default
    )
}

# download datasets (to avoid progress bar output in example gallery)
root = mne.datasets.mtrf.data_path()

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Eelbrain'
copyright = u'%i, Christian Brodbeck' % datetime.now().year

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = eelbrain.__version__.rsplit('.', 1)[0]
# The full version, including alpha/beta/rc tags.
release = eelbrain.__version__  # '0.0.3'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build', 'illustrations', 'images', 'static']

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['eelbrain.']

# Supress warnings for badges
suppress_warnings = ['image.nonlocal_uri']


# -- Custom Options -----------------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3.6', None),
    'imageio': ('https://imageio.readthedocs.io/en/stable/', None),
    'mne': ('http://martinos.org/mne/stable', None),
    'matplotlib': ('https://matplotlib.org', None),
    'nilearn': ('https://nilearn.github.io', None),
    'numpy': ('https://docs.scipy.org/doc/numpy', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'pyarrow': ('https://arrow.apache.org/docs/python', None),
}
# http://sphinx.pocoo.org/ext/intersphinx.html


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# new default: alabaster
html_theme = 'classic'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'stickysidebar': True}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'images/eelbrain.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'static/eelbrain.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['globaltoc.html', 'searchbox.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Eelbraindoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'Eelbrain.tex', u'Eelbrain Documentation',
     u'Christian Brodbeck', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'eelbrain', u'Eelbrain Documentation',
     [u'Christian Brodbeck'], 1)
]
