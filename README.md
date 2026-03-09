# histogram.py

`histogram.py` est un script d'exploration (EDA - Exploratory Data Analysis) qui affiche des histogrammes des notes pour un cours donné (feature numérique), séparées par maison (Gryffindor, Hufflepuff, Ravenclaw, Slytherin), afin de répondre à la question du sujet : **quel cours a une distribution de scores la plus homogène entre les quatre maisons**.

### Couleurs des maisons

- **Gryffindor** = brown (marron)
- **Hufflepuff** = red (rouge)
- **Ravenclaw** = yellow (jaune)
- **Slytherin** = green (vert)

## Fonctionnement

Le script crée des histogrammes superposés pour chaque cours, avec une barre (histogramme) par maison. 

### Les edges (bords des bins)

Pour chaque cours, le script :
1. Calcule les valeurs **min** et **max** de toutes les notes du cours
2. Divise cet intervalle en **10 bins** (barres) égaux
3. Les **edges** (bords) sont les limites de chaque bin, calculées de manière uniforme entre min et max

Cela garantit que tous les histogrammes d’un même cours utilisent les mêmes bins, ce qui permet une comparaison équitable entre les maisons. Chaque barre représente le nombre d’élèves (fréquence) dont la note se situe dans un intervalle donné. Ainsi, toutes les maisons sont comptées sur les mêmes intervalles (ex. ) ; sans cela, on pourrait avoir une maison sur [250,300] et une autre sur [200,250], ce qui décale les barres et fausse la comparaison.

## Pourquoi c'est utile

Cette visualisation permet d'identifier :
- Les cours **peu discriminants** (distributions très similaires entre maisons)
- Les cours qui **séparent mieux les maisons**

Ces informations permettent de choisir les features pertinentes pour entraîner la régression logistique et décider quel élève devra aller dans quelle maison.

## Entrée / Sortie

### Entrée
- `dataset_train.csv` (le jeu d'entraînement)

### Sortie
- Génère un fichier PNG par cours dans le dossier `histograms/`.
- Les valeurs manquantes (`None`) sont ignorées.

## Exemples de lancement

```bash
python3 histogram.py
```

Ou via le Makefile :

```bash
make histogram
```

# pair_plot

`pair_plot.py` génère une scatter plot matrix (pair plot) du dataset d'entraînement.
La diagonale affiche des histogrammes et le triangle inférieur affiche des scatterplots, colorés par maison, pour aider à choisir les features utiles à la régression logistique. 
(Question du sujet: “From this visualization, what features are you going to use…”.) 



Sigmoid la fonction sert a predire 
la derivé sert a savoir comment lerreur change en fonction du poids (apprendre) sans la derive je ne sais pas dans quel sens bouger theta

La dérivée, c’est la pente.

Si la pente est positive, tu es en train de monter : pour descendre (réduire l’erreur), tu vas dans l’autre sens.
​

Si la pente est négative, tu descends déjà : tu continues dans ce sens.
​

C’est exactement pour ça que la descente de gradient fonctionne : elle suit la pente de l’erreur pour la réduire.

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

# logreg_train

`logreg_train.py` va nous permettre déntrainer notre model one for all pour definir un poid qui va nous permettre de dire si ce nouveau eleves va etre dans cette maison ou dans une autre maison
