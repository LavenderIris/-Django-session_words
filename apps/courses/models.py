from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be more than 5 characters"
        return errors

class Course(models.Model):
    name =  models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
    

class DescriptionManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['desc']) < 5:
            errors["desc"] = "Description should be more than 15 characters"
        return errors

class Description(models.Model):
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    desc = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects =  DescriptionManager()
