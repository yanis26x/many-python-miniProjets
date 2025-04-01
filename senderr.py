import pywhatkit as kit
import datetime
import time

now = datetime.datetime.now()
kit.sendwhatmsg("+15142626266", "Cool Message sent via Python 26xxxxxx", now.hour, now.minute + 1)
