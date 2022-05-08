from django.contrib import admin

admin.site.site_header = "Lighthub Admin Dashboard"
admin.site.site_title = "Lighthub Admin"
admin.site.index_title = "Welcome to Lighthub Manager"
# Register your models here.

from .models import Survey, Question, Technology

# admin.site.register(Survey)
# admin.site.register(Question)
# admin.site.register(Technology)

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class SurveyAdmin(admin.ModelAdmin):
    fieldsets = [('title', {'fields' : ['title']}), ('Number Of Submissions', {'fields' : ['numberOfSubmissions'], 'classes': ['collapse']}) ]
    inlines = [QuestionInline]

admin.site.register(Survey, SurveyAdmin)