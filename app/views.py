from django.shortcuts import redirect, render
from app.forms import CargosForm
from app.models import cargos


def home(request):
    data = {}
    data["db"] = cargos.objects.all()
    return render(request, "index.html", data)


def form(request):
    data = {}
    data["form"] = CargosForm()
    return render(request, "form.html", data)


def create(request):
    form = CargosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")

def view(request, pk):
    data = {}
    data['db'] = cargos.objects.get(pk = pk) 
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = cargos.objects.get(pk = pk)
    data['form'] = CargosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = cargos.objects.get(pk = pk)
    form = CargosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
       form.save() 
    return redirect('home')
