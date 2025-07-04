from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer, UserRegisterSerializer


class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ExpenseIncome.objects.all()
        return ExpenseIncome.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'message': 'Record updated successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({
            'message': 'Record deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)


# ✅ User Registration View
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
