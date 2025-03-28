from django.shortcuts import render
from .forms import RegionForm

def region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return credits('region')

    else:
        form = RegionForm()

    ctx = {
        'form':form
    }
    return render(request,'region.html',ctx)
