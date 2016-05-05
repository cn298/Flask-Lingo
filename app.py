from flask import Flask, flash, redirect, render_template, g, request, url_for
import sqlite3

app = Flask(__name__)
app.database = "blog_posts.db"
app.secret_key = 'super spooky secret key'

# A list of words and their corresponding translations for our app
# words = {"Bonjour": "hello", "Jambon": "ham", "Fromage": "cheese"}


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/france', methods=['GET', 'POST'])
def france():
    g.db = connect_db()
    cur = g.db.execute("select * from words where language= ?", ("French",))
    words = [dict(word=row[0], translation=row[1]) for row in cur.fetchall()]
    g.db.close()
    print(words)
    points = 0
    if request.method == "POST":
        for word, translation in words.items():
            if request.form[word] == translation:
                points += 1
        flash(str(points))
        return redirect(url_for('france'))
    return render_template("france.html", words=words)

def connect_db():
    return sqlite3.connect(app.database)



if __name__ == '__main__':
    app.run(debug=True)
