# 📍 SoulCare Central – Project Roadmap

## 🗓️ Sprint 1 Tasks (April 13 – April 20)

- [ ] Create and push initial repo (Assigned: Shanancy)
- [x] Research related repos and evaluate for integration (Assigned: Shanancy)
### Sprint 1 Tasks

- [x] Find and evaluate Hint repo (Assigned: Shanancy)
- [x] Evaluate MindfulNotifier for cross-platform reminders (Assigned: Shanancy)
- [ ] Search for a Python-native reminder system to run and test
- [ ] Document setup and findings in this roadmap (Assigned: Shanancy)
- [ ] Create initial wireframe/mockup of UI layout (Assigned: Shanancy)
- [ ] Set up initial `README.md` and basic folder structure (Assigned:Shanancy)
- [ ] Create markdown doc listing desired features and stretch goals (Assigned: Shanancy)

## 📚 Findings from Related Projects
### 1. Hint (MacOS)
- Platform-specific but elegant reminders UI
- Possible inspiration for notification scheduling

### 2. Mindful Notifier
- Simple timer-based interface for focus sessions
- Lightweight and adaptable to different platforms

### 3. Box Breathing
- Very focused scope — strong breathing exercise logic

✅ Consider combining elements from Hint’s reminder UI and Box Breathing’s breathing control as modules.


## ✅ Evaluated Repository: Hint

**Repository:** [Hint – crsmithdev](https://github.com/crsmithdev/hint)

**Purpose:** Evaluate a macOS-based reminder system for potential use in the SoulCareCentral reminder feature.

**Findings:**
- Built with Swift and Objective-C for macOS only
- Uses Xcode storyboard for UI layout
- Implements periodic mindfulness break notifications in the system tray
- Simple, elegant concept that could inspire our cross-platform design

**Conclusion:**
The Hint repo is not directly portable to Python but offers excellent UX and timing logic inspiration. A cross-platform Python-based alternative will be explored for implementation.


---

## ✅ Evaluated Repository: MindfulNotifier

**Repository:** [MindfulNotifier](https://github.com/kmac/mindfulnotifier)

**Purpose:** Investigate a potential Python-based reminder system for SoulCare Solutions Central.

**Findings:**
- Project is built using **Flutter** (not Python)
- Source code located in `lib/`, written in Dart
- Designed as a cross-platform **mobile app** (Android/iOS)
- Includes logic for notifications and mindfulness reminders

**Conclusion:**
The MindfulNotifier project is well-structured and offers good design inspiration for mobile reminders, but it is **not Python-based** and therefore not directly usable in SoulCare. We will explore other Python-native options such as `BreakTimer` or build a custom reminder tool using `Tkinter`, `plyer`, or `schedule`.

