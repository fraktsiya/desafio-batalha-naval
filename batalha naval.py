import random
import os
import time

# --- CONFIGURAÇÕES DO JOGO ---
TAMANHO_TABULEIRO = 10
NAVIOS = {"Porta-aviões": 5, "Encouraçado": 4, "Cruzador": 3, "Submarino": 3, "Destróier": 2}

# --- SÍMBOLOS DO TABULEIRO ---
AGUA = "~"
NAVIO = "N"
ACERTO = "X"
ERRO = "O"

def limpar_tela():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_tabuleiro():
    """Cria um tabuleiro vazio."""
    return [[AGUA for _ in range(TAMANHO_TABULEIRO)] for _ in range(TAMANHO_TABULEIRO)]

def imprimir_tabuleiros(tabuleiro_jogador, tabuleiro_tiro):
    """Imprime o tabuleiro do jogador e o de tiro lado a lado."""
    limpar_tela()
    print("----------- BATALHA NAVAL -----------")
    print("\n   SEU TABULEIRO" + " " * (TAMANHO_TABULEIRO * 2 - 5) + "TABULEIRO DE TIRO")
    
    # Cabeçalho com letras
    header = "  " + " ".join([chr(ord('A') + i) for i in range(TAMANHO_TABULEIRO)])
    print(header + "    " + header)

    for i in range(TAMANHO_TABULEIRO):
        # Linha do tabuleiro do jogador
        linha_jogador_str = f"{i+1:<2}" + " ".join(tabuleiro_jogador[i])
        
        # Linha do tabuleiro de tiro
        linha_tiro_str = f"{i+1:<2}" + " ".join(tabuleiro_tiro[i])

        print(linha_jogador_str + "    " + linha_tiro_str)
    print("-" * 35)


def posicionar_navios(tabuleiro, navios):
    """Posiciona os navios aleatoriamente no tabuleiro."""
    for tamanho in navios.values():
        posicionado = False
        while not posicionado:
            orientacao = random.choice(['horizontal', 'vertical'])
            if orientacao == 'horizontal':
                linha = random.randint(0, TAMANHO_TABULEIRO - 1)
                coluna = random.randint(0, TAMANHO_TABULEIRO - tamanho)
                
                # Verifica se há espaço
                if all(tabuleiro[linha][c] == AGUA for c in range(coluna, coluna + tamanho)):
                    for c in range(coluna, coluna + tamanho):
                        tabuleiro[linha][c] = NAVIO
                    posicionado = True
            else: # vertical
                linha = random.randint(0, TAMANHO_TABULEIRO - tamanho)
                coluna = random.randint(0, TAMANHO_TABULEIRO - 1)
                
                # Verifica se há espaço
                if all(tabuleiro[l][coluna] == AGUA for l in range(linha, linha + tamanho)):
                    for l in range(linha, linha + tamanho):
                        tabuleiro[l][coluna] = NAVIO
                    posicionado = True

def converter_coordenada(jogada_str):
    """Converte uma string como 'A5' para coordenadas de matriz (4, 0)."""
    jogada_str = jogada_str.upper()
    if len(jogada_str) < 2 or len(jogada_str) > 3: return None
    
    col_letra = jogada_str[0]
    lin_num_str = jogada_str[1:]
    
    if not ('A' <= col_letra <= chr(ord('A') + TAMANHO_TABULEIRO - 1)) or not lin_num_str.isdigit():
        return None
        
    linha = int(lin_num_str) - 1
    coluna = ord(col_letra) - ord('A')

    if 0 <= linha < TAMANHO_TABULEIRO and 0 <= coluna < TAMANHO_TABULEIRO:
        return linha, coluna
    return None

def contar_navios_restantes(tabuleiro):
    """Conta quantas partes de navio ('N') ainda existem no tabuleiro."""
    return sum(linha.count(NAVIO) for linha in tabuleiro)

def turno_do_jogador(tabuleiro_computador, tabuleiro_tiro):
    """Lógica para o turno do jogador."""
    while True:
        jogada_str = input("\nSua vez! Digite a coordenada para atirar (ex: A5): ")
        coords = converter_coordenada(jogada_str)
        
        if coords is None:
            print("Coordenada inválida! Tente novamente.")
            continue
        
        linha, coluna = coords
        if tabuleiro_tiro[linha][coluna] != AGUA:
            print("Você já atirou aí! Escolha outra coordenada.")
            continue
            
        # Verifica o tiro
        if tabuleiro_computador[linha][coluna] == NAVIO:
            print(f"\nFOGO! Você acertou um navio em {jogada_str.upper()}!")
            tabuleiro_tiro[linha][coluna] = ACERTO
            tabuleiro_computador[linha][coluna] = ACERTO # Marca o acerto no tabuleiro real do PC
        else:
            print(f"\nÁGUA! Você errou o tiro em {jogada_str.upper()}.")
            tabuleiro_tiro[linha][coluna] = ERRO
        break

def turno_do_computador(tabuleiro_jogador):
    """Lógica para o turno do computador (IA aleatória)."""
    print("\nTurno do computador...")
    time.sleep(1)
    
    while True:
        linha = random.randint(0, TAMANHO_TABULEIRO - 1)
        coluna = random.randint(0, TAMANHO_TABULEIRO - 1)
        
        # Verifica se já atirou ali
        if tabuleiro_jogador[linha][coluna] not in [ACERTO, ERRO]:
            letra_col = chr(ord('A') + coluna)
            num_lin = linha + 1
            
            if tabuleiro_jogador[linha][coluna] == NAVIO:
                print(f"O computador acertou seu navio em {letra_col}{num_lin}!")
                tabuleiro_jogador[linha][coluna] = ACERTO
            else:
                print(f"O computador atirou na água em {letra_col}{num_lin}.")
                tabuleiro_jogador[linha][coluna] = ERRO
            break
    time.sleep(2)

def jogar():
    """Função principal que executa o jogo."""
    tabuleiro_jogador = criar_tabuleiro()
    tabuleiro_computador = criar_tabuleiro()
    tabuleiro_tiro_jogador = criar_tabuleiro() # Tabuleiro para o jogador marcar os tiros

    posicionar_navios(tabuleiro_jogador, NAVIOS)
    posicionar_navios(tabuleiro_computador, NAVIOS)

    while True:
        imprimir_tabuleiros(tabuleiro_jogador, tabuleiro_tiro_jogador)
        
        # Turno do Jogador
        turno_do_jogador(tabuleiro_computador, tabuleiro_tiro_jogador)
        if contar_navios_restantes(tabuleiro_computador) == 0:
            imprimir_tabuleiros(tabuleiro_jogador, tabuleiro_tiro_jogador)
            print("\nPARABÉNS! Você afundou todos os navios inimigos e venceu a batalha!")
            break
        
        # Turno do Computador
        imprimir_tabuleiros(tabuleiro_jogador, tabuleiro_tiro_jogador) # Mostra o resultado do tiro do jogador
        turno_do_computador(tabuleiro_jogador)
        if contar_navios_restantes(tabuleiro_jogador) == 0:
            imprimir_tabuleiros(tabuleiro_jogador, tabuleiro_tiro_jogador)
            print("\nFIM DE JOGO! O computador afundou todos os seus navios. Você perdeu.")
            break

if __name__ == "__main__":
    jogar()
