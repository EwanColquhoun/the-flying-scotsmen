from django.shortcuts import render
from django.views import View


class AwaitingRegDisplay(View):

    def get(self, request):

        return render(
            request,
            'booking/awaiting_reg.html',
        )
