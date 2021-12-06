"""Existe um WebService que retorna a seguinte estrutura:
SeatMap {
    int width;
    int height;
    List<Seat> seats;
}
Seat {
    int x;
    int y;
    boolean available;
}
Os valores de X e Y estão entre 0 e (width -1) e (height -1) respectivamente.
Os assentos na lista NÃO estão ordenados e pode haver assentos que não existem,
por exemplo o assento com X = 3 e Y = 2 pode não existir.
Construa uma função que receba um objeto do tipo SeatMap como parâmetro
e retorne uma List<List<Seat>> com os assentos de maneira ordenada.
A ordenação deve ser:
na lista de fora os assentos devem estar ordenados com o Y de forma crescente e,
na lista de dentro, os assentos devem ter o mesmo Y e
o X ordenados também em forma crescente.
Exemplo:
Lista de entrada:
[(x=3,y=2),(x=2,y=0),(x=0,y=2),(x=3,y=3),(x=2,y=2)]
Resultado esperado:
[
[(x=2,y=0)],
[(x=0,y=2), (x=2,y=2), (x=3,y=2)],
[(x=3,y=3)]
]
"""
"""
Existem algumas brechas que não foram bem explicadas.
Por exemplo, o inicio do problema sobre o webservice não está diretamente conectado
com o problema final. 
A entrada da função no primeiro momento recebe um Seatmap, porém no segundo momento recebe uma lista de tuplas.
A saída é esperada uma lista de listas de seat, porém no segundo momento a saida esperada é uma lista de lista de tuplas.

Sobre o seatmap, também fiquei confuso quanto ao SeatMap, dado que também ficou em aberto
se a lista de assentos vai realmente do 0 até width/height -1 e os assentos não disponivéis são os que não existem,
ou se podem ir de 0 até width/height -1 com intervalos discretos, porém esses assentos existentes podem estar indisponiveis
"""


class SeatMap:
    def __init__(self, width, height, seats):
        self.width = width
        self.height = height
        self._init_seats(seats)

    def _init_seats(self, seats):
        self.seats = []
        for seat in seats:
            self.seats.append(Seat(seat[0], seat[1], True))
        return self.seats

    def get_seats(self):
        result = []
        for seat in self.seats:
            result.append((seat.x, seat.y))
        return result


class Seat:
    def __init__(self, x, y, available):
        self.x = x
        self.y = y
        self.available = available


def sort_seat(seats: list) -> list:
    # O(n*logn)
    seats.sort(key=lambda item: item[0])
    seats_dict = dict()

    # O(n)
    for seat in seats:
        if not seat[1] in seats_dict:
            seats_dict[seat[1]] = []
        seats_dict[seat[1]].append(seat)

    keys = list(seats_dict.keys())
    # O(n*logn)
    keys.sort()
    result = []
    # O(n)
    for item in keys:
        result.append(seats_dict[item])

    return result


if __name__ == "__main__":
    seat_map = SeatMap(4, 3, [(3, 2), (2, 0), (0, 2), (3, 3), (2, 2)])
    assert seat_map.get_seats() == [(3, 2), (2, 0), (0, 2), (3, 3), (2, 2)]

    assert sort_seat(seat_map.get_seats()) == [[(2, 0)], [(0, 2), (2, 2), (3, 2)], [(3, 3)]]
