"""
Um jogo com tabuleiro unidirecional comporta dois jogadores.
Vence quem chegar primeiro a ultima casa do tabuleiro com menos turnos.
Para caminhar com as peças, os jogadores utilizam uma roleta que sorteia se devem andar 1, 2 ou 3 casas.
Caso tire um número maior na roleta, que casas faltantes, o jogador deve iniciar novamente o percurso (como um looping).
O tamanho mínimo do tabuleiro deve ser 3 casas sem um máximo.

Crie uma função que recebe o número de casas do tabuleiro e devolve:
1 - Quantidade mínimo de turnos para se chegar ao destino (caminho ótimo);
2 - Probabilidade de um usuário conseguir executar o caminho ótimo;
3 - Quantas combinações de movimentos diferentes um jogador conseguiria executar sem efetuar nenhum looping no tabuleiro.
"""
THREE = 3
TWO = 2
ONE = 1


def min_path(lenght):
    tabletop = 0
    count = [0, 0, 0]
    while lenght != tabletop:
        if tabletop + THREE <= lenght:
            tabletop += THREE
            count[2] += 1
        elif tabletop + TWO <= lenght:
            tabletop += TWO
            count[1] += 1
        elif tabletop + ONE <= lenght:
            tabletop += ONE
            count[0] += 1
    return sum(count)


def probability_optimum_path(optimum_steps):
    return 0.33 ** optimum_steps


if __name__ == "__main__":
    assert min_path(3) == 1
    assert min_path(4) == 2
    assert min_path(5) == 2
    assert min_path(6) == 2
    assert min_path(7) == 3
    assert min_path(8) == 3
    assert min_path(9) == 3
    assert min_path(10) == 4
    assert probability_optimum_path(min_path(3)) == 0.33
    assert probability_optimum_path(min_path(4)) == 0.10890000000000001
    assert probability_optimum_path(min_path(7)) == 0.035937000000000004
    assert probability_optimum_path(min_path(10)) == 0.011859210000000002
