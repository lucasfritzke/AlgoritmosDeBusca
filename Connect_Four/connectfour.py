# -*- coding: utf-8 -*-
"""ConnectFour.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17r6MWQaLANKaPumh4xarRjL123sbJN13

# **TRABALHO 2: BUSCA COMPETITIVA**
**Equipe:** Daniel Krüger, Eduardo Lyra, Lucas Fritzke e Luiz Henrique Martendal
<br>

## **Connect 4: Implementação Utilizando Minimax e Poda Alfa-Beta**


---

Connect Four é um jogo de tabuleiro de raciocínio lógico e estratégia, onde os jogadores se alternam para colocar fichas coloridas em uma grade vertical. O objetivo é ser o primeiro a formar uma linha de quatro fichas da mesma cor, seja na horizontal, vertical ou diagonal

 <br>

 **REGRAS:**


*   O jogo é jogado em um tabuleiro de 6 linhas por 7 colunas
*   Os jogadores se alternam para inserir uma peça em qualquer coluna não cheia
*   A peça cai até a linha mais baixa disponível da coluna
*   O objetivo é ser o primeiro a alinhar quatro peças consecutivas
*   Se o tabuleiro estiver cheio e nenhum jogador tiver alinhado quatro peças, o jogo termina em empate

<br>

## **Formulação completa do problema de busca**


---

### **Estado Inicial**

Tabuleiro vazio (" - "), representado por uma matriz 6x7

<br>

### **Estado Objetivo**

O estado objetivo é qualquer configuração do tabuleiro em que um dos jogadores tenha quatro peças consecutivas (seja horizontal, vertical ou diagonal). Também existe a possíbilidade de empate

<br>

### **Função Sucessor (Ações Possíveis)**

As ações possíveis são escolher uma coluna não cheia (de 1 a 7) e inserir uma peça

<br>

### **Custo de Caminho**

Todas as jogadas têm o mesmo custo, portanto consideraramos que o custo de caminho é igual para todas as ações
<br>


---



## **Algoritmo escolhido e tipo de Jogo**
Connect Four é um jogo determinístico, ou seja, o resultado de uma jogada é inteiramente determinado pelas ações dos jogadores, sem envolvimento de elementos aleatórios. Dentre os algoritmos, o escolhido foi o Minimax, pois permite simular e avaliar todas as possíveis jogadas dos jogadores, buscando sempre a decisão ótima para maximizar as chances de vitória. Porém, somente o Minimax não seria capaz de trazer jogadas viáveis, uma vez que a árvore de jogo é muito grande. Por isso, utilizamos a poda Alfa-Beta, que é uma otimização do Minimax e permite reduzir o número de estados avaliados, descartando ramos da árvore que não influenciam o resultado final. Também utilizamos uma função heurística para casos em que o algoritmo não pode explorar todas as possibilidades devido à limitação de profundidade.

# **Constantes do Código**
"""

import numpy as np

# Constantes do jogo
LINHAS = 6
COLUNAS = 7
PECA_VAZIA = "-"
PECA_JOGADOR = "X"
PECA_IA = "O"
PROFUNDIDADE_MAXIMA = 5

"""# **Métodos responsáveis por implementar as regras do jogo**"""

# Criar o tabuleiro
tabuleiro = np.full((LINHAS, COLUNAS), PECA_VAZIA)

# Função para imprimir o tabuleiro
def imprimir_tabuleiro():
    print("1   2   3   4   5   6   7")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 29)
    print("\n")

# Função para verificar se a jogada é válida
def jogada_valida(coluna):
    return tabuleiro[0][coluna] == PECA_VAZIA

# Função para obter a próxima linha disponível na coluna
def obter_linha_aberta(coluna):
    for linha in range(LINHAS - 1, -1, -1):
        if tabuleiro[linha][coluna] == PECA_VAZIA:
            return linha

# Função para verificar se há um vencedor
def verificar_vitoria():
    # Verificações horizontais, verticais e diagonais
    for c in range(COLUNAS - 3):
        for l in range(LINHAS):
            if tabuleiro[l][c] == tabuleiro[l][c + 1] == tabuleiro[l][c + 2] == tabuleiro[l][c + 3] != PECA_VAZIA:
                return tabuleiro[l][c]

    for c in range(COLUNAS):
        for l in range(LINHAS - 3):
            if tabuleiro[l][c] == tabuleiro[l + 1][c] == tabuleiro[l + 2][c] == tabuleiro[l + 3][c] != PECA_VAZIA:
                return tabuleiro[l][c]

    for c in range(COLUNAS - 3):
        for l in range(LINHAS - 3):
            if tabuleiro[l][c] == tabuleiro[l + 1][c + 1] == tabuleiro[l + 2][c + 2] == tabuleiro[l + 3][c + 3] != PECA_VAZIA:
                return tabuleiro[l][c]

    for c in range(COLUNAS - 3):
        for l in range(3, LINHAS):
            if tabuleiro[l][c] == tabuleiro[l - 1][c + 1] == tabuleiro[l - 2][c + 2] == tabuleiro[l - 3][c + 3] != PECA_VAZIA:
                return tabuleiro[l][c]

    return None  # Nenhum vencedor ainda

