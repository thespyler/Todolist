from django.urls import path, include
from .views import *
urlpatterns = [
	path('addtask/<name>', addtask),
]