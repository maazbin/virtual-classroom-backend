from rest_framework import serializers
from .models import User,Room,Discussion,Topic,Response,Comment,Enrolment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class EnrolmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrolment
        fields = ['student','room']