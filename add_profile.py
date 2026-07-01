html_block = '''
  <!-- ============================================================
     PROFILE SCREEN
     ============================================================ -->
  <div class="phone-wrapper" id="screen-profile" style="display: none;">
    <div class="phone-label">Profile Screen</div>
    <div class="phone-frame">
      <div class="status-bar dark">
        <span class="status-time">9:41</span>
        <div class="status-icons">
          <div class="signal-bars"><span></span><span></span><span></span><span></span></div>
          <div class="battery">
            <div class="battery-fill"></div>
          </div>
        </div>
      </div>

      <div class="screen-content profile-content">

        <!-- Banner -->
        <div class="profile-banner">
          <div class="profile-banner-gradient"></div>
        </div>

        <!-- Profile Header (avatar + completion ring + info) -->
        <div class="profile-header-section">
          <div class="profile-avatar-area">
            <div class="profile-completion-ring" id="profile-ring">
              <svg viewBox="0 0 120 120">
                <circle class="ring-bg" cx="60" cy="60" r="54"></circle>
                <circle class="ring-fill" cx="60" cy="60" r="54" id="profile-ring-fill"></circle>
              </svg>
              <img class="profile-avatar-img" src="my-profile.jpg" alt="Thanmaie" />
              <button class="profile-avatar-edit" aria-label="Edit profile photo">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
              </button>
            </div>
            <div class="profile-completion-label">
              <span class="completion-pct" id="profile-pct-text">0%</span>
              <span class="completion-word">Complete</span>
            </div>
            <p class="profile-completion-hint">Add two more photos to complete your profile.</p>
          </div>

          <!-- User Info -->
          <div class="profile-user-card">
            <div class="profile-name-row">
              <h1 class="profile-display-name">Thanmaie</h1>
              <svg class="profile-verified-badge fill-accent-gold" viewBox="0 0 24 24"><path d="M12 2l3.09 2.26L18.8 3.5l1.05 3.65 3.37 1.77-1.4 3.57.9 3.7-3.1 2.2-1.5 3.5-3.6-1.1-2.9 2.5-2.9-2.5-3.6 1.1-1.5-3.5-.9-3.7-1.4-3.57 3.37-1.77L1.15 7.15 2.2 3.5l3.71.76L9 2zm-.2 12.8l-3.3-3.3-1.4 1.4 4.7 4.7 9.3-9.3-1.4-1.4-7.9 7.9z"/></svg>
              <span class="profile-age-badge">21</span>
            </div>
            <div class="profile-meta-row">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
              <span>Psychology &middot; Junior &middot; UT Austin</span>
            </div>
            <div class="profile-meta-row">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              <span>Austin, TX</span>
            </div>
          </div>
        </div>

        <!-- Quick Actions -->
        <div class="profile-section">
          <div class="profile-quick-actions">
            <button class="quick-action-card">
              <div class="qa-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
              </div>
              <span class="qa-label">Edit Profile</span>
            </button>
            <button class="quick-action-card">
              <div class="qa-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09a1.65 1.65 0 0 0-1.08-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.32 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1.08z"></path></svg>
              </div>
              <span class="qa-label">Preferences</span>
            </button>
            <button class="quick-action-card">
              <div class="qa-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
              </div>
              <span class="qa-label">Privacy</span>
            </button>
            <button class="quick-action-card">
              <div class="qa-icon qa-icon-gold">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
              </div>
              <span class="qa-label">Verified</span>
            </button>
          </div>
        </div>

        <!-- My Photos -->
        <div class="profile-section">
          <h3 class="profile-section-title">My Photos</h3>
          <div class="profile-photos-grid">
            <div class="profile-photo-tile">
              <img src="my-profile.jpg" alt="Photo 1" />
            </div>
            <div class="profile-photo-tile">
              <img src="profile-maya.png" alt="Photo 2" onerror="this.src='my-profile.jpg'" />
            </div>
            <div class="profile-photo-tile">
              <img src="profile-whisky.jpg" alt="Photo 3" onerror="this.src='my-profile.jpg'" />
            </div>
            <div class="profile-photo-tile">
              <img src="profile-debian.jpg" alt="Photo 4" onerror="this.src='my-profile.jpg'" />
            </div>
            <div class="profile-photo-tile">
              <img src="profile-montana.jpg" alt="Photo 5" onerror="this.src='my-profile.jpg'" />
            </div>
            <div class="profile-photo-tile profile-photo-add">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
            </div>
          </div>
        </div>

        <!-- About Me -->
        <div class="profile-section">
          <div class="profile-section-header">
            <h3 class="profile-section-title">About Me</h3>
            <button class="profile-edit-icon" aria-label="Edit about">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
            </button>
          </div>
          <div class="profile-about-card">
            <p>I enjoy exploring coffee shops, late-night walks, and discovering new music. Always looking for the best tacos in Austin. Dog person. Psychology nerd.</p>
          </div>
        </div>

        <!-- Prompts -->
        <div class="profile-section">
          <h3 class="profile-section-title">Prompts</h3>
          <div class="profile-prompts-list">
            <div class="profile-prompt-card">
              <span class="prompt-question">The quickest way to my heart is&hellip;</span>
              <p class="prompt-answer">Recommending a book and actually meaning it.</p>
            </div>
            <div class="profile-prompt-card">
              <span class="prompt-question">My simple pleasures&hellip;</span>
              <p class="prompt-answer">Morning coffee on the porch, thunderstorms, and a really good playlist.</p>
            </div>
            <div class="profile-prompt-card">
              <span class="prompt-question">A typical Sunday&hellip;</span>
              <p class="prompt-answer">Farmers market, brunch with friends, then a movie marathon on the couch.</p>
            </div>
          </div>
        </div>

        <!-- Interests -->
        <div class="profile-section">
          <h3 class="profile-section-title">Interests</h3>
          <div class="profile-interests-wrap">
            <span class="profile-interest-pill">Photography</span>
            <span class="profile-interest-pill">Reading</span>
            <span class="profile-interest-pill">Travel</span>
            <span class="profile-interest-pill">Music</span>
            <span class="profile-interest-pill">Coffee</span>
            <span class="profile-interest-pill">Hiking</span>
            <span class="profile-interest-pill">Coding</span>
            <span class="profile-interest-pill">Film</span>
          </div>
        </div>

        <!-- Campus Identity -->
        <div class="profile-section">
          <h3 class="profile-section-title">Campus Identity</h3>
          <div class="profile-info-card">
            <div class="info-row">
              <span class="info-label">College</span>
              <span class="info-value">University of Texas at Austin</span>
            </div>
            <div class="info-row">
              <span class="info-label">Department</span>
              <span class="info-value">Psychology</span>
            </div>
            <div class="info-row">
              <span class="info-label">Graduation</span>
              <span class="info-value">2026</span>
            </div>
            <div class="info-row">
              <span class="info-label">Campus</span>
              <span class="info-value">Main Campus</span>
            </div>
            <div class="info-row">
              <span class="info-label">Verification</span>
              <span class="info-value info-value-verified">
                <svg class="fill-accent-gold" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="14" height="14"><path d="M12 2l3.09 2.26L18.8 3.5l1.05 3.65 3.37 1.77-1.4 3.57.9 3.7-3.1 2.2-1.5 3.5-3.6-1.1-2.9 2.5-2.9-2.5-3.6 1.1-1.5-3.5-.9-3.7-1.4-3.57 3.37-1.77L1.15 7.15 2.2 3.5l3.71.76L9 2zm-.2 12.8l-3.3-3.3-1.4 1.4 4.7 4.7 9.3-9.3-1.4-1.4-7.9 7.9z"/></svg>
                .edu Verified
              </span>
            </div>
          </div>
        </div>

        <!-- Dating Preferences -->
        <div class="profile-section">
          <h3 class="profile-section-title">Dating Preferences</h3>
          <div class="profile-info-card">
            <div class="info-row">
              <span class="info-label">Looking For</span>
              <span class="info-value">Long-term relationship</span>
            </div>
            <div class="info-row">
              <span class="info-label">Style</span>
              <span class="info-value">Monogamous</span>
            </div>
            <div class="info-row">
              <span class="info-label">Age Range</span>
              <span class="info-value">19 &ndash; 26</span>
            </div>
            <div class="info-row">
              <span class="info-label">Distance</span>
              <span class="info-value">Within 25 mi</span>
            </div>
            <div class="info-row">
              <span class="info-label">Languages</span>
              <span class="info-value">English, Telugu</span>
            </div>
          </div>
        </div>

        <!-- Privacy & Safety -->
        <div class="profile-section">
          <h3 class="profile-section-title">Privacy &amp; Safety</h3>
          <div class="profile-settings-card">
            <button class="settings-row">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"></line></svg>
              <span>Blocked Users</span>
              <span class="settings-chevron">&rsaquo;</span>
            </button>
            <button class="settings-row">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
              <span>Permissions</span>
              <span class="settings-chevron">&rsaquo;</span>
            </button>
            <button class="settings-row">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"></path><line x1="4" y1="22" x2="4" y2="15"></line></svg>
              <span>Report Issue</span>
              <span class="settings-chevron">&rsaquo;</span>
            </button>
            <button class="settings-row">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
              <span>Help Center</span>
              <span class="settings-chevron">&rsaquo;</span>
            </button>
            <button class="settings-row">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              <span>Safety Tips</span>
              <span class="settings-chevron">&rsaquo;</span>
            </button>
          </div>
        </div>

        <!-- App Information -->
        <div class="profile-section profile-app-info">
          <div class="app-info-links">
            <a href="#">Terms of Service</a>
            <span class="app-info-dot">&middot;</span>
            <a href="#">Privacy Policy</a>
            <span class="app-info-dot">&middot;</span>
            <a href="#">Feedback</a>
          </div>
          <div class="app-info-links">
            <a href="#">Rate QUAD</a>
            <span class="app-info-dot">&middot;</span>
            <a href="#">Share QUAD</a>
          </div>
          <p class="app-version">QUAD v1.0.0</p>
          <p class="app-tagline">Made with &hearts; on campus.</p>
        </div>

        <!-- Bottom spacer -->
        <div style="height: 16px;"></div>

      </div>

      <div class="app-nav">
        <!-- Will be replaced by replace_nav.py -->
      </div>
    </div>
  </div>
'''

with open('c:/frontend_quad/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find "JAVASCRIPT" in the comment block
idx = content.find('JAVASCRIPT')
if idx < 0:
    print("ERROR: Could not find JAVASCRIPT marker")
else:
    search_back = content.rfind('<!--', 0, idx)
    if search_back >= 0:
        line_start = content.rfind('\n', 0, search_back)
        if line_start < 0:
            line_start = 0
        else:
            line_start += 1
        
        insert_point = line_start
        new_content = content[:insert_point] + html_block + '\n' + content[insert_point:]
        
        with open('c:/frontend_quad/index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"SUCCESS: Profile HTML inserted at position {insert_point}")
    else:
        print("ERROR: Could not find comment start")
