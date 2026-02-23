import math
import matplotlib.pyplot as plt


class MojGenerator:
    def __init__(self, ziarno=123):
        self.stan = ziarno
        # Parametry LCG (standardowe wartości)
        self.a = 1664525
        self.c = 1013904223
        self.m = 2 ** 32

    def losuj_01(self):
        """Generuje liczbę z przedziału [0, 1)"""
        self.stan = (self.a * self.stan + self.c) % self.m
        return self.stan / self.m


# --- INICJACJA ---
gen = MojGenerator(ziarno=0)
ile = 500000

# --- ROZKŁAD POISSONA (Lambda = 4) ---
poisson_wyniki = []
lam = 4
L = math.exp(-lam)

for _ in range(ile):
    k = 0
    p = 1.0
    while p > L:
        k += 1
        p *= gen.losuj_01()
    poisson_wyniki.append(k - 1)

# --- ROZKŁAD GAUSSA (mu=0, sigma=1) ---
gauss_wyniki = []
mu = 0
sigma = 1

for _ in range(ile // 2):
    u1 = gen.losuj_01()
    u2 = gen.losuj_01()

    # Box-Muller
    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    z1 = math.sqrt(-2.0 * math.log(u1)) * math.sin(2.0 * math.pi * u2)

    gauss_wyniki.append(z0 * sigma + mu)
    gauss_wyniki.append(z1 * sigma + mu)

# --- WYKRESY ---
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.hist(poisson_wyniki, bins=range(max(poisson_wyniki) + 2), color='orange', edgecolor='black')
plt.title(f"Poisson (Własny Generator, lambda={lam})")

plt.subplot(2, 1, 2)
plt.hist(gauss_wyniki, bins=50, color='skyblue', edgecolor='black')
plt.title(f"Gauss (Własny Generator, mu={mu}, sigma={sigma})")

plt.tight_layout()
plt.show()