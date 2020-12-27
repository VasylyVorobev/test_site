from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/booking/', views.BookingView.as_view(), name='booking_form_url'),
    path('podbor-prepodavatelya/', views.SelectionTeacherView.as_view(), name='select_teacher_url'),
    path('profile/<slug:slug>', views.ProfilesDetail.as_view(), name='profile_detail'),
    path('', views.ProfilesList.as_view(), name='profiles_list'),
    path('<slug:category_slug>/', views.ProfilesList.as_view(), name='profiles_list_by_category'),

]
