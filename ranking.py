from settings import CATEGORIES
from unsplash import Unsplash
from PIL import Image, ImageTk
import pickle
from pathlib import Path
import random
import numpy as np

FPATH = Path("data/main.ranker")

class Ranker():
    def __init__(self):
        self.prefCat = random.randint(0, len(CATEGORIES))
        self.scores = np.zeros(len(CATEGORIES))
        self.up = Unsplash()
        self.tries = 1

    def getdata(self):
        for cat in CATEGORIES:
            for _ in range(self.tries):
                url = self.up.get_category_pic([cat])
                img = Image.open(url)
                img.show()
                n = int(input("n="))
                self.scores[CATEGORIES.index(cat)] += n

    def gen(self):
        self.prefCat = np.argmax(self.scores)

    def reco(self):
        print(self.scores)
        return self.up.get_category_pic([self.prefCat])


def make_ranker():
    if Path.exists(FPATH):
        return pickle.load(open(FPATH,'rb'))
    return Ranker()

def save_ranker(r):
    pickle.dump(r,open(FPATH,'wb'))


