# Introduction
Dossier comprend 9 dossiers, il faut les executer un après les autres. Le 
but de ces programmes est de créer un linéaire unique qui regroupe les deux sens. Les deux sens sont rassemblés sauf si les chaussés sont séparé de plus de 20m.
Il faut les executer les unes après les autres. 
# Les fichiers 
1) single road.py séparer le sens 1 du sens 2
2) qchainage.py divise les deux sens en sections et les fait une rotation 
3) extend.py les section font une rotation de 90 degres et allongés
4) line intersections.py création de point d'intersection entre le resultat de l'étape 4 et les deux sens
5) join.py création linéaire des points
6) calculate field.py création d'un champ x, y , xbis, ybis. Les deux derniers sont egale a la moyenne du sens 1 et le sens 2. 
sauf si ils sont séparé de plus de 20m.
7) merge.py fusionne les deux sens 
8) buffer.py créer un zone tampon autour de la route concernés
9) pytable.py renseigne la table attributaire avec les informations contenue dans le titre généré par Prmachine. 
# Installer les fichiers pythons: 
git clone https://github.com/Dunckleosteus/Pygis-.git
# Dans qgis
![image](https://user-images.githubusercontent.com/89072004/166252464-5e6857ec-92d4-43f1-ba31-fd6215ca4cb8.png)
![image](https://user-images.githubusercontent.com/89072004/166252613-079a285e-2e02-4249-b38f-4d40f611d124.png)
# Exemple d'utilisation
## Les fichiers 
![image](https://user-images.githubusercontent.com/89072004/166417067-27eef900-c659-4b6e-bc4e-0e983a77d8bd.png)
On regroupe ces shapefiles par route ici on a dux routes qui suivent l'A6, une qui suit l'A40 et une qui suit l'A31. \
![image](https://user-images.githubusercontent.com/89072004/166417377-afe0e449-fd73-4e1d-b4cf-763bb48304e3.png)
## Extraction des routes concernés 
Pour cette étape il faut un fichier qui recense les routes en France. Faire une extraction par attribut de l'intégralité de L'A6, l'A40 & l'A31.
![image](https://user-images.githubusercontent.com/89072004/166418038-0c276610-40cc-4d9d-95bb-0a7dc7c3a50e.png)
Save selected as: \
Et sauvegarder sous shapefile, j'utilise la projection 2154.
Voici le resultat: 
![image](https://user-images.githubusercontent.com/89072004/166418484-b19c62be-1a0b-4f3c-8c69-8b09f73bef63.png)
## Lancer python 
Ouvrir les fichiers pygis dans la console intégré, il faut noter que les filepaths dans le programme seront a changer: \
![image](https://user-images.githubusercontent.com/89072004/166418753-6dd0ad57-ecfc-40ab-963a-2b30d73fbbd6.png)
### Single_road.py
Cette fonction prend une route en entree et crée un tracé par sens. \
Cliquer sur la route a transformer ensuite lancer le programme avec la petite flece verte. \
![image](https://user-images.githubusercontent.com/89072004/166421712-03827b81-0542-4567-80cc-1559a6a7c7b6.png)
On passe de ce resulat: \
![image](https://user-images.githubusercontent.com/89072004/166422057-54201502-0bdc-4957-89e1-bd28a67d7276.png)
A ce resultat : \
![image](https://user-images.githubusercontent.com/89072004/166422111-44e43d0d-38f2-478f-98a7-f43bb025f2cd.png)
### 


Plugins>python console>editor
