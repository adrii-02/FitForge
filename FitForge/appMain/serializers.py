from rest_framework import serializers
from .models.model_user import User  # Reemplaza con tus modelos

class UserSerializer(serializers.ModelSerializer):
    #type_user = TypeUserSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'age', 'gender', 'length', 'weight']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user