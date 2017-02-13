from rest_framework import serializers
from models import Deed, Pledge
from django.contrib.auth.models import User

class DeedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Deed
		field = ('title', 'description', 'type', 'inactive_pledges', 'active_pledges', 'tags', 'created', 'updated')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('email', 'username', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User(
			email=validated_data['email'],
			username=validated_data['username']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user

class PledgeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pledge
		user = UserSerializer()
		deed = DeedSerializer()
		field = ('threshold', 'active')
		extra_kwargs = {
			'user': {'required': False}
		}

	def create(self, validated_data):
		pledge = Pledge(
			user=validated_data['user'],
			deed=validated_data['deed'],
			threshold=validated_data['threshold'],
			active=validated_data['active']
		)
		pledge.save()
		return pledge
