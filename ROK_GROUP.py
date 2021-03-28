rok_group = ["Гітарист", "Барабанщик", "Піаніст", "Вокаліст"]
suma_pay_members = 0
pay_members_per_month = 100
pay_members_per_year = pay_members_per_month * 12
for member in rok_group:
    print(member, end='  ')
    suma_pay_members += pay_members_per_year
suma_pay_members = str(suma_pay_members)
print('\n'+suma_pay_members)
