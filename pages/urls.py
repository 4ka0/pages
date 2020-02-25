from django.urls import path
from .views import HomePageView
from .views import AboutPageView
from .views import TranslationPageView
from .views import CodingPageView
from .views import ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('translation/', TranslationPageView.as_view(), name='translation'),
    path('coding/', CodingPageView.as_view(), name='coding'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
