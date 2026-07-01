html_block = '''
  <!-- ============================================================
     MESSAGES SCREEN
     ============================================================ -->
  <div class="phone-wrapper" id="screen-messages" style="display: none;">
    <div class="phone-label">Messages Screen</div>
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

      <div class="screen-content messages-content">
        <!-- Messages Header -->
        <div class="messages-header">
          <div class="messages-title-group">
            <h1 class="messages-title">Messages</h1>
            <p class="messages-subtitle">Stay connected with your campus.</p>
          </div>
          <button class="messages-search-toggle" aria-label="Search conversations">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>
          </button>
        </div>

        <!-- Search Bar -->
        <div class="messages-search-bar">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>
          <input type="search" placeholder="Search conversations" aria-label="Search conversations" />
        </div>

        <!-- Campus Moments (Quad Moments) -->
        <div class="moments-section">
          <h3 class="moments-label">Quad Moments</h3>
          <div class="moments-scroll">
            <!-- Add Moment (current user) -->
            <div class="moment-item moment-add">
              <div class="moment-ring add-ring">
                <img src="my-profile.jpg" alt="You" onerror="this.src='my-profile.jpg'" />
                <div class="moment-add-badge">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                </div>
              </div>
              <span class="moment-name">Add</span>
            </div>

            <!-- Maya's Moment -->
            <div class="moment-item">
              <div class="moment-ring has-moment">
                <img src="profile-maya.png" alt="Maya" onerror="this.src='my-profile.jpg'" />
              </div>
              <span class="moment-name">Maya</span>
            </div>

            <!-- Whiskey's Moment -->
            <div class="moment-item">
              <div class="moment-ring has-moment">
                <img src="profile-whisky.jpg" alt="Whiskey" onerror="this.src='my-profile.jpg'" />
              </div>
              <span class="moment-name">Whiskey</span>
            </div>

            <!-- Debbie's Moment -->
            <div class="moment-item">
              <div class="moment-ring">
                <img src="profile-debian.jpg" alt="Debbie" onerror="this.src='my-profile.jpg'" />
              </div>
              <span class="moment-name">Debbie</span>
            </div>

            <!-- Charlie's Moment -->
            <div class="moment-item">
              <div class="moment-ring">
                <img src="profile-montana.jpg" alt="Charlie" onerror="this.src='my-profile.jpg'" />
              </div>
              <span class="moment-name">Charlie</span>
            </div>

            <!-- Sophia placeholder -->
            <div class="moment-item">
              <div class="moment-ring has-moment">
                <img src="my-profile.jpg" alt="Sophia" />
              </div>
              <span class="moment-name">Sophia</span>
            </div>
          </div>
        </div>

        <!-- Conversation List -->
        <div class="conversation-list">

          <!-- Conversation: Whiskey (unread, active now) -->
          <div class="conversation-item unread">
            <div class="convo-avatar-wrapper">
              <img class="convo-avatar" src="profile-whisky.jpg" alt="Whiskey" onerror="this.src='my-profile.jpg'" />
              <div class="convo-online-dot"></div>
            </div>
            <div class="convo-body">
              <div class="convo-top-row">
                <span class="convo-name">Whiskey &#x1F436;</span>
                <span class="convo-time">Now</span>
              </div>
              <div class="convo-bottom-row">
                <span class="convo-preview">I found the best walking trail &#x1F602;</span>
                <span class="convo-unread-badge">1</span>
              </div>
            </div>
          </div>

          <!-- Conversation: Maya (unread) -->
          <div class="conversation-item unread">
            <div class="convo-avatar-wrapper">
              <img class="convo-avatar" src="profile-maya.png" alt="Maya" onerror="this.src='my-profile.jpg'" />
            </div>
            <div class="convo-body">
              <div class="convo-top-row">
                <span class="convo-name">Maya</span>
                <span class="convo-time">2m</span>
              </div>
              <div class="convo-bottom-row">
                <span class="convo-preview">That coffee recommendation was actually amazing.</span>
                <span class="convo-unread-badge">3</span>
              </div>
            </div>
          </div>

          <!-- Conversation: Debbie (unread) -->
          <div class="conversation-item unread">
            <div class="convo-avatar-wrapper">
              <img class="convo-avatar" src="profile-debian.jpg" alt="Debbie" onerror="this.src='my-profile.jpg'" />
              <div class="convo-online-dot"></div>
            </div>
            <div class="convo-body">
              <div class="convo-top-row">
                <span class="convo-name">Debbie</span>
                <span class="convo-time">5m</span>
              </div>
              <div class="convo-bottom-row">
                <span class="convo-preview">Listen to this song &#x1F3B5;</span>
                <span class="convo-unread-badge">1</span>
              </div>
            </div>
          </div>

          <!-- Conversation: Aarav (read) -->
          <div class="conversation-item">
            <div class="convo-avatar-wrapper">
              <img class="convo-avatar" src="profile-montana.jpg" alt="Aarav" onerror="this.src='my-profile.jpg'" />
            </div>
            <div class="convo-body">
              <div class="convo-top-row">
                <span class="convo-name">Aarav</span>
                <span class="convo-time">1h</span>
              </div>
              <div class="convo-bottom-row">
                <span class="convo-preview">See you after class!</span>
              </div>
            </div>
          </div>

          <!-- Conversation: Sophia (read) -->
          <div class="conversation-item">
            <div class="convo-avatar-wrapper">
              <img class="convo-avatar" src="my-profile.jpg" alt="Sophia" />
            </div>
            <div class="convo-body">
              <div class="convo-top-row">
                <span class="convo-name">Sophia</span>
                <span class="convo-time">Yesterday</span>
              </div>
              <div class="convo-bottom-row">
                <span class="convo-preview">Finished the assignment?</span>
              </div>
            </div>
          </div>

          <!-- Conversation: Charlie (read, typing) -->
          <div class="conversation-item">
            <div class="convo-avatar-wrapper">
              <img class="convo-avatar" src="profile-montana.jpg" alt="Charlie" onerror="this.src='my-profile.jpg'" />
            </div>
            <div class="convo-body">
              <div class="convo-top-row">
                <span class="convo-name">Charlie</span>
                <span class="convo-time">2d</span>
              </div>
              <div class="convo-bottom-row">
                <span class="convo-preview convo-typing">Typing<span class="typing-dots"><span>.</span><span>.</span><span>.</span></span></span>
              </div>
            </div>
          </div>

        </div>
      </div>

      <div class="app-nav">
        <!-- Will be replaced by replace_nav.py -->
      </div>
    </div>
  </div>
'''

with open('c:/frontend_quad/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find "JAVASCRIPT" in the comment block and work backwards to get the full marker
idx = content.find('JAVASCRIPT')
if idx < 0:
    print("ERROR: Could not find JAVASCRIPT marker")
else:
    # Find the start of the comment block (go back to find "<!-- ===")
    search_back = content.rfind('<!--', 0, idx)
    if search_back >= 0:
        # We want everything from the "  <!-- ===" line
        # Find the start of that line
        line_start = content.rfind('\n', 0, search_back)
        if line_start < 0:
            line_start = 0
        else:
            line_start += 1  # skip the newline itself
        
        insert_point = line_start
        new_content = content[:insert_point] + html_block + '\n' + content[insert_point:]
        
        with open('c:/frontend_quad/index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"SUCCESS: Messages HTML inserted at position {insert_point}")
    else:
        print("ERROR: Could not find comment start")
