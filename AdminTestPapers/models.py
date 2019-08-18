from django.db import models
from django.contrib.auth.models import User

# A User Model (Teachers And Students)
class SiteUser(models.Model):
  user_type_choices = [
    ("T","Teacher"),
    ("S","Student"),
  ]
  user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
  user_type = models.CharField(max_length = 1, choices = user_type_choices,default = "S",blank = False)
  def __str__(self):
    return '%s %s' % (self.user.username, self.user_type)

# Question Paper Model
class QuestionPaper(models.Model):
  teacher = models.ForeignKey(SiteUser, on_delete = models.CASCADE,default = None)
  pub_date = models.DateTimeField('date published')
  title_text = models.CharField(max_length = 100)
  def __str__(self):
    return 'Test : %s By: %s' % (self.title_text, self.teacher.user.username)

  # question = models.ManyToManyField(Question)

# Question Model
class Question(models.Model):
  # teacher = models.ForeignKey(SiteUser, on_delete = models.CASCADE,default = None)
  q_paper = models.ForeignKey(QuestionPaper, on_delete=models.CASCADE)
  created_at = models.DateTimeField('date published')
  question_text = models.CharField(max_length = 300)
  op1_text = models.CharField(max_length=100)
  op2_text = models.CharField(max_length = 100)
  op3_text = models.CharField(max_length = 100)
  op4_text = models.CharField(max_length = 100)
  ans_text = models.CharField(max_length = 100)

# Model Handeling Marks Score By A Particular Student In A Particular Question (In A Particular Test)
class MarksFromTheQuestion(models.Model):
  question = models.ForeignKey(Question, on_delete = models.CASCADE)
  test = models.ForeignKey(QuestionPaper, on_delete = models.CASCADE)
  student = models.ForeignKey(SiteUser, on_delete = models.CASCADE, default = None)
  correct = models.BooleanField(default = False)
