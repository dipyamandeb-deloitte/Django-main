from django.db import models

# Create your models here.



class Project(models.Model):
    project_id = models.BigAutoField(primary_key=True)
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    created_by = models.CharField(max_length=50)
    def __str__(self) :

        return "%s %s % s %s" %(self.project_id,self.project_title, self.project_description,self.created_by)


class Issues(models.Model):
    issue_id = models.BigAutoField(primary_key=True)
    issue_title = models.CharField(max_length=200)
    issue_description = models.TextField()
    issue_type = models.CharField(max_length=50, default="pending", choices=

                                  (('Bug','Bug'),

                                  ('Task','Task'),

                                  ('Story', 'Story'),

                                  ('Epic','Epic'),
  
                                  ))
    project= models.ForeignKey(Project, on_delete=models.CASCADE)


    
class Assigned(models.Model):
    assigned_id = models.BigAutoField(primary_key=True)
    assigned_title = models.CharField(max_length=200)
    assigned_band= models.CharField(max_length=50, default="pending", choices=

                                  (('B6','B6'),
                                  ('B5L','B5L'),
                                  ('B7', 'B7'),
                                  ('B5','B5'),
                                  ('B4','B4'),
  
                                  ))
    Issues= models.ForeignKey(Issues, on_delete=models.CASCADE)


class Comments(models.Model):
    author= models.CharField(primary_key=True, default="pending",max_length=50)
    text= models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now_add=True)
    Issue1= models.ForeignKey(Issues, on_delete=models.CASCADE)
    



