from django.urls import path
from .views import *

urlpatterns = [
	path('', main),
	path('check/', check),
	path('login/', new_log),
	path('<name>/', function),
	path('signin/', signin),
	path('addlikes/', addlike),	
]