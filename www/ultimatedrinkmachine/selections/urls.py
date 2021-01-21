from django.urls import path

from . import views
app_name = "selections"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("<int:recipe_id>/selected/", views.forms_selected, name='selected'),
    path("<int:recipe_id>/package/", views.package, name='package'),
    path("<int:recipe_id>/post_dispense/", views.post_dispense, name='post_dispense'),
    path("add_drink/", views.add_drink, name="add_drink"),
    path('post_adddrink/', views.post_adddrink, name="post_adddrink"),
    path('deleterecipe/', views.delete_recipe, name="delete_recipe"),
    path('postdelete/', views.post_delete, name='post_delete')
]
