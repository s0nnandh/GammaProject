from rest_framework import serializers
from .models import Person
from .models import Group
from .models import MessageForm,Message_seen

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name','userid','email','password','Token_key','group_set']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageForm
        fields = ['printer','priority','time','header','text','seen']

class Mess(serializers.ModelSerializer):
    class Meta:
        model = Message_seen
        fields = '__all__'