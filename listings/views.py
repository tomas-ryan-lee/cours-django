from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {
        'bands': bands
    })

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {
        'band': band
    })