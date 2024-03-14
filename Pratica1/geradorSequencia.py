import random

def gerar_sequencia(tamanho):
  sequencia = []
    
  # Gera uma quantidade ímpar de 'a'
  num_a = random.randint(1, tamanho)
  if num_a % 2 == 0:
    num_a += 1  
  for _ in range(num_a):
    sequencia.append('a')

  # Gera uma quantidade múltipla de 3 de 'b'
  num_b = random.randint(1, tamanho)
  if num_b % 3 != 0:
    num_b += 3 - (num_b % 3)
    
  for _ in range(num_b):
    sequencia.append('b')

  # Preenche o restante da sequência com 'a' ou 'b' aleatoriamente
  for _ in range(tamanho - num_a - num_b * 3):
    sequencia.append(random.choice(['a', 'b']))

  random.shuffle(sequencia)  # Embaralha a sequência
  return ''.join(sequencia)