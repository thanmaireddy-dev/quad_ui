css_block = '''

/* ============================================================
   PHASE 5 – MESSAGES
   ============================================================ */

/* Main container */
.messages-content {
  background: var(--screen-bg);
  padding: 28px 20px 16px;
  display: flex;
  flex-direction: column;
  gap: 0;
}

/* ---- Header ---- */
.messages-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 22px;
}

.messages-title {
  font-size: 28px;
  font-weight: 800;
  color: var(--heading-color);
  letter-spacing: -0.5px;
  line-height: 1.2;
}

.messages-subtitle {
  font-size: 14px;
  color: var(--secondary);
  margin-top: 4px;
}

.messages-search-toggle {
  background: none;
  border: none;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s;
  flex-shrink: 0;
}

.messages-search-toggle:hover {
  background: rgba(0, 0, 0, 0.04);
}

.messages-search-toggle svg {
  width: 22px;
  height: 22px;
  stroke: var(--heading-color);
}

/* ---- Search Bar ---- */
.messages-search-bar {
  display: flex;
  align-items: center;
  gap: 10px;
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 11px 16px;
  margin-bottom: 24px;
  transition: border-color 0.22s, box-shadow 0.22s;
}

.messages-search-bar:focus-within {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(13, 43, 36, 0.07);
}

.messages-search-bar svg {
  width: 18px;
  height: 18px;
  stroke: #A09A91;
  flex-shrink: 0;
}

.messages-search-bar input {
  flex: 1;
  border: none;
  background: transparent;
  font-size: 15px;
  color: var(--text);
  font-family: var(--font);
  outline: none;
}

.messages-search-bar input::placeholder {
  color: #B8B3AB;
}

/* ---- Quad Moments ---- */
.moments-section {
  margin-bottom: 28px;
}

.moments-label {
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--secondary);
  margin-bottom: 16px;
}

.moments-scroll {
  display: flex;
  gap: 18px;
  overflow-x: auto;
  padding-bottom: 6px;
  scrollbar-width: none;
}

.moments-scroll::-webkit-scrollbar {
  display: none;
}

.moment-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  flex-shrink: 0;
}

.moment-ring {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  padding: 3px;
  border: 2px solid var(--border);
  position: relative;
  transition: transform 0.22s ease, border-color 0.22s ease;
}

.moment-ring:hover {
  transform: scale(1.06);
}

.moment-ring.has-moment {
  border-color: var(--primary);
}

.moment-ring.add-ring {
  border: 2px dashed var(--border);
}

.moment-ring img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  display: block;
}

.moment-name {
  font-size: 11px;
  font-weight: 500;
  color: var(--secondary);
  letter-spacing: 0.1px;
  max-width: 64px;
  text-align: center;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* Add Moment badge */
.moment-add-badge {
  position: absolute;
  bottom: -2px;
  right: -2px;
  width: 22px;
  height: 22px;
  background: var(--primary);
  border: 2.5px solid var(--screen-bg);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.moment-add-badge svg {
  width: 12px;
  height: 12px;
  stroke: #FFFFFF;
}

/* ---- Conversation List ---- */
.conversation-list {
  display: flex;
  flex-direction: column;
}

.conversation-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 16px 4px;
  border-bottom: 1px solid rgba(229, 225, 216, 0.5);
  cursor: pointer;
  border-radius: 12px;
  transition: background 0.2s ease;
}

.conversation-item:last-child {
  border-bottom: none;
}

.conversation-item:hover {
  background: rgba(13, 43, 36, 0.025);
}

/* Avatar */
.convo-avatar-wrapper {
  position: relative;
  flex-shrink: 0;
}

.convo-avatar {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  object-fit: cover;
  display: block;
  border: 1px solid rgba(229, 225, 216, 0.6);
}

.convo-online-dot {
  position: absolute;
  bottom: 2px;
  right: 2px;
  width: 12px;
  height: 12px;
  background: var(--success);
  border: 2.5px solid var(--screen-bg);
  border-radius: 50%;
}

/* Body */
.convo-body {
  flex: 1;
  min-width: 0;
}

.convo-top-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 4px;
}

.convo-name {
  font-size: 15px;
  font-weight: 500;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.convo-emoji {
  font-weight: 400;
}

.convo-time {
  font-size: 12px;
  font-weight: 400;
  color: #A09A91;
  flex-shrink: 0;
  margin-left: 8px;
}

.convo-bottom-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.convo-preview {
  font-size: 14px;
  font-weight: 400;
  color: var(--secondary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  flex: 1;
  line-height: 1.4;
}

/* Unread state */
.conversation-item.unread .convo-name {
  font-weight: 700;
  color: var(--heading-color);
}

.conversation-item.unread .convo-preview {
  color: var(--text);
  font-weight: 500;
}

.conversation-item.unread .convo-time {
  color: var(--primary);
  font-weight: 600;
}

.convo-unread-badge {
  flex-shrink: 0;
  min-width: 20px;
  height: 20px;
  background: var(--primary);
  color: #FFFFFF;
  font-size: 11px;
  font-weight: 700;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 6px;
  animation: badgePulse 2s infinite;
}

@keyframes badgePulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.08); }
}

/* Typing indicator */
.convo-typing {
  color: var(--accent) !important;
  font-weight: 500 !important;
  font-style: italic;
}

.typing-dots span {
  animation: typingBlink 1.4s infinite;
  font-style: normal;
}

.typing-dots span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-dots span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typingBlink {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 1; }
}
'''

with open('c:/frontend_quad/styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

content += css_block

with open('c:/frontend_quad/styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Messages CSS appended.")