# Função para verificar se o tabuleiro está cheio (empate)
def verificar_empate():
    return all(tabuleiro[0][c] != PECA_VAZIA for c in range(COLUNAS))

"""# **Implemetação do algoritmo de Busca Competitiva**
<br>
O objetivo da IA é maximizar sua pontuação e minimizar a do oponente, enquanto a poda Alfa-Beta reduz o número de nós a serem avaliados, melhorando o desempenho

## **Função de Avaliação (avaliar_tabuleiro)**
Utiliza uma matriz de pesos (matriz de heurística) que atribui um valor a cada posição do tabuleiro. O objetivo é dar maior peso para posições mais centrais, onde a chance de formar sequências de quatro peças é maior. A função soma esses valores para peças da IA e subtrai para peças do jogador

## **Algoritmo Minimax**

Avalia todas as jogadas possíveis, explorando a árvore de decisões até uma profundidade pré-determinada. Se o nó atual é de "maximização", o algoritmo busca o valor máximo, enquanto se é de "minimização", busca o valor mínimo. A poda Alfa-Beta é usada para reduzir o número de estados explorados, interrompendo a busca em ramos que não irão alterar o resultado.

## **Função de Escolha de Jogada**

A função principal da IA que testa todas as colunas e usa o algoritmo Minimax para identificar a coluna que maximiza a pontuação de acordo com a avaliação heurística
"""

# Matriz de heurística para avaliação das posições do tabuleiro
tabuleiro_avaliacao = np.array([[3, 4, 5, 7, 5, 4, 3],
                                [4, 6, 8, 10, 8, 6, 4],
                                [5, 7, 11, 13, 11, 7, 5],
                                [5, 7, 11, 13, 11, 7, 5],
                                [4, 6, 8, 10, 8, 6, 4],
                                [3, 4, 5, 7, 5, 4, 3]])

# Função de avaliação do tabuleiro
def avaliar_tabuleiro():
    valor = 0  # Inicializa o valor total de avaliação do tabuleiro

    # Percorre todas as linhas e colunas do tabuleiro
    for l in range(LINHAS):
        for c in range(COLUNAS):
            # Se a peça na posição atual for da IA, adiciona o valor da matriz de heurística
            if tabuleiro[l][c] == PECA_IA:
                valor += tabuleiro_avaliacao[l][c]
            # Se a peça na posição atual for do jogador, subtrai o valor da matriz de heurística
            elif tabuleiro[l][c] == PECA_JOGADOR:
                valor -= tabuleiro_avaliacao[l][c]

    return valor  # Retorna o valor total de avaliação do tabuleiro

