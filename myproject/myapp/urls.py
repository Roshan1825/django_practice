from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lists'),
    path('addedit/', views.list_add_edit, name='addEdit'),
    path('list/<int:note_id>/', views.detail, name='detail')
]