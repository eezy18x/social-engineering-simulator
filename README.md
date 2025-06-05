# Social Engineering Attack 

This project simulates phishing attacks for ethical and educational purposes only.

---

## Features (Current)

- Simulate a phishing email with a clickable link (localhost link)
- Run a local Flask server serving a fake Gmail login page
- Capture submitted email and password into a local file `creds.txt`
- Designed for ethical training and demonstration only

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/eezy18x/social-engineering-simulator.git
cd social-engineering-simulator
```

Install dependencies:

Make sure you have Python 3 and pip installed.

bash
Copy code
pip install flask
Start the phishing server:

bash
Copy code
python3 phishing_server/app.py
The server will run on http://localhost:5000

Simulate phishing email:

In another terminal, run the main simulation script:

bash
Copy code
python3 main.py
Choose the phishing simulation option. It will show a fake phishing email with a clickable link:
http://localhost:5000

Use the link:

Open the link in a browser, enter fake email and password credentials.
Credentials will be saved locally in phishing_server/creds.txt.

Notes
This tool is for ethical use only, for training and awareness.

The phishing pages are hosted locally and do not send any data externally.

Do not use this for any illegal or malicious activities.

Future Work
Add more phishing templates (Facebook, PayPal, etc.)

Add a dashboard to view captured credentials

Enhance UI to look more realistic


