hourpayment =  float(input())
monthlyworkedhour = int(input())
salarywithoutstolen = hourpayment*monthlyworkedhour
salary = str(salarywithoutstolen)
print("Seu salário bruto é de: "+salary+".")
inssstolen = str(salary*.08)
print("O roubo do INSS foi de: "+inssstolen+".")
sindicatestolen = str(salary*0.05)
print("O roubo do sindicato foi de: "+sindicatestolen+".")
governamentstolen = salary*0.11
print("O roubo do imposto de renda foi de: "+governamentstolen+".")
