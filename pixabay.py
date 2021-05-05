import requests
import random
import shutil
from pathlib import Path

url = "https://pixabay.com/api"

class PixaBay:
    def __init__(self,api_key):
        self.api_key = api_key
        Path("./pictures").mkdir(exist_ok=True)
        self.ppath = Path("./pictures")
    def get_random_img(self):
        r = requests.get(url,params={"key":self.api_key,"category":"backgrounds"})
        data = r.json()
        choice = random.choice(data["hits"])
        img_url = choice["largeImageURL"]
        filename = Path(f"{hash(img_url)}.jpg")
        r = requests.get(img_url,stream=True)
        r.raw.decode_content = True
        fpath = self.ppath/filename
        with open(fpath, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        return fpath
