from django.urls import path
from .views import *

urlpatterns = [
    path('', Welcome.as_view()),
    path('f/<int:id>/', NameId.as_view()),
]
