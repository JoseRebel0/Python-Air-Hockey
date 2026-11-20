# Python Air Hockey

Este é um jogo simples em Python, desenvolvido nas aulas de Programação no 10.º ano, como projeto de avaliação dos conhecimentos de Python.

## Descrição do Jogo

- **Jogo 1 contra 1**: Dois jogadores podem competir um contra o outro no mesmo teclado.
  - O Jogador 1 usa as teclas `W`, `A`, `S`, `D` para controlar a sua personagem.
  - O Jogador 2 usa as teclas de seta (`←`, `↑`, `→`, `↓`) para controlar a sua personagem.
- **Contador de Pontos**: O jogo inclui um sistema de pontuação para determinar o vencedor.

## Como Jogar

1. Clone este repositório para a sua máquina.
2. Certifique-se de que tem o Python instalado no seu sistema.
3. Execute o jogo com o seguinte comando:
   ```bash
   python game.py
   ```

## Requisitos

- Python 3.x

## Problemas Conhecidos e Limitações

- **Sem barreiras**: Os jogadores conseguem atravessar os limites visuais do campo, o que pode prejudicar a experiência de jogo.
- **Falta de física no disco**: O disco move-se de forma errática e não tem direção nem controlo adequados, o que afeta a dinâmica do jogo.
- **O jogo nunca termina**: O jogo não tem um fim definido nem uma condição de vitória, sendo necessário parar manualmente quando se quiser.
