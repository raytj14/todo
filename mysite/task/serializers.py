from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """todoモデル用のシリアライザ"""  
    class Meta:
        model = Todo
        fields = ['todo', 'created_at', 'updated_at'] 
