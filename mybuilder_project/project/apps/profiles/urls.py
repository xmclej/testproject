from django.urls import path
from project.apps.profiles import views

app_name = 'profiles'
urlpatterns = [
    path('edit/<int:pk>', views.edit_user.as_view(), name='edit-user'),
]
