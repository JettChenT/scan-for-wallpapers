from unsplash import Unsplash
from wallpaper import set_wallpaper
from ranking import Ranker,make_ranker,save_ranker
import typer

up = Unsplash()
app = typer.Typer()
ranker = Ranker()

@app.command()
def category(cat:str):
    fpath = up.get_category_pic([cat])
    typer.echo(f"CATEGORY: {cat}")
    typer.echo(fpath)
    set_wallpaper(fpath)

@app.command()
def random():
    fpath = up.get_random_img()
    set_wallpaper(fpath)


@app.command()
def rank():
    ranker = make_ranker()
    ranker.getdata()
    save_ranker(ranker)

@app.command()
def recommend():
    ranker = make_ranker()
    ranker.gen()
    fpath = ranker.reco()
    typer.echo(f"Recommended category:{ranker.prefCat}")
    set_wallpaper(fpath)

if __name__ == "__main__":
    app()