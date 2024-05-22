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
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        weight = request.POST.get('weight')
        email = request.POST.get('email')
        blood_group = request.POST.get('blood_group')
        last_donation_date = request.POST.get('last_donation_date')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        Donor.object.create(name=name, age=age, weight=weight, email=email, blood_group=blood_group, 
                      last_donation_date=last_donation_date, phone_number=phone_number, 
                      address=address, city=city, state=state, zip_code=zip_code)
        donor.save()
        return redirect('donor_detail')  # or any other success URL
    return render(request, 'register.html')

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