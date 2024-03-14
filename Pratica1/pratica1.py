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
# 5. AFD 𝐴 = {𝑥 ∈ Σ* ∣ 𝑥 mod 2 =
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
        self.states = ['q0', 'q1', 'q2', 'q3', 'Trap']
        self.alphabet = ['a', 'b']
        self.initial_state = 'q0'
        self.final_states = ['q3']
        self.transitions = {
            'q0': {'a': 'Trap', 'b': 'q1'},
            'q1': {'a': 'q1', 'b': 'q2'},
            'q2': {'a': 'q3', 'b': 'Trap'},
            'q3': {'a': 'Trap', 'b': 'Trap'},
            'Trap': {'a': 'Trap', 'b': 'Trap'}
        }

    def accept(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            if current_state == self.final_states:
                return False
            current_state = self.transitions[current_state].get(symbol)
            if current_state is None:
                False
        return current_state in self.final_states


class EX2:
    def __init__(self):
        self.states = ['q0', 'q1', 'q2']
        self.alphabet = ['', 'a', 'b']
        self.initial_state = 'q0'
        self.final_states = ['q0']
        self.transitions = {
            'q0': {'': 'q0'},
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


class EX7:
    def __init__(self):
        self.states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']
        self.alphabet = ['a', 'b']
        self.initial_state = 'q0'
        self.final_states = ['q1', 'q2', 'q4']
        self.transitions = {
            'q0': {'a': 'q1', 'b': 'q2'},
            'q1': {'a': 'q0', 'b': 'q3'},
            'q2': {'a': 'q3', 'b': 'q4'},
            'q3': {'a': 'q2', 'b': 'q5'},
            'q4': {'a': 'q5', 'b': 'q0'},
            'q5': {'a': 'q4', 'b': 'q1'},
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


def main():
    inputsTrueEx1 = ['bba', 'baba', 'baaba', 'baaaba', 'baaaaaaaaaba']
    inputsFalseEx1 = ['b', 'ba', 'baa', 'baaa']
    inputsTrueEx2 = ['', 'aaa', 'bbb', 'ababab',
                     'bababa', 'ababababb', 'babababaa', 'abb', 'bba']
    inputsFalseEx2 = ['a', 'b', 'ab', 'ba', 'abab', 'baba',
                      'abababab', 'babababa', 'ababababab', 'bababababa']
    inputsTrueEx3 = ["aa", "bb", "abab", "baba", "aabb", "bbaa", "ab", "ba", "abba", "ababab",
                     "baba", "abababab", "babbabab", "aabbaabbaabb", "baabbaabbaab", "ababbaababba"]
    inputsFalseEx3 = ['aabbababababb', 'baababbaababb',
                      'abbabbabbabba', 'a', 'aba', 'bab', 'abaaabb']
    inputsTrueEx4 = ['ab', 'aa', 'aaabbb', 'abbbbb',
                     'aaabbb', 'bb', 'bbbb', 'aaaabb']
    inputsFalseEx4 = ['a', 'b', 'abba', 'baba',
                      'ababab', 'bababa', 'ababababab', 'bababababa']
    inputsTrueEx5 = ['0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32', '34', '36', '38', '40', '42', '44', '46',
                     '48', '50', '52', '54', '56', '58', '60', '62', '64', '66', '68', '70', '72', '74', '76', '78', '80', '82', '84', '86', '88', '90', '92', '94', '96', '98']
    inputsFalseEx5 = ['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29', '31', '33', '35', '37', '39', '41', '43', '45', '47',
                      '49', '51', '53', '55', '57', '59', '61', '63', '65', '67', '69', '71', '73', '75', '77', '79', '81', '83', '85', '87', '89', '91', '93', '95', '97', '99']
    inputsTrueEx6 = ['0', '5', '10', '15', '20', '25', '30', '35', '40',
                     '45', '50', '55', '60', '65', '70', '75', '80', '85', '90', '95']
    inputsFalseEx6 = ['1', '2', '3', '4', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17', '18', '19', '21', '22', '23', '24', '26', '27', '28', '29', '31', '32', '33', '34', '36', '37', '38', '39', '41', '42', '43', '44', '46', '47', '48',
                      '49', '51', '52', '53', '54', '56', '57', '58', '59', '61', '62', '63', '64', '66', '67', '68', '69', '71', '72', '73', '74', '76', '77', '78', '79', '81', '82', '83', '84', '86', '87', '88', '89', '91', '92', '93', '94', '96', '97', '98', '99']
    inputsTrueEx7 = ['baabbbbaaab', 'babbbbbbbbbbb', 'abaaaabbaabbaab', 'bbbbbabbbb', 'abbbaabbabaaaabbbbabb', 'bbabaabbbabbbbbaabaaa',
                     'abaabbaaaa', 'bbabaababbbaaabb', 'baababaaaa', 'bababbbbbbbbbba', 'bbaabbabb', 'bbbaaabbbaa', 'aaaaabbb', 'abbbbbbbbbaa', 'a']
    inputsFalseEx7 = ['', 'bbb', 'bababaaaa',
                      'babababaa', 'abb', 'bba', 'aaabbbaaabbbaa']

    ex1 = EX1()
    print('EXERCÍCIO 1')
    print('\nENTRADAS VÁLIDAS PADRÕES: ', inputsTrueEx1, '\n')
    for input_string in inputsTrueEx1:
        if ex1.accept(input_string):
            print(f'ENTRADA: "{input_string}" ACEITA.')
        else:
            print(f'ENTRADA: "{input_string}" NEGADA.')

    print('\nENTRADAS INVÁLIDAS PADRÕES: ', inputsFalseEx1, '\n')
    for input_string in inputsFalseEx1:
        if not ex1.accept(input_string):
            print(f'ENTRADA: "{input_string}" NEGADA.')
        else:
            print(f'ENTRADA: "{input_string}" ACEITA.')

    input("Press Enter to continue...")
    clear()

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

    ex4 = EX4()
    print('EXERCÍCIO 4')
    print('\nENTRADAS VÁLIDAS PADRÕES: ', inputsTrueEx4, '\n')
    for input_string in inputsTrueEx4:
        if ex4.accept(input_string):
            print(f'ENTRADA: "{input_string}" ACEITA.')
        else:
            print(f'ENTRADA: "{input_string}" NEGADA.')

    print('\nENTRADAS INVÁLIDAS PADRÕES: ', inputsFalseEx4, '\n')
    for input_string in inputsFalseEx4:
        if not ex4.accept(input_string):
            print(f'ENTRADA: "{input_string}" NEGADA.')
        else:
            print(f'ENTRADA: "{input_string}" ACEITA.')

    input("Press Enter to continue...")
    clear()

    ex5 = EX5()
    print('EXERCÍCIO 5')
    print('\nENTRADAS VÁLIDAS PADRÕES: ', inputsTrueEx5, '\n')
    for input_string in inputsTrueEx5:
        if ex5.accept(input_string):
            print(f'ENTRADA: "{input_string}" ACEITA.')
        else:
            print(f'ENTRADA: "{input_string}" NEGADA.')

    print('\nENTRADAS INVÁLIDAS PADRÕES: ', inputsFalseEx5, '\n')
    for input_string in inputsFalseEx5:
        if not ex5.accept(input_string):
            print(f'ENTRADA: "{input_string}" NEGADA.')
        else:
            print(f'ENTRADA: "{input_string}" ACEITA.')

    input("Press Enter to continue...")
    clear()

    ex6 = EX6()
    print('EXERCÍCIO 6')
    print('\nENTRADAS VÁLIDAS PADRÕES: ', inputsTrueEx6, '\n')
    for input_string in inputsTrueEx6:
        if ex6.accept(input_string):
            print(f'ENTRADA: "{input_string}" ACEITA.')
        else:
            print(f'ENTRADA: "{input_string}" NEGADA.')

    print('\nENTRADAS INVÁLIDAS PADRÕES: ', inputsFalseEx6, '\n')
    for input_string in inputsFalseEx6:
        if not ex3.accept(input_string):
            print(f'ENTRADA: "{input_string}" NEGADA.')
        else:
            print(f'ENTRADA: "{input_string}" ACEITA.')

    input("Press Enter to continue...")
    clear()

    ex7 = EX7()
    print('EXERCÍCIO 7')
    print('\nENTRADAS VÁLIDAS PADRÕES: ', inputsTrueEx7, '\n')
    for input_string in inputsTrueEx7:
        if ex7.accept(input_string):
            print(f'ENTRADA: "{input_string}" ACEITA.')
        else:
            print(f'ENTRADA: "{input_string}" NEGADA.')

    print('\nENTRADAS INVÁLIDAS PADRÕES: ', inputsFalseEx7, '\n')
    for input_string in inputsFalseEx7:
        if not ex7.accept(input_string):
            print(f'ENTRADA: "{input_string}" NEGADA.')
        else:
            print(f'ENTRADA: "{input_string}" ACEITA.')

    input("Press Enter to continue...")
    clear()


main()
