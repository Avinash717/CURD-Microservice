# -*- coding: utf-8 -*-

from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("Companymodel",views.Companyapi)
router.register("Jobsmodel",views.Jobsapi)

urlpatterns = [   
	path('',include(router.urls)),
]# -*- coding: utf-8 -*-

