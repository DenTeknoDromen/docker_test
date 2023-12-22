from flask import Flask, render_template, redirect
import random
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

app = Flask(__name__)

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

def generate_wise_saying():
    sayings = [
        "A journey of a thousand miles begins with a single step.",
        "The only thing we have to fear is fear itself.",
        "The early bird catches the worm.",
        "Actions speak louder than words.",
        "Where there is a will, there is a way.",
        "Patience is a virtue.",
        "The more you give, the more you receive.",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.",
        "Haste makes waste.",
        "The best way to predict the future is to create it.",
    ]

    return random.choice(sayings)

@app.route('/index')
def home():
    wise_saying = generate_wise_saying()
    return render_template('page.html', wise_saying=wise_saying)

@app.errorhandler(404)
def page_notfound(error):
    return redirect("/index")

# Startar servern när man kör filen
# Samma som "flask --app run test run --host=0.0.0.0 --port=8000"
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)