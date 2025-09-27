# server.py - Navigation handling code to mimic JavaScript functionality

from flask import Flask, render_template, request, redirect, url_for, jsonify

# Navigation data structure (equivalent to JavaScript navigationData)
NAVIGATION_DATA = {
    'html': {
        'title': 'HTML',
        'pageTitle': 'HTML Dashboard',
        'sidebar': [
            {'icon': 'fas fa-chart-area', 'text': 'Overview', 'id': 'overview'},
            {'icon': 'fas fa-chart-line', 'text': 'Traffic', 'id': 'traffic'},
            {'icon': 'fas fa-chart-pie', 'text': 'Conversions', 'id': 'conversions'},
            {'icon': 'fas fa-users', 'text': 'Audience', 'id': 'audience'},
            {'icon': 'fas fa-mobile-alt', 'text': 'Devices', 'id': 'devices'},
            {'icon': 'fas fa-clock', 'text': 'Real-time', 'id': 'realtime'}
        ]
    },
    'css': {
        'title': 'CSS',
        'pageTitle': 'CSS Dashboard',
        'sidebar': [
            {'icon': 'fas fa-palette', 'text': 'Styles Overview', 'id': 'overview'},
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
            {'icon': 'fas fa-code', 'text': 'Fundamentals', 'id': 'overview'},
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
                    <p>Learn the building blocks of web development with HTML5 semantic elements, forms, and accessibility.</p>
                </div>
            '''
        },
        'traffic': {
            'title': 'HTML Structure',
            'content': '''
                <div style="margin-bottom: 2rem;">
                    <h3>Document Structure</h3>
                    <pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Document&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;main&gt;Content here&lt;/main&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
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
                    <h3>CSS Fundamentals</h3>
                    <p>Master styling, layouts, animations, and responsive design with CSS3.</p>
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
                    <h3>JavaScript Fundamentals</h3>
                    <p>Learn modern JavaScript, async programming, and DOM manipulation.</p>
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

def update_navigation(section):
    """
    Equivalent to JavaScript updateNavigation() function
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

def update_content(section, subsection=None):
    """
    Equivalent to JavaScript updateContent() function
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

# Flask route handlers that mimic the JavaScript event listener behavior

@app.route('/dashboard/<language>')
def language_dashboard(language):
    """
    Main route that mimics the JavaScript topNavLinks event listener
    This is equivalent to: link.addEventListener('click', (e) => {...})
    """
    # Equivalent to: const section = link.dataset.section
    section = language.lower()
    
    # Equivalent to: updateNavigation(section)
    nav_data = update_navigation(section)
    
    # Equivalent to: updateContent(section, getDefaultSubSection(section))
    content_data = update_content(section, nav_data['default_subsection'])
    
    # Template context data to pass to the template
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
        
        # Navigation items (for top nav)
        'nav_item1': 'HTML',
        'nav_item2': 'CSS', 
        'nav_item3': 'JavaScript',
        'main_nav_icon1': 'fas fa-code',
        'main_nav_icon2': 'fas fa-palette',
        'main_nav_icon3': 'fas fa-js-square',
        
        # Active states
        'html_active': 'active' if section == 'html' else '',
        'css_active': 'active' if section == 'css' else '',
        'js_active': 'active' if section == 'javascript' else ''
    }
    
    # Equivalent to: closeMobileSidebar() - handled by template/CSS
    return render_template('dashboard/dashboard.html', **template_context)

@app.route('/dashboard/<language>/<subsection>')
def language_subsection(language, subsection):
    """
    Route for handling subsection navigation
    This mimics the sidebar link event listeners
    """
    section = language.lower()
    
    # Update navigation for the section
    nav_data = update_navigation(section)
    
    # Update content for the specific subsection
    content_data = update_content(section, subsection)
    
    # Same template context as above, but with updated subsection
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

# AJAX route for dynamic content updates (if you want to keep some JavaScript)
@app.route('/api/navigation/<section>')
def api_navigation(section):
    """
    API endpoint that returns navigation data as JSON
    Can be used with JavaScript for dynamic updates
    """
    nav_data = update_navigation(section)
    return jsonify(nav_data)

@app.route('/api/content/<section>/<subsection>')
def api_content(section, subsection):
    """
    API endpoint that returns content data as JSON
    Can be used with JavaScript for dynamic content loading
    """
    content_data = update_content(section, subsection)
    return jsonify(content_data)

# Usage example in your main server.py:
"""
# Add this to your existing server.py file:

# Import the functions at the top
from server_navigation_code import (
    NAVIGATION_DATA, 
    CONTENT_TEMPLATES, 
    update_navigation, 
    update_content, 
    get_default_subsection
)

# Add the route handlers
@app.route('/dashboard/<language>')
def language_dashboard(language):
    # ... (copy the function from above)

@app.route('/dashboard/<language>/<subsection>')  
def language_subsection(language, subsection):
    # ... (copy the function from above)
"""