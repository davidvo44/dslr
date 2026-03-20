# DSLR - Data Science x Logistic Regression

Projet 42 consistant à recréer un **Choixpeau magique** à l'aide d'une **régression logistique** implémentée en **one-vs-all** (one-vs-rest), sans utiliser de bibliothèque de machine learning.

L'objectif est de :
- explorer un dataset d'élèves de Poudlard,
- visualiser les distributions et les relations entre les matières,
- choisir des features pertinentes,
- entraîner un modèle,
- prédire la maison des élèves du fichier de test.

---

## 1. Objectifs du projet

Ce projet suit les étapes classiques d'un petit pprojet de data science :

1. analyser les données avec un `describe`,
2. visualiser les distributions avec des histogrammes,
3. repérer les corrélations avec des scatter plots et un pair plot,
4. sélectionner des matières pertinentes,
5. entraîner une régression logistique One for all,
6. générer un fichier de prédictions au format demandé.

Le sujet impose également de **ne pas utiliser les fonctions qui font tout le travail à notre place** comme :
- `describe()`
- `mean()`
- `std()`
- `percentile()`
- ou tout équivalent direct venant d'une bibliothèque de data science

Dans ce projet, les statistiques utiles et les calculs principaux sont donc réalisés manuellement.

---

## 2. Technologies utilisées

- Python 3
- `pandas` pour lire les fichiers CSV
- `matplotlib` pour les visualisations
- `click` et `InquirerPy` pour l'interface en ligne de commande
- `alive-progress` pour la barre de progression


## 3. Structure du projet

```text
.
├── describe/
│   ├── describe.py
│   ├── houseStat.py
│   ├── subjectStat.py
│   ├── utilsDescribe.py
│   ├── StatInterface.py
│   └── sheetTemplate.py
├── logregTrain/
│   ├── logreg_train.py
│   ├── normalization.py
│   └── menu_train.py
├── datasets/
│   ├── dataset_train.csv
│   └── dataset_test.csv
├── histogram.py
├── scatter_plot.py
├── pair_plot.py
├── logreg_predict.py
├── stochastic_train.py
├── utils.py
├── Makefile
└── requirements.txt
```

### Rôle des principaux fichiers

- `describe/describe.py`
  - point d'entrée du programme `describe`
- `describe/houseStat.py`
  - calcule des statistiques agrégées par maison
- `describe/subjectStat.py`
  - calcule des statistiques par matière
- `histogram.py`
  - génère des histogrammes par matière et par maison
- `scatter_plot.py`
  - génère des scatter plots entre paires de matières
- `pair_plot.py`
  - génère une matrice de visualisation globale
- `logregTrain/logreg_train.py`
  - entraîne le modèle de régression logistique One for all
- `logreg_predict.py`
  - applique les poids appris sur le dataset de test
- `stochastic_train.py`
  - version bonus avec entraînement stochastique

---

## 4. Installation

Créer l'environnement virtuel et installer les dépendances :

```bash
make
```

Cette commande :
- crée un environnement virtuel `.venv`
- met `pip` à jour
- installe les dépendances depuis `requirements.txt`

---

## 5. Utilisation

### 5.1. Analyse statistique

```bash
make describe
```

ou

```bash
.venv/bin/python -m describe.describe datasets/dataset_train.csv
```

Le programme propose un menu avec deux vues :
- `House Stat`
- `Subject Stat`

### 5.2. Histogrammes

```bash
make histogram
```

ou

```bash
.venv/bin/python -m histogram datasets/dataset_train.csv
```

Le script calcule le cours dont la distribution est la plus homogène entre les quatre maisons, puis génère son histogramme dans :

```text
histograms/best_course.png
```

Le nom du cours sélectionné est également affiché dans le terminal.

### 5.3. Scatter plots

```bash
make scatter_plot
```

ou

```bash
.venv/bin/python -m scatter_plot datasets/dataset_train.csv
```

