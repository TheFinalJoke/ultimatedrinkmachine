from django.urls import path

from . import views
app_name = "selections"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("<int:pk>/", views.SelectedView.as_view(), name='selected')
]
