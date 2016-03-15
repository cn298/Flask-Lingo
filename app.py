from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'super spooky secret key'

# A list of words and their corresponding translations for our app
words = {"bonjour": "hello", "jambon": "ham", "fromage": "cheese"}


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Reset visitor score to 0 each time page is loaded
    points = 0
    if request.method == "POST":
        # Loop through every word + corresponding translation in dictionary
        for word, translation in words.items():
            # Check if the users translation is correct
            if request.form[word] == translation:
                # If it is then increase the point tally
                points += 1
        # Flash a message to the screen showing the users score
        flash(str(points))
        # Then refresh the page to dispay the score
        return redirect(url_for('quiz'))

    # If the request method isn't a POST request, just load the template
    return render_template("quiz.html", words=words)

if __name__ == '__main__':
    app.run(debug=True)
