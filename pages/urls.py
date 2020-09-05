# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:25:57 2020

@author: Keyvan
"""

from django.urls import path
from .views import homePageInfo

urlpatterns = [
        path('', homePageInfo, name = 'home')
        ]