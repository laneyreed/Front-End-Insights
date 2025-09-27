# Add this code to your existing server.py file

from flask import Flask, render_template, request, redirect, url_for, jsonify

# Navigation data structure (equivalent to JavaScript navigationData)
NAVIGATION_DATA = {
    'html': {
        'title': 'HTML',
        'pageTitle': 'HTML Dashboard',
        'sidebar': [
            {'icon': 'fas fa-chart-area', 'text': 'Overview', 'id': 'overview'},
            {'icon': 'fas fa-chart-line', 'text': 'Elements', 'id': 'elements'},
            {'icon': 'fas fa-chart-pie', 'text': 'Forms', 'id': 'forms'},
            {'icon': 'fas fa-users', 'text': 'Semantic', 'id': 'semantic'},
            {'icon': 'fas fa-mobile-alt', 'text': 'Accessibility', 'id': 'accessibility'},
            {'icon': 'fas fa-clock', 'text': 'Best Practices', 'id': 'best-practices'}
        ]
    },
    'css': {
        'title': 'CSS',
        'pageTitle': 'CSS Dashboard',
        'sidebar': [
            {'icon': 'fas fa-palette', 'text': 'Overview', 'id': 'overview'},
            {'icon': 'fas fa-paint-brush', 'text': 'Selectors', 'id': 'selectors'},
            {'icon': 'fas fa-layer-group', 'text': 'Layouts', 'id': 'layouts'},
            {'icon': 'fas fa-mobile-alt', 'text': 'Responsive', 'id': 'responsive'},
            {'icon': 'fas fa-magic', 'text': 'Animations', 'id': 'animations'},
            {'icon': 'fas fa-cogs', 'text': 'Frameworks', 'id': 'frameworks'}
        ]
    },
    'javascript': {
        'title': 'JavaScript',
        'pageTitle': 'JavaScript Dashboard',
        'sidebar': [
            {'icon': 'fas fa-code', 'text': 'Overview', 'id': 'overview'},
            {'icon': 'fas fa-function', 'text': 'Functions', 'id': 'functions'},
            {'icon': 'fas fa-object-group', 'text': 'Objects', 'id': 'objects'},
            {'icon': 'fas fa-sync-alt', 'text': 'Async/Await', 'id': 'async'},
            {'icon': 'fas fa-dom', 'text': 'DOM', 'id': 'dom'},
            {'icon': 'fas fa-plug', 'text': 'APIs', 'id': 'apis'}
        ]
    }
}

