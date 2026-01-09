VALORANT AFTER-GAME ANALYZER

A command-line tool that analyzes your most recent Valorant match and identifies
which opponents are currently streaming on Twitch. It highlights your kills and
deaths involving those live streamers and provides direct links to their channels.


WHAT IT DOES
- Fetches your latest Valorant match data
- Identifies all opponents from that match
- Searches each opponent on Twitch
- Tracks kills and deaths against live streamers
- Displays direct Twitch links for easy viewing


REQUIREMENTS
- Python 3.x
- Internet connection
- Command Prompt / Terminal


DEPENDENCIES
- requests
- python-dotenv
- webbrowser (built-in)


SETUP
1. Create a `.env` file in the project root:

   AUTH_TOKEN=your_valorant_api_token

2. Update the CONFIG section in the script with:
   - region   (e.g. na, eu)
   - platform (e.g. pc)
   - username (your in-game name)
   - tag      (your Valorant tag)

3. Install required libraries:

   pip install requests python-dotenv


USAGE
Run the script from the project directory:

   python main.py

The script will:
1. Fetch your most recent match
2. Open Twitch search pages for each opponent
3. Prompt you to confirm which opponents are live
4. Display your kills and deaths against live streamers
5. Output Twitch links for quick access


PROJECT STRUCTURE
- main.py     : Main application logic
- main.spec   : PyInstaller spec file
- build/      : Compiled executable output


NOTES
- Browser tabs will open automatically for Twitch searches
- Uses HenrikDev’s Valorant API for match data
- Designed to be run from the command line only


TECH STACK

Language:
- Python 3

Libraries:
- requests        (HTTP requests)
- python-dotenv   (environment variables)
- webbrowser     (browser automation)

Tools:
- PyInstaller     (executable packaging)

APIs:
- HenrikDev Valorant API
- Twitch API
