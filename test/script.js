// Navigation data structure
const navigationData = {
    analytics: {
        title: 'Analytics',
        pageTitle: 'Analytics Dashboard',
        sidebar: [
            { icon: 'fas fa-chart-area', text: 'Overview', id: 'overview' },
            { icon: 'fas fa-chart-line', text: 'Traffic', id: 'traffic' },
            { icon: 'fas fa-chart-pie', text: 'Conversions', id: 'conversions' },
            { icon: 'fas fa-users', text: 'Audience', id: 'audience' },
            { icon: 'fas fa-mobile-alt', text: 'Devices', id: 'devices' },
            { icon: 'fas fa-clock', text: 'Real-time', id: 'realtime' }
        ]
    },
    projects: {
        title: 'Projects',
        pageTitle: 'Project Management',
        sidebar: [
            { icon: 'fas fa-list', text: 'All Projects', id: 'all-projects' },
            { icon: 'fas fa-play', text: 'Active', id: 'active-projects' },
            { icon: 'fas fa-pause', text: 'On Hold', id: 'onhold-projects' },
            { icon: 'fas fa-check-circle', text: 'Completed', id: 'completed-projects' },
            { icon: 'fas fa-calendar', text: 'Timeline', id: 'project-timeline' },
            { icon: 'fas fa-users-cog', text: 'Team', id: 'project-team' }
        ]
    },
    users: {
        title: 'Users',
        pageTitle: 'User Management',
        sidebar: [
            { icon: 'fas fa-users', text: 'All Users', id: 'all-users' },
            { icon: 'fas fa-user-plus', text: 'Add User', id: 'add-user' },
            { icon: 'fas fa-user-shield', text: 'Admins', id: 'admin-users' },
            { icon: 'fas fa-user-check', text: 'Active Users', id: 'active-users' },
            { icon: 'fas fa-user-times', text: 'Inactive Users', id: 'inactive-users' },
            { icon: 'fas fa-id-badge', text: 'Roles', id: 'user-roles' }
        ]
    },
    settings: {
        title: 'Settings',
        pageTitle: 'System Settings',
        sidebar: [
            { icon: 'fas fa-cog', text: 'General', id: 'general-settings' },
            { icon: 'fas fa-shield-alt', text: 'Security', id: 'security-settings' },
            { icon: 'fas fa-bell', text: 'Notifications', id: 'notification-settings' },
            { icon: 'fas fa-palette', text: 'Appearance', id: 'appearance-settings' },
            { icon: 'fas fa-database', text: 'Backup', id: 'backup-settings' },
            { icon: 'fas fa-plug', text: 'Integrations', id: 'integration-settings' }
        ]
    }
};

