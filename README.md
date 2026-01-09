

````
# 🎯 Valorant After-Game Analyzer

A command-line tool that analyzes your **most recent Valorant match** and identifies
which opponents are **currently streaming on Twitch**. It highlights your **kills and deaths**
involving live streamers and provides **direct links** to their channels.

---

## 🚀 Features

- Fetches your latest Valorant match data
- Identifies all opponents from that match
- Searches each opponent on Twitch
- Tracks kills and deaths against live streamers
- Provides direct Twitch links for easy viewing

---

## 🖥️ Requirements

- Python 3.x  
- Internet connection  
- Command Prompt / Terminal  

---

## 📦 Dependencies

- `requests`
- `python-dotenv`
- `webbrowser` *(built-in)*

Install required libraries:

```bash
pip install requests python-dotenv
````

---

## ⚙️ Setup

1. Create a `.env` file in the project root:

```env
AUTH_TOKEN=your_valorant_api_token
```

2. Update the **CONFIG** section in the script with:

   * `region` (e.g. `na`, `eu`)
   * `platform` (e.g. `pc`)
   * `username` (your in-game name)
   * `tag` (your Valorant tag)

---

## ▶️ Usage

Run the script from the project directory:

```bash
python main.py
```

### The script will:

1. Fetch your most recent match
2. Open Twitch search pages for each opponent
3. Prompt you to confirm which opponents are live
4. Display your kills and deaths against live streamers
5. Output Twitch links for quick access

---

## 📁 Project Structure

```text
.
├── main.py        # Main application logic
├── main.spec      # PyInstaller spec file
├── build/         # Compiled executable output
└── .env           # Environment variables (not committed)
```

---

## 📝 Notes

* Browser tabs open automatically for Twitch searches
* Designed to run **from the command line only**
* Uses the **HenrikDev Valorant API** for match data

---

## 🛠️ Tech Stack

### Language

* Python 3

### Libraries

* `requests` – HTTP requests
* `python-dotenv` – Environment variable management
* `webbrowser` – Browser automation

### Tools

* PyInstaller – Executable packaging

### APIs

* HenrikDev Valorant API
* Twitch API

---

## ⚠️ Disclaimer

This project is not affiliated with Riot Games or Twitch.
All game data is retrieved through publicly available APIs.

```

---

