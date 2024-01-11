from rest_framework import serializers

from .models import Exercise, Reps, Routine, Series, Type_User, User


class TypeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_User
        fields = ['id', 'admin', 'user']

class UserSerializer(serializers.ModelSerializer):
    type_user = TypeUserSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'age', 'gender', 'length', 'weight', 'type_user']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class RoutineSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Routine
        fields = ['id', 'name', 'user']

class ExerciseSerializer(serializers.ModelSerializer):
    routine = RoutineSerializer()

    class Meta:
        model = Exercise
        fields = ['id', 'name', 'routine']

class SeriesSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = Series
        fields = ['id', 'exercise']

class RepsSerializer(serializers.ModelSerializer):
    series = SeriesSerializer()

    class Meta:
        model = Reps
        fields = ['id', 'num_reps', 'rpe', 'series']