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
    Des qu'on a trouve W et B, on peut appliquer la fonction:
        Y = W * x + B;
        puis:
            S(Y) = 1 / (1 + e^-Y);
        Trouve la probabilite de trouver vers le cote 1, ou 0;

Etape 4:
    L’algorithme : One vs All
    Principe: calculer S(Y) pour:
        Gryffindor : 1, Other 0;
        Ravenclaw : 1, Other 0;
        Slytherin : 1, Other 0;
        Hufflepuff : 1, Other 0;
    Appliquer a chaque Matiere pour plus de Precision;


DB a Stocker:

    House,Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying
    RavenclawBias,0,0,0,0,0,0,0,0,0,0,0,0
    RavenclawWeight,0,0,0,0,0,0,0,0,0,0,0,0
    GryffundorBias,0,0,0,0,0,0,0,0,0,0,0,0
    GryffundorWeight,0,0,0,0,0,0,0,0,0,0,0,0
    SlytherinBiai,0,0,0,0,0,0,0,0,0,0,0,0
    SlytherinWeight,0,0,0,0,0,0,0,0,0,0,0,0
    HufflepuffBias,0,0,0,0,0,0,0,0,0,0,0,0
    HufflepuffWeight,0,0,0,0,0,0,0,0,0,0,0,0



# Lien Utile

https://mrmint.fr/gradient-descent-algorithm

https://www.geeksforgeeks.org/machine-learning/derivative-of-the-sigmoid-function/

