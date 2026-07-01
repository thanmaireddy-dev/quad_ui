css_block = '''
/* ============================================================
   PHASE 4 – CAMPUS CONFESSIONS
   ============================================================ */

/* Main Container */
.confessions-content {
  background: var(--screen-bg);
  padding: 32px 20px 40px; /* Generous overall padding */
  display: flex;
  flex-direction: column;
  gap: 24px; /* Default spacing between major sections */
  position: relative;
}

/* Header */
.confessions-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px; /* Extra breathing room */
}

.confessions-title {
  font-size: 28px;
  font-weight: 800;
  color: var(--heading-color);
  letter-spacing: -0.5px;
  line-height: 1.2;
}

.confessions-subtitle {
  font-size: 14px;
  color: var(--secondary);
  margin-top: 6px;
}

.confessions-settings-btn {
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
}

.confessions-settings-btn:hover {
  background: rgba(0, 0, 0, 0.04);
}

.confessions-settings-btn svg {
  width: 22px;
  height: 22px;
  fill: var(--heading-color);
}

/* Filter Tabs */
.confessions-filter-tabs {
  display: flex;
  background: rgba(13, 43, 36, 0.04);
  border-radius: 20px;
  padding: 4px;
  margin-bottom: 4px;
}

.filter-tab {
  flex: 1;
  padding: 8px 12px;
  border-radius: 16px;
  border: none;
  background: transparent;
  color: var(--secondary);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.25s ease;
}

.filter-tab.active {
  background: #FFFFFF;
  color: var(--primary);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

/* Streak Card */
.confessions-streak-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 24px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
}

.streak-header {
  display: flex;
  align-items: center;
  gap: 8px;
}

.streak-fire {
  font-size: 20px;
}

.streak-title {
  font-size: 17px;
  font-weight: 700;
  color: var(--heading-color);
}

.streak-text {
  font-size: 14px;
  color: var(--secondary);
  margin-top: 6px;
  margin-bottom: 16px;
}

.streak-progress-bar {
  height: 8px;
  background: #EDEAE4;
  border-radius: 4px;
  overflow: hidden;
}

.streak-progress-fill {
  height: 100%;
  background: var(--accent);
  border-radius: 4px;
}

/* Campus Pulse */
.campus-pulse-card {
  background: transparent;
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 20px;
}

.pulse-title {
  font-size: 14px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--secondary);
  margin-bottom: 16px;
}

.pulse-stats {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.pulse-stat {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex: 1;
}

.pulse-stat-val {
  font-size: 16px;
  font-weight: 700;
  color: var(--heading-color);
}

.pulse-stat-label {
  font-size: 11px;
  color: var(--secondary);
  margin-top: 4px;
  line-height: 1.3;
}

.pulse-divider {
  width: 1px;
  height: 24px;
  background: var(--border);
  margin: 0 12px;
}

/* Confession Cards */
.confession-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 24px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.confession-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);
}

.confession-card.featured {
  border: 1.5px solid var(--accent);
  background: linear-gradient(to bottom right, #FCFBF8, #F9F7F1);
}

.confession-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.confession-tag {
  background: #EDEAE4;
  color: var(--secondary);
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 12px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.confession-card.featured .confession-tag {
  background: rgba(147, 119, 28, 0.1);
  color: var(--accent);
}

.confession-time {
  font-size: 12px;
  color: #A09A91;
  font-weight: 500;
}

.confession-text {
  font-size: 16px;
  color: var(--heading-color);
  line-height: 1.65;
  font-weight: 400;
  margin-bottom: 24px; /* Space between text and reaction row */
}

/* Reaction Row */
.confession-reaction-row {
  display: flex;
  align-items: center;
  gap: 16px;
  border-top: 1px solid var(--border);
  padding-top: 16px;
}

.reaction-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: transparent;
  border: none;
  color: var(--secondary);
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  padding: 6px 8px;
  border-radius: 8px;
  transition: all 0.2s ease;
  margin-left: -8px; /* Align visual left with content */
}

.reaction-btn svg {
  width: 20px;
  height: 20px;
  stroke: var(--secondary);
  transition: stroke 0.2s ease, transform 0.2s ease;
}

.reaction-btn:hover {
  background: rgba(0, 0, 0, 0.03);
  color: var(--primary);
}

.reaction-btn:hover svg {
  stroke: var(--primary);
  transform: scale(1.05);
}

.share-btn {
  margin-right: -8px;
}

/* Floating Action Button */
.fab-share {
  position: absolute;
  bottom: 32px;
  right: 20px;
  background: var(--primary);
  color: #FFFFFF;
  border: none;
  border-radius: 30px;
  padding: 14px 20px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 600;
  box-shadow: 0 8px 24px rgba(13, 43, 36, 0.25);
  cursor: pointer;
  transition: transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275), background 0.2s;
  z-index: 100;
}

.fab-share svg {
  width: 20px;
  height: 20px;
  stroke: #FFFFFF;
}

.fab-share:hover {
  transform: translateY(-4px) scale(1.02);
  background: var(--primary-hover);
}

.fab-share:active {
  transform: scale(0.96);
}
'''

with open('c:/frontend_quad/styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

content += '\n' + css_block

with open('c:/frontend_quad/styles.css', 'w', encoding='utf-8') as f:
    f.write(content)
