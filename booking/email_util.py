import smtplib
import ssl
import os
import yagmail
from django.core.mail import send_mail


def booking_email(booking):
    send_mail(
        'New Booking Request',
        f"""
#         Subject: NEW BOOKING

#         You have a new booking request to approve
#         Member Username: {booking.username}
#         Booking Date: {booking.date}
#         Slot: {booking.slot}
#         Aircraft: {booking.aircraft}
#         Instructor Requested: {booking.instructor_requested}
#         Notes: {booking.notes}

#         Click here to visit the admin site

#         https://the-flying-scotsmen.herokuapp.com/admin/booking/booking/

#         Thanks.""",
        None,
        ['theflyingscotsmen.booking@gmail.com'],
        fail_silently=False,
    )

# def booking_email(booking):
#     adminEmail = os.environ.get('ADMIN_EMAIL')
#     password = os.environ.get('EMAIL_PASSWORD')
#     yag = yagmail.SMTP(adminEmail, password)
#     contents = [f"""
#         Subject: NEW BOOKING

#         You have a new booking request to approve
#         Member Username: {booking.username}
#         Booking Date: {booking.date}
#         Slot: {booking.slot}
#         Aircraft: {booking.aircraft}
#         Instructor Requested: {booking.instructor_requested}
#         Notes: {booking.notes}

#         Click here to visit the admin site

#         https://the-flying-scotsmen.herokuapp.com/admin/booking/booking/

#         Thanks."""]
#     yag.send(adminEmail, 'New Booking', contents)

# class EmailConfig:
#     sender_email = "theflyingscotsmen.booking@gmail.com"
#     receiver_email = "theflyingscotsmen.booking@gmail.com"
#     smtp_server = "smtp.gmail.com"
#     port = 465
#     password = os.environ.get('EMAIL_PASSWORD')

#     @classmethod
#     def send_email(self, message):
#         context = ssl.create_default_context()
#         try:
#             with smtplib.SMTP(self.smtp_server, self.port) as server:
#                 server.ehlo()  # Can be omitted
#                 server.starttls(context=context)
#                 server.ehlo()  # Can be omitted
#                 server.login(self.sender_email, self.password)
#                 server.sendmail(self.sender_email, self.receiver_email, message)
#         except smtplib.SMTPException as error:
#             print(error)


def contact_email(contact):
    send_mail(
        'New Contact Request',
        f"""
        Subject: CONTACT

        You have a new contact request from {contact.name}

        Telephone - {contact.telephone}
        Email - {contact.email}
        Message - {contact.message}


        Click here to visit the admin site

        https://the-flying-scotsmen.herokuapp.com/admin/contact/

        Thanks.""",
        None,
        ['theflyingscotsmen.booking@gmail.com'],
        fail_silently=False,
    )

# def send_email_to_admin(booking):
#     # sender_email = "theflyingscotsmen.booking@gmail.com"
#     # receiver_email = "theflyingscotsmen.booking@gmail.com"
#     message = f"""
#     Subject: NEW BOOKING

#     You have a new booking request to approve
#     Member Username: {booking.username}
#     Booking Date: {booking.date}
#     Slot: {booking.slot}
#     Aircraft: {booking.aircraft}
#     Instructor Requested: {booking.instructor_requested}
#     Notes: {booking.notes}

#     Click here to visit the admin site

#     https://the-flying-scotsmen.herokuapp.com/admin/booking/booking/

#     Thanks."""
    # smtp_server = "smtp.gmail.com"
    # port = 587  # For starttls
    # sender_email = "theflyingscotsmen.booking@gmail.com"
    # password = os.environ.get('EMAIL_PASSWORD')

    # # Create a secure SSL context
    # context = ssl.create_default_context()
    # EmailConfig.send_email(message)
    # Try to log in to server and send email

    # try:
    #     server = smtplib.SMTP(EmailConfig.smtp_server, EmailConfig.port)
    #     server.ehlo()
    #     server.starttls(context=context)  # Secure the connection
    #     server.ehlo()
    #     server.login(EmailConfig.sender_email, EmailConfig.password)
    #     server.sendmail(EmailConfig.sender_email, Email.Config.receiver_email, message)
    # except Exception as e:
    #     # Print any error messages to stdout
    #     print(e)
    # finally:
    #     server.quit()


def register_email(user):
    send_mail(
        'New Registration Request',
        f"""
        Subject: REGISTER

        You have a new registration request from {user.first_name}

        Username - {user.username}
        First Name - {user.first_name}
        Last Name - {user.last_name}
        Email - {user.email}
        Message - {user.message}


        Click here to visit the admin site

        https://the-flying-scotsmen.herokuapp.com/admin/booking/group_member/

        Thanks.""",
        None,
        ['theflyingscotsmen.booking@gmail.com'],
        fail_silently=False,
    )


# def send_contact_email_to_admin(contact):
#     sender_email = "theflyingscotsmen.booking@gmail.com"
#     receiver_email = "theflyingscotsmen.booking@gmail.com"
#     message = f"""
#     Subject: CONTACT

#     You have a new contact request from {contact.name}

#     Telephone - {contact.telephone}
#     Email - {contact.email}
#     Message - {contact.message}


#     Click here to visit the admin site

#     https://the-flying-scotsmen.herokuapp.com/admin/contact/

#     Thanks."""

#     smtp_server = "smtp.gmail.com"
#     port = 587  # For starttls
#     sender_email = "theflyingscotsmen.booking@gmail.com"
#     password = os.environ.get('EMAIL_PASSWORD')

#     # Create a secure SSL context
#     context = ssl.create_default_context()

#     # Try to log in to server and send email
#     try:
#         server = smtplib.SMTP(smtp_server, port)
#         server.ehlo()
#         server.starttls(context=context)  # Secure the connection
#         server.ehlo()
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message)
#     except Exception as e:
#         # Print any error messages to stdout
#         print(e)
#     finally:
#         server.quit()


# def send_register_email_to_admin(user):
#     sender_email = "theflyingscotsmen.booking@gmail.com"
#     receiver_email = "theflyingscotsmen.booking@gmail.com"
#     message = f"""
#     Subject: REGISTER

#     You have a new registration request from {user.first_name}

#     Username - {user.username}
#     First Name - {user.first_name}
#     Last Name - {user.last_name}
#     Email - {user.email}
#     Message - {user.message}


#     Click here to visit the admin site

#     https://the-flying-scotsmen.herokuapp.com/admin/booking/group_member/

#     Thanks."""

#     smtp_server = "smtp.gmail.com"
#     port = 587  # For starttls
#     sender_email = "theflyingscotsmen.booking@gmail.com"
#     password = os.environ.get('EMAIL_PASSWORD')

#     # Create a secure SSL context
#     context = ssl.create_default_context()

#     # Try to log in to server and send email
#     try:
#         server = smtplib.SMTP(smtp_server, port)
#         server.ehlo()
#         server.starttls(context=context)  # Secure the connection
#         server.ehlo()
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message)
#     except Exception as e:
#         # Print any error messages to stdout
#         print(e)
#     finally:
#         server.quit()
