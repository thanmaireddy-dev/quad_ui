import re

with open('c:/frontend_quad/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def get_nav_html(active_tab, is_disabled=False):
    opacity_style = ' style="opacity: 0.5; pointer-events: none;"' if is_disabled else ''
    
    return f'''      <div class="app-nav"{opacity_style}>
        <button class="app-nav-item{' active' if active_tab == 'discover' else ''}" onclick="document.querySelectorAll('.phone-wrapper').forEach(w => w.style.display='none'); document.getElementById('screen-discover').style.display='flex';">
          <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon>
          </svg>
          <span class="nav-label">Discover</span>
          <div class="nav-active-indicator"></div>
        </button>
        
        <button class="app-nav-item{' active' if active_tab == 'confessions' else ''}" onclick="alert('Confessions coming soon')">
          <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
          </svg>
          <span class="nav-label">Confessions</span>
          <div class="nav-active-indicator"></div>
        </button>

        <div class="app-nav-item app-nav-center{' active' if active_tab == 'flames' else ''}">
          <button class="nav-center-circle" onclick="document.querySelectorAll('.phone-wrapper').forEach(w => w.style.display='none'); document.getElementById('screen-flames').style.display='flex';">
            <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
              <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"></path>
            </svg>
          </button>
          <span class="nav-label">FLAMES</span>
          <div class="nav-active-indicator"></div>
        </div>

        <button class="app-nav-item{' active' if active_tab == 'messages' else ''}" onclick="alert('Messages coming soon')">
          <div class="nav-notification-dot"></div>
          <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
            <polyline points="22,6 12,13 2,6"></polyline>
          </svg>
          <span class="nav-label">Messages</span>
          <div class="nav-active-indicator"></div>
        </button>

        <button class="app-nav-item{' active' if active_tab == 'profile' else ''}" onclick="alert('Profile coming soon')">
          <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
            <circle cx="12" cy="7" r="4"></circle>
          </svg>
          <span class="nav-label">Profile</span>
          <div class="nav-active-indicator"></div>
        </button>
      </div>'''

def replacer(match):
    full_text_before = content[:match.start()]
    id_match = list(re.finditer(r'id="screen-([^"]+)"', full_text_before))
    if id_match:
        screen_id = id_match[-1].group(1)
    else:
        screen_id = "unknown"
        
    is_disabled = "opacity: 0.5" in match.group(0)
    
    active = "discover"
    if "flames" in screen_id:
        active = "flames"
        
    return get_nav_html(active, is_disabled)

# Match <div class="app-nav"[^>]*>...</div> where </div> is exactly the closing tag for app-nav.
# We know the inner structure only has <button>...</button>, so the first </div> that is indented at exactly 6 spaces is the closing one.
# Wait, the app-nav is closed by </div> that is 6 spaces indented.
# A regex to match up to the first occurrence of \n      </div>
new_content = re.sub(r'      <div class="app-nav"[^>]*>.*?\n      </div>', replacer, content, flags=re.DOTALL)

with open('c:/frontend_quad/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
