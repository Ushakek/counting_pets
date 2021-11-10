from django.urls import path

from .views import CreateView

app_name = 'pets'
urlpatterns = [
    path('pets/', CreateView.as_view())
]
