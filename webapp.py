from flask import Flask
from flask import request
from flask import render_template
from markupsafe import escape
from flask import redirect

from indeed import get_indeed_jobs
from stackoverflow import get_so_jobs

app = Flask("__name__")

dic = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        fromDB = dic.get(word)

        if fromDB:
            jobs = fromDB
        else:
            jobs = get_indeed_jobs(word)
            dic[word] = jobs

    else:
        return redirect("/")

    return render_template(
        "report.html", 
        searchingBy = word, 
        jobCounts = len(jobs), 
        jobs = jobs)

if __name__ == "__main__": app.run(host="0.0.0.0", port=9000)

