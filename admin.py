from django.contrib import admin
from .models import Instructor, Program, HomePageMessage, QuestionAnswer
# Register your models here.

admin.site.register(Instructor)
admin.site.register(Program)
admin.site.register(HomePageMessage)
admin.site.register(QuestionAnswer)