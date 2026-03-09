# DataUnchain — Official Website

> **Drop documents. Get structured data. 100% offline.**

This repository hosts the source code for the official [dataunchain.com](https://dataunchain.com) website, built with **Jekyll** and deployed on GitHub Pages.

## Tech Stack

- **Jekyll** — Static site generator
- **Tailwind CSS** (via CDN) — Utility-first CSS framework
- **GitHub Pages** — Hosting and deployment

## Quick Start

```bash
git clone https://github.com/dataunchain/dataunchain.github.io.git
cd dataunchain.github.io
bundle install
bundle exec jekyll serve --livereload
```

Open `http://localhost:4000` in your browser.

## Structure

```
dataunchain.github.io/
├── _config.yml          # Jekyll configuration
├── _data/               # Navigation data (EN/IT)
├── _includes/           # Nav, footer, shared components
├── _layouts/            # Page layouts
├── _posts/              # Blog posts (EN/IT)
├── en/                  # English pages
├── it/                  # Italian pages
├── assets/              # CSS, JS, images
└── index.html           # Language redirect
```

## License

MIT — © Antonio Trento
