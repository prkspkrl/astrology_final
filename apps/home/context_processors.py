from .models import Contact

def contactus(request):
    contact = Contact.objects.first()
    return dict(contact=contact)