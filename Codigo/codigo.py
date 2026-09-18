def funcao(n):
  if n == 0 or n == 1:
    return 1
  return n * funcao(n - 1)


valor = int(input("\nInforme um valor: "))

print(f"\n{funcao(valor)}\n")
