from django.urls import path

from .views import startView, addView, deleteView

urlpatterns = [
    path('', startView, name='start'),
    path('add/', addView, name='add'),
    path('delete/', deleteView, name='delete')
    
]
