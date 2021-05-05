from appscript import app, mactypes
from pathlib import Path

def set_wallpaper(path:Path):
    app('Finder').desktop_picture.set(mactypes.File(str(path.absolute())))