from django.shortcuts import render
from .models import StudentProfile
from .forms import ContactForm

# Afișează datele din CV
def about_view(request):
    profile = StudentProfile.objects.first()  # preia primul profil din baza de date
    return render(request, 'core/about.html', {'profile': profile})

# Pagina de contact
def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()  # salvează mesajul în DB
    return render(request, 'core/contact.html', {'form': form})