// Content templates for each section
const contentTemplates = {
    analytics: {
        overview: {
            title: 'Analytics Overview',
            content: `
                <div class="stats-grid">
                    <div class="stat-card">
                        <h3>Total Visitors</h3>
                        <div class="value">24,532</div>
                        <div class="change positive">+12.5% from last month</div>
                    </div>
                    <div class="stat-card">
                        <h3>Page Views</h3>
                        <div class="value">156,890</div>
                        <div class="change positive">+8.2% from last month</div>
                    </div>
                    <div class="stat-card">
                        <h3>Bounce Rate</h3>
                        <div class="value">34.2%</div>
                        <div class="change negative">-2.1% from last month</div>
                    </div>
                    <div class="stat-card">
                        <h3>Conversion Rate</h3>
                        <div class="value">3.8%</div>
                        <div class="change positive">+0.7% from last month</div>
                    </div>
                </div>
                <div style="margin-top: 2rem;">
                    <h3 style="margin-bottom: 1rem; color: #1e293b;">Recent Activity</h3>
                    <div style="background: #f8fafc; padding: 2rem; border-radius: 8px; text-align: center; color: #64748b;">
                        <i class="fas fa-chart-line" style="font-size: 3rem; margin-bottom: 1rem; color: #cbd5e1;"></i>
                        <p>Analytics data visualization would appear here</p>
                    </div>
                </div>
            `
        },
        traffic: {
            title: 'Traffic Analytics',
            content: `
                <div style="background: #f8fafc; padding: 2rem; border-radius: 8px; text-align: center; color: #64748b; margin-bottom: 2rem;">
                    <i class="fas fa-chart-line" style="font-size: 3rem; margin-bottom: 1rem; color: #cbd5e1;"></i>
                    <h3 style="color: #475569; margin-bottom: 0.5rem;">Traffic Overview</h3>
                    <p>Detailed traffic analytics and charts would be displayed here</p>
                </div>
                <div class="stats-grid">
                    <div class="stat-card">
                        <h3>Organic Traffic</h3>
                        <div class="value">18,420</div>
                        <div class="change positive">+15.3% from last month</div>
                    </div>
                    <div class="stat-card">
                        <h3>Direct Traffic</h3>
                        <div class="value">4,832</div>
                        <div class="change positive">+5.1% from last month</div>
                    </div>
                    <div class="stat-card">
                        <h3>Referral Traffic</h3>
                        <div class="value">1,280</div>
                        <div class="change negative">-2.8% from last month</div>
                    </div>
                </div>
            `
        }
    },
    projects: {
        'all-projects': {
            title: 'All Projects',
            content: `
                <div style="margin-bottom: 2rem;">
                    <h3 style="margin-bottom: 1rem; color: #1e293b;">Project Overview</h3>
                    <ul class="list-group">
                        <li class="list-item">
                            <div class="item-info">
                                <h4>Website Redesign</h4>
                                <p>Complete overhaul of company website</p>
                            </div>
                            <span class="item-status status-active">Active</span>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>Mobile App Development</h4>
                                <p>iOS and Android app development</p>
                            </div>
                            <span class="item-status status-pending">In Progress</span>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>Database Migration</h4>
                                <p>Migrate to new cloud infrastructure</p>
                            </div>
                            <span class="item-status status-inactive">On Hold</span>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>API Integration</h4>
                                <p>Third-party service integrations</p>
                            </div>
                            <span class="item-status status-active">Active</span>
                        </li>
                    </ul>
                </div>
            `
        },
        'active-projects': {
            title: 'Active Projects',
            content: `
                <div style="margin-bottom: 2rem;">
                    <h3 style="margin-bottom: 1rem; color: #1e293b;">Currently Active Projects</h3>
                    <ul class="list-group">
                        <li class="list-item">
                            <div class="item-info">
                                <h4>Website Redesign</h4>
                                <p>Progress: 75% | Due: Next week</p>
                            </div>
                            <span class="item-status status-active">Active</span>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>API Integration</h4>
                                <p>Progress: 45% | Due: End of month</p>
                            </div>
                            <span class="item-status status-active">Active</span>
                        </li>
                    </ul>
                </div>
            `
        }
    },
    users: {
        'all-users': {
            title: 'All Users',
            content: `
                <div style="margin-bottom: 2rem;">
                    <h3 style="margin-bottom: 1rem; color: #1e293b;">User Directory</h3>
                    <ul class="list-group">
                        <li class="list-item">
                            <div class="item-info">
                                <h4>John Doe</h4>
                                <p>Administrator • john.doe@company.com</p>
                            </div>
                            <span class="item-status status-active">Active</span>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>Jane Smith</h4>
                                <p>Project Manager • jane.smith@company.com</p>
                            </div>
                            <span class="item-status status-active">Active</span>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>Mike Johnson</h4>
                                <p>Developer • mike.johnson@company.com</p>
                            </div>
                            <span class="item-status status-inactive">Inactive</span>
                        </li>
                        <li class="list-item">
                            <div class="item-info">
                                <h4>Sarah Wilson</h4>
                                <p>Designer • sarah.wilson@company.com</p>
                            </div>
                            <span class="item-status status-pending">Pending</span>
                        </li>
                    </ul>
                </div>
            `
        },
        'add-user': {
            title: 'Add New User',
            content: `
                <div style="max-width: 600px;">
                    <h3 style="margin-bottom: 1.5rem; color: #1e293b;">Create New User Account</h3>
                    <form style="display: grid; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #374151;">Full Name</label>
                            <input type="text" style="width: 100%; padding: 0.75rem; border: 1px solid #d1d5db; border-radius: 6px;" placeholder="Enter full name">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #374151;">Email Address</label>
                            <input type="email" style="width: 100%; padding: 0.75rem; border: 1px solid #d1d5db; border-radius: 6px;" placeholder="Enter email address">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #374151;">Role</label>
                            <select style="width: 100%; padding: 0.75rem; border: 1px solid #d1d5db; border-radius: 6px;">
                                <option>Select a role</option>
                                <option>Administrator</option>
                                <option>Project Manager</option>
                                <option>Developer</option>
                                <option>Designer</option>
                            </select>
                        </div>
                        <div style="margin-top: 1rem;">
                            <button type="submit" class="btn btn-primary">Create User</button>
                        </div>
                    </form>
                </div>
            `
        }
    },
    settings: {
        'general-settings': {
            title: 'General Settings',
            content: `
                <div style="max-width: 600px;">
                    <h3 style="margin-bottom: 1.5rem; color: #1e293b;">General Configuration</h3>
                    <div style="display: grid; gap: 1.5rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #374151;">Company Name</label>
                            <input type="text" style="width: 100%; padding: 0.75rem; border: 1px solid #d1d5db; border-radius: 6px;" value="Your Company Name">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #374151;">Time Zone</label>
                            <select style="width: 100%; padding: 0.75rem; border: 1px solid #d1d5db; border-radius: 6px;">
                                <option>UTC-05:00 Eastern Time</option>
                                <option>UTC-06:00 Central Time</option>
                                <option>UTC-07:00 Mountain Time</option>
                                <option>UTC-08:00 Pacific Time</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #374151;">Language</label>
                            <select style="width: 100%; padding: 0.75rem; border: 1px solid #d1d5db; border-radius: 6px;">
                                <option>English</option>
                                <option>Spanish</option>
                                <option>French</option>
                                <option>German</option>
                            </select>
                        </div>
                        <div style="margin-top: 1rem;">
                            <button type="button" class="btn btn-primary">Save Settings</button>
                        </div>
                    </div>
                </div>
            `
        },
        'security-settings': {
            title: 'Security Settings',
            content: `
                <div style="max-width: 600px;">
                    <h3 style="margin-bottom: 1.5rem; color: #1e293b;">Security Configuration</h3>
                    <div style="display: grid; gap: 1.5rem;">
                        <div style="padding: 1rem; background: #f8fafc; border-radius: 8px;">
                            <h4 style="color: #1e293b; margin-bottom: 0.5rem;">Two-Factor Authentication</h4>
                            <p style="color: #64748b; font-size: 0.9rem; margin-bottom: 1rem;">Add an extra layer of security to your account</p>
                            <button class="btn btn-primary">Enable 2FA</button>
                        </div>
                        <div style="padding: 1rem; background: #f8fafc; border-radius: 8px;">
                            <h4 style="color: #1e293b; margin-bottom: 0.5rem;">Password Policy</h4>
                            <p style="color: #64748b; font-size: 0.9rem; margin-bottom: 1rem;">Configure password requirements for all users</p>
                            <button class="btn btn-secondary">Configure</button>
                        </div>
                        <div style="padding: 1rem; background: #f8fafc; border-radius: 8px;">
                            <h4 style="color: #1e293b; margin-bottom: 0.5rem;">Login History</h4>
                            <p style="color: #64748b; font-size: 0.9rem; margin-bottom: 1rem;">View recent login activity</p>
                            <button class="btn btn-secondary">View History</button>
                        </div>
                    </div>
                </div>
            `
        }
    }
};

