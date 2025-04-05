import smtplib
import getpass


EMAIL_ADDRESS = 'sunbaking@yandex.ru'
EMAIL_PASSWORD = getpass.getpass('Enter password: ')
"""dulviftmzkssindd"""           
print(1)

smtp = smtplib.SMTP('smtp.yandex.ru', 587)
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

smtp.sendmail(EMAIL_ADDRESS, 'befordshir@gmail.com', msg)

smtp.quit()