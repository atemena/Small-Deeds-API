from django.shortcuts import render
from rest_framework import generics
from serializer import DeedSerializer, PledgeSerializer
from models import Deed, Pledge
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin
# Create your views here.


#API Views
class DeedList(generics.ListCreateAPIView):
	queryset = Deed.objects.all()
	serializer_class = DeedSerializer

class DeedDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Deed.objects.all()
	serializer_class = DeedSerializer

class PledgeList(generics.ListCreateAPIView):
	serializer_class = PledgeSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		user = self.request.user
		return Pledge.objects.filter(user=user)

	def perform_create(self, serializer):
		user = self.request.user
		queryset = Pledge.objects.filter(user=user, deed=self.request.data['deed'])
		if queryset.exists():
			raise ValidationError('You have already pledged to this deed!')
		pledge = self.request.data
		serializer.save(user=user, deed=Deed.objects.get(pk=pledge['deed']), threshold=pledge['threshold'], active=pledge['active'])


# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def login(request):
# 	import pdb; pdb.set_trace();
# 	import rest_auth_views;
# 	rest_auth_views.obtain_auth_token(request)