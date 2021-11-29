from rest_framework import serializers
from .model import language

class languageSerializer(serializers.ModelSerializer):
	class Meta:
		Model = language
		fields = ('id', 'name', 'paradigm')

