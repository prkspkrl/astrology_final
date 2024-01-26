from django.urls import path
from . import views


urlpatterns = [
    path('', views.Homepage, name= 'home'),
    path('service/<int:pk>', views.ServiceDetails, name= 'service'),
    path('contact', views.Contact, name= 'contact'),
    path('blog', views.Blogs, name= 'blogs'),
    path('blog-detail/<str:slug>', views.BlogDetail, name= 'blogdetail'),
    path('send_message', views.send_message, name= 'send_message'),
]