from django.contrib import admin
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    # Define how the admin interface should display the fields
    list_display = ['question_text', 'question_image']

class AnswerAdmin(admin.ModelAdmin):
    # Define how the admin interface should display the fields
    list_display = ['question', 'answer_text', 'answer_image']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)