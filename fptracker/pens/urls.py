from django.urls import path

from . import views

urlpatterns = [
    path('pens/add', views.edit_pen, name="add_pen"),
    path('pens/edit/<int:pen_id>', views.edit_pen, name="edit_pen"),
    path('pens/delete/<int:pen_id>', views.delete_pen, name="delete_pen"),
    path('', views.index, name='index'),
]
