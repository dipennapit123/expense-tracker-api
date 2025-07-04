from rest_framework import serializers
from .models import ExpenseIncome
from django.contrib.auth.models import User


class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ExpenseIncome
        fields = [
            'id',
            'user',
            'title',
            'description',
            'amount',
            'transaction_type',
            'tax',
            'tax_type',
            'created_at',
            'updated_at',
            'total',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'user', 'total']

    def get_total(self, obj):
        if obj.tax_type == 'flat':
            return obj.amount + obj.tax
        elif obj.tax_type == 'percentage':
            return obj.amount + (obj.amount * obj.tax / 100)
        return obj.amount


# ✅ Registration serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