// DOM Elements
const topNavLinks = document.querySelectorAll('.nav-link[data-section]');
const sidebar = document.getElementById('sidebar');
const sidebarTitle = document.getElementById('sidebar-title');
const sidebarNav = document.getElementById('sidebar-nav');
const pageTitle = document.getElementById('page-title');
const contentBody = document.getElementById('content-body');
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const overlay = document.getElementById('overlay');

// Current state
let currentSection = 'analytics';
let currentSubSection = 'overview';

// Initialize the dashboard
function initializeDashboard() {
    updateNavigation('analytics');
    updateContent('analytics', 'overview');
}

// Update main navigation
function updateNavigation(section) {
    // Update active state in top nav
    topNavLinks.forEach(link => {
        link.classList.remove('active');
        if (link.dataset.section === section) {
            link.classList.add('active');
        }
    });

    // Update sidebar
    const sectionData = navigationData[section];
    sidebarTitle.textContent = sectionData.title;
    pageTitle.textContent = sectionData.pageTitle;

    // Generate sidebar navigation
    const sidebarHTML = `
        <ul>
            ${sectionData.sidebar.map(item => `
                <li>
                    <a href="#" data-subsection="${item.id}" class="${item.id === getDefaultSubSection(section) ? 'active' : ''}">
                        <i class="${item.icon}"></i>
                        ${item.text}
                    </a>
                </li>
            `).join('')}
        </ul>
    `;
    
    sidebarNav.innerHTML = sidebarHTML;

    // Add event listeners to sidebar links
    const sidebarLinks = sidebarNav.querySelectorAll('a[data-subsection]');
    sidebarLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const subSection = link.dataset.subsection;
            updateSidebarActive(subSection);
            updateContent(section, subSection);
            closeMobileSidebar();
        });
    });

    currentSection = section;
}

