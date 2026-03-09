import linecache
import os

apikey= ""

os.getlogin()
def apikey_grab():
    line = linecache.getline("apikeys.txt", 1).strip()
    return line.split("=")[1]

apikey = apikey_grab()
print(apikey)

apikey_grab()
