# importando as bibliotecas
from email.message import EmailMessage
import ssl
import smtplib
import mimetypes
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')

# Definindo os componentes do email
password = open('Senha App.txt', 'r').read() # Você precisa ter uma senha de app do gmail. Você pode passá-la diretamente
from_email = 'py.estudos.onbtcd@gmail.com'
to_email = 'py.estudos.onbtcd@gmail.com'
subject = f'IBOVESPA - {date} '
body = open('pscreen_email/index.html.txt', 'r', encoding='utf-8').read()

# Estruturando a mensagem via e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body, subtype='html')

safe = ssl.create_default_context()

# Adicionando Anexo
anex = f'pscreen_email/ibovespa_{date}.png'
mime_type, mime_subtype = mimetypes.guess_type(anex)[0].split('/')
with open(anex, 'rb') as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anex
    )

# Enviando o e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )
    print('E-mail enviado com sucesso!')