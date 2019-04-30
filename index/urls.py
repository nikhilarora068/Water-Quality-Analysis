from django.urls import path
from index import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('plot/', views.plot, name = "plot"),
    path('state/<str:state_name>/', views.state_chart, name = "state_chart"),
    path('state_wise/', views.state_wise, name = "state_wise"),
    path('theory/', views.theory, name = "theory"),
]
