from re import T
from django.contrib import admin
from .models import Inquiry, Answer, Faq
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'updated_by')
    list_filter = ('category',)
    search_fields = ('title',)


class AnswerInline(admin.TabularInline):
    model = Answer
    verbose_name = '답변'
    verbose_name_plural = '답변들'



@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):

    actions = ['answer_complete_alert']
    
    @admin.action(description='답변완료 안내발송')
    def answer_complete_alert(self, request, queryset):
        is_phone = Inquiry.objects.get(is_phone=True)
        is_email = Inquiry.objects.get(is_email=True)

        if is_phone and is_email:
            print(is_phone)
            print(is_email)



    list_display = ('title', 'category', 'created_at', 'created_by')
    list_filter = ('category',)
    search_fields = ('title', 'email', 'phone', )
    inlines = [AnswerInline]
