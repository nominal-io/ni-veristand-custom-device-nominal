"""Sphinx configuration for the NI VeriStand docs: Nominal's custom device that streams
VeriStand channels in real time.

Built with `just build-docs`. .github/workflows/deploy-docs.yml deploys the build to this
repo's GitHub Pages, and the Nominal docs hub (nominal-io/pub-docs) pulls it from there and
serves it at /ni/veristand/.
"""

import sys
from pathlib import Path

from nominal_sphinx_theme import theme_options

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE / "_ext"))

project = "NI VeriStand"
copyright = "Nominal, Inc."

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "nominal_sphinx_theme",
    "site_links",  # [text](site:/quickstart/...) links to other projects on the docs hub
]

myst_enable_extensions = ["colon_fence", "deflist", "attrs_inline", "attrs_block", "fieldlist"]
# links to other sites open in a new tab
myst_links_external_new_tab = True
myst_heading_anchors = 6

# CLAUDE.md holds the rules for writing these pages; it isn't one
exclude_patterns = ["_build", "CLAUDE.md"]

html_theme = "shibuya"
html_title = project
html_copy_source = False
html_context = {
    "source_type": "github",
    "source_user": "nominal-io",
    "source_repo": "ni-veristand-custom-device-nominal",
    "source_version": "main",
    "source_docs_path": "/docs/",
}
html_theme_options = theme_options(
    github_url="https://github.com/nominal-io/ni-veristand-custom-device-nominal",
)
