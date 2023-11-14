import os

def init():
    if not os.path.exists("data"):
        print("servers directory does not exist, creating...")
        os.mkdir("./data")
        print(str("./data")+" directory created")
        #os.mkdir(os.path.join(core.serversDir,'sampleServer'))
        #print("data directory and start script created, Visit: "+ui.link("https://www.minecraft.net/en-us/download/server")+" to download the most recent server.jar to the sampleServer directory to get started")