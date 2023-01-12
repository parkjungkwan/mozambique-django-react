from datetime import datetime

def currentTime():
    today = datetime.now()
    return f"{today.time()}"
