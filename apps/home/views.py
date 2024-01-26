from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact, Review, Slider, OurService, AboutUs, WhyChooseUs, ContactForm, WebsiteShortDescription, Blog
from django.core.exceptions import MultipleObjectsReturned
from django.http import Http404
from django.contrib import messages



def Homepage(request):
    review = Review.objects.all()
    slider = Slider.objects.all()
    our_service = OurService.objects.all()
    aboutus = AboutUs.objects.first()
    whychoose = WhyChooseUs.objects.all()
    service_desc = WebsiteShortDescription.objects.filter(where=WebsiteShortDescription.SERVICE)
    zodiac_sign = WebsiteShortDescription.objects.filter(where=WebsiteShortDescription.ZODIAC_SIGN)
    review_desc = WebsiteShortDescription.objects.filter(where=WebsiteShortDescription.REVIEW)
    choose_us_desc = WebsiteShortDescription.objects.filter(where=WebsiteShortDescription.CHOOSE_US)

    context = {
        'slider':slider,
        'review':review,
        'our_service':our_service,
        'aboutus':aboutus,
        'whychoose':whychoose,
        'service_desc':service_desc,
        'zodiac_sign':zodiac_sign,
        'review_desc':review_desc,
        'choose_us_desc':choose_us_desc,
    }
    return render(request, 'home.html', context)

def ServiceDetails(request, pk):
    service_desc = get_object_or_404(OurService, pk=pk)
    context = {
        'service_desc':service_desc,
    }

    return render(request, 'service-detail.html', context)



def Contact(request):
    return render(request, 'contact.html', context=None)

def send_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact_form = ContactForm(name=name, email=email, phone=phone, message=message)
        contact_form.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/contact')

def Blogs(request):
    blog = Blog.objects.all()

    context ={
        'blog':blog,
    }
    return render(request, 'blog.html', context)


def BlogDetail(request,slug):
    blogs = get_object_or_404(Blog, slug=slug)
    context = {
        'blogs':blogs,
    }
    return render(request, 'blog-details.html', context)
