import pywhatkit as kit
import datetime
import time

now = datetime.datetime.now()
kit.sendwhatmsg("+15142626266", "Cool Message sent via Python 26xxxxxx", now.hour, now.minute + 1)
# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+910123456789", "Salut! ", 13, 30, 15, True, 2)