# Content templates (equivalent to JavaScript contentTemplates)
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
                    <p>Learn the building blocks of web development with HTML5 semantic elements, forms, and accessibility best practices.</p>
                </div>
            '''
        },
        'elements': {
            'title': 'HTML Elements',
            'content': '''
                <div style="margin-bottom: 2rem;">
                    <h3>Common HTML Elements</h3>
                    <ul class="list-group">
                        <li class="list-item">
                            <div class="item-info">
                                <h4>&lt;div&gt;</h4>
                                <p>Generic container element</p>
                            </div>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>&lt;span&gt;</h4>
                                <p>Inline generic container</p>
                            </div>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>&lt;p&gt;</h4>
                                <p>Paragraph element</p>
                            </div>
                        </li>
                    </ul>
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
                    <div class="stat-card">
                        <h3>Pseudo-classes</h3>
                        <div class="value">40+</div>
                        <div class="change positive">Interactive States</div>
                    </div>
                </div>
                <div style="margin-top: 2rem;">
                    <h3>CSS Fundamentals</h3>
                    <p>Master styling, layouts, animations, and responsive design with modern CSS3 techniques.</p>
                </div>
            '''
        },
        'selectors': {
            'title': 'CSS Selectors',
            'content': '''
                <div style="margin-bottom: 2rem;">
                    <h3>Selector Types</h3>
                    <ul class="list-group">
                        <li class="list-item">
                            <div class="item-info">
                                <h4>Element Selector</h4>
                                <p>h1, p, div { }</p>
                            </div>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>Class Selector</h4>
                                <p>.class-name { }</p>
                            </div>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>ID Selector</h4>
                                <p>#id-name { }</p>
                            </div>
                        </li>
                    </ul>
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
                    <div class="stat-card">
                        <h3>Methods</h3>
                        <div class="value">200+</div>
                        <div class="change positive">Array & Object Methods</div>
                    </div>
                </div>
                <div style="margin-top: 2rem;">
                    <h3>JavaScript Fundamentals</h3>
                    <p>Learn modern JavaScript, async programming, DOM manipulation, and API integration.</p>
                </div>
            '''
        },
        'functions': {
            'title': 'JavaScript Functions',
            'content': '''
                <div style="margin-bottom: 2rem;">
                    <h3>Function Types</h3>
                    <ul class="list-group">
                        <li class="list-item">
                            <div class="item-info">
                                <h4>Function Declaration</h4>
                                <p>function name() { }</p>
                            </div>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>Arrow Function</h4>
                                <p>const name = () => { }</p>
                            </div>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>Anonymous Function</h4>
                                <p>function() { }</p>
                            </div>
                        </li>
                    </ul>
                </div>
            '''
        }
    }
}

def get_default_subsection(section):
    """Get the default subsection for a given section (first sidebar item)"""
    if section in NAVIGATION_DATA:
        return NAVIGATION_DATA[section]['sidebar'][0]['id']
    return 'overview'

def update_navigation_data(section):
    """
    Python equivalent of JavaScript updateNavigation() function
    Returns navigation data for the specified section
    """
    if section not in NAVIGATION_DATA:
        section = 'html'  # Default fallback
    
    section_data = NAVIGATION_DATA[section]
    default_subsection = get_default_subsection(section)
    
    return {
        'section': section,
        'title': section_data['title'],
        'page_title': section_data['pageTitle'],
        'sidebar': section_data['sidebar'],
        'default_subsection': default_subsection,
        'current_section': section
    }

def update_content_data(section, subsection=None):
    """
    Python equivalent of JavaScript updateContent() function
    Returns content for the specified section and subsection
    """
    if section not in NAVIGATION_DATA:
        section = 'html'  # Default fallback
    
    if subsection is None:
        subsection = get_default_subsection(section)
    
    # Get content template
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

# Add these route handlers to your existing Flask app:

# Main route that mimics the JavaScript event listener behavior
def language_dashboard_handler(app):
    """
    This function mimics the JavaScript:
    topNavLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const section = link.dataset.section;
            updateNavigation(section);
            updateContent(section, getDefaultSubSection(section));
            closeMobileSidebar();
        });
    });
    """
    
    @app.route('/dashboard/<language>')
    def language_dashboard(language):
        # Equivalent to: const section = link.dataset.section
        section = language.lower()
        
        # Equivalent to: updateNavigation(section)
        nav_data = update_navigation_data(section)
        
        # Equivalent to: updateContent(section, getDefaultSubSection(section))
        content_data = update_content_data(section, nav_data['default_subsection'])
        
        # Prepare template context
        template_context = {
            # Navigation data
            'current_section': nav_data['section'],
            'dashboard_title': 'Front-End Insights',
            'dashboard_title_icon': 'fas fa-chart-line',
            'page_title': nav_data['page_title'],
            'sidebar_title': nav_data['title'],
            'sidebar_nav': nav_data['sidebar'],
            
            # Content data
            'content_title': content_data['title'],
            'content_body': content_data['content'],
            'current_subsection': content_data['subsection'],
            
            # Navigation items for template
            'nav_item1': 'HTML',
            'nav_item2': 'CSS', 
            'nav_item3': 'JavaScript',
            'main_nav_icon1': 'fas fa-code',
            'main_nav_icon2': 'fas fa-palette',
            'main_nav_icon3': 'fas fa-js-square',
            
            # Active states for navigation highlighting
            'html_active': 'active' if section == 'html' else '',
            'css_active': 'active' if section == 'css' else '',
            'js_active': 'active' if section == 'javascript' else ''
        }
        
        # closeMobileSidebar() equivalent handled by template/CSS
        return render_template('dashboard/dashboard.html', **template_context)
    
    @app.route('/dashboard/<language>/<subsection>')
    def language_subsection(language, subsection):
        """Handle subsection navigation"""
        section = language.lower()
        
        # Update navigation and content for specific subsection
        nav_data = update_navigation_data(section)
        content_data = update_content_data(section, subsection)
        
        template_context = {
            'current_section': nav_data['section'],
            'dashboard_title': 'Front-End Insights',
            'dashboard_title_icon': 'fas fa-chart-line',
            'page_title': nav_data['page_title'],
            'sidebar_title': nav_data['title'],
            'sidebar_nav': nav_data['sidebar'],
            
            'content_title': content_data['title'],
            'content_body': content_data['content'],
            'current_subsection': content_data['subsection'],
            
            'nav_item1': 'HTML',
            'nav_item2': 'CSS', 
            'nav_item3': 'JavaScript',
            'main_nav_icon1': 'fas fa-code',
            'main_nav_icon2': 'fas fa-palette',
            'main_nav_icon3': 'fas fa-js-square',
            
            'html_active': 'active' if section == 'html' else '',
            'css_active': 'active' if section == 'css' else '',
            'js_active': 'active' if section == 'javascript' else ''
        }
        
        return render_template('dashboard/dashboard.html', **template_context)

# Usage in your server.py file:
"""
# In your main server.py file, add this code:

# Import the navigation functions and data
from server_navigation_code import (
    NAVIGATION_DATA,
    CONTENT_TEMPLATES,
    update_navigation_data,
    update_content_data,
    get_default_subsection,
    language_dashboard_handler
)

# Initialize the route handlers
language_dashboard_handler(app)

# That's it! Your Flask app now mimics the JavaScript navigation behavior
"""