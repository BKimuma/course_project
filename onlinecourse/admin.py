from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission, Course_Instructor, Submission_Choice

# Register your models here.
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text']

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title', 'course']
    search_fields = ['title', 'course']
    
    def lesson_number(self, obj):
        return obj.id
    
    lesson_number.short_description = 'Lesson Number'

class LearnerAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner, LearnerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission)
admin.site.register(Submission_Choice)
admin.site.register(Course_Instructor)
