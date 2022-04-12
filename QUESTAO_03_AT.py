salario = float(input("Renda mensal total: "))

moradia = float(input("Gastos totais com moradia: "))

educacao = float(input("Gastos totais com educação: "))

transporte = float(input("Gastos totais com transporte: "))

calcMoradia = 100 * moradia / salario
calcEducacao = 100 * educacao / salario
calcTransporte = 100 * transporte / salario

calcMoradiaIdeal = salario * 0.3
calcEducacaoIdeal = salario * 0.2
calcTransporteIdeal = salario * 0.15

print("Diagnostico: ")

if calcMoradia > 30:
    print(f"Seus gastos totais com moradia comprometem {calcMoradia} % de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {calcMoradiaIdeal}.")
else:
    print(f"Seus gastos de moradia estão dentro da margem recomendada.")


if calcEducacao > 20:
    print(f"Seus gastos totais com educação comprometem {calcEducacao} % de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R$ {calcEducacaoIdeal}.")
else:
    print(f"Seus gastos de educação estão dentro da margem recomendada.")


if calcTransporte > 15:
    print(f"Seus gastos totais com transporte comprometem {calcTransporte}% de sua renda total. O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$ {calcTransporteIdeal}.")
else:
    print(f"Seus gastos de transporte estão dentro da margem recomendada.")
