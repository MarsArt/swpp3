# from django import forms
# from django.contrib.auth import authenticate
# from django.shortcuts import get_object_or_404
# from .models import *
#
# class AskForm(forms.Form):
#     title=forms.CharField(max_length=100, label='Вопрос')
#     text=forms.CharField(widget=forms.Textarea, label='описание')
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if title.strip() == '':
#             raise forms.ValidationError('Title is empty', code='validation_error')
#         return title
#
#     def clean_text(self):
#         text = self.cleaned_data['text']
#         if text.strip() == '':
#             raise forms.ValidationError('Title is empty', code='validation_error')
#         return text
#
#     def save(self):
#         if self._user.is_anonymous():
#             self.cleaned_data['author_id'] = 1
#         else:
#             self.cleaned_data['author'] = self._user
#         ask = Question(**self.cleaned_data)
#         ask.save()
#         return ask
#
# class AnswerForm(forms.Form):
#     text = forms.CharField(widget=forms.Textarea, label='Введите ответ')
#     question = forms.IntegerField(widget=forms.HiddenInput)
#
#     def clean_text(self):
#         text = self.cleaned_data['text']
#         if text.strip() == '':
#             raise forms.ValidationError('Text is empty', code='validation_error')
#         return text
#     def clean_question(self):
#         question = self.cleaned_data['question']
#         if question == 0:
#             raise forms.ValidationError('incorrec question number', code='validation_error')
#         return  question
#
#     def save(self):
#         self.cleaned_data['question'] = get_object_or_404(
#             Question, pk=self.cleaned_data['question'])
#         if self._user.is_anonymous():
#             self.cleaned_data['author_id'] = 1
#         else:
#             self.cleaned_data['author'] = self._user
#         answer =Answer(**self.cleaned_data)
#         answer.save()
#         return answer
#
# class SignupForm(forms.Form):
#     username = forms.CharField(max_length=50, label='Логин')
#     email = forms.EmailField(label='email')
#     password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
#
#     def clean_username(self):
#         username=self.cleaned_data['username']
#         if username.strip() == '':
#             raise forms.ValidationError('username is empty', code='validation_error')
#         return username
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if email.strip() == '':
#             raise forms.ValidationError('email is empty', code='validation_error')
#         return email
#
#     def clean_password(self):
#         password = self.cleaned_data['password']
#         if password.strip() == '':
#             raise forms.ValidationError('password is empty', code='validation_error')
#         return password
#
#     def save(self):
#         user = User.objects.create_user(**self.cleaned_data)
#         user.save()
#         auth = authenticate(**self.cleaned_data)
#         return auth
#
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=50, label="Логин")
#     password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if username.strip == '':
#             raise forms.ValidationError('username is empty', code='validation_error')
#         return username
#
#     def clean_password(self):
#         password = self.cleaned_data['password']
#         if password.strip() == '':
#             raise forms.ValidationError('password is empty', code='validation_error')
#         return password
#
#     def save(self):
#         user = authenticate(** self.cleaned_data)
#         return  user
