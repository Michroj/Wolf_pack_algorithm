import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sforyWilka(liczbaIteracji, rozmiarPopulacji, wspolczynnikWspolpracy, wspolczynnikRuchu):
    # Funkcja celu, którą chcemy zminimalizować
    def funkcjaCelu(x):
        return np.sum((x - np.arange(1, len(x) + 1))**2)

    # Inicjalizacja populacji wilków
    populacja = np.random.uniform(0, 10, size=(rozmiarPopulacji, 10))

    # Funkcja wywoływana w każdej klatce animacji
    def update(frame):
        nonlocal populacja

        # Obliczenie wartości funkcji celu dla każdego wilka
        funkcjeCelu = np.apply_along_axis(funkcjaCelu, axis=1, arr=populacja)

        # Sortowanie populacji według wartości funkcji celu
        posortowanaPopulacja = populacja[np.argsort(funkcjeCelu)]

        # Wybór lidera stada - wilka o najmniejszej wartości funkcji celu
        lider = posortowanaPopulacja[0]

        # Aktualizacja położenia każdego wilka
        nowaPopulacja = np.zeros_like(populacja)
        for j in range(rozmiarPopulacji):
            # Aktualizacja położenia wilka zgodnie z algorytmem wilka
            nowePolozenie = populacja[j] + wspolczynnikWspolpracy * np.random.uniform(-1, 1, size=10) * (lider - populacja[j]) + wspolczynnikRuchu * np.random.uniform(-1, 1, size=10) * (posortowanaPopulacja[np.random.randint(1, rozmiarPopulacji)] - populacja[j])
            nowaPopulacja[j] = nowePolozenie

        # Aktualizacja populacji
        populacja = nowaPopulacja

        # Wyświetlenie aktualnego stanu populacji
        plt.cla()
        plt.scatter(populacja[:, 0], populacja[:, 1], c='blue', label='Populacja wilków')
        plt.scatter(lider[0], lider[1], c='red', marker='x', label='Lider stada')
        plt.xlabel('Wymiar 1')
        plt.ylabel('Wymiar 2')
        plt.title('Algorytm Wilka - Iteracja {}'.format(frame))
        plt.legend()

    # Inicjalizacja animacji
    fig = plt.figure()
    anim = FuncAnimation(fig, update, frames=liczbaIteracji, interval=500)

    # Wyświetlenie animacji
    plt.show()

# Wywołanie funkcji sforyWilka z odpowiednimi parametrami
sforyWilka(100, 50, 0.5, 0.2)
