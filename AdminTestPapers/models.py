from django.db import models
from django.contrib.auth.models import User

# Teacher Or TestMaker's Model
class TeacherUser(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)

# Student's Model
class StudentUser(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)

# Question Model
class Question(models.Model):
  teacher = models.ForeignKey(TeacherUser, on_delete = models.CASCADE,default = None)
  question_text = models.CharField(max_length = 300)
  op1_text = models.CharField(max_length = 100)
  op2_text = models.CharField(max_length = 100)
  op3_text = models.CharField(max_length = 100)
  op4_text = models.CharField(max_length = 100)
  ans_text = models.CharField(max_length = 100)
  
# Question Paper Model
class QuestionPaper(models.Model):
  teacher = models.ForeignKey(TeacherUser, on_delete = models.CASCADE,default = None)
  pub_date = models.DateTimeField('date published') 
  title_text = models.CharField(max_length = 100)
  question = models.ManyToManyField(Question)

# Model Handeling Marks Score By A Particular Student In A Particular Question (In A Particular Test)
class MarksFromTheQuestion(models.Model):
  question = models.ForeignKey(Question, on_delete = models.CASCADE)
  test = models.ForeignKey(QuestionPaper, on_delete = models.CASCADE)
  student = models.ForeignKey(StudentUser, on_delete = models.CASCADE, default = None)
  correct = models.BooleanField(default = 0)









