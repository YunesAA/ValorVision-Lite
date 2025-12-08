================================================================================
                        VALORANT AFTER-GAME ANALYZER
================================================================================

DESCRIPTION:
This tool analyzes your most recent Valorant match and identifies which opponents
are currently streaming on Twitch. It then displays your interactions (kills and
deaths) with those live streamers.

This tool only runs on command prompt

PURPOSE:
- Fetch your latest match data from the Valorant API
- Identify all opponents from that match
- Search for those opponents on Twitch
- Track which enemies you killed or were killed by
- Provide direct links to their Twitch channels for viewing

DEPENDENCIES:
- Python 3.x
- requests library (for API calls)
- python-dotenv (for environment variables)

SETUP:
1. Create a .env file in this directory with the following:
   AUTH_TOKEN=<your_valorant_api_token>

2. Configure your Valorant player info in the CONFIG section:
   - region (e.g., "na", "eu")
   - platform (e.g., "pc")
   - username (your in-game name)
   - tag (your in-game tag number)

3. Install dependencies:
   pip install requests python-dotenv

USAGE:
python main.py

The script will:
1. Fetch your latest match
2. Open Twitch search pages for each opponent
3. Prompt you to mark which opponents are live
4. Show your interactions (kills/deaths) with live streamers
5. Display Twitch links for easy access

FILES:
- main.py: Main script
- main.spec: PyInstaller spec file for creating executable
- build/: Contains compiled executable files

NOTES:
- Requires active internet connection
- Opens browser tabs for Twitch searches
- Uses Henrik Dev Valorant API for match data

================================================================================

LANGUAGES, TOOLS & FRAMEWORKS/LIBRARIES:

Languages:
- Python 3.x

Libraries:
- requests - HTTP library for API calls
- python-dotenv - Environment variable management
- webbrowser - Browser automation

Tools:
- PyInstaller - Executable packaging (main.spec)

APIs:
- Henrik Dev Valorant API - Match and player data
- Twitch API - Streamer information

================================================================================