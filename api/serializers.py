from app.models import Todo
from rest_framework import serializers

# Create your serializers here
class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = "__all__"