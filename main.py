from pixabay import PixaBay
from wallpaper import set_wallpaper

pb = PixaBay("<YOUR-API-KEY>")
fpath = pb.get_random_img()
set_wallpaper(fpath)