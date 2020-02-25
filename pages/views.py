from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class TranslationPageView(TemplateView):
    template_name = 'translation.html'

class CodingPageView(TemplateView):
    template_name = 'coding.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'
