list_of_passwords = {3: 12,
                     4: 13,
                     5: 1423,
                     6: 121524,
                     7: 162534,
                     8: 13172635,
                     9: 1218273645,
                     10: 141923283746,
                     11: 11029384756,
                     12: 12131511124210394857,
                     13: 112211310495867,
                     14: 1611325212343114105968,
                     15: 1214114232133124115106978,
                     16: 1317115262143531341251161079,
                     17: 11621531441351261171089,
                     18: 12151811724272163631545414513612711810,
                     19: 118217316415514613712811910,
                     20: 13141911923282183731746416515614713812911}
first_field = int(input("Введите число от 3 до 20: "))
list_ = []
second_field = []
for i in range(1, first_field):
    list_.append(i)

for j in (list_):
    for k in (list_):
        if first_field % (j + k) == 0 and j < k:
           second_field.append(j)
           second_field.append(k)

password = ""
for i in second_field:
    password += str(i)
print(password)

if int(password) in list_of_passwords.values():
    print("Какая радость, Вас не насадило на пики, удачи в приключении! ")
else:
    print('Неправильный пароль, что ж, надеюсь у Вас есть вторая жизнь :) ')
