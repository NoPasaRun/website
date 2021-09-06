from django.urls import path
from .views import MainView, CreateView, ShowAddView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('create/', CreateView.as_view(), name='create'),
    path('add/content/<int:pk>', ShowAddView.as_view(), name='add_content')
]