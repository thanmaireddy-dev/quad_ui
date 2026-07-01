html_block = '''
  <!-- ============================================================
     CONFESSIONS FEED
     ============================================================ -->
  <div class="phone-wrapper" id="screen-confessions" style="display: none;">
    <div class="phone-label">Confessions Screen</div>
    <div class="phone-frame">
      <div class="status-bar light">
        <span class="status-time">9:41</span>
        <div class="status-icons">
          <div class="signal-bars"><span></span><span></span><span></span><span></span></div>
          <div class="battery">
            <div class="battery-fill"></div>
          </div>
        </div>
      </div>

      <div class="screen-content confessions-content">
        <!-- Confessions Header -->
        <div class="confessions-header">
          <div class="confessions-title-group">
            <h1 class="confessions-title">Confessions Feed</h1>
            <p class="confessions-subtitle">Anonymous stories from your campus</p>
          </div>
          <button class="confessions-settings-btn" aria-label="Settings">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <circle cx="12" cy="12" r="3"></circle>
              <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
            </svg>
          </button>
        </div>

        <!-- Filter Tabs -->
        <div class="confessions-filter-tabs">
          <button class="filter-tab active">Trending</button>
          <button class="filter-tab">Recent</button>
          <button class="filter-tab">Mine</button>
        </div>

        <!-- Streak Card -->
        <div class="confessions-streak-card">
          <div class="streak-header">
            <span class="streak-fire">🔥</span>
            <span class="streak-title">4 Day Streak</span>
          </div>
          <p class="streak-text">Keep sharing, stay connected.</p>
          <div class="streak-progress-bar">
            <div class="streak-progress-fill" style="width: 57%;"></div>
          </div>
        </div>

        <!-- Campus Pulse -->
        <div class="campus-pulse-card">
          <h3 class="pulse-title">Campus Pulse</h3>
          <div class="pulse-stats">
            <div class="pulse-stat">
              <span class="pulse-stat-val">213</span>
              <span class="pulse-stat-label">confessions today</span>
            </div>
            <div class="pulse-divider"></div>
            <div class="pulse-stat">
              <span class="pulse-stat-val">Library</span>
              <span class="pulse-stat-label">most active location</span>
            </div>
            <div class="pulse-divider"></div>
            <div class="pulse-stat">
              <span class="pulse-stat-val">Finals</span>
              <span class="pulse-stat-label">trending topic</span>
            </div>
          </div>
        </div>

        <!-- Featured Confession -->
        <div class="confession-card featured">
          <div class="confession-header">
            <div class="confession-tag">Featured</div>
            <div class="confession-time">2h ago</div>
          </div>
          <p class="confession-text">I accidentally made eye contact with my crush in the dining hall and instead of smiling, I panicked and shoved a whole unpeeled banana in my mouth. I have to transfer now right?</p>
          <div class="confession-reaction-row">
            <button class="reaction-btn like-btn">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
              <span>1.2k</span>
            </button>
            <button class="reaction-btn comment-btn">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
              <span>45</span>
            </button>
            <button class="reaction-btn share-btn" style="margin-left: auto;">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </button>
          </div>
        </div>

        <!-- Confession Feed -->
        <div class="confession-card">
          <div class="confession-header">
            <div class="confession-tag">Crush</div>
            <div class="confession-time">4h ago</div>
          </div>
          <p class="confession-text">To the guy with the green beanie in intro to psych: your notes are immaculate and your handwriting is literally art. Please sit next to me again.</p>
          <div class="confession-reaction-row">
            <button class="reaction-btn like-btn">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
              <span>342</span>
            </button>
            <button class="reaction-btn comment-btn">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
              <span>12</span>
            </button>
            <button class="reaction-btn share-btn" style="margin-left: auto;">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </button>
          </div>
        </div>

        <div class="confession-card">
          <div class="confession-header">
            <div class="confession-tag">Academic</div>
            <div class="confession-time">5h ago</div>
          </div>
          <p class="confession-text">I just submitted a 10 page paper that I wrote entirely between 2 AM and 6 AM. I don't even know what I argued but I cited 15 sources so let's hope for the best.</p>
          <div class="confession-reaction-row">
            <button class="reaction-btn like-btn">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
              <span>891</span>
            </button>
            <button class="reaction-btn comment-btn">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
              <span>64</span>
            </button>
            <button class="reaction-btn share-btn" style="margin-left: auto;">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </button>
          </div>
        </div>
        
        <!-- Space at bottom for floating button -->
        <div style="height: 80px;"></div>

        <!-- Floating Action Button -->
        <button class="fab-share">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          Share Anonymously
        </button>

      </div>
      <div class="app-nav">
        <!-- Will be replaced by replace_nav.py -->
      </div>
    </div>
  </div>
'''

with open('c:/frontend_quad/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '<!-- ============================================================\n     JAVASCRIPT – Interaction Logic'
new_content = content.replace(target, html_block + '\n  ' + target)

with open('c:/frontend_quad/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
