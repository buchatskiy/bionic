from django.db import models

class Group(models.Model):
    group_text=models.CharField(max_length=200)
    def __unicode__(self):
        return self.group_text

class Student (models.Model):
    student=models.ForeignKey(Group)
    student_text=models.CharField(max_length=200)
    def __unicode__(self):
        return self.student_text
