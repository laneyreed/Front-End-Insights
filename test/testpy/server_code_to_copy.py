# ==============================================================================
# ADD THIS CODE TO YOUR EXISTING server.py FILE
# This mimics your JavaScript topNavLinks.forEach event listener behavior
# ==============================================================================

# Navigation data structure (Python version of your JavaScript navigationData)
NAVIGATION_DATA = {
    'html': {
        'title': 'HTML',
        'pageTitle': 'HTML Dashboard',
        'sidebar': [
            {'icon': 'fas fa-chart-area', 'text': 'Overview', 'id': 'overview'},
            {'icon': 'fas fa-code', 'text': 'Elements', 'id': 'elements'},
            {'icon': 'fas fa-wpforms', 'text': 'Forms', 'id': 'forms'},
            {'icon': 'fas fa-sitemap', 'text': 'Semantic', 'id': 'semantic'},
            {'icon': 'fas fa-universal-access', 'text': 'Accessibility', 'id': 'accessibility'},
            {'icon': 'fas fa-check-circle', 'text': 'Best Practices', 'id': 'best-practices'}
        ]
    },
    'css': {
        'title': 'CSS',
        'pageTitle': 'CSS Dashboard', 
        'sidebar': [
            {'icon': 'fas fa-palette', 'text': 'Overview', 'id': 'overview'},
            {'icon': 'fas fa-crosshairs', 'text': 'Selectors', 'id': 'selectors'},
            {'icon': 'fas fa-th', 'text': 'Layouts', 'id': 'layouts'},
            {'icon': 'fas fa-mobile-alt', 'text': 'Responsive', 'id': 'responsive'},
            {'icon': 'fas fa-magic', 'text': 'Animations', 'id': 'animations'},
            {'icon': 'fas fa-layer-group', 'text': 'Frameworks', 'id': 'frameworks'}
        ]
    },
    'javascript': {
        'title': 'JavaScript',
        'pageTitle': 'JavaScript Dashboard',
        'sidebar': [
            {'icon': 'fas fa-code', 'text': 'Overview', 'id': 'overview'},
            {'icon': 'fas fa-function', 'text': 'Functions', 'id': 'functions'},
            {'icon': 'fas fa-cube', 'text': 'Objects', 'id': 'objects'},
            {'icon': 'fas fa-sync-alt', 'text': 'Async/Await', 'id': 'async'},
            {'icon': 'fas fa-sitemap', 'text': 'DOM', 'id': 'dom'},
            {'icon': 'fas fa-plug', 'text': 'APIs', 'id': 'apis'}
        ]
    }
}

# Content templates
CONTENT_TEMPLATES = {
    'html': {
        'overview': {
            'title': 'HTML Overview',
            'content': '''
                <div class="stats-grid">
                    <div class="stat-card">
                        <h3>HTML Elements</h3>
                        <div class="value">150+</div>
                        <div class="change positive">Standard Elements</div>
                    </div>
                    <div class="stat-card">
                        <h3>Semantic Tags</h3>
                        <div class="value">25+</div>
                        <div class="change positive">HTML5 Semantic</div>
                    </div>
                    <div class="stat-card">
                        <h3>Form Elements</h3>
                        <div class="value">20+</div>
                        <div class="change positive">Input Types</div>
                    </div>
                </div>
                <div style="margin-top: 2rem;">
                    <h3 style="margin-bottom: 1rem; color: #1e293b;">HTML Fundamentals</h3>
                    <p>Master the structural foundation of web development with HTML5. Learn semantic elements, accessibility best practices, forms, multimedia integration, and modern HTML standards.</p>
                </div>
            '''
        }
    },
    'css': {
        'overview': {
            'title': 'CSS Overview',
            'content': '''
                <div class="stats-grid">
                    <div class="stat-card">
                        <h3>CSS Properties</h3>
                        <div class="value">500+</div>
                        <div class="change positive">Standard Properties</div>
                    </div>
                    <div class="stat-card">
                        <h3>Selectors</h3>
                        <div class="value">30+</div>
                        <div class="change positive">Selector Types</div>
                    </div>
                </div>
                <div style="margin-top: 2rem;">
                    <h3 style="margin-bottom: 1rem; color: #1e293b;">CSS Fundamentals</h3>
                    <p>Elevate your designs with advanced CSS3 techniques including Flexbox, Grid layouts, animations, and responsive design patterns.</p>
                </div>
            '''
        }
    },
    'javascript': {
        'overview': {
            'title': 'JavaScript Overview',  
            'content': '''
                <div class="stats-grid">
                    <div class="stat-card">
                        <h3>ES6+ Features</h3>
                        <div class="value">50+</div>
                        <div class="change positive">Modern JS</div>
                    </div>
                    <div class="stat-card">
                        <h3>Built-in Objects</h3>
                        <div class="value">40+</div>
                        <div class="change positive">Native APIs</div>
                    </div>
                </div>
                <div style="margin-top: 2rem;">
                    <h3 style="margin-bottom: 1rem; color: #1e293b;">JavaScript Fundamentals</h3>
                    <p>Build dynamic, interactive web applications with modern JavaScript. Master ES6+ syntax, async programming, and DOM manipulation.</p>
                </div>
            '''
        }
    }
}

