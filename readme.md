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
Plugins>python console>editor
