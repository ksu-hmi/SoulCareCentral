# 📍 SoulCare Central – Project Roadmap

## 🗓️ Sprint 1 Tasks (April 13 – April 20)

- [x] Create and push initial repo (Assigned: Shanancy)
- [x] Research related repos and evaluate for integration (Assigned: Shanancy)
### Sprint 1 Tasks

- [x] Find and evaluate Hint repo (Assigned: Shanancy)
- [x] Evaluate MindfulNotifier for cross-platform reminders (Assigned: Shanancy)
- [x] Search for a Python-native reminder system to run and test
- [x] Document setup and findings in this roadmap (Assigned: Shanancy)
- [x] Create initial wireframe/mockup of UI layout (Assigned: Shanancy)
- [x] Set up initial `README.md` and basic folder structure (Assigned:Shanancy)
- [x] Create markdown doc listing desired features and stretch goals (Assigned: Shanancy)

### 🗓️ Sprint 2 Task List (April 19 – April 28)

- [x] Evaluate and run a Python-native reminder system (Pomodoro Timer)
- [x] Add break-time affirmations and stretch/water reminder messages
- [x] Add soft chime sound during breaks
- [x] Change background color to reflect session type
- [x] Display random stretch pose visuals during breaks
- [ ] Add journaling prompt popup after long breaks
- [ ] Add affirmations to study time
- [x] Add settings screen to customize work/break durations

### Sprint 3 Task List (April 28 - May1)

- [x] Customized Pomodoro Timer for SoulCare Central
  - [x] Added stretch and water break reminders
  - [x] Added random affirmations during work sessions
  - [x] Added journal prompts and mood tracking after work sessions
  - [x] Changed background colors for work, short break, and long break
  - [x] Created and resized SoulCare Central logo
  - [x] Enlarged timer box and logo to better fill the window
- [x] Set up start and reset timer functionality
- [x] Set up affirmations and stretch pose image display
- [x] Improved GUI design for clean, professional appearance

---

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


## ✅ Evaluated Repository: Pomodoro-Timer (Python + Tkinter)

**Repository:** [https://github.com/Mahesh-Vard/Pomodoro-Timer](https://github.com/Mahesh-Vard/Pomodoro-Timer)

**Purpose:** Evaluate a simple, Python-based time management app for potential adaptation into SoulCare’s reminder feature.

**Findings:**
- Built with Python and Tkinter (GUI)
- Implements standard Pomodoro intervals (25 min work, 5 min break, 20 min long break)
- Runs successfully on macOS and shows a functioning GUI
- Well-structured and easy to modify

**Conclusion:**
This is a solid foundation to integrate SoulCare features like:
- Daily affirmations during breaks
- Mood journaling prompts after sessions
- Notification-style reminders to stretch, drink water, or breathe

✅ Will move forward with customization for SoulCare Solutions Central.
---

## ✅ Feature Added: Stretch Pose Visuals During Breaks

**Date Added:** April 19, 2025  
**Contributor:** Shanancy  

### Description:
Implemented random stretch pose visuals that appear during short and long breaks in the SoulCare Pomodoro Timer. The visuals are selected from a set of local image files in the `stretch_poses/` directory and displayed in the GUI using Tkinter.

### Features:
- Dynamically loads a new image each break session
- Integrates with existing reminder and sound features
- Designed for accessibility and relaxation

### Impact:
This feature boosts user engagement by encouraging physical movement alongside mental breaks, supporting SoulCare's holistic wellness goals.

### Next Steps:
- Include “Skip Pose” functionality
- Integrate Journal prompts for longer breaks 

## ✅ Feature Added: Affirmations During Study Sessions

**Date Added:** April 26, 2025  
**Contributor:** Shanancy  

### Description:
Implemented positive affirmations that appear at the beginning of each work session to promote focus, motivation, and encouragement. Affirmations fade in smoothly to create a calm and supportive study environment.

### Features:
- Pulls random affirmations from a separate `affirmations.py` module
- Displays a new affirmation at the start of each work period
- Smooth fade-in effect added using Tkinter’s `after()` method
- Complements stretch visuals and reminders during breaks for full wellness experience

### Impact:
Boosts user engagement and emotional support during focused study periods. Reinforces SoulCare’s mission to improve both mental and physical wellness during daily habits.

### Next Steps:
- Add journal prompts for longer breaks
- Customize logo

### Sprint 3 Updates

**Selected Base Project**
- Chose a Pomodoro Timer application as the foundation for SoulCare Central, providing a structured timer framework for wellness routines.

**Stretch and Water Break Reminders**
- Integrated randomized stretch and hydration reminders during breaks to encourage physical activity and self-care.

**Random Affirmations During Work Sessions**
- Added motivational affirmations during work periods to promote mental positivity and mindfulness.

**Journal Prompts and Mood Tracking**
- Implemented journal prompts and mood tracking after work sessions to support self-reflection and emotional wellness tracking.

**Dynamic Background Color Changes**
- Developed dynamic background color changes to visually distinguish between work sessions, short breaks, and long breaks, enhancing user experience.

**SoulCare Central Logo Integration**
- Created, resized, and embedded a SoulCare Central logo to personalize branding and promote app identity.

**Enlarged Timer Box and Resized Visual Elements**
- Increased canvas and logo sizes to better utilize screen space and improve readability of session timers.

**Start and Reset Functionality**
- Implemented full start and reset timer controls, enabling users to manage session flows easily.

**GUI Refinement**
- Aligned design elements (fonts, background colors, layout) to create a clean, calming, and professional user interface in line with SoulCare’s branding.

