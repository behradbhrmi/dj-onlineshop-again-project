from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'pages/home.html'


class AboutUs(TemplateView):
    template_name = 'pages/aboutus.html'


class ContactUs(TemplateView):
    template_name = 'pages/contactus.html'
