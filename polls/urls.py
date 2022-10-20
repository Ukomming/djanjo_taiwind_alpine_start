from django.urls  import path
from . import views

urlpatterns = [
    path('',views.home),
    path('form/',views.ModelForm),
    path('forms/',views.Form),
]