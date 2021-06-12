from flask import Flask
from flask import request
from flask import render_template
from markupsafe import escape
from flask import redirect
from flask import send_file

from make_csv_file import make_csv
from indeed import get_indeed_jobs
from stackoverflow import get_so_jobs

app = Flask("__name__")

#DB
dic = {}

#홈
@app.route("/")
def index():
    return render_template("index.html")

#웹 스크래핑 결과
@app.route("/report")
def report():
    word = request.args.get('word')
    # 검색한 단어가 있다면
    if word:
        word = word.lower()
        fromDB = dic.get(word)
        
        # DB에 해당 단어가 있다면
        if fromDB:
            jobs = fromDB
        else:
            jobs = get_indeed_jobs(word)
            dic[word] = jobs

    else:
        return redirect("/")

    # report.html을 보여준다.
    return render_template(
        "report.html", 
        searchingBy = word, 
        jobCounts = len(jobs), 
        jobs = jobs)

#웹 스크래핑 결과 csv파일로 다운로드 받기
@app.route("/export")
def export():
    try:
        word = request.args.get('word')

        if word:
            word = word.lower()
            yesDB = dic.get(word)

            if yesDB:

                make_csv(yesDB)
                return send_file('jobs.csv')
                
            else:
                raise Exception

        else:
            raise Exception

        

    except:
        return redirect("/")

if __name__ == "__main__": app.run(host="0.0.0.0", port=9000)

