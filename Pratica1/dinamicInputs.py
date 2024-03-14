import pratica1

class UserTerminalInteration:
  def runStepByStep(values):
    input_string = input("Digite a entrada: ")
    current_state = values.initial_state
    for symbol in input_string:
        if symbol not in values.alphabet:
            print("Símbolo inválido:", symbol)
            return
          
        print("Estado atual:", current_state)
        print("Símbolo atual:", symbol)

        next_state = values.transitions[current_state].get(symbol)
        if next_state is None:
            print("Não há continuação para essa entrada [", symbol, "]")
            print("\nA entrada é NEGADA!")
            return

        current_state = next_state
        print("Próximo estado:", current_state)
        print("---------------------")
        input("Pressione Enter para continuar...")

        print("Estado final:", current_state)
        if current_state in values.final_states:
            print("\nA entrada é ACEITA!")
        else:
            print("\nA entrada é NEGADA!")
            
        return
      
  def runAutomato(values):
    input_string = input("Digite a entrada: ")
    current_state = values.initial_state
    for symbol in input_string:
        if symbol not in values.alphabet:
            print("Símbolo inválido:", symbol)
            return
        current_state = values.transitions[current_state].get(symbol)
        if current_state is None:
            print("Não há continuação para essa entrada [", symbol, "]")
            return
    if current_state in values.final_states:
        print("\nA entrada é ACEITA!")
        return
    else:
        print("\nA entrada é NEGADA!")
        return
      
  def testAutomatoWithDefaultValues(automato):
    inputsTrueEx1 = ['baba', 'bba', 'baaaaaaaba', 'baaaaba']
    inputsFalseEx1 = ['bbb', 'ababab', 'aabbaa', 'babab', 'baab']
    
    print('\nENTRADAS VÁLIDAS PADRÕES: ', inputsTrueEx1, '\n')

    for input_string in inputsTrueEx1:
      if automato.accept(input_string):
          print(f'A entrada "{input_string}" é aceita pelo autômato.')
      else:
          print(f'A entrada "{input_string}" não é aceita pelo autômato.')

    print('\nENTRADAS INVÁLIDAS PADRÕES: ', inputsFalseEx1, '\n')
    for input_string in inputsFalseEx1:
        if not automato.accept(input_string):
            print(f'A entrada "{input_string}" não é aceita pelo autômato.')
        else:
            print(f'A entrada "{input_string}" é aceita pelo autômato.')
    
  
def main():
  print("Escolha o autômato que deseja testar:")
  print("1 - Ex 1")
  # print("2 - Ex 2")
  # print("3 - Ex 3")
  # print("4 - Ex 4")
  # print("5 - Ex 5")
  # print("6 - Ex 6")
  # print("7 - Ex 7")
  option = int(input("\nDigite o número da opção: "))
  
  if option == 1:
    ex1 = EX1()
    print("Escolha o modo de teste:")
    print("1 - Passo a passo")
    print("2 - Automático")
    print("3 - Testar com valores padrões")
    mode = int(input("\nDigite o número da opção: "))
    if mode == 1:
      UserTerminalInteration.runStepByStep(ex1)
    elif mode == 2:
      UserTerminalInteration.runAutomato(ex1)
    elif mode == 3:
      UserTerminalInteration.testAutomatoWithDefaultValues(ex1)
    else:
      print("Opção inválida!")
  else:
    print("Opção inválida!")
    
main()