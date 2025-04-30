import time
from datetime import datetime
from notifypy import Notify

# Time you will get the Notif (24h)
heure_cible = "23:45"  # change This! 

message = "Yo ! Go get sum Swagg!"


while True:
    maintenant = datetime.now().strftime("%H:%M")
    if maintenant == heure_cible:
        notification = Notify()
        notification.title = "Salut !26x"
        notification.message = message
        notification.send()
        break
    time.sleep(30)  # check every 30 sec 