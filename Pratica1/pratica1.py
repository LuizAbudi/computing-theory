# Autor: Luiz Gustavo Pasini Abudi - 2020703
# Matéria: Teoria da Computação
# Professor: Rogerio Aparecido Gonçalves
# Instituição: UTFPR-CM - Universidade Tecnológica Federal do Paraná - Câmpus Campo Mourão
# Curso: Ciências da Computação
# Data: 14/03/2024
# Descrição: Prática 1 - AFD
# Serão feitos autômatos finitos determinísticos (AFD) para as seguintes linguagens:
  # Ex 1 - AFD 𝐴 = {𝑏𝑎^n𝑏𝑎 ∣ 𝑛 ≥ 0}
  # Ex 2 - AFD 𝐴 = {𝑥 ∈ {𝑎, 𝑏}* ∣ |𝑥| mod 3 = 0}
  # Ex 3 - AFD 𝐴 = {𝑤 ∈ {𝑎, 𝑏}* ∣ (|𝑤|𝑎 + |𝑤|𝑏) mod 2 = 0}
  # Ex 4 - AFD 𝐴 = {𝑎^𝑚 𝑏^𝑛 ∣ 𝑚, 𝑛 ≥ 0 ∧ (𝑚 + 𝑛) mod 2 = 0}
  # Para o ex 5 e 6 Σ = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
    # 5. AFD 𝐴 = {𝑥 ∈ Σ* ∣ 𝑥 mod 2 = 0} 
    # 6. AFD 𝐴 = {𝑥 ∈ Σ* ∣ 𝑥 mod 5 = 0}
  # Ex 7 - Obter um autômato finito que reconheça a linguagem L = {w ∈ {a, b}* | w contém uma quantidade ímpar de símbolos a e uma quantidade múltipla de 3 de símbolos b}.
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class EX1:
  def __init__(self):
    self.states = ['q0', 'q1', 'q2', 'q3']
    self.alphabet = ['a', 'b']
    self.initial_state = 'q0'
    self.final_states = ['q3']
    self.transitions = {
      'q0': {'b': 'q1'},
      'q1': {'a': 'q1', 'b': 'q2'},
      'q2': {'a': 'q3'}      
    }

  def accept(self, input_string):
    current_state = self.initial_state
    for symbol in input_string:
      if symbol not in self.alphabet:
        return False
      if current_state == self.final_states and symbol != 'a':
        return False
      current_state = self.transitions[current_state].get(symbol)
      if current_state is None:
        False
    return current_state in self.final_states
  
class EX2:
  def __init__(self):
    self.states = ['q0', 'q1', 'q2']
    self.alphabet = ['','a', 'b']
    self.initial_state = 'q0'
    self.final_states = ['q0']
    self.transitions = {
      'q0': {' ': 'q0'},
      'q0': {'a': 'q1', 'b': 'q1'},
      'q1': {'a': 'q2', 'b': 'q2'},
      'q2': {'a': 'q0', 'b': 'q0'}
    }
    
  def accept(self, input_string):
    current_state = self.initial_state
    for symbol in input_string:
      if symbol not in self.alphabet:
        return False
      current_state = self.transitions[current_state].get(symbol)
      if current_state is None:
        return False
    return current_state in self.final_states
  
class EX3:
  def __init__(self):
    self.states = ['q0', 'q1', 'q2', 'q3']
    self.alphabet = ['', 'a', 'b']
    self.initial_state = 'q0'
    self.final_states = ['q0', 'q3']
    self.transitions = {
      'q0': {'a': 'q1', 'b': 'q2'},
      'q1': {'a': 'q0', 'b': 'q3'},
      'q2': {'a': 'q3', 'b': 'q0'},
      'q3': {'a': 'q1', 'b': 'q2'}
    }
    
  def accept(self, input_string):
    current_state = self.initial_state
    for symbol in input_string:
      if symbol not in self.alphabet:
        return False
      current_state = self.transitions[current_state].get(symbol)
      if current_state is None:
        return False
    return current_state in self.final_states
  
class EX4:
  def __init__(self):
    self.states = ['q0', 'q1', 'q2', 'q3']
    self.alphabet = ['', 'a', 'b']
    self.initial_state = 'q0'
    self.final_states = ['q0', 'q3']
    self.transitions = {
      'q0': {'a': 'q1', 'b': 'q2'},
      'q1': {'a': 'q0', 'b': 'q3'},
      'q2': {'b': 'q3'},
      'q3': {'b': 'q2'}
    }
    
  def accept(self, input_string):
    current_state = self.initial_state
    for symbol in input_string:
      if symbol not in self.alphabet:
        return False
      current_state = self.transitions[current_state].get(symbol)
      if current_state is None:
        return False
    return current_state in self.final_states
  
