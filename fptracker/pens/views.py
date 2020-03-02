from django.shortcuts import render, redirect
from pens.models import Pen, PenForm, Ink, InkForm

# Create your views here.

def index(request):

    all_pens = Pen.objects.all()
    all_inks = Ink.objects.all()
    context = {
        'pen_list': all_pens,
        'ink_list': all_inks,
        'page_title': "Fountain Pen Collection",
    }
    return render(request, "index.html", context)

def edit_object(request, obj_id=None):
    if request.method == 'POST':
        if obj_id is not None:
             pen = Pen.objects.get(id=obj_id)
             form = PenForm(request.POST, instance=pen)
        else:
            form = PenForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        if obj_id is not None:
             pen = Pen.objects.get(id=obj_id)
             form = PenForm(instance=pen)
        else:
            form = PenForm()

    context = {
        'form': form,
        'obj_id': obj_id
    }
    return render(request, "edit_object.html", context)

def delete_pen(request, obj_id):
    pen = Pen.objects.get(id=obj_id)
    pen.delete()
    return redirect(index)

def edit_ink(request, ink_id=None):
    if request.method == 'POST':
        if ink_id is not None:
            ink = Ink.objects.get(id=ink_id)
            form = InkForm(request.POST, instance=ink)
        else:
            form = InkForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        if ink_id is not None:
            ink = Ink.objects.get(id=ink_id)
            form = InkForm(instance=ink)
        else:
            form = InkForm()

    context = {
        'form': form,
        'ink_id': ink_id
    }

    return render(request, 'edit_ink.html', context)

def delete_ink(request, ink_id):
    ink = Ink.objects.get(id=ink_id)
    ink.delete()
    return redirect('/')
