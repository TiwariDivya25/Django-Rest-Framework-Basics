from rest_framework import serializers
from blogs.models import Blog, Comment
from students.models import Students
from employees.models import Employee

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True) 
    class Meta:
        model = Blog
        fields = '__all__'