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

