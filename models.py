from django.db import models


class Project(models.Model):
    project_id = models.BigAutoField(primary_key=True)
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    created_by = models.CharField(max_length=50)


class Issues(models.Model):
    issue_id = models.BigAutoField(primary_key=True)
    issue_title = models.CharField(max_length=200)
    issue_description = models.TextField()
    issue_type = models.CharField(max_length=50)