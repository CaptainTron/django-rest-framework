from django.urls import path
from . import views

urlpatterns = [ 
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('book-slot/<int:center_id>/', views.book_slot, name='book_slot'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'), 
    path('add-center/', views.add_center, name='add_center'),
    path('remove-center/<int:center_id>/', views.remove_center, name='remove_center'),
    path('dosage-details/', views.dosage_details, name='dosage_details'),
    path('add-center/', views.add_center, name='add_center'),
]