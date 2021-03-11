from django.urls import path
from hello_world import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    # (path, modul view.nama fungsinya, nama template)
]
