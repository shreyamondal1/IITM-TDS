---
marp: true
theme: my-theme
paginate: true
paginate-style: "font-size: 0.7em; color: #666; position: absolute; bottom: 10px; right: 20px;"
math: katex
---

<!-- _class: intro -->

# Product Documentation Presentation
### Technical Writer — Software Engineering
**Email:** 23f1001792@ds.study.iitm.ac.in

---

<!-- _class: section -->

# Custom Theme Demo
This presentation uses:

- A custom theme (`my-theme`)
- Page numbers
- KaTeX math
- Custom CSS
- Marp directives

---

<!-- _backgroundImage: "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200" -->
<!-- _class: bg-demo -->

# Slide with Background Image

Text stays readable because Marp applies overlay & text-shadow styling as required.

---

# Algorithmic Complexity Example

Using KaTeX:

\[
T(n) = n \log n + 3n + O(1)
\]

This is the typical complexity of efficient comparison-based sorts (e.g. mergesort).

---

# Documentation Notes

- This entire presentation is a single **Markdown** file
- Can be converted to PDF, PPTX, HTML using **Marp CLI**
- Ideal for maintainability in version control
- Custom styling applied via theme

---

<!-- Theme must be in the same markdown file or separate; we’ll include it inline -->

<style>
section.intro h1 {
  color: #2a6fff;
  text-align: center;
}

section.intro {
  background: #eef5ff;
}

section.section {
  border-left: 8px solid #2a6fff;
  padding-left: 20px;
}

section.bg-demo h1 {
  color: white;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
}

:root {
  --my-accent: #2a6fff;
}
</style>

<!-- Custom Theme -->
<style>
@theme my-theme {
  backgroundColor: #fff;
  color: #111;
  header: {
    font-size: 1.8em;
    color: var(--my-accent);
  }
}
</style>
