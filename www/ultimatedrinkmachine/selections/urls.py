from django.urls import path

from . import views
app_name = "selections"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("<int:recipe_id>/selected/", views.forms_selected, name='selected'),
    path("<int:recipe_id>/package/", views.package, name='package'),
]
