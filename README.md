# 🎥 Tiktok_watcher
TikTok Watcher is an automated Python tool that uses Playwright to browse TikTok videos based on a search query. The tool can simulate watching videos for a random amount of time, optionally skipping some videos according to a configured percentage. It supports login persistence through storage state.

## 🚀 Features
- Launches a Chromium browser (using local Chrome executable).
- Loads previous login state if available, or prompts for login.
- Searches TikTok for a specified query.
- Iterates through video results and either skips or watches videos.
- Detects video duration and waits accordingly.
- Saves login state for subsequent runs.
- Configurable skip percentage and search query via `.env` file.

## 📦 Requirements
- 🐍 Python 3.8+
- 🎭 Playwright

## 🛠️ Installation
1. Clone the repository:
```bash
git clone https://github.com/androxiz/tiktok_watcher.git
cd tiktok-watcher
```
2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Install Playwright browsers:
```bash
playwright install
```

## ⚙️ Configuration
Create a .env file in the project root with the following variables:
```bash
SEARCH_QUERY=your_search_term_here
SKIP_PERCENT=12
```

- SEARCH_QUERY — the search keyword for TikTok videos.
- SKIP_PERCENT — percentage (0-100) of videos to skip watching.

## ▶️ Usage
Run the main script:
```bash
python main.py
```

- On the first run, the browser will open a login page. Log in manually and press Enter in the terminal (or just press Enter to skip the auth).
- The login state will be saved to state.json for subsequent runs.
- The script will search TikTok, then watch or skip videos based on configuration.

## ⚠️ Notes
- The script requires a stable internet connection and a valid TikTok account.

- Video duration detection may sometimes fail; in such cases, a default watch time is used.

- The Chromium executable path is hardcoded to a local Chrome installation; adjust it if necessary in the script.
