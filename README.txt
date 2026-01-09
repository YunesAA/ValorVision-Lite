---

# 🎮 Valorant After-Game Analyzer

A command-line tool that analyzes your **most recent Valorant match** and identifies which opponents are **live on Twitch**, then shows your **kills and deaths** against those streamers.

> ⚠️ Runs **only in Command Prompt / Terminal** (no GUI).

---

## 📌 Description

This tool:

* Fetches your **latest Valorant match**
* Identifies **all opponents**
* Searches each opponent on **Twitch**
* Lets you confirm which opponents are **currently live**
* Displays your **kills/deaths** against those live streamers
* Provides **direct Twitch links** for easy viewing

---

## 🎯 Purpose

* Retrieve match data from the Valorant API
* Detect opponents from your last game
* Find opponents on Twitch
* Track:

  * Who you killed
  * Who killed you
* Quickly jump into their live streams

---

## ⚙️ Dependencies

* **Python 3.x**
* **requests** – API calls
* **python-dotenv** – environment variable handling

Install dependencies:

```bash
pip install requests python-dotenv
```

---

## 🛠️ Setup

### 1️⃣ Create a `.env` file

In the project root, add:

```env
AUTH_TOKEN=your_valorant_api_token
```

### 2️⃣ Configure player info

Edit the **CONFIG** section in the script:

* `region` (e.g. `na`, `eu`)
* `platform` (e.g. `pc`)
* `username` (your in-game name)
* `tag` (your Riot tag)

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

### What happens next:

1. Your latest match is fetched
2. Twitch search pages open for each opponent
3. You confirm which opponents are live
4. The script shows:

   * Your kills vs them
   * Their kills vs you
5. Twitch links are displayed for quick access

---

## 📁 Project Structure

```
.
├── main.py        # Main script
├── main.spec      # PyInstaller spec file
├── build/         # Compiled executable output
├── .env           # Environment variables (not committed)
```

---

## 📝 Notes

* Requires an **active internet connection**
* Opens **browser tabs** for Twitch searches
* Match data provided by **Henrik Dev Valorant API**

---

## 🧰 Languages, Tools & APIs

### Languages

* Python 3.x

### Libraries

* `requests` – HTTP requests
* `python-dotenv` – environment variables
* `webbrowser` – browser automation

### Tools

* **PyInstaller** – executable packaging

### APIs

* **Henrik Dev Valorant API** – match & player data
* **Twitch API** – streamer lookup

---
