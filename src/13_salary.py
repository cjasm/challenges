"""Escreva uma função que determina o número de avos a serem pagos a um funcionário de 13º e férias em seu ultimo ano de trabalho  ele possui no emprego.
Se o funcionário permanecer empregado por pelo menos 15 dias no mês, ele tem direito ao avo daquele mês.

O Benefício 13º zera anualmente, já Férias zera-se a cada aniversário de trabalho.

Assinatura:
inteiro calculaAvos(Data dataInicio, Data dataFim, Benefício);
O objeto Data possui quaisquer métodos e parâmetros necessários.
"""
"""
Discussão
Esse primeiro exercicio eu senti falta de exemplos concretos.
existem muitas questões quanto a validação desses dados.
Sendo Assim, tentei testar algumas fronteiras.

Converti a assinatura do método de 'java' para python
e senti que a questão ficou dúbia no enunciado quando fala que deveria ser
retornado o avos. Poderia ser apenas a fraçao de tempo ou a fração do salário.
Contudo, fiquei com a última opção devido à entrada do método.
"""

from datetime import date
from dateutil.relativedelta import relativedelta


def _meses_trabalhados(inicio: date, fim: date) -> int:
    """

    :param inicio: data inicial
    :param fim: data final
    :return: meses trabalhados no periodo
    """
    delta = relativedelta(fim, inicio)
    meses = delta.months
    meses += 1 if delta.days >= 15 else 0

    return meses


def _calcula_decimo(inicio: date, fim: date, avos: float) -> float:
    """
    Calcula o valor do décimo terceiro

    :param inicio: data inicial
    :param fim: data final
    :param float avos: fracao do beneficio
    :return: valor proporcional do décimo terceiro
    """
    if (fim.year - inicio.year) < 1:
        meses = _meses_trabalhados(inicio, fim)
    else:
        meses = _meses_trabalhados(date(fim.year, 1, 1), fim)
    return meses * avos


def _calcula_ferias(inicio: date, fim: date, avos: float) -> float:
    """
    Calcula o valor das férias

    :param inicio: data inicial
    :param fim: data final
    :param float avos: fracao do beneficio
    :return: valor proporcional das ferias
    """
    meses = _meses_trabalhados(inicio, fim)
    return meses * avos


def calcula_avos(data_inicio: date, data_fim: date, beneficio: float) -> (float, float):
    """
    Função que calcula o quanto o funcionário vai receber de ferias
    e de décimo terceiro.

    :param data_inicio: data inicial
    :param data_fim: data final
    :param beneficio: o beneficio salarial
    :return: o valor do decimo terceiro e das ferias
    """
    avos = beneficio / 12
    decimo = _calcula_decimo(data_inicio, data_fim, avos)
    ferias = _calcula_ferias(data_inicio, data_fim, avos)
    return decimo, ferias


if __name__ == '__main__':
    # Dia
    # Menos de 15 dias
    init = date(2020, 1, 11)
    end = date(2020, 1, 12)
    assert _calcula_decimo(init, end, 100) == 0
    assert _calcula_ferias(init, end, 100) == 0
    # Com 15 dias
    init = date(2020, 1, 11)
    end = date(2020, 1, 26)
    assert _calcula_decimo(init, end, 100) == 100.0
    assert _calcula_ferias(init, end, 100) == 100.0
    # Mais de 15 e Menos de 1 mês
    init = date(2020, 1, 11)
    end = date(2020, 2, 10)
    assert _calcula_decimo(init, end, 100) == 100.0
    assert _calcula_ferias(init, end, 100) == 100.0
    # Mês
    # Um mês completo
    init = date(2020, 1, 11)
    end = date(2020, 2, 11)
    assert _calcula_decimo(init, end, 100) == 100.0
    assert _calcula_ferias(init, end, 100) == 100.0
    init = date(2020, 2, 1)
    end = date(2020, 2, 28)
    assert _calcula_decimo(init, end, 100) == 100.0
    assert _calcula_ferias(init, end, 100) == 100.0
    # comecando com menos de 15 e terminando com mais de 15
    init = date(2020, 1, 14)
    end = date(2020, 8, 1)
    assert _calcula_decimo(init, end, 100) == 700.0
    assert _calcula_ferias(init, end, 100) == 700.0
    init = date(2020, 1, 11)
    end = date(2020, 8, 26)
    assert _calcula_decimo(init, end, 100) == 800.0
    assert _calcula_ferias(init, end, 100) == 800.0
    # Ano
    # ano diferente e mais de 15 dias
    init = date(2020, 12, 1)
    end = date(2021, 8, 26)
    assert _calcula_decimo(init, end, 100) == 800.0
    assert _calcula_ferias(init, end, 100) == 900.0
    init = date(2020, 8, 1)
    end = date(2021, 7, 26)
    assert _calcula_decimo(init, end, 100) == 700.0
    assert _calcula_ferias(init, end, 100) == 1200.0
    # ano diferentes e menos de 15 dias
    init = date(2020, 12, 1)
    end = date(2021, 7, 14)
    assert _calcula_decimo(init, end, 100) == 600.0
    assert _calcula_ferias(init, end, 100) == 700.0
    # mais de um ano e menos de 15 dias
    init = date(2020, 8, 1)
    end = date(2021, 8, 14)
    assert _calcula_decimo(init, end, 100) == 700.0
    assert _calcula_ferias(init, end, 100) == 0.0
    # mais de um ano e mais de 15 dias
    init = date(2020, 8, 1)
    end = date(2021, 8, 16)
    assert _calcula_decimo(init, end, 100) == 800.0
    assert _calcula_ferias(init, end, 100) == 100.0
    # mais de um ano e um mes
    init = date(2020, 8, 1)
    end = date(2021, 9, 1)
    assert _calcula_decimo(init, end, 100) == 800.0
    assert _calcula_ferias(init, end, 100) == 100.0
    # mais de um ano e um mes
    init = date(2020, 8, 1)
    end = date(2021, 9, 1)
    assert _calcula_decimo(init, end, 100) == 800.0
    assert _calcula_ferias(init, end, 100) == 100.0
    # mais de um ano e comecando com mais de 15 e terminando com menos de 15
    init = date(2020, 8, 16)
    end = date(2021, 9, 7)
    assert _calcula_decimo(init, end, 100) == 800.0
    assert _calcula_ferias(init, end, 100) == 100.0
    # Dois anos
    # dois anos exatos
    init = date(2020, 5, 8)
    end = date(2022, 5, 7)
    assert _calcula_decimo(init, end, 100) == 400.0
    assert _calcula_ferias(init, end, 100) == 1200.0
    # dois anos e menos de 15 dias
    init = date(2020, 5, 8)
    end = date(2022, 5, 14)
    assert _calcula_decimo(init, end, 100) == 400.0
    assert _calcula_ferias(init, end, 100) == 0.0
    # dois anos e mais de 15 dias
    init = date(2020, 5, 8)
    end = date(2022, 5, 27)
    assert _calcula_decimo(init, end, 100) == 500.0
    assert _calcula_ferias(init, end, 100) == 100.0