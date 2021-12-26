import secrets
import string

number = int(input('Введите кол-во символов в пароле: '))


alphabet_1 = string.digits
password_1 = ''.join(secrets.choice(alphabet_1) for i in range(number))  


alphabet_2 = string.ascii_letters
password_2 = ''.join(secrets.choice(alphabet_2) for i in range(number))  


print(f'Пароль только из цифр: {password_1}')
print(f'Пароль только из букв: {password_2}')


input()