from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, HyperlinkedModelSerializer

from apps.account.models import User
from .models import Resume, Skill, WorkExperience


class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = ('name',)


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'about', 'phone_no',)


class WorkExperienceSerializer(ModelSerializer):

    class Meta:
        model = WorkExperience
        fields = ('name',)

class ResumeSerializer(ModelSerializer):
    
    skill = SkillSerializer(many=True)
    user = UserSerializer()
    work_experience = WorkExperienceSerializer(many=True)

    class Meta:
        model = Resume
        fields = ('id', 'user', 'skill', 'work_experience', 'work_experience_time',)


class UserResumeSerializer(ModelSerializer):
    
    class Meta:
        model = Resume
        exclude = ('user',)
