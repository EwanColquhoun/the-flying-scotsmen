from django.core.mail import send_mail


def booking_email(booking):
    send_mail(
        'New Booking Request',
        f"""
        Subject: NEW BOOKING

        You have a new booking request to approve
        Member Username: {booking.username}
        Booking Date: {booking.date}
        Slot: {booking.slot}
        Aircraft: {booking.aircraft}
        Instructor Requested: {booking.instructor_requested}
        Notes: {booking.notes}

        Click here to visit the admin site

        https://the-flying-scotsmen.herokuapp.com/admin/booking/booking/

        Thanks.""",
        None,
        ['theflyingscotsmen.booking@gmail.com'],
        fail_silently=True,
    )


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
        fail_silently=True,
    )


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
        fail_silently=True,
    )
