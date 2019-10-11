from django import forms
from django.core.mail import send_mail


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        if self.is_valid():
            assunto = 'Contato'
            mensagem = self.cleaned_data['mensagem']
            email = self.cleaned_data['email']

            send_mail(
                assunto, mensagem, email, ['weslleyborgesdev@gmail.com']
            )

