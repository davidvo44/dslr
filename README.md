# histogram.py

## 📊 But

`histogram.py` est un script d'exploration (EDA - Exploratory Data Analysis) qui affiche des histogrammes des notes pour un cours donné (feature numérique), séparées par maison (Gryffindor, Hufflepuff, Ravenclaw, Slytherin), afin de répondre à la question du sujet : **quel cours a une distribution de scores la plus homogène entre les quatre maisons**.

### 🎨 Couleurs des maisons

- **Gryffindor** = brown (marron)
- **Hufflepuff** = red (rouge)
- **Ravenclaw** = yellow (jaune)
- **Slytherin** = green (vert)

## ⚙️ Fonctionnement

Le script crée des histogrammes superposés pour chaque cours, avec une barre (histogramme) par maison. 

### Les edges (bords des bins)

Pour chaque cours, le script :
1. Calcule les valeurs **min** et **max** de toutes les notes du cours
2. Divise cet intervalle en **10 bins** (barres) égaux
3. Les **edges** (bords) sont les limites de chaque bin, calculées de manière uniforme entre min et max

Cela garantit que tous les histogrammes d’un même cours utilisent les mêmes bins, ce qui permet une comparaison équitable entre les maisons. Chaque barre représente le nombre d’élèves (fréquence) dont la note se situe dans un intervalle donné. Ainsi, toutes les maisons sont comptées sur les mêmes intervalles (ex. ) ; sans cela, on pourrait avoir une maison sur [250,300] et une autre sur [200,250], ce qui décale les barres et fausse la comparaison.

## 💡 Pourquoi c'est utile

Cette visualisation permet d'identifier :
- Les cours **peu discriminants** (distributions très similaires entre maisons)
- Les cours qui **séparent mieux les maisons**

Ces informations permettent de choisir les features pertinentes pour entraîner la régression logistique et décider quel élève devra aller dans quelle maison.

## 📥 Entrée / Sortie

### Entrée
- `dataset_train.csv` (le jeu d'entraînement)

### Sortie
- Génère un fichier PNG par cours dans le dossier `histograms/`.
- Les valeurs manquantes (`None`) sont ignorées.

## 🚀 Exemples de lancement

```bash
python3 histogram.py
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

