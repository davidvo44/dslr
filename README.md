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


# Log Train

Etape 1: 
    Transformer Maison en nombre en appliquant la tech du One For All:
        ex: Gryffundor = 1;
        Hufflepuff = Slytherin = Ravenclaw = 0;

Etape 2:
Utilisation du Machine Learning
Faire recherche du Poids W et du Biais B de la fonction Logistic Regression: z = w * x + b:
Pour Cela, entrainer le modele;
Repeter l'etape jusqu'a difference minime

Pour cela:
    
∂L / ∂w ​= 1/n * ​∑( y^​ − y )⋅x;
w= w − α * ∂L / ∂w;

∂L / ∂b ​= 1/n * ​∑( y^​−y)
b = b − α * ∂L / ∂b

Repeter l'etape jusqu'a difference faible entre les deux W et les deux B


Etape 3?:
L’algorithme : One vs All


# Lien Utile

https://mrmint.fr/gradient-descent-algorithm
https://www.geeksforgeeks.org/machine-learning/derivative-of-the-sigmoid-function/

https://mrmint.fr/logistic-regression-machine-learning-introduction-simple