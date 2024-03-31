from django.shortcuts import render

# Create your views here.


def prenotazioneViews(request):
    return render(request, 'Prenotazione/SitePrenotazione.html')