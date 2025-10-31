from random import randint
import matplotlib.pyplot as plt

def simule_cpp(n: int) -> int:
    """
    Simule le problème du collectionneur de coupons pour n coupons.
    Retourne le nombre de tirages nécessaires pour obtenir les n coupons différents.
    """
    nb_tirages = 0
    coupon = set()
    while len(coupon) < n:
        coupon.add(randint(0, n-1))
        nb_tirages += 1
    return nb_tirages


def simule_cpp_moyenne_et_dispertion(n_tests: int = 100, n_max: int = 200):
    """
    Pour chaque n de 1 à n_max :
    - fait n_tests simulations de simule_cpp(n)
    - retourne une liste contenant toutes les valeurs simulées pour chaque n
    """
    liste_groupes = []
    for n in range(1, n_max + 1):
        sous_liste = [simule_cpp(n) for _ in range(n_tests)]
        liste_groupes.append(sous_liste)
    return liste_groupes


def affiche_moyenne(data: list, output_file: str = "resultat_cpp.png"):
    """
    Affiche tous les points (en bleu) et la moyenne (en rouge sous forme de ligne continue).
    Sauvegarde le graphique dans un fichier image.
    """
    plt.figure(figsize=(12, 6))
    tableau_moyenne = []
    for i, sous_liste in enumerate(data, start=1):
        plt.scatter([i] * len(sous_liste), sous_liste, color='blue', alpha=0.3, s=8)

    moyennes = [sum(s) / len(s) for s in data]
    tableau_moyenne.append(moyennes)
    plt.plot(range(1, len(moyennes) + 1), moyennes, color='red', linewidth=2, label="Moyenne")

    plt.title("Simulation du Collectionneur de Coupons\nPoints (bleu) et Moyenne (ligne rouge)")
    plt.xlabel("n (nombre de coupons différents)")
    plt.ylabel("Nombre moyen de tirages")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(output_file, dpi=300)
    plt.close()
    print(f"Graphique sauvegardé sous : {output_file}")
    return tableau_moyenne
