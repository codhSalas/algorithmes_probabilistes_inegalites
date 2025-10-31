from src.BoiteNoire import *
import math
import random
import matplotlib.pyplot as plt

def monte_carlo_1d(fonction, a, b, N=100000):
    somme = 0
    for i in range(N):
        x = random.uniform(a, b)
        somme += fonction(x)
    
    volume = b - a
    return volume * (somme / N)

def monte_carlo_2d(fonction, a, b, c, d, N=100000):
    somme = 0
    for i in range(N):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        somme += fonction(x, y)
    
    surface = (b - a) * (d - c)
    return surface * (somme / N)

def monte_carlo_3d(fonction, a, b, c, d, e, f, N=100000):
    somme = 0
    for i in range(N):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        z = random.uniform(e, f)
        somme += fonction(x, y, z)
    
    volume = (b - a) * (d - c) * (f - e)
    return volume * (somme / N)


def f(x):
    return x * (1 - x) * (math.sin(200 * x * (1 - x)))**2

def monte_carlo_avec_visualisation(nombre_tirages=10000):
    valeurs_x = []
    valeurs_f = []
    somme = 0
    
    for i in range(nombre_tirages):
        x = random.uniform(0, 1)
        valeur_fonction = f(x)
        
        valeurs_x.append(x)
        valeurs_f.append(valeur_fonction)
        somme += valeur_fonction
    
    integrale = 1 * (somme / nombre_tirages)  
    
    plt.plot(valeurs_x, valeurs_f, "b.", markersize=1)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Méthode de Monte Carlo - f(x) = x(1-x)sin²(200x(1-x))\nIntégrale ≈ {integrale:.6f}")
    plt.grid(True)
    plt.savefig("bt_resultats.png", dpi=300)
    plt.close()
    
    return integrale

if __name__ == "__main__":

    resultat1 = monte_carlo_1d(fonction1, 0, 1)
    print(f"Intégrale 1: {resultat1}")

    resultat2 = monte_carlo_1d(fonction2, 0, math.sqrt(3))
    print(f"Intégrale 2: {resultat2}")

    resultat3 = monte_carlo_2d(fonction3, 1, 3, -2, 1)
    print(f"Intégrale 3: {resultat3}")

    resultat4 = monte_carlo_3d(fonction4, 1, 2, -2, 0, 2, 6)
    print(f"Intégrale 4: {resultat4}")