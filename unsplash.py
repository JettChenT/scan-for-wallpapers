import requests
import shutil
from settings import CATEGORIES
from pathlib import Path

url = "https://source.unsplash.com"

def conv(x):
    if type(x)==str:
        return x
    return CATEGORIES[x]

class Unsplash:
    def __init__(self):
        Path("./pictures").mkdir(exist_ok=True)
        self.ppath = Path("./pictures")
        self.resolution = "5120x3200"

    def get_pic(self,r):
        filename = Path(f"{hash(r.url)}.jpg")
        r.raw.decode_content = True
        fpath = self.ppath / filename
        with open(fpath, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        return fpath

    def get_random_img(self):
        r = requests.get(f"{url}/random/{self.resolution}",stream=True)
        return self.get_pic(r)

    def get_category_pic(self,categories:list):
        qurl = f"{url}/{self.resolution}/?{','.join(list(map(conv,categories)))}"
        print(qurl)
        r = requests.get(qurl,stream=True)
        return self.get_pic(r)