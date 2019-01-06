from django.contrib import admin
from examapp.models import FirstQuestion
from examapp.models import SecondQuestion
from examapp.models import ThirdQuestion
from examapp.models import FourthQuestion
from examapp.models import FifthQuestion
class FirstQuestionAdmin(admin.ModelAdmin):
    list_display=['answer','marks','username']
admin.site.register(FirstQuestion,FirstQuestionAdmin)
class SecondQuestionAdmin(admin.ModelAdmin):
    list_display=['answer','marks','username']
admin.site.register(SecondQuestion,SecondQuestionAdmin)
class ThirdQuestionAdmin(admin.ModelAdmin):
    list_display=['answer','marks','username']
admin.site.register(ThirdQuestion,ThirdQuestionAdmin)
class FourthQuestionAdmin(admin.ModelAdmin):
    list_display=['answer','marks','username']
admin.site.register(FourthQuestion,FourthQuestionAdmin)
class FifthQuestionAdmin(admin.ModelAdmin):
    list_display=['answer','marks','username']
admin.site.register(FifthQuestion,FifthQuestionAdmin)

# Register your models here.
