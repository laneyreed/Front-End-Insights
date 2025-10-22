# FrontEnd Insights Template Structure

# Extends [base.html.jinja2](./base.html)
- [`├── index.html.jinja2`](./index.html)
- [`├── dashboard.html.jinja2`](./dashboard/dashboard.html.jinja2) includes:
  - [`├── top-nav.html.jinja2`](./dashboard/top-nav.html.jinja2)
  - [`├── sidebar.html.jinja2`](./dashboard/sidebar.html.jinja2)
  - [`├── lang_home.html.jinja2`](./dashboard/lang_home.html.jinja2) uses imports from:
    - [`├── _lang-home.html.jinja2`](./dashboard/macros/_lang-home.html.jinja2) (macro)
  - [`├── concept.html.jinja2`](./dashboard/concept.html) includes:
    - [`├── sematic.html.jinja2`](./dashboard/langconcepts/htmlconcepts/sematic.html.jinja2)
    - [`├── flexbox.html.jinja2`](./dashboard/langconcepts/cssconcepts/flexbox.html.jinja2)


    - [`├── _concept.html.jinja2`](./dashboard/macros/_concept.html.jinja2)(macro) includes:
      - [`├── example-code.html.jinja2`](./dashboard/components/example-code.html.jinja2)
      - [`├── mini-website.html.jinja2`](./dashboard/components/mini-website.html.jinja2)
      


### Site Home Page

### Dashboard
- [`dashboard.html`](./dashboard/dashboard.html)
  - recevies language, concepts list, and resources list variables, for the selected language, from the server
  - conditionally renders language home page or a language concept page
  - if the URL parameter `concept` is **None** then the [language home page](./dashboard/lang_home.html.jinja2)(`lang_home.html.jinja2`) is rendered 
  - if the URL parameter `concept` is **not None** then the [language concept page](./dashboard/concept.html.jinja2)(`concept.html.jinja2`) is rendered

- [language home page](./dashboard/lang_home.html.jinja2)
  - uses the [language home macro](./dashboard/macros/_lang-home.html.jinja2)(`_lang-home.html`) to render the selected language home page content, based on the language variable from the server
  - the language variable is passed to the server from either
    - the site home page when a language link is clicked
    - the dashboard's top navigation when a language is selected from the menu

- [language concept page](./dashboard/concept.html.jinja2)
  - includes a language concept page based on the `concept` URL parameter value
    - the `concept` URL parameter value comes from the [sidebar](./dashboard/sidebar.html.jinja2)(`sidebar.html.jinja2`) when a concept is selected from the sidebar menu
  - uses the [language home macro](./dashboard/macros/_lang-home.html.jinja2)(`_lang-home.html`) to render the selected language home page content, based on the language variable from the server