# histogram.py

`histogram.py` est un script d'exploration (EDA - Exploratory Data Analysis) qui affiche des histogrammes des notes pour un cours donné (feature numérique), séparées par maison (Gryffindor, Hufflepuff, Ravenclaw, Slytherin), afin de répondre à la question du sujet : **quel cours a une distribution de scores la plus homogène entre les quatre maisons**.

### Couleurs des maisons

- **Gryffindor** = brown (marron)
- **Hufflepuff** = red (rouge)
- **Ravenclaw** = yellow (jaune)
- **Slytherin** = green (vert)

## Pourquoi c'est utile

Cette visualisation permet d'identifier :
- Les cours **peu discriminants** (distributions très similaires entre maisons)
- Les cours qui **séparent mieux les maisons**

Ces informations permettent de choisir les features pertinentes pour entraîner la régression logistique et décider quel élève devra aller dans quelle maison.

## Entrée / Sortie

### Entrée
- `dataset_train.csv` (le jeu d'entraînement)

### Sortie
- Une fenêtre de plot (matplotlib) avec l'histogramme comparatif par maison
- Le script ignore les valeurs manquantes pour ne pas biaiser la distribution

## 🚀 Exemples de lancement

```bash
python histogram.py datasets/dataset_train.csv
```

```bash
python histogram.py datasets/dataset_train.csv "Astronomy"
```

Ou via le Makefile :

```bash
make histogram
```
---

# Describe

describe.py génère un tableau de statistiques résumant les notes des élèves de Hogwarts, organisées soit par maison, soit par matière. L’analyse s’appuie sur plusieurs indicateurs clés pour décrire la distribution des notes:  

- **Count** : Nombre d'élèves/notes  
- **Mean** : Moyenne des notes  
- **Std** : Écart-type  
- **Min / Max** : Note minimum / maximum  
- **25%, 50%, 75%** : Quartiles (notes aux pourcentages indiqués)

#### Deux choix de tableau disponible: 
- La premiere permet de comparer les stats des notes en fonctions de la maison
- Le second met en comparaison les stats en fonctions des matieres.

### Observation du tableau de maison

#### Taille des échantillons (Count)

- **Hufflepuff** a le plus grand nombre d’élèves.  
- **Slytherin** est le plus petit échantillon, donc ses statistiques peuvent être légèrement moins stables.

#### Moyenne (Mean)

- En moyenne, les valeurs de **Hufflepuff** sont légèrement plus grandes que celles des autres maisons.  
- Les moyennes des autres maisons sont relativement proches (~3800–3880).

#### Dispersion (Std)

- **Ravenclaw** a la plus grande dispersion, donc les notes sont très écartées autour de la moyenne.  
- **Hufflepuff** et **Gryffindor** sont plus concentrées.

#### Étendue des notes (Min / Max)

- **Ravenclaw** présente des valeurs négatives extrêmes, ce qui explique l’écart-type élevé.  
- **Hufflepuff** et **Slytherin** ont des valeurs minimales proches de zéro → les scores négatifs sont rares.  
- **Gryffindor** a une étendue plus petite.


### Conclusion

- **Hufflepuff** : moyenne la plus élevée, distribution concentrée, valeurs min > 0 → élèves avec scores plutôt élevés et homogènes.  
- **Ravenclaw** : grande variabilité, valeurs négatives → quelques élèves très faibles et quelques très forts.  
- **Slytherin** : moyenne faible, mais étendue grande, distribution centrée.  
- **Gryffindor** : moyenne intermédiaire, peu de dispersion → valeurs globalement stables.

---
# pair_plot

`pair_plot.py` génère une scatter plot matrix (pair plot) du dataset d'entraînement.
La diagonale affiche des histogrammes et le triangle inférieur affiche des scatterplots, colorés par maison, pour aider à choisir les features utiles à la régression logistique. 
(Question du sujet: “From this visualization, what features are you going to use…”.) 

# Sigmoïde & Dérivée

Sigmoid : la fonction sert à prédire la probabilité h = σ(θᵀx) ∈.
La dérivée sert à savoir comment l'erreur change en fonction du poids (apprendre). Sans la dérivée, je ne sais pas dans quel sens bouger theta.

La dérivée, c'est la pente.

Si la pente est positive, tu es en train de monter : pour descendre (réduire l'erreur), tu vas dans l'autre sens.

Si la pente est négative, tu descends déjà : tu continues dans ce sens.

C'est exactement pour ça que la descente de gradient fonctionne : elle suit la pente de l'erreur pour la réduire.

exp(x) (exponentielle)
- exp(x) = e^x.
- Elle sert à modéliser une croissance/décroissance continue et c’est la brique qui permet
  à la sigmoïde de transformer un score en probabilité.
- Sans bibliothèque, on calcule exp(x) avec la série de Taylor :
  exp(x) ≈ 1 + x + x^2/2! + x^3/3! + x^4/4! + ...
  (plus on ajoute de termes, plus c’est précis).

Sigmoïde
- La sigmoïde transforme un score z (n’importe quel réel) en une valeur entre 0 et 1 :
  sigmoid(z) = 1 / (1 + exp(-z))
- Interprétation :
  z très positif  -> sigmoid(z) proche de 1
  z = 0           -> sigmoid(z) = 0.5
  z très négatif  -> sigmoid(z) proche de 0
- Dans la régression logistique, z = theta^T x (somme des poids * features).

# Log Train

L’algorithme : One vs All

`logreg_train.py` va nous permettre d'entraîner notre modèle **one-vs-all** pour définir un **poids** (θ) qui va nous permettre de dire si ce nouvel élève va être dans cette maison ou dans une autre. Pour cela, et pour **chaque maison**, nous allons définir `theta[house] = [0.0, 0.0, 0.0, 0.0, 0.0]` en choisissant 4 matières que nous avons trouvées pertinentes grâce aux deux derniers programmes qui nous permettent de visualiser les différences entre maisons.

Ensuite, grâce à différentes formules telles que la fonction **sigmoid** , **score_lineaire** et le **gradient descent**

L'algorithme One-vs-All
1. `theta[house] = [0.0, 0.0, 0.0, 0.0, 0.0]` (4 features pertinentes)
2. **score_lineaire** z = θᵀ × x  chaque feature × son poids
3. **sigmoïde** : σ(z) = 1/(1+e^{-z}) → transforme score en proba [0,1]
4. **gradient descent** θ ← θ - α × (1/m) × Σᵢ eᵢ × xᵢⱼ cest le poid - le learning rate * (1/le nombre d'eleves) * la somme de chaque erreurs * le poids 

 on obtient un θ optimise par maison qui va permettre au prochain programme `logreg_predict` de placer chaque élève dans la maison correspondante. Nous aurons par exemple `theta["Gryffindor"] = [-1.1489, 3.9738, -6.8656, 15.9071, -13.0446]`. En lecture, le biais à -1.148 permet de voir que le programme devrait marcher correctement vu que chaque élève qui va être testé a **75% de chance de ne pas correspondre** à la maison Gryffindor, donc le biais sera négatif.



# Lien Utile

https://mrmint.fr/gradient-descent-algorithm
https://www.geeksforgeeks.org/machine-learning/derivative-of-the-sigmoid-function/

https://mrmint.fr/logistic-regression-machine-learning-introduction-simple




