import smtplib

def send_email_alert(alerts):

    sender = "your_email@gmail.com"
    receiver = "receiver_email@gmail.com"
    password = "your_app_password"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)

        message = "\n".join(alerts)

        subject = "SOC ALERT"

        email = f"Subject: {subject}\n\n{message}"

        server.sendmail(sender, receiver, email)
        server.quit()

    except Exception as e:
        print("Email error:", e)