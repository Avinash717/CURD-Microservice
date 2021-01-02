from .models import jobs_model,company_model
from .serializers import job_serializer,company_serializer

from rest_framework import viewsets


class Companyapi(viewsets.ModelViewSet):
	 queryset=company_model.objects.all()
	 serializer_class=company_serializer
	 
class Jobsapi(viewsets.ModelViewSet):
	 queryset=jobs_model.objects.all()
	 serializer_class=job_serializer