from dataclasses import field
from rest_framework import serializers
from .models import FeedBack




class FeedBackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = FeedBack
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('userid', 'pollsid'),
                message=("Feedback Already Given")
            )
        ]