from unsplash import Unsplash
from wallpaper import set_wallpaper

up = Unsplash()
fpath = up.get_random_img()

set_wallpaper(fpath)
