from django.contrib import admin
from AdminTestPapers.models import SiteUser, Question, QuestionPaper, MarksFromTheQuestion
# Register your models here.
admin.site.register(SiteUser)
admin.site.register(Question)
admin.site.register(QuestionPaper)
admin.site.register(MarksFromTheQuestion)