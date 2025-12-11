from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('medicines/', views.medicine_list, name='medicine-list'),
    path('medicines/add/', views.medicine_add, name='medicine-add'),
    path('medicines/edit/<int:pk>/', views.medicine_edit, name='medicine-edit'),
    path('medicines/delete/<int:pk>/', views.medicine_delete, name='medicine-delete'),
]
