from rest_framework.serializers import ModelSerializer

from apps.account.models import User
from .models import Education, Resume, Skill, WorkExperience, Language


class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = ('id', 'name',)


class EducationSerializer(ModelSerializer):

    class Meta:
        model = Education
        fields = ('id', 'name',)


class LanguageSerializer(ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'name',)


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'profile', 'about', 'phone_no',)


class WorkExperienceSerializer(ModelSerializer):

    class Meta:
        model = WorkExperience
        fields = ('id', 'name',)


class ResumeSerializer(ModelSerializer):
    
    skill = SkillSerializer(many=True)
    user = UserSerializer()
    education = EducationSerializer(many=True)
    language = LanguageSerializer(many=True)
    work_experience = WorkExperienceSerializer(many=True)

    class Meta:
        model = Resume
        fields = ('id', 'user', 'skill', 'language', 'education', 'work_experience', 'work_experience_time',)


class UserResumeSerializer(ModelSerializer):
    
    class Meta:
        model = Resume
        exclude = ('user',)
