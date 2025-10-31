from src.simule import simule_cpp_moyenne_et_dispertion, affiche_moyenne
from src.bt import *

if __name__ == "__main__":
    data = simule_cpp_moyenne_et_dispertion(n_tests=100, n_max=200)
    affiche_moyenne(data, output_file="cpp_resultats.png")
    resultat1 = monte_carlo_1d(fonction1, 0, 1)
    print(f"Intégrale 1: {resultat1}")

    resultat2 = monte_carlo_1d(fonction2, 0, math.sqrt(3))
    print(f"Intégrale 2: {resultat2}")

    resultat3 = monte_carlo_2d(fonction3, 1, 3, -2, 1)
    print(f"Intégrale 3: {resultat3}")

    resultat4 = monte_carlo_3d(fonction4, 1, 2, -2, 0, 2, 6)
    print(f"Intégrale 4: {resultat4}")
    
    resultat = monte_carlo_avec_visualisation(10000)
    print(f"Approximation de l'intégrale : {resultat}")