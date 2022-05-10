from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('category/<int:category_id>', get_category, name='category'),
]
