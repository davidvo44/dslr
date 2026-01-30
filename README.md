# histogram.py

## 📊 But

`histogram.py` est un script d'exploration (EDA - Exploratory Data Analysis) qui affiche des histogrammes des notes pour un cours donné (feature numérique), séparées par maison (Gryffindor, Hufflepuff, Ravenclaw, Slytherin), afin de répondre à la question du sujet : **quel cours a une distribution de scores la plus homogène entre les quatre maisons**.

### 🎨 Couleurs des maisons

- **Gryffindor** = brown (marron)
- **Hufflepuff** = red (rouge)
- **Ravenclaw** = yellow (jaune)
- **Slytherin** = green (vert)

## 💡 Pourquoi c'est utile

Cette visualisation permet d'identifier :
- Les cours **peu discriminants** (distributions très similaires entre maisons)
- Les cours qui **séparent mieux les maisons**

Ces informations permettent de choisir les features pertinentes pour entraîner la régression logistique et décider quel élève devra aller dans quelle maison.

## 📥 Entrée / Sortie

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

