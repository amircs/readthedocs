# -*- coding: utf-8 -*-
#
# Google Genomics documentation build configuration file, created by
# sphinx-quickstart on Wed Apr 30 15:58:16 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import sphinx.environment
from docutils.utils import get_source_line

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Google Genomics'
copyright = u'2015, Google Inc'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = 'v1'
# The full version, including alpha/beta/rc tags.
release = 'v1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'includes/*']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# THIS IS THE GOOGLE GENOMICS FOOTER
rst_epilog = """
------------------------------------------------------------------------------------

.. container:: ggfooter

  Have feedback or corrections?  All improvements to these docs are welcome! You can
  click on the "Edit on GitHub" link at the top right corner of this page or
  `file an issue <https://github.com/googlegenomics/start-here/issues>`_.

  Need more help?  Please see https://cloud.google.com/genomics/support.

.. GLOBAL REPLACEMENTS CAN GO HERE

.. ### Data links
.. _Personal Genome Project: http://www.personalgenomes.org/
.. _PGP: http://www.personalgenomes.org/
.. _ClinVar: http://www.ncbi.nlm.nih.gov/clinvar/
.. _UCSC Sequence and Annotation Data: http://hgdownload.cse.ucsc.edu/
.. _Tute's documentation: https://docs.google.com/document/d/1_Kryc4qAqw1NRezaqDJ1tXUSCbxEkKK4SSi_kZuyHtU/pub
.. _Cancer Genomics Cloud: http://cgc.systemsbiology.net/

.. _Illumina Platinum Genomes project data: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/platinum_genomes.html
.. _1000 Genomes project data: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/1000_genomes.html

.. ### Gene links
.. _BRCA1: http://ghr.nlm.nih.gov/gene/BRCA1
.. _BRCA2: http://ghr.nlm.nih.gov/gene/BRCA2

.. ### GA4GH Links
.. _GA4GH: http://ga4gh.org/#/api
.. _Global Alliance for Genomics and Health API: http://ga4gh.org/#/api
.. _Global Alliance for Genomics and Health Beacon: http://ga4gh.org/#/beacon

.. ### VCF documentation links
.. _VCF specification: http://samtools.github.io/hts-specs/VCFv4.2.pdf
.. _gVCF: https://sites.google.com/site/gvcftools/home/about-gvcf
.. _gVCF conventions: https://sites.google.com/site/gvcftools/home/about-gvcf/gvcf-conventions

.. ### Corporate ecosystem links
.. _Complete Genomics: http://www.completegenomics.com
.. _Illumina: https://www.illumina.com

.. ### Google genomics organizational links
.. _googlegenomics github organization: https://github.com/googlegenomics
.. _Contact us: google-genomics-contact@googlegroups.com

.. ### Google Guide Links
.. _Application Default Credentials: https://developers.google.com/identity/protocols/application-default-credentials

.. ### Google Product Links
.. _Google BigQuery: https://cloud.google.com/bigquery/
.. _Google Cloud Dataflow: https://cloud.google.com/dataflow/
.. _Google Cloud Storage: https://cloud.google.com/storage/
.. _Google Compute Engine: https://cloud.google.com/compute/
.. _Google Cloud Platform Console: https://console.cloud.google.com/
.. _Google Genomics: https://cloud.google.com/genomics/
.. _Google Cloud Datalab: https://cloud.google.com/datalab/
.. _Google Cloud Dataproc: https://cloud.google.com/dataproc/

.. ### Deep links into the Developers Console
.. _Project List: https://console.developers.google.com/project
.. _click-to-deploy NCBI BLAST: https://console.developers.google.com/project/_/launcher/details/click-to-deploy-images/ncbiblast
.. _click-to-deploy Bioconductor: https://console.developers.google.com/project/_/mc/template/bioconductor
.. _Deployments: https://console.developers.google.com/project/_/deployments

.. ### Deep links into cloud.google.com documentation
.. _Compute Engine resource quota: https://cloud.google.com/compute/docs/resource-quotas
.. _Compute Engine quota request form: https://docs.google.com/a/google.com/forms/d/1vb2MkAr9JcHrp6myQ3oTxCyBv2c7Iyc5wqIKqE3K4IE/viewform
.. _Compute Engine Preemptible Virtual Machines: https://cloud.google.com/preemptible-vms/
.. _Google BigQuery query reference: https://cloud.google.com/bigquery/query-reference
.. _cloud.google.com/genomics: https://cloud.google.com/genomics
.. _What is Google Genomics: https://cloud.google.com/genomics/what-is-google-genomics
.. _Google Genomics fundamentals: https://cloud.google.com/genomics/what-is-google-genomics#fundamentals
.. _Google Genomics Pricing: https://cloud.google.com/genomics/pricing
.. _Google Genomics Tools: https://cloud.google.com/genomics/install-genomics-tools
.. _Google Genomics API: https://cloud.google.com/genomics/reference/rest/
.. _Google Genomics Reads API: https://cloud.google.com/genomics/reference/rest/v1/reads
.. _Google Genomics Variants API: https://cloud.google.com/genomics/reference/rest/v1/variants
.. _Load Genomic Variants: https://cloud.google.com/genomics/v1/load-variants
.. _Understanding the BigQuery Variants Table Schema: https://cloud.google.com/genomics/v1/bigquery-variants-schema

.. _Using Google Cloud Storage with Big Data: https://cloud.google.com/storage/docs/working-with-big-data
.. _gsutil: https://cloud.google.com/storage/docs/gsutil
.. _install gcloud: https://cloud.google.com/sdk/
.. _persistent disk: https://cloud.google.com/compute/docs/tutorials/compute-engine-disks-price-performance-and-persistence
.. _selecting the right persistent disk: https://cloud.google.com/compute/docs/tutorials/compute-engine-disks-price-performance-and-persistence#selecting_the_right_disk

.. ### Open ecosystem links
.. _Apache Spark: https://spark.apache.org/
.. _Apache Hadoop: https://hadoop.apache.org/
.. _Docker: https://www.docker.com/
.. _Elasticluster: https://elasticluster.readthedocs.org
.. _Elasticluster repo: https://github.com/gc3-uzh-ch/elasticluster
.. _Grid Engine: http://gridengine.info/
.. _NCBI BLAST: http://blast.ncbi.nlm.nih.gov/Blast.cgi
.. _NCBI BLAST Cloud Documentation: http://ncbi.github.io/blast-cloud/
.. _S3IT: http://www.s3it.uzh.ch/
.. _SLURM: https://computing.llnl.gov/linux/slurm/
.. _ALPN: http://www.eclipse.org/jetty/documentation/9.2.10.v20150310/alpn-chapter.html

.. _Bioconductor: http://www.bioconductor.org/
.. _Using Bioconductor: http://www.bioconductor.org/install/
.. _Dockerized Bioconductor: http://bioconductor.org/help/docker/
.. _GoogleGenomics Bioconductor package: http://bioconductor.org/packages/release/bioc/html/GoogleGenomics.html

.. _IGV: https://www.broadinstitute.org/igv/
.. _Picard: http://broadinstitute.github.io/picard/
.. _GATK: https://www.broadinstitute.org/gatk/
.. _HTSJDK: https://github.com/samtools/htsjdk/

.. _gridengine array job: http://wiki.gridengine.info/wiki/index.php/Simple-Job-Array-Howto

.. ### googlegenomics github links
.. _gatk-tools-java: https://github.com/googlegenomics/gatk-tools-java
.. _Data Analysis using Google Genomics: https://github.com/googlegenomics/codelabs/tree/master/R/1000Genomes-BRCA1-analysis
.. _Quality Control using Google Genomics: https://github.com/googlegenomics/codelabs/tree/master/R/PlatinumGenomes-QC
.. _BiocDockerOnGCE launch script: https://raw.githubusercontent.com/googlegenomics/gce-images/master/launch-scripts/bioconductorRStudioGCE.sh
.. _Grid Computing Tools github repo: https://github.com/googlegenomics/grid-computing-tools
.. _getting-started-bigquery: https://github.com/googlegenomics/getting-started-bigquery
.. _bigquery-examples: https://github.com/googlegenomics/bigquery-examples

.. ### R package links
.. _VariantAnnotation: http://bioconductor.org/packages/release/bioc/html/VariantAnnotation.html
.. _ggbio: http://bioconductor.org/packages/release/bioc/html/ggbio.html
.. _ggplot2: http://cran.r-project.org/web/packages/ggplot2/index.html
.. _dplyr: http://cran.r-project.org/web/packages/dplyr/index.html
.. _bigrquery: http://cran.r-project.org/web/packages/bigrquery/index.html
.. _GoogleGenomics: http://bioconductor.org/packages/release/bioc/html/GoogleGenomics.html

.. ### Python installation and package links
.. _Python user scheme: https://docs.python.org/2/install/index.html#alternate-installation-the-user-scheme
.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

.. ### Genomics API Getting started examples in github
.. _Python getting started: https://github.com/googlegenomics/getting-started-with-the-api/tree/master/python
.. _Java getting started: https://github.com/googlegenomics/getting-started-with-the-api/tree/master/java
.. _Go getting started: https://github.com/googlegenomics/getting-started-with-the-api/tree/master/go

"""

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

#------------[ For Local Development ] -------------------------------------
# See https://github.com/snide/sphinx_rtd_theme for theme install instructions.
import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'GoogleGenomicsdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'GoogleGenomics.tex', u'Google Genomics Documentation',
   u'Google Genomics <https://cloud.google.com/genomics>', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'googlegenomics', u'Google Genomics Documentation',
     [u'Google Genomics <https://cloud.google.com/genomics>'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'GoogleGenomics', u'Google Genomics Documentation',
   u'Google Genomics <https://cloud.google.com/genomics>', 'GoogleGenomics', 'Google Genomics Cookbook',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# -- Silence certain warnings -------------------------------------------

# http://stackoverflow.com/questions/12772927/specifying-an-online-image-in-sphinx-restructuredtext-format
def _warn_node(self, msg, node):
    if not msg.startswith('nonlocal image URI found:'):
        self._warnfunc(msg, '%s:%s' % get_source_line(node))

sphinx.environment.BuildEnvironment.warn_node = _warn_node
