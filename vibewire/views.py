from django.shortcuts import render
from .models import Vibewire
from .forms import vibewireForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.

def index(request):
    return render(request, 'index.html')

def vibewire_list(request):
        vibewires = vibewire.objects.all().order_by('-created_at')
        return render(request, 'vibewire_list.html', {'vibewires' : vibewires})

@login_required
def vibewire_create(request):
    if request.method == "POST":
        form = vibewireForm(request.POST, request.FILES)
        if form.is_valid():
            vibewire = form.save(commit=False)
            vibewire.user = request.user
            vibewire.save()
            return redirect('vibewire_list')

    else:
        form = vibewireForm()
    return render(request, 'vibewire_form.html', {'form': form})

@login_required
def vibewire_edit(request, vibewire_id):
    vibewire_instance = get_object_or_404(Vibewire, pk=vibewire_id, user = request.user)
    if request.method == 'POST':
        form = vibewireForm(request.POST, request.FILES, instance=vibewire_instance)
        if form.is_valid():
            vibewire_instance = form.save(commit=False)
            vibewire_instance.user = request.user
            vibewire_instance.save()
            return redirect('vibewire_list')
    else:
        form = vibewireForm(instance=vibewire_)
    return render(request, 'vibewire_form.html', {'form': form})

@login_required
def vibewire_delete(request, vibewire_id):
    vibewire = get_object_or_404(Vibewire, pk=vibewire_id, user = request.user)
    if request.method == 'POST':
        vibewire.delete()
        return redirect('vibewire_list')
    return render(request, 'vibewire_confirm_delete.html', {'vibewire': vibewire})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('vibewire_list')
    else:
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    