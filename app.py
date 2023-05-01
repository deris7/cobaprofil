from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def halamanprofil():
    return render_template("profil_page1.html")


@app.route("/pendidikan")
def halamanpendidikan():
    return render_template("pendidikan.html")


if __name__ == "__main__":
    app.run()
