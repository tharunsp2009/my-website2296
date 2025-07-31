from flask import Flask, request, send_from_directory
from email.message import EmailMessage
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('attached_assets', 'index.html')

@app.route('/style.css')
def css():
    return send_from_directory('attached_assets', 'style.css')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    # Save to file
    with open("messages.txt", "a") as file:
        file.write(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}\n{'='*40}\n")

    # Send Email Notification
    msg = EmailMessage()
    msg['Subject'] = f'📥 New Message from {name}'
    msg['From'] = 'tharunsp2006@gmail.com'
    msg['To'] = 'tharunsp2006@gmail.com'
    msg.set_content(f"""
    Name: {name}
    Email: {email}
    Phone: {phone}
    Message: {message}
    """)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('tharunsp2006@gmail.com', 'adne zvzc cenr cppm')
            smtp.send_message(msg)
        print("✅ Email sent.")
    except Exception as e:
        print("❌ Email sending failed:", e)

    return f"<h2>Thanks {name}, your message was received!</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)


