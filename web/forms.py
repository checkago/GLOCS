from django import forms

from web.models import Feedback


class FeedbackForm(forms.ModelForm):
    comment = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'rows': '2'})
    )
    email = forms.EmailField(required=False, widget=forms.EmailInput)
    # captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Имя'
        self.fields['phone'].label = 'Номер телефона'
        self.fields['email'].label = 'E-mail'
        self.fields['comment'].label = 'Коментарий'
        self.fields['agreement'].label = 'Согласие'

    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['com', 'net', 'org', 'xyz', 'de', 'fr', 'ua', 'nl', 'cz', 'group', 'biz', 'dk']:
            raise forms.ValidationError(f'Использование почтового ящика в домене .{domain} заблокированно')
        return email

    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'email', 'comment', 'agreement')