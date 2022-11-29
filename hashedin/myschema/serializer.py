from rest_framework import serializers
from .models import Project,Issues,Assigned,Comments
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    project_id= serializers.ReadOnlyField()
    class Meta:
        model= Project
        fields= '__all__'


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    issue_id= serializers.ReadOnlyField()
    class Meta:
        model= Issues
        fields= '__all__'

class AssignedSerializer(serializers.HyperlinkedModelSerializer):
    assigned_id= serializers.ReadOnlyField()
    class Meta:
        mdoel = Assigned
        fields= '__all__'

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author= serializers.ReadOnlyField()
    class Meta:
        model= Comments
        fields= '__all__'
    