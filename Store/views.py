from django.shortcuts import render
from Store.forms import *


# Create your views here.
def verkaufen_view(request, *args, **kwargs):
    form_verkaufen = VerkaufenForm(request.POST or None)
    context = {
        'form_verkaufen': form_verkaufen,
    }

    if form_verkaufen.is_valid():
        pass
    return render(request, 'verkauf.html', context)
