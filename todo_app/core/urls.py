from django.urls import path
from .views import Home, add, delete, complete, clear

app_name = 'core'


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add/', add, name='add'),
    path('delete/<int:item_id>/', delete, name='delete'),
    path('complete/<int:item_id>/', complete, name='complete'),
    path('clear/', clear, name='clear'),
]
