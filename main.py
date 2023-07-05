# internal modules
import requests
import json # to process the GET request
import datetime, time # logging, cooldown
import webbrowser # to open web triggers


# The amount of of number signs indicates comment's unimportance

# change this to your account's:
authBearer = "Bearer XXX"
cooldown = 3 # never below 1, as it limits for 60 requests per minute for some things
stopKey = "q" # Stops the script

# logs
logAvailables = True # after holding the stop key, it'll print the log of when an available chance is found
allowWebTrigger = False # Allows to open the page below after it gets triggered, and only triggers once in a script's lifetime
openSiteTrigger = "https://web.whatsapp.com/send/?phone=XXXXXXXXXXXX&text=X" # read above. can be "api" for application or "web" for WA web
ballontipTrigger = False # Whenever it finds a chance, it'll do a notification.


# external modules
import keyboard # to check if key pressed or no, stopping the requests' loop
if ballontipTrigger:
    import ballontip # Windows' notifications, get "pypiwin32" if "win32api" isn't found


## colors for aesthetics
class colors:
    end = "\033[0m"
    black = "\033[90m"
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    blue = "\033[94m"
    magenta = "\033[95m"
    cyan = "\033[96m"
    white = "\033[97m"

# ids in the site:
shadowingIds = [
    "administration",
    "accounting",
    "marketing",
    "law",
    "it",
    "film",
    "medical",
    "pharmacy",
    "engineering"
]

# will change to your input's allowance
targetIds = []

i = 0
for sId in shadowingIds:
    print(f"{colors.blue}( {colors.green}{i}{colors.blue} ){colors.black} - {colors.white}{sId}{colors.end}")
    i += 1

for targetId in input(f"Input your targets' indexs: {colors.black}(0, 1, 2) {colors.yellow}").split(" "):
    targetIds.append(shadowingIds[int(targetId)])
print(f"{colors.end}")

lastAvailables = []

while not keyboard.is_pressed(stopKey):
    request = requests.get(
        "https://api.jsp.elham.training/api/students/opportunities/fields/riyadh",
        headers={
            "authorization" : authBearer
        }
    )

    print(f'''
Ratelimit Limit:     {request.headers['X-Ratelimit-Limit']}
Ratelimit Remaining: {request.headers['X-Ratelimit-Remaining']}
Ratelimit Reset:     {request.headers['X-Ratelimit-Reset']}
    ''')

    for x in json.loads(request.content):
        if x["id"] in targetIds:
            print(f"{colors.end}{x['id']} {colors.black}({x['count']}) {f'{colors.green}available!{colors.end}' if x['count'] > 0 else f'{colors.red}unavailable{colors.end}'}") # forgive me,
            
            if x['count'] > 0:
                if logAvailables:
                    lastAvailables.append(f"{x['id']}{colors.black} - {colors.end}{datetime.datetime.now()}")
                
                if allowWebTrigger:
                    allowWebTrigger = False
                    webbrowser.open(f'{openSiteTrigger}\n{x["id"]}')
                    time.sleep(9) # just in case the site doesn't load fast, sites are bloated nowadays with nonsense
                    keyboard.press_and_release("enter")
                
                if ballontipTrigger:
                    ballontip.balloon_tip("Found a Chance!", x["name"]["en"].capitalize())
    
    time.sleep(cooldown)
    print("\n") # for readability.

print(f"last availables: {lastAvailables if logAvailables else f'{colors.red}log disabled{colors.end}'}")
