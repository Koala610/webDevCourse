"""hhback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import test, interract_with_company_list, interract_with_company_details, interract_with_vacancy_details, interract_with_vacancy_list
from api.views import get_vacancies, get_top_ten
urlpatterns = [
    path('test/', test),
    path("companies/", interract_with_company_list),
    path("companies/<int:id>/", interract_with_company_details),
    path("companies/<int:id>/vacancies/", get_vacancies),
    path("vacancies/", interract_with_vacancy_list),
    path("vacancies/<int:id>/", interract_with_vacancy_details),
    path("vacancies/top_ten/", get_top_ten)

]