# Função Minimax com poda Alfa-Beta melhorada
def minimax(profundidade, alfa, beta, maximizando):
    vencedor = verificar_vitoria()  # Verifica se há um vencedor no estado atual do tabuleiro

    # Verifica as condições terminais do jogo (vitória da IA, vitória do jogador ou empate)
    if vencedor == PECA_IA:
        return None, 1_000_000 + profundidade  # Vitória da IA, retorna um valor alto ajustado pela profundidade
    elif vencedor == PECA_JOGADOR:
        return None, -1_000_000 - profundidade  # Vitória do jogador, retorna um valor baixo ajustado pela profundidade
    elif verificar_empate() or profundidade == 0:
        return None, avaliar_tabuleiro()  # Empate ou profundidade máxima atingida, avalia o tabuleiro

    melhor_coluna = None  # Inicializa a melhor coluna como None

    # Se o nó atual é de maximização
    if maximizando:
        valor_maximo = -np.inf  # Inicializa o valor máximo com um valor negativo infinito

        # Percorre todas as colunas do tabuleiro
        for coluna in range(COLUNAS):
            if jogada_valida(coluna):  # Verifica se a jogada na coluna atual é válida
                linha = obter_linha_aberta(coluna)  # Obtém a próxima linha disponível na coluna
                tabuleiro[linha][coluna] = PECA_IA  # Faz a jogada temporária para a IA

                # Chama recursivamente o minimax com profundidade reduzida e alternando para o jogador
                _, novo_valor = minimax(profundidade - 1, alfa, beta, False)

                tabuleiro[linha][coluna] = PECA_VAZIA  # Desfaz a jogada temporária

                # Se o valor encontrado for maior que o valor máximo atual, atualiza o valor máximo
                if novo_valor > valor_maximo:
                    valor_maximo = novo_valor
                    melhor_coluna = coluna  # Atualiza a melhor coluna

                alfa = max(alfa, valor_maximo)  # Atualiza o valor de alfa
                if alfa >= beta:  # Poda Alfa-Beta: interrompe a busca se alfa for maior ou igual a beta
                    break

        return melhor_coluna, valor_maximo  # Retorna a melhor coluna e o valor máximo encontrado

    # Caso contrário, o nó atual é de minimização
    else:
        valor_minimo = np.inf  # Inicializa o valor mínimo com um valor positivo infinito

        # Percorre todas as colunas do tabuleiro
        for coluna in range(COLUNAS):
            if jogada_valida(coluna):  # Verifica se a jogada na coluna atual é válida
                linha = obter_linha_aberta(coluna)  # Obtém a próxima linha disponível na coluna
                tabuleiro[linha][coluna] = PECA_JOGADOR  # Faz a jogada temporária para o jogador

                # Chama recursivamente o minimax com profundidade reduzida e alternando para a IA
                _, novo_valor = minimax(profundidade - 1, alfa, beta, True)

                tabuleiro[linha][coluna] = PECA_VAZIA  # Desfaz a jogada temporária

                # Se o valor encontrado for menor que o valor mínimo atual, atualiza o valor mínimo
                if novo_valor < valor_minimo:
                    valor_minimo = novo_valor
                    melhor_coluna = coluna  # Atualiza a melhor coluna

                beta = min(beta, valor_minimo)  # Atualiza o valor de beta
                if alfa >= beta:  # Poda Alfa-Beta: interrompe a busca se alfa for maior ou igual a beta
                    break

        return melhor_coluna, valor_minimo  # Retorna a melhor coluna e o valor mínimo encontrado


# Função para a jogada da IA
def buscar_melhor_jogada():
    melhor_valor = -float('inf')
    melhor_coluna = None
    for coluna in range(COLUNAS):  # Inicia os testes da coluna 1 até 7
        if jogada_valida(coluna):
            linha = obter_linha_aberta(coluna)
            # coloca temporariamente a peça da IA
            tabuleiro[linha][coluna] = PECA_IA
            # A partir dessa possibilidade avança um nível da árvore
            _, valor = minimax(PROFUNDIDADE_MAXIMA - 1, -float('inf'), float('inf'), False)
            # volta ao estado inicial do tabuleiro
            tabuleiro[linha][coluna] = PECA_VAZIA
            # Se esse ramo da árvore for o melhor, guarda a coluna e o valor
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_coluna = coluna
    return melhor_coluna

"""# **Métodos que integram as chamadas da IA x Humano**

"""

def jogada_ia():
    coluna = buscar_melhor_jogada()
    if coluna is not None:
        linha = obter_linha_aberta(coluna)
        tabuleiro[linha][coluna] = PECA_IA
        if verificar_vitoria() == PECA_IA:
            imprimir_tabuleiro()
            print("IA venceu!\n")
            return True
    return False

# Função para a jogada do jogador
def jogada_humano():
    imprimir_tabuleiro()
    coluna = int(input("Escolha uma coluna (1-7): ")) - 1
    if jogada_valida(coluna):
        linha = obter_linha_aberta(coluna)
        tabuleiro[linha][coluna] = PECA_JOGADOR
        if verificar_vitoria() == PECA_JOGADOR:
            imprimir_tabuleiro()
            print("Jogador venceu!\n")
            return True
    else:
        print("Coluna inválida ou cheia! Tente novamente.")
        jogada_humano()
    return False

# Função principal para gerenciar o jogo
def jogar():
    while True:
        if jogada_humano():
            break
        if verificar_empate():
            imprimir_tabuleiro()
            print("Deu empate!!!")
            break
        if jogada_ia():
            break
        if verificar_empate():
            imprimir_tabuleiro()
            print("Deu empate!!!")
            break

# Função principal
def main():
    print("Bem-vindo ao Connect Four!")
    jogar()

if __name__ == "__main__":
    main()