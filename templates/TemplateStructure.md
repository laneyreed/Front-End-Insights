# FrontEnd Insights Template Structure

## Overview
This document outlines the template structure and organization for the FrontEnd Insights application, including template inheritance, includes, macros, and their relationships.

## Template Hierarchy

### Base Template
- **File**: `base.html`
- **Purpose**: Root template that defines the main HTML structure
- **Contains**:
  - HTML document structure (doctype, html, head, body)
  - Meta tags and viewport settings
  - CSS links (main.css, FontAwesome)
  - Block definitions for extensibility
  - Footer content

#### Template Blocks in base.html:
```jinja2
{% block title %}{% endblock title %}        # Page title
{% block header %}{% endblock header %}      # Header navigation
{% block main %}{% endblock main %}          # Main content area
```

### Dashboard Template
- **File**: `dashboard/dashboard.html`
- **Extends**: `base.html`
- **Purpose**: Main dashboard layout for all language sections
- **Conditional Rendering**: Uses template logic to render different content based on URL parameters


## Include Templates

### Navigation Components

#### Top Navigation
- **File**: `dashboard/top-nav.html`
- **Purpose**: Main site navigation bar
- **Features**:
  - Brand logo/title
  - Language navigation links (HTML, CSS, JavaScript, Python)
  - Active state detection using `request.view_args`
  - FontAwesome icons for each language

#### Sidebar Navigation
- **File**: `dashboard/sidebar.html`
- **Purpose**: Dynamic concept navigation for each language
- **Features**:
  - Language-specific title display
  - Dynamic concept list rendering
  - Active concept highlighting
  - URL generation with `url_for()`

### Content Templates

#### Language Home Pages
- **HTML**: `dashboard/html/html-home.html`
- **CSS**: `dashboard/css/css-home.html`
- **JavaScript**: `dashboard/javascript/javascript-home.html`
- **Python**: `dashboard/python/python-home.html`

#### Concept Pages
- **Semantic Elements**: `dashboard/html/semantic-elements.html`
- Additional concept pages follow similar structure

## Macro System

### Concept Macros
- **File**: `dashboard/macros/_concept.html`
- **Purpose**: Reusable components for concept documentation

#### Available Macros:

##### 1. `render_concept(tag_name, tag_purpose, best_practices)`
- **Purpose**: Main concept wrapper that renders complete concept sections
- **Parameters**:
  - `tag_name`: HTML element name
  - `tag_purpose`: Description of element purpose
  - `best_practices`: List of best practice strings
- **Structure**: Calls header macro, content caller, and best practices macro

##### 2. `render_concept_header(tag_name, tag_purpose)`
- **Purpose**: Renders the concept header section
- **Parameters**:
  - `tag_name`: HTML element name
  - `tag_purpose`: Element description
- **Structure**: Creates header with tag display and description

##### 3. `render_best_practices(best_practices)`
- **Purpose**: Renders best practices section
- **Parameters**:
  - `best_practices`: List of practice strings
- **Structure**: Creates formatted list of best practices


## Template Variables and Context

### Global Variables
- `lang`: Current language (HTML, CSS, JavaScript, Python)
- `concepts`: List of concepts for current language
- `request`: Flask request object for URL parameters

### URL Parameters
- `language`: Language identifier in URL
- `concept`: Specific concept identifier
- Used for conditional rendering and active state detection



## Template Relationships

### Inheritance Chain
```
base.html
    └── dashboard/dashboard.html
```

### Include Relationships
```
dashboard.html includes:
    ├── dashboard/top-nav.html
    ├── dashboard/sidebar.html
    └── [conditional content includes]
        ├── dashboard/html/html-home.html
        ├── dashboard/html/semantic-elements.html
        ├── dashboard/css/css-home.html
        ├── dashboard/javascript/javascript-home.html
        └── dashboard/python/python-home.html
```

### Macro Dependencies
```
semantic-elements.html imports from:
    └── dashboard/macros/_concept.html

```

## Best Practices

1. **Template Inheritance**: Use `{% extends %}` for main layout structure
2. **Modular Includes**: Use `{% include %}` for reusable UI components
3. **Macro Usage**: Use macros for repeated content patterns with variations
4. **Conditional Rendering**: Use template logic for dynamic content based on context
5. **Block Organization**: Define clear, semantic blocks for extensibility
6. **Active States**: Use request context for navigation active states
7. **URL Generation**: Use `url_for()` for dynamic URL generation

## Future Considerations

- Consider implementing template caching for performance
- Evaluate macro organization as the number of concepts grows
- Consider implementing template fragments for AJAX loading
- Evaluate need for custom template filters or globals
