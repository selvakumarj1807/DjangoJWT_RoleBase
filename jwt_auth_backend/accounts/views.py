from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer, UserSerializer
from .models import User
from .permissions import IsAdminUser, IsCustomerUser
from django.contrib.auth import logout


from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from .models import User
from .forms import CustomUserCreationForm
from django.contrib import messages

@login_required
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully!")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def userLogout_view(request):
    logout(request)
    return redirect('login')  # or your login URL name

def is_admin_or_superuser(user):
    return user.is_authenticated and (user.is_superuser or user.role == 'admin')

@login_required
@user_passes_test(is_admin_or_superuser)
def custom_admin_dashboard(request):
    context = {
        'total_users': User.objects.count(),
        'total_admins': User.objects.filter(role='admin').count(),
        'total_staff': User.objects.filter(role='staff').count(),
        'total_customers': User.objects.filter(role='customer').count(),
        'users': User.objects.all().order_by('-date_joined'),
    }
    return render(request, 'accounts/admin_dashboard.html', context)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def logout_view(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logout successful"})
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    

    
