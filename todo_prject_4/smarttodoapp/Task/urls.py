from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from .views import (
    TaskListCreateView,
    TaskDetailView,
    CompleteTaskView,
    DashboardView,
    SearchTaskView,
    PriorityFilterView,
    StatusFilterView,RegisterView,
    RegisterView,
    login_page,
    register_page,
    dashboard_page,
    home_page,
)

urlpatterns = [

   path('api/tasks/', TaskListCreateView.as_view()),
path('api/tasks/<int:pk>/', TaskDetailView.as_view()),
path('api/dashboard/', DashboardView.as_view()),
path('api/search/', SearchTaskView.as_view()),
path('api/filter/priority/', PriorityFilterView.as_view()),
path('api/filter/status/', StatusFilterView.as_view()),
path('api/register/', RegisterView.as_view()),
path('api/login/', TokenObtainPairView.as_view()),

path(
    'register/',
    RegisterView.as_view(),
    name='register'
),
    

    path('api/login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    
    path('',home_page,name='home-page'
),
    path('login/', login_page, name='login-page'),

path(
    'register-page/',
    register_page,
    name='register-page'
),

path(
    'dashboard-page/',
    dashboard_page,
    name='dashboard-page'
),
] 
