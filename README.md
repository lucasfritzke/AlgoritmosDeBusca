# Algoritmos de Busca Competitiva

Este repositório contém implementações de algoritmos de busca competitiva aplicados em jogos como 'Connect Four' e 'Jogo da Velha' utilizando o algoritmo Minimax com poda Alfa-Beta.

## Motivação

Desde o início da Inteligência Artificial (IA), jogos de estratégia têm sido utilizados como benchmarks para medir o progresso e a eficácia de algoritmos.
Nos primórdios da IA, pesquisadores enxergavam os jogos como uma plataforma ideal para desafiar computadores a resolver problemas complexos de planejamento e decisão. 

Um dos maiores marcos foi em 1997, quando o Deep Blue, desenvolvido pela IBM, derrotou o campeão mundial de xadrez Garry Kasparov. Este evento representou um avanço significativo na história da IA, evidenciando a eficácia de algoritmos de busca como o Minimax com técnicas de poda para otimizar o processo de decisão. Outro momento icônico foi em 2016, quando o AlphaGo, do Google DeepMind, venceu o campeão mundial de Go, um jogo tradicionalmente considerado mais complexo do que o xadrez, devido ao seu vasto espaço de possibilidades.

Esses sucessos demonstram como algoritmos de busca competitiva podem ser aplicados não apenas em jogos, mas também em diversas áreas da otimização e da tomada de decisões. Jogos fornecem um ambiente controlado para testar e aprimorar esses algoritmos, tornando-os mais robustos e aplicáveis em situações do mundo real.

## Funcionalidades

- **Implementação do Connect Four** com o algoritmo Minimax e poda Alfa-Beta.
- **Implementação do Jogo da Velha** utilizando poda Alfa-Beta.
- Explicação detalhada do algoritmo e sua aplicação.

## Como Funciona

O algoritmo Minimax com poda Alfa-Beta é utilizado para determinar a melhor jogada em jogos de tabuleiro como Connect Four e Jogo da Velha. Ele utiliza uma estratégia de otimização para reduzir o número de nós analisados durante a busca, mantendo a precisão da decisão. A poda Alfa-Beta elimina ramos do espaço de busca que não precisam ser explorados, melhorando a eficiência do algoritmo sem comprometer o resultado.

## Estrutura do Projeto

- `ConnectFour.ipynb` - Caderno Jupyter com explicação e implementação do Connect Four.
- `connectfour.py` - Arquivo Python com a implementação completa do jogo Connect Four.
- `JogoDaVelhaAlphaBeta.ipynb` - Caderno Jupyter com a implementação do Jogo da Velha.
- `JogoDaVelha_PodaAlfaBeta.py` - Arquivo Python com a implementação do algoritmo Minimax com poda Alfa-Beta para o Jogo da Velha.
