from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Booking, Aircraft, Slot
# from .forms import CommentForm
# from django.http import HttpResponseRedirect
# from django.contrib import messages


# class BookingList(generic.ListView):
#     model = Aircraft
#     queryset = Aircraft.objects.all()
#     template_name = 'index.html'


class CalendarDisplay(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'booking/index.html',      
        )