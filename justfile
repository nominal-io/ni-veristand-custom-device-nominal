#!/usr/bin/env just --justfile

# Show what is available
default:
    @just --list

# The user docs in docs/, published on the Nominal docs hub at /ni/veristand/. Python is
# here only for these, through uv. Warnings fail the build, as they do in CI.
#
# Build the docs into docs/_build/dirhtml
build-docs:
    uv run --group docs sphinx-build -E -W --keep-going -b dirhtml docs docs/_build/dirhtml

# Serve the docs on http://127.0.0.1:8000, rebuilding on page edits
serve-docs:
    uv run --group docs --with sphinx-autobuild sphinx-autobuild -b dirhtml docs docs/_build/dirhtml
