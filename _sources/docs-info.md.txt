# Documentation info

The EEG Lab documentation is contained in the `kcni-eeg-lab/doc` folder of this repo. 

A subset of the pages in this folder are included in the *official* [documentation website](https://krembilneuroinformatics.github.io/kcni-eeg-lab). This is a sphinx-based website that auto-built on every new PR using github's continuous integration functionality, and served from the is hosted on the gh-pages branch of this repo. 

So, following a commit you will see any changes to the docs pages in typically ~20 seconds. 

Any pages to be included in the docs site need to be specified in `doc/index.rst`.

This setup allows us to maintain both 'rough' and 'polished' documentation, without conflict. 

To add a docs page:

- Create the file in the `doc` folder (e.g. `kcni-eeg-lab/doc/mynewdocfile.md`)
- If you want this file to appear on the site, edit the `kcni-eeg-lab/doc/index.rst` file accordingly

If you have admin access on the repo, the easiest way to do this is usually using the github browser-based text editor. 
