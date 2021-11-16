import os
import smtplib, ssl


def send_email_to_admin(username, date):
    sender_email = "theflyingscotsmen.booking@gmail.com"
    receiver_email = "theflyingscotsmen.booking@gmail.com"
    message = f"""
    Subject: NEW BOOKING

    Hi Admin,

    You have a new booking request to approve from {username} for {date}.
    
    Click here to visit the admin site
    
    https://the-flying-scotsmen.herokuapp.com/admin/booking/booking/
    
    Thanks."""


    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "theflyingscotsmen.booking@gmail.com"
    password = os.environ.get('EMAIL_PASSWORD')

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 