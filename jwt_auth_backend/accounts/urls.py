from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, get_user_profile, logout_view, register_view, userLogout_view
from accounts import views as accounts_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logout_view, name='logout'),
    path('view-accounts/', get_user_profile, name='user_profile'),
    path('', accounts_views.custom_admin_dashboard, name='custom_admin'),
    path('UserLogout/', userLogout_view, name='UserLogout'),
    path('UserRegister/', register_view, name='UserRegister'),
]
