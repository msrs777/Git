from flask import Flask, request

app = Flask(__name__)

WEBHOOK_SECRET = "github-webhook-secret-2026"


@app.route("/")
def home():
    return "GitHub App is running!"


@app.route("/webhook", methods=["POST"])
def webhook():
    event = request.headers.get("X-GitHub-Event")

    print("GitHub Event:", event)

    data = request.json

    if event == "push":
        repository = data["repository"]["full_name"]
        print("Push received from:", repository)

    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