// Update sidebar active state
function updateSidebarActive(subSection) {
    const sidebarLinks = sidebarNav.querySelectorAll('a[data-subsection]');
    sidebarLinks.forEach(link => {
        link.classList.remove('active');
        if (link.dataset.subsection === subSection) {
            link.classList.add('active');
        }
    });
}

// Get default subsection for a section
function getDefaultSubSection(section) {
    return navigationData[section].sidebar[0].id;
}

// Update main content
function updateContent(section, subSection) {
    const template = contentTemplates[section]?.[subSection];
    
    if (template) {
        contentBody.innerHTML = `
            <div>
                <h2 style="color: #1e293b; margin-bottom: 1.5rem; font-size: 1.5rem; font-weight: 600;">${template.title}</h2>
                ${template.content}
            </div>
        `;
    } else {
        contentBody.innerHTML = `
            <div style="text-align: center; padding: 4rem 2rem; color: #64748b;">
                <i class="fas fa-file-alt" style="font-size: 4rem; margin-bottom: 1rem; color: #cbd5e1;"></i>
                <h3 style="color: #475569; margin-bottom: 0.5rem;">Content Not Available</h3>
                <p>The content for this section is currently being developed.</p>
            </div>
        `;
    }
    
    currentSubSection = subSection;
}

// Mobile menu functions
function openMobileSidebar() {
    sidebar.classList.add('open');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeMobileSidebar() {
    sidebar.classList.remove('open');
    overlay.classList.remove('active');
    document.body.style.overflow = '';
}

// Event listeners
topNavLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const section = link.dataset.section;
        updateNavigation(section);
        updateContent(section, getDefaultSubSection(section));
        closeMobileSidebar();
    });
});

mobileMenuToggle.addEventListener('click', () => {
    if (sidebar.classList.contains('open')) {
        closeMobileSidebar();
    } else {
        openMobileSidebar();
    }
});

overlay.addEventListener('click', closeMobileSidebar);

// Handle window resize
window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        closeMobileSidebar();
    }
});

// Initialize the dashboard when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeDashboard);