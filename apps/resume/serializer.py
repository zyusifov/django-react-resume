from rest_framework.serializers import ModelSerializer
from .models import Resume


class ResumeSerializer(ModelSerializer):
    
    class Meta:
        model = Resume
        fields = '__all__'


class UserResumeSerializer(ModelSerializer):
    
    class Meta:
        model = Resume
        exclude = ('user', )