import smtplib

# Credenciais
remetente = "mayconwas2018@gmail.com"
senha = "linkedsouls51"

# Informações da mensagem
destinatario = "mayconwas2018@gmail.com"
assunto      = "Teste Python"
texto        = '''...'''

# Preparando a mensagem
msg = '\r\n'.join([
  'From: %s' % remetente,
  'To: %s' % destinatario,
  'Subject: %s' % assunto,
  '',
  '%s' % texto
  ])

# Enviando o email
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(remetente,senha)
server.sendmail(remetente, destinatario, msg)
server.quit()
