# (Jogo da Forca)
 
import random
 
tabuleiro = ['''
>>>>>>>>>>Jogo da Forca<<<<<<<<<<
 
+---+
|   |
    |
    |
    |
    |
=========''', '''
 
+---+
|   |
O   |
    |
    |
    |
=========''', '''
 
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 
 +---+
 |   |
 O   |
/|   |
    |
    |
=========''', '''
 
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
''']
 
 
class JogoForca:
 
   def __init__(self, palavra):
       self.palavra = palavra
       self.letra_errada = []
       self.letra_certa = []
 
   # Método para advinhar a letra
   def achou(self, letra):
       if letra in self.palavra and letra not in self.letra_certa:
           self.letra_certa.append(letra)
       elif letra not in self.palavra and letra not in self.letra_errada:
           self.letra_errada.append(letra)
       else:
           return False
       return True
 
   # Método para verificar se o jogo terminou
   def forca_over(self):
       # Jogo acaba quando o jogador ganhar ou a letra errada for igual a 6
       return self.winner() or (len(self.letra_errada) == 6)
 
   # Método para verificar se o jogador venceu
   def winner(self):
       if '_' not in self.oculta_palavra():
           return True
       return False
 
   # Método para ocultar a linha no jogo
   def oculta_palavra(self):
       rtn = ''
       for letter in self.palavra:
           if letter not in self.letra_certa:
               rtn += '_'
           else:
               rtn += letter
       return rtn
 
   # Método para checar o status do game e imprimir o jogo na tela
   def print_game_status(self):
       print(tabuleiro[len(self.letra_errada)])
       print('\nPalavra: ' + self.oculta_palavra())
       print('\nLetras erradas: ',)
       for letra in self.letra_errada:
           print(letra,)
       print()
       print('Letras corretas: ',)
       for letra in self.letra_certa:
           print(letra,)
       print()
 
# Método para ler uma palavra de forma aleatória do banco de palavras
 
 
def palavra_aleatoria():
   with open("palavras.txt", "rt") as f:
       banco_palavras = f.readlines()
   return banco_palavras[random.randint(0, len(banco_palavras))].strip()
 
# Método Main - Exucução do Jogo
 
 
def main():
 
   # objeto
   game = JogoForca(palavra_aleatoria())
 
   # Enquanto o jogo não tiver terminado, solicita uma letra e faz a leitura do caracter
   while not game.forca_over():
       game.print_game_status()
       chute = input('\nDigite uma letra: ')
       game.achou(chute)
 
   # Verifica o status do jogo
   game.print_game_status()
 
   # De acordo com o status, imprime mensagem na tela para o usuário
   if game.winner():
       print('\nParabéns! Você venceu!!!')
   else:
       print('\nGame over! Você perdeu.')
       print(f'A palavra era {game.palavra}')
       print("""
                   ███████████████████████████
                   ███████▀▀▀░░░░░░░▀▀▀███████
                   ████▀░░░░░░░░░░░░░░░░░▀████
                   ███│░░░░░░░░░░░░░░░░░░░│███
                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██
                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
                   ██▌░│██████▌░░░▐██████│░▐██
                   ███░│▐███▀▀░░▄░░▀▀███▌│░███
                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
                   ████▄─┘██▌░░░░░░░▐██└─▄████
                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
                   ███████▄░░░░░░░░░░░▄███████
                   ██████████▄▄▄▄▄▄▄██████████
                   ███████████████████████████
 
       """)
 
 
# Exucuta o programa
if __name__ == "__main__":
   main()
