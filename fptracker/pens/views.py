from django.shortcuts import render
from pens.models import Pen

# Create your views here.

def index(request):

    all_pens = Pen.objects.all()

    context = {
        'pen_list': all_pens,
        'page_title': "Fountain Pen Collection"
    }
    return render(request, "index.html", context)
