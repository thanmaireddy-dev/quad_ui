css_block = '''

/* ============================================================
   PHASE 6 - PROFILE
   ============================================================ */

/* Main container - no side padding, banner is full-bleed */
.profile-content {
  background: var(--screen-bg);
  padding: 0 0 16px;
  display: flex;
  flex-direction: column;
  gap: 0;
}

/* ---- Banner ---- */
.profile-banner {
  width: 100%;
  height: 160px;
  background: linear-gradient(135deg, #0D2B24 0%, #173D34 40%, #1E4D43 70%, #245A4F 100%);
  position: relative;
  flex-shrink: 0;
}

.profile-banner-gradient {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 40%, rgba(13, 43, 36, 0.25) 100%);
}

/* ---- Profile Header Section ---- */
.profile-header-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: -52px;
  padding: 0 24px;
  position: relative;
  z-index: 10;
}

/* Avatar + Completion Ring */
.profile-avatar-area {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.profile-completion-ring {
  width: 104px;
  height: 104px;
  position: relative;
}

.profile-completion-ring svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

.ring-bg {
  fill: none;
  stroke: var(--border);
  stroke-width: 4;
}

.ring-fill {
  fill: none;
  stroke: var(--accent);
  stroke-width: 4;
  stroke-linecap: round;
  stroke-dasharray: 339.29;
  stroke-dashoffset: 339.29;
  transition: stroke-dashoffset 2s cubic-bezier(0.4, 0, 0.2, 1);
}

.profile-avatar-img {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 88px;
  height: 88px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid var(--surface);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.profile-avatar-edit {
  position: absolute;
  bottom: 4px;
  right: 4px;
  width: 28px;
  height: 28px;
  background: var(--primary);
  border: 2.5px solid var(--surface);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.2s;
}

.profile-avatar-edit:hover {
  transform: scale(1.1);
}

.profile-avatar-edit svg {
  width: 13px;
  height: 13px;
  stroke: #FFFFFF;
}

/* Completion Label */
.profile-completion-label {
  display: flex;
  align-items: baseline;
  gap: 4px;
  margin-top: 4px;
}

.completion-pct {
  font-size: 18px;
  font-weight: 800;
  color: var(--accent);
  letter-spacing: -0.3px;
}

.completion-word {
  font-size: 13px;
  font-weight: 500;
  color: var(--secondary);
}

.profile-completion-hint {
  font-size: 13px;
  color: var(--secondary);
  text-align: center;
  margin-top: 2px;
  margin-bottom: 8px;
}

/* ---- User Info Card ---- */
.profile-user-card {
  width: 100%;
  text-align: center;
  margin-top: 16px;
  margin-bottom: 8px;
}

.profile-name-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}

.profile-display-name {
  font-size: 24px;
  font-weight: 800;
  color: var(--heading-color);
  letter-spacing: -0.4px;
}

.profile-verified-badge {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.profile-age-badge {
  font-size: 15px;
  font-weight: 600;
  color: var(--secondary);
}

.profile-meta-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  margin-top: 6px;
  font-size: 14px;
  color: var(--secondary);
}

.profile-meta-row svg {
  width: 15px;
  height: 15px;
  flex-shrink: 0;
}

/* ---- Profile Sections (shared) ---- */
.profile-section {
  padding: 0 20px;
  margin-top: 28px;
}

.profile-section-title {
  font-size: 14px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--secondary);
  margin-bottom: 14px;
}

.profile-section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.profile-edit-icon {
  background: none;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s;
}

.profile-edit-icon:hover {
  background: rgba(0, 0, 0, 0.04);
}

.profile-edit-icon svg {
  width: 16px;
  height: 16px;
  stroke: var(--secondary);
}

/* ---- Quick Actions ---- */
.profile-quick-actions {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}

.quick-action-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 16px 6px 14px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
  font-family: var(--font);
}

.quick-action-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
  border-color: rgba(13, 43, 36, 0.2);
}

.qa-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: rgba(13, 43, 36, 0.06);
  display: flex;
  align-items: center;
  justify-content: center;
}

.qa-icon svg {
  width: 18px;
  height: 18px;
  stroke: var(--primary);
}

.qa-icon-gold {
  background: rgba(147, 119, 28, 0.08);
}

.qa-icon-gold svg {
  stroke: var(--accent);
}

.qa-label {
  font-size: 11px;
  font-weight: 600;
  color: var(--secondary);
  letter-spacing: 0.1px;
}

/* ---- My Photos Grid ---- */
.profile-photos-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
}

.profile-photo-tile {
  aspect-ratio: 1;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.profile-photo-tile:hover {
  transform: scale(1.03);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.profile-photo-tile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.profile-photo-add {
  background: var(--surface);
  border: 1.5px dashed var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: none;
}

.profile-photo-add:hover {
  border-color: rgba(13, 43, 36, 0.3);
  box-shadow: none;
}

.profile-photo-add svg {
  width: 24px;
  height: 24px;
  stroke: var(--secondary);
}

/* ---- About Me Card ---- */
.profile-about-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 20px;
}

.profile-about-card p {
  font-size: 15px;
  color: var(--text);
  line-height: 1.65;
}

/* ---- Prompts ---- */
.profile-prompts-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.profile-prompt-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 20px;
  transition: transform 0.2s, box-shadow 0.2s;
}

.profile-prompt-card:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
}

.prompt-question {
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--accent);
  display: block;
  margin-bottom: 8px;
}

.prompt-answer {
  font-size: 15px;
  font-weight: 400;
  color: var(--text);
  line-height: 1.6;
}

/* ---- Interests ---- */
.profile-interests-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.profile-interest-pill {
  display: inline-flex;
  align-items: center;
  padding: 7px 16px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  font-size: 13px;
  font-weight: 500;
  color: var(--text);
  transition: border-color 0.2s, background 0.2s;
}

.profile-interest-pill:hover {
  border-color: rgba(13, 43, 36, 0.25);
  background: rgba(13, 43, 36, 0.03);
}

/* ---- Info Cards (Campus Identity, Dating Prefs) ---- */
.profile-info-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 18px;
  overflow: hidden;
}

.info-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 20px;
  border-bottom: 1px solid rgba(229, 225, 216, 0.5);
}

.info-row:last-child {
  border-bottom: none;
}

.info-label {
  font-size: 14px;
  font-weight: 500;
  color: var(--secondary);
}

.info-value {
  font-size: 14px;
  font-weight: 600;
  color: var(--heading-color);
  text-align: right;
}

.info-value-verified {
  display: flex;
  align-items: center;
  gap: 5px;
  color: var(--accent);
}

.info-value-verified svg {
  flex-shrink: 0;
}

/* ---- Settings Card (Privacy & Safety) ---- */
.profile-settings-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 18px;
  overflow: hidden;
}

.settings-row {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 20px;
  border-bottom: 1px solid rgba(229, 225, 216, 0.5);
  background: none;
  border-left: none;
  border-right: none;
  border-top: none;
  width: 100%;
  cursor: pointer;
  transition: background 0.15s;
  font-family: var(--font);
  text-align: left;
}

.settings-row:last-child {
  border-bottom: none;
}

.settings-row:hover {
  background: rgba(13, 43, 36, 0.025);
}

.settings-row svg {
  width: 20px;
  height: 20px;
  stroke: var(--secondary);
  flex-shrink: 0;
}

.settings-row span:nth-child(2) {
  flex: 1;
  font-size: 15px;
  font-weight: 500;
  color: var(--text);
}

.settings-chevron {
  font-size: 22px;
  color: #B8B3AB;
  font-weight: 300;
  line-height: 1;
}

/* ---- App Information ---- */
.profile-app-info {
  text-align: center;
  padding-top: 12px;
}

.app-info-links {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 6px;
}

.app-info-links a {
  font-size: 13px;
  color: var(--secondary);
  text-decoration: none;
  transition: color 0.2s;
}

.app-info-links a:hover {
  color: var(--primary);
}

.app-info-dot {
  color: var(--border);
  font-size: 13px;
}

.app-version {
  font-size: 12px;
  color: #B8B3AB;
  margin-top: 12px;
}

.app-tagline {
  font-size: 12px;
  color: #B8B3AB;
  margin-top: 4px;
}
'''

with open('c:/frontend_quad/styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

content += css_block

with open('c:/frontend_quad/styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Profile CSS appended.")
