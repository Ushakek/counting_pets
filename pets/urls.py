from django.urls import path

from .views import CreateView, PostPhotosView

app_name = 'pets'
urlpatterns = [
    path('pets/', CreateView.as_view()),
    path('pets/<pk>/photos/', PostPhotosView.as_view())
]
