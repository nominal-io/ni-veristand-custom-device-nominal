# docs/

These pages build here and are published on the Nominal docs hub (nominal-io/pub-docs) at
`/ni/veristand/`. The repo's CLAUDE.md brings in the hub's writing rules, and those apply
here in full. This file adds what is specific to the pages.

## Where the facts come from

Quote labels and messages exactly as the source has them, labels in bold.

- The menu entry, the device's pages and its **Export Configuration** button:
  `source/Custom Device Nominal Core Streaming.xml`.
- The **CD Configuration**, **Nominal Configuration** and **Channel Configuration** tabs, with
  their fields, defaults and help text: `source/System Explorer/Main Page.vi`. The channel
  pages, such as the time source's modes, are `Time.vi`, `Enable.vi` and `Decimation.vi` beside it.
- The device's channel names: `source/Shared/Constants.vi`.
- What the device does while running, such as finding or creating the dataset and timestamping
  samples: `source/Engine/`.
- What a release contains and where its files go: `Built/`, the build output, which git ignores.
  It matches the zip on the GitHub release.
- The README, for installing and deploying. Check it against the source, which wins.

The VIs are binary. Read their labels in LabVIEW, or as strings from the VI file, where the front
panel's are zlib-compressed. nominal-io/veristand-client is a different repo, not a source for
these pages.

## Names

Every "Nominal Core" in the source is wrong, as the repo's CLAUDE.md says. Write "Nominal".
Until the source is renamed, quote the names a reader has to find exactly as they are, such as
the **Nominal Core Streaming** menu entry, its folder and files, and the release's zip. Report
any other use of the name rather than copying it.

## Rules for these pages

- Readers know VeriStand: System Explorer, system definitions, targets, mappings and system
  channels. Explain only what is Nominal's.
- Don't repeat what the device already shows, such as a field's help text. Name the field and
  say when to change it.
- State only what the source shows or what has been run. VeriStand's own behavior, such as its
  system channels and menu labels, needs a check in VeriStand or its user manual before a page
  relies on it. The manual's pages on ni.com load with JavaScript, so ask your human for the PDF.
- For anything in the Nominal app, such as API keys, assets and datasets, link the hub's
  quickstart pages rather than describing the app from memory.
- Link to other projects on the hub as `[text](site:/{lang}/{project}/{page}/)`, never with an
  absolute URL, so the hub's offline copy works. These links resolve on the hub but not on this
  repo's own Pages.
- Keep the Trademarks section at the end of `index.md`.

## Building

`just build-docs` builds into `docs/_build/dirhtml`, with warnings failing the build as in CI.
Run it before calling a change done. `just serve-docs` serves a live preview on
http://127.0.0.1:8000.

`.github/workflows/docs-check.yml` builds every pull request. `deploy-docs.yml` deploys every
push to `main` to this repo's GitHub Pages, which are public, and pub-docs pulls that deploy.
