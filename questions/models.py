from django.db import models

from hashid_field import HashidAutoField
# Create your models here.


class Question(models.Model):
    id = HashidAutoField(primary_key=True)
    title = models.CharField(max_length=30)
    question = models.TextField()
    pub_date = models.DateTimeField()
    last_modified = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.title

class Answer(models.Model):
    id = HashidAutoField(primary_key=True)
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    code = models.TextField()#MDTextField()
    explanation = models.TextField()#MDTextField()
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return self.question.title + "-Answer"
