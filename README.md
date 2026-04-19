# Sirhc Cockpit
**That Gardening Realtor AI Team — Internal Ops App**
*Built by Sirhc for Chris Drawdy · eXp Realty · San Antonio TX*

---

## What This Is

Sirhc Cockpit is a mobile-first progressive web app (PWA) that runs the daily operations of That Gardening Realtor. It tracks active deals, leads, tasks, content, mileage, and expenses — and syncs everything directly to Sirhc, the AI assistant, with one tap.

No login. No subscription. Installs on your phone like a native app. All data stays on your device until you sync.

---

## Install on Your Phone

1. Open **Samsung Internet** and go to:
   `https://thatgardeningrealtor.github.io/cockpit/`
2. Tap the menu → **Add page to** → **Home screen**
3. Open from your home screen — no address bar, full screen

**To confirm you have the latest version:** Tap **Vendors** tab → scroll to the bottom → check the version stamp (e.g. `v0.7 · Apr 18`).

**To update after a new version is pushed:** Close the app completely → reopen it. Network-first service worker fetches the latest automatically.

---

## Quick Start

1. Open the app — morning briefing fires automatically
2. Set your **3 Priorities** for the day
3. Make your calls — log each one via **Log Update** (action strip)
4. Log any mileage or expenses via **💰 Log Miles / Expense** on the home screen
5. Hit **🌿 Sync to Sirhc** — Sirhc reads everything at next session

---

## Feature Cheatsheet

### Home Screen (Cockpit Tab)
| Feature | What It Does |
|---|---|
| Today's 3 Priorities | Tap to open · check off · edit next action |
| Pipeline Snapshot | Quick view of active deals · tap to open |
| Today's Calendar | Google Calendar events for today (requires auth) |
| Weekly Rhythm | Your IN/ON schedule · tap any day to edit |
| 🕵️ Mission Briefing | Opens the daily briefing overlay |
| 🌿 Sync to Sirhc | Pushes all data to Sirhc via GitHub |
| 💰 Log Miles / Expense | Quick mileage or expense entry |
| Message Sirhc | Leave notes for Sirhc — sent with next sync |
| Last Synced | Shows when data was last pushed |

### Bottom Navigation
| Tab | What's There |
|---|---|
| 🏠 Cockpit | Home · priorities · pipeline · calendar |
| 🏡 Deals | Active listings and transactions |
| 👥 Leads | Buyers · sellers · prospects · investors |
| 📋 Tasks | Full task queue with logs |
| 🎨 Content | Content pipeline · ideas through posted |
| 🔧 Vendors | Contractors · lenders · team · loan programs |

### Action Strip (Bottom Buttons)
| Button | What It Does |
|---|---|
| 🌿 New Lead | Sage intake form — logs a new lead |
| 🔄 Log Update | Sirhc update form — logs activity on any deal or lead |
| 🎨 Content | Violet content form — adds to content pipeline |
| 📋 Lauren | Lauren tab — Bold Trail sync and admin |

### Deal / Lead Cards
Tap any card to open the full modal:
- **Next Action** — edit what comes next (shows on card preview)
- **Log Update** — green-tinted field · logs a timestamped activity entry
- **Activity Log** — full history · tap header to collapse
- **Save & Close** — saves everything · button sits above the log

### Expense Tracker
- **Log:** 💰 button on home screen → toggle Mileage or Expense → fill in → Save
- **Summary:** Today's totals + this month's running total shown on home screen
- **Tax Report:** Vendors tab → 📊 Export Tax Report → downloads CSV

---

## The AI Team

| Agent | Role | Trigger |
|---|---|---|
| **Sirhc** | Main assistant · deal ops · daily brief · session lead | Any session |
| **Sage** | Lead intake · profile builder · Bold Trail campaigns | `lead_*.txt` in team-inbox |
| **Violet** | Content · social media · newsletter | `content_*.txt` in team-inbox |
| **Rex** | App developer · Cockpit builder · bug fixes | `appdev_*.txt` in team-inbox |
| **Larry** | Retired · fishing | — |

---

## Sync Cycle

```
Log something in app
      ↓
Sync button glows green
      ↓
Tap 🌿 Sync to Sirhc
      ↓
Snapshot pushed to GitHub
      ↓
Sirhc reads it at next session start
      ↓
Deal files + lead files updated automatically
```

---

## Version Log

| Version | Date | What Changed |
|---|---|---|
| v0.1 | Apr 13 | Initial build · deals · leads · tasks · vendors |
| v0.2 | Apr 14 | PWA setup · manifest · service worker · GitHub Pages |
| v0.3 | Apr 15 | Morning briefing · typewriter effect · secret agent theme |
| v0.4 | Apr 16 | GitHub sync via Contents API · snapshot auto-read |
| v0.5 | Apr 17 | Log updates persist to localStorage · dynamic dropdown · cockpit buttons |
| v0.6 | Apr 18 | Sync button fixed · token modal · Message Sirhc · version stamp · last synced · glow indicator · card modal UX improvements |
| v0.7 | Apr 18 | Mileage & expense tracker · tax CSV export · Save & Close above activity log · collapsible log |

---

## Known Issues / Coming Soon

- [ ] Google Calendar auth — calendar strip pending connection
- [ ] Mission Briefing button — fix in progress (v0.8)
- [ ] Post-sync recap modal — coming in v0.8
- [ ] Live Claude API chat — planned ON day build
- [ ] Add task directly from Tasks tab — coming soon

---

## File Structure

```
cockpit/
├── index.html          ← The entire app (single file)
├── manifest.json       ← PWA manifest
├── sw.js               ← Service worker (network-first cache)
├── icon-192.jpg        ← App icon
├── icon-512.jpg        ← App icon (large)
├── sirhc-snapshot.txt  ← Live data export · read by Sirhc each session
└── README.md           ← This file
```

---

*Community first. Business grows from that.*
*Plant the seed. Water it daily. Trust the season. 🌱*

*Built by Sirhc · That Gardening Realtor AI Team*
