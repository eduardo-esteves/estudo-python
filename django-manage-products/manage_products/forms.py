from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=200)
    email = forms.EmailField(label='E-mail', max_length=200)
    subject = forms.CharField(label='Assunto', max_length=200)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        msg_content = f'Nome: {name}\n E-mail: {email}\n Assunto:{subject}\n Mensagem: {message}'
        mail = EmailMessage(
            subject=f'Olá {name} Recebemos seu email',
            body=msg_content,
            from_email='contato@dominio.com.br',
            to=['contato@dominio.com.br',],
            headers={
                'Reply-To': email,
            }
        )

        mail.send()
