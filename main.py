from dotenv import load_dotenv
import os
import requests
import webbrowser
import time


# -------------- AUTHENTICATION --------------
load_dotenv()
auth_token = os.getenv("AUTH_TOKEN")
headers = {"Authorization": f"{auth_token}"}
# --------------------------------------------

# ------------------ CONFIG ------------------
region = "na"
platform = "pc"
username = "Not Milk" # username without tag
tag = "notme" # tag without #
my_ign = f"{username}#{tag}"
# --------------------------------------------


# ---------------- FUNCTIONS -----------------
def time_to_minutes(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}m {seconds}s"

def print_players(players):
    for ign in players:
        print(f" - {ign}")
# --------------------------------------------

# Get your most recent match
matchlist = requests.get(f"https://api.henrikdev.xyz/valorant/v4/matches/{region}/{platform}/{username}/{tag}", headers=headers).json()

if not matchlist.get("data"):
    print("❌ Could not fetch match list. Check name, tag, or region.")
    exit()

players = []

for player in matchlist["data"][0]["players"]:
    player_name = f"{player['name']}#{player['tag']}"
    players.append({
        "name": player["name"],
        "tag": player["tag"],
        "ign": player_name
    })

print(f"✅ Found {len(players)} players in last match.")


opponents = []
for player in players:
    ign = f"{player['name']}#{player['tag']}"
    if ign.lower() != my_ign.lower():
        opponents.append(ign)

print(f"\n✅ Found {len(opponents)} opponents in last match (excluding you).")
print("Here are their in-game names:")  

print_players(opponents)

# Prompt user after Twitch search
live_streamers = []
for ign in opponents:
    twitch_name = ign.split("#")[0]
    twitch_url = f"https://www.twitch.tv/search?term={twitch_name}"
    print(f"\n🔎 Opening Twitch search for {ign}...")
    webbrowser.open(twitch_url)
    time.sleep(0.5) 
    

    ans = input(f"Is {ign} live on Twitch? (y/n): ").strip().lower()
    if ans == "y":
        live_streamers.append(ign)

print(f"\n You marked {len(live_streamers)} players as live on Twitch.")
print("Here are the players you marked as live:")

print_players(live_streamers)

print("Now checking which ones you killed...")

number_of_rounds = matchlist["data"][0]["teams"][0]["rounds"]["won"] + matchlist["data"][0]["teams"][0]["rounds"]["lost"]
print(number_of_rounds, "rounds")


interactions = []

for kill in matchlist["data"][0]["kills"]:
    killer_name = kill["killer"]["name"]
    killer_tag = kill["killer"]["tag"]
    killer_username = f"{killer_name}#{killer_tag}"

    victim_name = kill["victim"]["name"]
    victim_tag = kill["victim"]["tag"]
    victim_username = f"{victim_name}#{victim_tag}"

    round_num = kill["round"]
    time_seen = kill["time_in_match_in_ms"] // 1000 

    if killer_username.lower() == my_ign.lower() or victim_username.lower() == my_ign.lower():
        interactions.append({
            "killer": f"{killer_name}#{killer_tag}",
            "victim": f"{victim_name}#{victim_tag}",
            "round": round_num+1,
            "time": time_to_minutes(time_seen)
        })


print("==============You killed these players:==============")
for interaction in interactions:    
    if interaction["killer"].lower() == my_ign.lower() and interaction["victim"] in [s for s in live_streamers]:
        print(f"{interaction['victim']} in Round {interaction['round']} at {interaction['time']}")


print("\n==============You died to these players:==============")
for interaction in interactions: 
    if interaction["victim"].lower() == my_ign.lower() and interaction["killer"] in [s for s in live_streamers]:
        print(f"{interaction['killer']} in Round {interaction['round']} at {interaction['time']}")

print("\n==============Summary:==============")
for streamer in live_streamers:
    twitch_name = streamer.split("#")[0]
    print(f"https://www.twitch.tv/search?term={twitch_name}")

#exit application upon closing the window
input("\n\nPress Enter to exit...")
input("\nare you sure you want to exit? (Press Enter to confirm)")
# Print all killer/victim interactions
# for interaction in interactions:
#     print(interaction)
