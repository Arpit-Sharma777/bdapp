from django import forms
from django.shortcuts import render,redirect
from .forms import DonorForm
from .models import Donor

BLOOD_GROUPS = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)
class SearchForm(forms.Form):
    blood_group = forms.ChoiceField(choices=BLOOD_GROUPS)

def register_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_detail')  # or any other success URL
    else:
        form = DonorForm()
    return render(request, 'register.html', {'form': form})

def search(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            blood_group = form.cleaned_data['blood_group']
            donors = Donor.objects.filter(blood_group=blood_group)
            return render(request, "donors/search.html", {"donors": donors})
    else:
        form = SearchForm()
    return render(request, "donors/search.html", {"form": form})

def donor_detail(request, pk):
    donor = get_object_or_404(Donor, pk=pk)
    # ...
    return render(request, 'donor_detail.html', {'donor': donor})
def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'donor_list.html', {'donors': donors})