from flask import Flask, request, render_template, url_for
from scraper import scrape_questions, scrape_users

app = Flask(__name__)
app.config['SECRET_KEY'] = "thanksbhaiiboii"

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template("home.html")

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        tag = request.form.get("tag")
        questions_count = int(request.form.get("questions_count"))
        questions = scrape_questions(tag, questions_count)

        #working on data
        row_data = list()
        for dict in questions:
            mylist = [0, 0, 0, 0, 0]
            mylist[0] = dict['index']
            mylist[1] = dict['question']
            mylist[2] = dict['votes']
            mylist[3] = dict['views']
            mylist[4] = dict['link']
            row_data.append(mylist)
        return render_template("question_results.html", result=row_data)

    return render_template("questions.html")

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        username = request.form.get("username")
        user_info, users_count = scrape_users(username)

        #working on data
        row_data = list()
        for dict in user_info:
            mylist = [0, 0, 0, 0, 0]
            mylist[0] = dict['display_name']
            mylist[1] = dict['reputation']
            mylist[2] = dict['badge_counts']
            mylist[3] = dict['location']
            mylist[4] = dict['link']
            row_data.append(mylist)
        return render_template("user_results.html", count=users_count, result=row_data)

    return render_template("users.html")

if __name__ == '__main__':
    app.run(debug=True)
