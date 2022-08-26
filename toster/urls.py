from django.urls import path
from toster.views import index, test5

urlpatterns = [
    path('', index, name='index'),
    path('test5', test5, name='test5'),
]
