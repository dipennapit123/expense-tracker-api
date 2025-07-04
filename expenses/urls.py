from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ExpenseIncomeViewSet, UserRegisterView

# Register the transactions endpoint
router = DefaultRouter()
router.register('transactions', ExpenseIncomeViewSet, basename='transactions')

urlpatterns = [
    path('auth/register/', UserRegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),  # Includes /api/transactions/
]