Le script compare toutes les paires de matières avec la corrélation de Pearson, sélectionne les deux features les plus similaires, puis génère un scatter plot dans :

```text
scatter_plots/scatter_plot.png
```

Les noms des deux matières retenues ainsi que leur corrélation sont affichés dans le terminal.

### 5.4. Pair plot

```bash
make pair_plot
```

ou

```bash
.venv/bin/python -m pair_plot datasets/dataset_train.csv
```

Le résultat est enregistré dans :

```text
pair_plots/pair_plot.png
```

### 5.5. Entraînement du modèle

```bash
make logreg_train
```

ou

```bash
.venv/bin/python -m logregTrain.logreg_train datasets/dataset_train.csv
```

Le programme propose un choix :
- sélection manuelle des matières,
- ou sélection prédéfinie.

L'entraînement génère :
- `datasets/db.csv` pour les poids du modèle,
- `datasets/normalization.csv` pour les moyennes et écarts-types utilisés à la normalisation.

### 5.6. Prédiction

```bash
make logreg_predict
```

ou

```bash
.venv/bin/python -m logreg_predict datasets/dataset_test.csv
```

Le script lit :
- `datasets/db.csv`
- `datasets/normalization.csv`
- `datasets/dataset_test.csv`

Puis il produit le fichier :

```text
datasets/houses.csv
```

avec le format suivant :

```csv
Index,Hogwarts House
0,Gryffindor
1,Hufflepuff
2,Ravenclaw
```

---

## 6. Describe

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

## 7. histogram.py

`histogram.py` est un script d'exploration de données qui répond à la question :

> Which Hogwarts course has a homogeneous score distribution between all four houses?

L'idée est de comparer, pour chaque matière, les résultats moyens des quatre maisons afin de trouver le cours où les maisons ont les scores les plus proches.

### Méthode utilisée

Pour chaque matière :
1. on calcule la moyenne des notes de chaque maison ;
2. on calcule ensuite la moyenne globale de ces 4 moyennes ;
3. on mesure à quel point les moyennes des maisons s'écartent de cette moyenne globale.

Si on note :
- \( \mu_{G,c} \) = moyenne de Gryffindor pour le cours \(c\)
- \( \mu_{H,c} \) = moyenne de Hufflepuff pour le cours \(c\)
- \( \mu_{R,c} \) = moyenne de Ravenclaw pour le cours \(c\)
- \( \mu_{S,c} \) = moyenne de Slytherin pour le cours \(c\)

alors on calcule d'abord :

\[
\mu_c = \frac{\mu_{G,c} + \mu_{H,c} + \mu_{R,c} + \mu_{S,c}}{4}
\]

Puis un score de dispersion :

\[
V_c = \frac{
(\mu_{G,c} - \mu_c)^2 +
(\mu_{H,c} - \mu_c)^2 +
(\mu_{R,c} - \mu_c)^2 +
(\mu_{S,c} - \mu_c)^2
}{4}
\]

Le cours retenu est celui dont \(V_c\) est le plus petit, car cela signifie que les moyennes des quatre maisons sont les plus proches. Cette formule correspond à une variance des moyennes de groupes, donc à une mesure simple de dispersion entre maisons. [web:221][web:222][web:92]

### Visualisation

Une fois le meilleur cours trouvé, le script affiche son histogramme en séparant les notes par maison avec des couleurs différentes.

L'histogramme utilise davantage de `bins` pour obtenir des barres plus fines et donc une lecture plus détaillée de la distribution. Dans Matplotlib, augmenter le nombre de bins rend l'histogramme plus précis visuellement. [web:327][web:328][web:333]

### Pourquoi c'est utile

Cette visualisation permet de voir si les distributions des quatre maisons se chevauchent fortement ou non.  
Un cours homogène est un cours où les maisons ont des profils proches, donc une matière peu discriminante pour la classification. [web:315][web:318]


## 8. scatter_plot.py

