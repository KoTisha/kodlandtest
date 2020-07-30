from django.urls import path
from core import views

urlpatterns = [
    path('', views.MainFormView.as_view(), name='index'),
    path('add/', views.AddFormView.as_view(), name='add'),
    path('<int:state>/', views.StateFormView.as_view(), name='state'),
]