class EX5:
  def __init__(self):
    self.states = ['q0', 'q1', 'q2']
    self.alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    self.initial_state = 'q0'
    self.final_states = ['q1']
    self.transitions = {
      'q0': {'0': 'q1', '1': 'q2', '2': 'q1', '3': 'q2', '4': 'q1', '5': 'q2', '6': 'q1', '7': 'q2', '8': 'q1', '9': 'q2'},
      'q1': {'0': 'q1', '1': 'q2', '2': 'q1', '3': 'q2', '4': 'q1', '5': 'q2', '6': 'q1', '7': 'q2', '8': 'q1', '9': 'q2'},
      'q2': {'0': 'q1', '1': 'q2', '2': 'q1', '3': 'q2', '4': 'q1', '5': 'q2', '6': 'q1', '7': 'q2', '8': 'q1', '9': 'q2'}
    }
    
  def accept(self, input_string):
    current_state = self.initial_state
    for symbol in input_string:
      if symbol not in self.alphabet:
        return False
      current_state = self.transitions[current_state].get(symbol)
      if current_state is None:
        return False
    return current_state in self.final_states
  
class EX6:
  def __init__(self):
    self.states = ['q0', 'q1', 'q2']
    self.alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    self.initial_state = 'q0'
    self.final_states = ['q1']
    self.transitions = {
      'q0': {'0': 'q1', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q1', '6': 'q2', '7': 'q2', '8': 'q2', '9': 'q2'},
      'q1': {'0': 'q1', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q1', '6': 'q2', '7': 'q2', '8': 'q2', '9': 'q2'},
      'q2': {'0': 'q1', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q1', '6': 'q2', '7': 'q2', '8': 'q2', '9': 'q2'}
    }
    
  def accept(self, input_string):
    current_state = self.initial_state
    for symbol in input_string:
      if symbol not in self.alphabet:
        return False
      current_state = self.transitions[current_state].get(symbol)
      if current_state is None:
        return False
    return current_state in self.final_states

# class EX7:
#   def __init__(self):
#     self.states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
#     self.alphabet = ['', 'a', 'b']
#     self.initial_state = 'q0'
#     self.final_states = ['q0', 'q1', 'q5', 'q8', 'q9']
#     self.transitions = {
#       'q0': {'a': 'q1', 'b': 'q2'},
#       'q1': {'a': 'q3', 'b': 'q6'},
#       'q2': {'a': 'q4', 'b': 'q0'},
#       'q3': {'a': 'q1', 'b': 'q4'},
#       'q4': {'a': 'q9', 'b': 'q5'},
#       'q5': {'a': 'q7', 'b': 'q3'},
#       'q6': {'a': 'q4', 'b': 'q8'},
#       'q7': {'a': 'q9', 'b': 'q5'},
#       'q8': {'a': 'q6', 'b': 'q10'},
#       'q9': {'a': 'q10', 'b': 'q7'},
#       'q10': {'a': 'q10', 'b': 'q10'}      
#     }
  


def main():
  inputsTrueEx2 = ['', 'aaa', 'bbb', 'ababab', 'bababa', 'ababababb', 'babababaa', 'abb', 'bba']
  inputsFalseEx2 = ['a', 'b', 'ab', 'ba', 'abab', 'baba', 'abababab', 'babababa', 'ababababab', 'bababababa']
  inputsTrueEx3 = ["aa", "bb", "abab", "baba", "aabb", "bbaa", "ab", "ba", "abba", "ababab", "baba", "abababab", "babbabab", "aabbaabbaabb", "baabbaabbaab", "ababbaababba"]
  inputsFalseEx3 = ['aabbababababb', 'baababbaababb', 'abbabbabbabba', 'a', 'aba', 'bab', 'abaaabb']

  ex2 = EX2()
  print('EXERCÍCIO 2')
  print('\nENTRADAS VÁLIDAS PADRÕES: ', inputsTrueEx2, '\n')
  for input_string in inputsTrueEx2:
    if ex2.accept(input_string):
      print(f'ENTRADA: "{input_string}" ACEITA.')
    else:
      print(f'ENTRADA: "{input_string}" NEGADA.')
        
  print('\nENTRADAS INVÁLIDAS PADRÕES: ', inputsFalseEx2, '\n')
  for input_string in inputsFalseEx2:
      if not ex2.accept(input_string):
        print(f'ENTRADA: "{input_string}" NEGADA.')
      else:
        print(f'ENTRADA: "{input_string}" ACEITA.')
        
  input("Press Enter to continue...")
  clear()
  
  ex3 = EX3()
  print('EXERCÍCIO 3')
  print('\nENTRADAS VÁLIDAS PADRÕES: ', inputsTrueEx3, '\n')
  for input_string in inputsTrueEx3:
    if ex3.accept(input_string):
      print(f'ENTRADA: "{input_string}" ACEITA.')
    else:
      print(f'ENTRADA: "{input_string}" NEGADA.')
  
  print('\nENTRADAS INVÁLIDAS PADRÕES: ', inputsFalseEx3, '\n')
  for input_string in inputsFalseEx3:
      if not ex3.accept(input_string):
        print(f'ENTRADA: "{input_string}" NEGADA.')
      else:
        print(f'ENTRADA: "{input_string}" ACEITA.')
  
  input("Press Enter to continue...")
  clear()

  
  

main()