Le script `scatter_plot.py` répond à la question :

> What are the two features that are similar?

L'objectif est de trouver les deux matières les plus proches au sens d'une relation linéaire forte, puis d'afficher un nuage de points entre ces deux variables.

### Méthode utilisée

Pour chaque paire de matières \(X\) et \(Y\) :
1. on conserve uniquement les élèves pour lesquels les deux notes existent ;
2. on calcule la moyenne de \(X\) et la moyenne de \(Y\) ;
3. on calcule la corrélation de Pearson.

Si \(x_i\) et \(y_i\) sont les notes d'un élève pour deux matières, alors la corrélation vaut :

\[
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}
{\sqrt{\sum (x_i - \bar{x})^2}\sqrt{\sum (y_i - \bar{y})^2}}
\]

où \( \bar{x} \) et \( \bar{y} \) sont les moyennes des deux matières.

Le coefficient \(r\) est compris entre \(-1\) et \(1\) :
- \(r \approx 1\) : forte corrélation positive ;
- \(r \approx -1\) : forte corrélation négative ;
- \(r \approx 0\) : faible relation linéaire.

Le script compare toutes les paires de matières et conserve celle dont la valeur absolue \(|r|\) est la plus grande. La corrélation de Pearson est une mesure standard de la force d'une relation linéaire entre deux variables numériques. [web:256][web:266][web:267]

### Visualisation

Une fois la meilleure paire trouvée, le script génère un scatter plot coloré par maison.  
Le nuage de points permet de vérifier visuellement si les deux matières évoluent ensemble et si les maisons occupent des zones différentes ou non. Les scatter plots sont utilisés précisément pour visualiser la direction, la forme et la force d'une relation entre deux variables. [web:265][web:267][web:292]

### Pourquoi c'est utile

Deux matières très corrélées apportent souvent une information redondante au modèle.  
Cette étape aide donc à éviter de sélectionner plusieurs features qui disent presque la même chose.

### Pair plot

Le script `pair_plot.py` sert à obtenir une vue d'ensemble des relations entre toutes les matières.

Il permet d'identifier :
- les matières qui séparent bien les maisons,
- celles qui semblent redondantes,
- et celles qui sont intéressantes à garder pour l'entraînement.

---
## 9. Régression logistique

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

## 10. Gestion des valeurs manquantes

Le dataset contient des valeurs absentes dans certaines matières.

Dans ce projet :
- les statistiques ignorent les valeurs manquantes,
- les visualisations n'utilisent pas les points invalides,
- l'entraînement ne conserve que les lignes exploitables pour les matières sélectionnées,
- la prédiction ignore les matières non disponibles pour un élève.

Cette gestion permet d'éviter de fausser les calculs.

---

## 11. Fichiers générés

Selon les scripts exécutés, le projet génère :

- `histograms/`
- `scatter_plots/`
- `pair_plots/`
- `datasets/db.csv`
- `datasets/normalization.csv`
- `datasets/houses.csv`

---

## 12. Bonus

Le fichier `stochastic_train.py` propose une version bonus avec une variante de la descente de gradient :
- **stochastic gradient descent**

Cette approche met à jour les poids à partir d'un seul élève à la fois, contrairement à la version obligatoire qui calcule son gradient sur l'ensemble du batch.

---

## 13. Résumé

Ce projet implémente un pipeline complet de machine learning simple, sans bibliothèque d'apprentissage automatique :

- exploration statistique,
- visualisation des données,
- sélection de features,
- normalisation,
- entraînement d'une régression logistique one-vs-all,
- génération d'un fichier final de prédictions.

Il permet de comprendre concrètement les bases de la data science et de la classification supervisée sur un cas multiclasses.


# Lien Utile

https://mrmint.fr/gradient-descent-algorithm
https://www.geeksforgeeks.org/machine-learning/derivative-of-the-sigmoid-function/

https://mrmint.fr/logistic-regression-machine-learning-introduction-simple

