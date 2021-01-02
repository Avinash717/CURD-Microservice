from django.contrib import admin
from .models import jobs_model,company_model
# Register your models here.
admin.site.register(company_model)
admin.site.register(jobs_model)
