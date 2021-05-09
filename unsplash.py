import requests
import shutil
from pathlib import Path

url = "https://source.unsplash.com"

class Unsplash:
    def __init__(self):
        Path("./pictures").mkdir(exist_ok=True)
        self.ppath = Path("./pictures")

    def get_random_img(self):
        r = requests.get(url + "/random/2560x1600",stream=True)
        filename = Path(f"{hash(r.url)}.jpg")
        r.raw.decode_content = True
        fpath = self.ppath/filename
        with open(fpath, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        return fpath
