# RoPhi Lab Website

Official website for the **Robotics and Physical Intelligence Lab** (RoPhi Lab), built with [Quarto](https://quarto.org/).

**Live site:** [https://rophi-lab.github.io](https://rophi-lab.github.io)

## Pages

| Page | File |
|------|------|
| Home | `index.qmd` |
| People | `people.qmd` |
| Research | `research.qmd` |
| Publications | `publications.qmd` |
| Teaching | `teaching.qmd` |
| Contact | `contact.qmd` |

## Local development

1. Install [Quarto](https://quarto.org/docs/get-started/).
2. From the repository root:

```bash
quarto preview
```

To build the site without previewing:

```bash
quarto render
```

Output is written to `_site/`.

## Publishing to GitHub Pages

This repository includes a GitHub Actions workflow (`.github/workflows/publish.yml`) that renders the site and publishes to the `gh-pages` branch on pushes to `main` or `master`.

**One-time setup:**

1. In the repository on GitHub: **Settings → Actions → General → Workflow permissions**, enable **Read and write permissions**.
2. Push to `main`. After the workflow completes, open **Settings → Pages** and confirm the site is served from the `gh-pages` branch (Quarto’s publish action configures this automatically on first run).

Alternatively, publish once from your machine:

```bash
quarto publish gh-pages
```

## Customization

- **Site title, navbar, theme:** `_quarto.yml`
- **Styles:** `styles.css`
- **Publications:** add entries to `references.bib` and update `publications.qmd`
- **Logo & images:** replace files in `assets/`
