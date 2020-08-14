from rest_framework import serializers
from .models import Memo, User


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'age',
                  'bio', 'birth_place', 'school', 'occupation', 'what_are_you_seeking_on_site',
                  'is_active']
