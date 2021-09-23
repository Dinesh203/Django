from django.urls import path
from . import views

urlpatterns = [
    path("", views.Add_Show, name="Add_Show"),
    path("delete_data/<int:id>/", views.delete_data, name="delete_date"),
    path("<int:id>/", views.update_date, name="update_date"),
]
