import os, sys
try:
    import pyautogui, requests, io, time
    from colorama import init, Fore
except:
    os.system(f'{sys.executable} -m pip install pyautogui requests colorama > /dev/null 2>&1')
    import pyautogui, requests, io, time
    from colorama import init, Fore

init(autoreset=True)

if os.name == 'nt':
    os.system('title shop2sca & cls')
elif 'termux' in os.environ.get('PREFIX', ''):
    pass
else:
    os.system('clear')

print(Fore.RED + """
   _____ __                        _____ _____     _____ 
  / ___// /_  ____ _____  _____   / ___// ___/    / ___/
  \__ \/ __ \/ __ `/ __ \/ ___/   \__ \/ __ \______\__ \ 
 ___/ / / / / /_/ / /_/ (__  )   ___/ / /_/ /_____/__/ / 
/____/_/ /_/\__,_/ .___/____/   /____/\____/     /____/  
                /_/                                      
""" + Fore.RESET)

webhook = input(Fore.CYAN + "[?] Webhook URL : " + Fore.RESET)
delay = input(Fore.YELLOW + "[?] Délai entre chaque capture (secondes) : " + Fore.RESET)
mode = input(Fore.MAGENTA + "[?] Mode [1] Durée en minutes / [2] Nombre de captures : " + Fore.RESET)

if mode == "1":
    limit = int(input(Fore.MAGENTA + "[?] Durée en minutes : " + Fore.RESET)) * 60
    end_time = time.time() + limit
elif mode == "2":
    limit = int(input(Fore.MAGENTA + "[?] Nombre de captures : " + Fore.RESET))
else:
    sys.exit()

print(Fore.GREEN + "\n[+] Capture en cours...\n" + Fore.RESET)

count = 0

def capture_and_send():
    img = pyautogui.screenshot()
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    try:
        requests.post(webhook, files={'file': ('screenshot.png', buf, 'image/png')}, data={'username': 'SHOP2SCA', 'content': '**Nouvelle capture**'})
    except:
        t = str(int(time.time()))
        with open(f'screenshot_{t}.png', 'wb') as f:
            f.write(buf.read())

while True:
    if mode == "1" and time.time() > end_time:
        break
    if mode == "2" and count >= limit:
        break
    capture_and_send()
    count += 1
    time.sleep(float(delay))