import smtplib
import getpass


EMAIL_ADDRESS = 'befordshir@gmail.com'
EMAIL_PASSWORD = getpass.getpass('Enter password: ')
"""dulviftmzkssindd"""
'''XSWbgt169'''           
print(1)

smtp = smtplib.SMTP('smtp-mail.outlook.com', 587)
"""smtp.ehlo()
smtp.starttls()
smtp.ehlo()"""
print(2)
status_code, response = smtp.ehlo()
print(f'[*] Echoing the server {status_code} {response}')

status_code, response = smtp.starttls()
print(f'[*] Starting TLS connection {status_code} {response}')

status_code, response = smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
print(f'[*] Logging in {status_code} {response}')



smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

msg = f'my email is {EMAIL_ADDRESS}'

smtp.sendmail(EMAIL_ADDRESS, 'befordshir@mail.ru', msg)

smtp.quit()