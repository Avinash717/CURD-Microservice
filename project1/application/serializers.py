# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import jobs_model,company_model

class job_serializer(serializers.ModelSerializer):
	class Meta:
		model=jobs_model
		fields="__all__"	  
class company_serializer(serializers.ModelSerializer):
	jobs= job_serializer(read_only=True,many=True)
	class Meta:
		model=company_model
		fields="__all__"