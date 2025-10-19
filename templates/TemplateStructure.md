# FrontEnd Insights Template Structure

# Extends [base.html](./base.html)
- [`├── index.html`](./index.html)
- [`├── dashboard.html`]((./dashboard/dashboard.html)) includes:
  - [`├── top-nav.html`](./dashboard/top-nav.html)
  - [`├── sidebar.html`](./dashboard/sidebar.html)
  - [`├── lang_home.html`](./dashboard/lang_home.html)(conditionally rendered based on language using macro) imports from:
    - [`├── _lang-home.html`](./dashboard/macros/_lang-home.html) (macro)
  - [`├── semantic-elements.html`](./dashboard/html/semantic-elements.html)(conditionally rendered based on request parameters) imports from:
    - [`├── _concept.html`](./dashboard/macros/_concept.html)(macro) includes:
      - [`├── example-code.html`](./dashboard/components/example-code.html)
      - [`├── mini-website.html`](./dashboard/components/mini-website.html)
      
  
