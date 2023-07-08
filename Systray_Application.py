import pystray
from PIL import Image
from subprocess import call, check_output, CalledProcessError
import threading
import time

def check_rule():
    cmd = 'netsh advfirewall firewall show rule name="_01 Block steam(Program)"'
    try:
        output = check_output(cmd, shell=True).decode()
        if "No rules match the specified criteria." in output:
            return False
        else:
            return True
    except CalledProcessError:
        return False

def action_block(icon, item):
    call('block_steam_traffic.bat', shell=True)
    threading.Thread(target=update_icon_with_image, args=(icon, 'blocked_icon.png')).start()

def action_block_exit(icon, item):
    call('block_steam_traffic.bat', shell=True)
    icon.stop()

def action_unblock(icon, item):
    call('unblock_steam_traffic.bat', shell=True)
    threading.Thread(target=update_icon_with_image, args=(icon, 'unblocked_icon.png')).start()

def action_unblock_exit(icon, item):
    call('unblock_steam_traffic.bat', shell=True)
    icon.stop()

def exit_action(icon, item):
    icon.stop()

def menu_items():
    status = check_rule()
    if status:
        return (pystray.MenuItem('Unblock', action_unblock),
                pystray.Menu.SEPARATOR,
                pystray.MenuItem('Unblock and Exit', action_unblock_exit),
                pystray.MenuItem('Exit without unblocking', exit_action),)
    else:
        return (pystray.MenuItem('Block', action_block),
                pystray.Menu.SEPARATOR,
                pystray.MenuItem('Block and Exit', action_block_exit),
                pystray.MenuItem('Exit', exit_action),)

def update_icon_with_image(icon, image_path):
    time.sleep(1)
    icon.stop()
    image = Image.open(image_path)
    icon = pystray.Icon("Steam Status", icon=image, menu=menu_items())
    icon.run()

status = check_rule()
if status:
    icon = pystray.Icon("Steam Status", icon=Image.open("blocked_icon.png"), menu=menu_items())
else:
    icon = pystray.Icon("Steam Status", icon=Image.open("unblocked_icon.png"), menu=menu_items())

icon.run()