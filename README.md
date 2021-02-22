# Inline HTML

Using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
to parse and inject inline JS, CSS into HTML.

## Installation

- Requires Python and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

## Usage

The script takes an input HTML file and produces an output HTML file.

The script looks for all `<script>` and `<link>` tags that have an "inline" attribute.

`<script>` tags use the "src" attribute to determine which file to inject.  Similarly, `<link>` tags use the "href" attribute.

`<script>` tags have their contents replaced with the file while `<link>` tags are completely replaced with `<style>` tags.

The root location of the JavaScript and CSS files defaults to the script's working directory, but each can be specified as command line arguments.

By default, the input file is named "index.html" and the output file is named "out.html".  File paths can be specified as command lines arguments.

Example usage:
```shell
inline \
  --javascript src \
  --css styles \
  --entry main.html \
  --output build/index.html \
```

## Motivation

My primary motivation is for use with developing Google Apps Script web apps.
GAS only sends HTML files to clients.
You can link to external (e.g. CDN) files, but not regular JavaScript/CSS files saved in your GAS project.
To work around this, regular JavaScript/CSS files are maintained in the git repo and local development environment, and `inline` is used in the build pipeline to produce a single HTML file that can be synced with [clasp](https://github.com/google/clasp).