def get_default_subsection(section):
    """Python equivalent of JavaScript: getDefaultSubSection(section)"""
    if section in NAVIGATION_DATA:
        return NAVIGATION_DATA[section]['sidebar'][0]['id']
    return 'overview'

def update_navigation_server(section):
    """Python equivalent of JavaScript: updateNavigation(section)"""
    if section not in NAVIGATION_DATA:
        section = 'html'
    
    section_data = NAVIGATION_DATA[section]
    return {
        'section': section,
        'title': section_data['title'],
        'page_title': section_data['pageTitle'],
        'sidebar': section_data['sidebar'],
        'default_subsection': get_default_subsection(section)
    }

def update_content_server(section, subsection=None):
    """Python equivalent of JavaScript: updateContent(section, subSection)"""
    if section not in NAVIGATION_DATA:
        section = 'html'
    
    if subsection is None:
        subsection = get_default_subsection(section)
    
    template = CONTENT_TEMPLATES.get(section, {}).get(subsection)
    
    if template:
        return {
            'title': template['title'],
            'content': template['content'],
            'section': section,
            'subsection': subsection
        }
    else:
        return {
            'title': 'Content Not Available',
            'content': '''
                <div style="text-align: center; padding: 4rem 2rem; color: #64748b;">
                    <i class="fas fa-file-alt" style="font-size: 4rem; margin-bottom: 1rem; color: #cbd5e1;"></i>
                    <h3 style="color: #475569; margin-bottom: 0.5rem;">Content Not Available</h3>
                    <p>The content for this section is currently being developed.</p>
                </div>
            ''',
            'section': section,
            'subsection': subsection
        }

# ==============================================================================
# ROUTE HANDLERS - Python equivalent of your JavaScript event listeners
# ==============================================================================

# This route mimics your JavaScript:
# topNavLinks.forEach(link => {
#     link.addEventListener('click', (e) => {
#         e.preventDefault();
#         const section = link.dataset.section;
#         updateNavigation(section);
#         updateContent(section, getDefaultSubSection(section));
#         closeMobileSidebar();
#     });
# });

# ADD THESE ROUTES TO YOUR EXISTING server.py FILE:

# @app.route('/dashboard/<language>')
# def language_dashboard(language):
#     """Main dashboard route - mimics JavaScript navigation event listener"""
#     
#     # JavaScript: const section = link.dataset.section;
#     section = language.lower()
#     
#     # JavaScript: updateNavigation(section);
#     nav_data = update_navigation_server(section)
#     
#     # JavaScript: updateContent(section, getDefaultSubSection(section));
#     content_data = update_content_server(section, nav_data['default_subsection'])
#     
#     # Prepare template context
#     context = {
#         'dashboard_title': 'Front-End Insights',
#         'dashboard_title_icon': 'fas fa-chart-line',
#         'current_section': section,
#         'page_title': nav_data['page_title'],
#         'sidebar_title': nav_data['title'],
#         'sidebar_nav': nav_data['sidebar'],
#         'current_subsection': content_data['subsection'],
#         'content_title': content_data['title'],
#         'content_body': content_data['content'],
#         'nav_item1': 'HTML',
#         'nav_item2': 'CSS',
#         'nav_item3': 'JavaScript',
#         'main_nav_icon1': 'fas fa-code',
#         'main_nav_icon2': 'fas fa-palette', 
#         'main_nav_icon3': 'fas fa-js-square'
#     }
#     
#     # JavaScript: closeMobileSidebar(); (handled by CSS/JS on frontend)
#     return render_template('dashboard/dashboard.html', **context)

# @app.route('/dashboard/<language>/<subsection>')
# def language_subsection(language, subsection):
#     """Subsection route - handles sidebar navigation"""
#     section = language.lower()
#     nav_data = update_navigation_server(section)
#     content_data = update_content_server(section, subsection)
#     
#     context = {
#         'dashboard_title': 'Front-End Insights',
#         'dashboard_title_icon': 'fas fa-chart-line',
#         'current_section': section,
#         'page_title': nav_data['page_title'],
#         'sidebar_title': nav_data['title'],
#         'sidebar_nav': nav_data['sidebar'],
#         'current_subsection': subsection,
#         'content_title': content_data['title'],
#         'content_body': content_data['content'],
#         'nav_item1': 'HTML',
#         'nav_item2': 'CSS',
#         'nav_item3': 'JavaScript',
#         'main_nav_icon1': 'fas fa-code',
#         'main_nav_icon2': 'fas fa-palette',
#         'main_nav_icon3': 'fas fa-js-square'
#     }
#     
#     return render_template('dashboard/dashboard.html', **context)

# ==============================================================================
# INSTRUCTIONS FOR INTEGRATION
# ==============================================================================

"""
To integrate this into your server.py file:

1. Copy all the code above (NAVIGATION_DATA, functions, etc.) 

2. Uncomment and add the two route handlers:
   - language_dashboard(language) 
   - language_subsection(language, subsection)

3. Make sure you have these imports in your server.py:
   from flask import Flask, render_template, request, redirect, url_for

4. Your JavaScript navigation will now work server-side!

The behavior is identical to your JavaScript:
- Click navigation link → Flask route handles it
- updateNavigation() → update_navigation_server() 
- updateContent() → update_content_server()
- Template renders with new data
- Mobile sidebar closes via CSS
"""