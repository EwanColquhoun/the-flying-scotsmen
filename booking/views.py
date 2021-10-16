from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Booking, Aircraft, Slot
from .forms import BookingForm
# from django.http import HttpResponseRedirect
from django.contrib import messages


# class BookingList(generic.ListView):
#     model = Aircraft
#     queryset = Aircraft.objects.all()
#     template_name = 'index.html'


class HomeDisplay(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'booking/index.html',
        )


class BookingDisplay(View):

    def get(self, request, *args, **kwargs):
        current_user = request.user
        bookings = Booking.objects.filter(username=current_user).filter(approved=True)
        
        return render(
            request,
            'booking/bookings.html',
            {
                "bookings": bookings,
                "bookingform": BookingForm(),
            },
        )

    def post(self, request, *args, **kwargs):
        current_user = request.user
        bookings = Booking.objects.filter(username=current_user).filter(approved=True)
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'Your booking will be added once approved by admin. Thank you.')
            return redirect('bookings')
        else:
            booking_form = BookingForm()

        return render(
            request,
            'booking/bookings.html',
            {
                "bookings": bookings,
                "bookingform": BookingForm(),
            },
        )
        
    # def editBooking(request, booking_id):

    #     booking = get_object_or_404(Booking, id=booking_id)
    #     if request.method == 'POST':
    #         form = BookingForm()(request.POST, instance=booking)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('bookings')
    #     form = BookingForm()(instance=booking)
    #     context = {
    #         'form': form,
    #         'booking': booking,
    #     }
    #     return render(request, "logbook/edit.html", context)