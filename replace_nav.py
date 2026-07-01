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
        
        <button class="app-nav-item{' active' if active_tab == 'confessions' else ''}" onclick="document.querySelectorAll('.phone-wrapper').forEach(w => w.style.display='none'); document.getElementById('screen-confessions').style.display='flex';">
          <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
          </svg>
          <span class="nav-label">Confessions</span>
          <div class="nav-active-indicator"></div>
        </button>

        <button class="app-nav-item{' active' if active_tab == 'messages' else ''}" onclick="document.querySelectorAll('.phone-wrapper').forEach(w => w.style.display='none'); document.getElementById('screen-messages').style.display='flex';">
          <div class="nav-notification-dot"></div>
          <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
            <polyline points="22,6 12,13 2,6"></polyline>
          </svg>
          <span class="nav-label">Messages</span>
          <div class="nav-active-indicator"></div>
        </button>

        <button class="app-nav-item{' active' if active_tab == 'profile' else ''}" onclick="document.querySelectorAll('.phone-wrapper').forEach(w => w.style.display='none'); document.getElementById('screen-profile').style.display='flex';">
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
    elif "confessions" in screen_id:
        active = "confessions"
    elif "messages" in screen_id:
        active = "messages"
    elif "profile" in screen_id:
        active = "profile"
        
    return get_nav_html(active, is_disabled)

# Match <div class="app-nav"[^>]*>...</div> where </div> is exactly the closing tag for app-nav.
# We know the inner structure only has <button>...</button>, so the first </div> that is indented at exactly 6 spaces is the closing one.
# Wait, the app-nav is closed by </div> that is 6 spaces indented.
# A regex to match up to the first occurrence of \n      </div>
new_content = re.sub(r'      <div class="app-nav"[^>]*>.*?\n      </div>', replacer, content, flags=re.DOTALL)

with open('c:/frontend_quad/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
