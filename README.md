# Desafio - Jogo de Batalha Naval

## 📝 Descrição

Este projeto é uma implementação em Python do clássico jogo Batalha Naval. O jogo é executado via terminal (console) e coloca o jogador contra uma inteligência artificial (computador).

O objetivo do desafio é demonstrar a capacidade de estruturar a lógica de um jogo, manipular estruturas de dados (como matrizes para o tabuleiro) e gerenciar o estado do jogo (turnos, acertos, erros e condição de vitória).

## 🏗️ Estrutura do Projeto

* **`batalha_naval.py`**: Arquivo único que contém toda a lógica do jogo, incluindo:
    * Criação e exibição dos tabuleiros (o do jogador e o de tiro).
    * Posicionamento aleatório dos navios para o jogador e para o computador.
    * Lógica de turnos alternados.
    * Validação de jogadas.
    * Lógica de "tiro" da IA (aleatória).
    * Verificação de acertos, erros e navios afundados.
    * Detecção da condição de fim de jogo.
* **`README.md`**: Esta documentação, explicando o projeto, como executá-lo e as regras.

## ⚙️ Como Executar o Jogo

1.  Certifique-se de ter o **Python 3** instalado em seu computador.
2.  Faça o download do arquivo `batalha_naval.py`.
3.  Abra um terminal (ou Prompt de Comando no Windows) na pasta onde o arquivo foi salvo.
4.  Execute o seguinte comando para iniciar o jogo:
    ```bash
    python batalha_naval.py
    ```

## 룰 Como Jogar

* Ao iniciar, os navios serão posicionados aleatoriamente nos tabuleiros do jogador e do computador.
* Você verá dois tabuleiros:
    * **SEU TABULEIRO:** Mostra seus navios (`N`), água (`~`), seus navios que foram atingidos (`X`) e tiros na água (`O`).
    * **TABULEIRO DE TIRO:** Onde você marca seus tiros. Mostra os acertos (`X`), erros (`O`) e água não explorada (`~`).
* Na sua vez, insira uma coordenada para atirar (ex: `A5`, `C10`, `J1`).
* O jogo informará se você acertou um navio ou a água.
* Em seguida, o computador fará a jogada dele.
* O jogo termina quando um dos jogadores afundar todos os navios do oponente.
