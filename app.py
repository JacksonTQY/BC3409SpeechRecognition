from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        print("File received")
        filename = secure_filename(file.filename)
        print(filename)
        file.save("static/"+filename)
        a = sr.AudioFile("static/"+filename)
        with a as source:
            a = sr.Recognizer().record(a)
        s = sr.Recognizer().recognize_google(a)
        return render_template("index.html", result=s)
    else:
        return render_template("index.html", result="2")


if __name__ == "__main__":
    app.run()