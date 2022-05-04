from tkinter.tix import Tree
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

CATEGORY_ONE = '1'
CATEGORY_TWO = '2'
CATEGORY_THREE = '3'

CATEGORY_CHOICES = [
    (CATEGORY_ONE, '일반'),
    (CATEGORY_TWO, '계정'),
    (CATEGORY_THREE, '기타'),
]


class Faq(models.Model):
    title = models.CharField(verbose_name='질문 제목', max_length=80, default="")
    content = models.TextField(verbose_name='질문 내용')
    category = models.CharField(
        choices=CATEGORY_CHOICES, verbose_name='카테고리', max_length=2, default=CATEGORY_THREE)
    created_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='faq_created_by')
    updated_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='faq_updated_by', null=True)
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='최종수정일시', auto_now=True)


class Inquiry(models.Model):

    STATUS_ONE = '1'
    STATUS_TWO = '2'
    STATUS_THREE = '3'

    STATUS_CHOICES = [
        (STATUS_ONE, '문의 등록'),
        (STATUS_ONE, '접수 완료'),
        (STATUS_ONE, '답변 완료'),
    ]
    status = models.CharField(
        verbose_name='상태', max_length=2, choices=STATUS_CHOICES, default=STATUS_ONE)
    category = models.CharField(
        verbose_name='카테고리', max_length=2, choices=CATEGORY_CHOICES, default=CATEGORY_THREE)
    title = models.CharField(verbose_name='질문 제목', max_length=80)
    email = models.EmailField(verbose_name='이메일', blank=Tree)  # 체크박스로 수신유무결정
    is_email = models.BooleanField(verbose_name="이메일 수신 여부", default=False)
    phone = models.CharField(
        verbose_name='문자메세지', max_length=12, blank=True)  # 체크박스로 수신유무결정
    is_phone = models.BooleanField(verbose_name="문자메세지 수신여부", default=False)
    content = models.TextField(verbose_name="문의 내용")
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)

    created_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='inquiry_created_by')
    updated_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='inquiry_updated_by')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='최종수정일시', auto_now=True)


class Answer(models.Model):
    inquiry = models.ForeignKey(to="Inquiry", on_delete=models.CASCADE)
    content = models.TextField(verbose_name='답변내용')

    created_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='answer_created_by')
    updated_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='answer_updated_by')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='최종수정일시', auto_now=True)
