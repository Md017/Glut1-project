# Analyse des trajectoires de dynamique moléculaires de la protéine GLUT1 transporteuse de glucose

## Obejctifs
* Identifier les ions chlores qui sont en interaction avec les différents sites de liaisons du glucose
* déterminer l'influence des interactions ions Cl-protein sur le réseau de la protéine
* Visualer le réseau protéique 
## Materiels et Méthodes 
Ce projet a neccessité l'utilisation des outils suivants:
* Gromacs
* Python 
* gRINN ( get Residues Interaction Network ) un logiciel d'analyse de réseau proteique 
* Pymol et VMD pour la visualisation 
La méthode utilisée est la suivante:
* Calculer avec Gromacs les coordonnées des ions Cl et celles des centre de masse des differents sites de liaison du glucose
* Calculer la distance( en nm) entre ions et chlore et chaque site pour chaque frame à l'aide de la commande gmx pairdist
* identifier à l'aide d'un script python les chlores qui sont à une distance inférieure à 1 A°, 2 A° ou 3.6 A° des sites. 
* Représenter les distances en fonction du numéro de frames pour chaque chlore identifié 
* Récupérer les fragments de trajectoires pour chaque chlore à l'aide de la commande gmx trjconv 
* Lancer pour chacune de ces trajectoires une simulation sur gRINN 
* Enfin analyser les résultats de gRINN 
# Dossiers du projets
Les données de ce projet sont réparties dans quatre dossiers principaux :
## le dossier GROMACS_simulations-folder
Ce dossier comporte 5 sous dossier dont:
* com_coord_for_sites : contient les coordonnées des centre de masses pour differents sites
* coordonnes_without-COM : contient les coordonnées de chaque atoms d'un site donnée
* index file: contient le fichier index dans lequel nous avons créé des groupes d'atomes qui composent chaque site
* main file : contient les fichiers necessaires pour nos simulations gromacs dont wt_start.pdb la structure protéique, wt_rep.tpr le fichier de topologie et wt_rep-100ps.xtc la trajectoire 
* pairdist : contient les fichiers de distances Cl-site et le script python pour identifier les chlores et reprénter les distances
* script_folder contient essnetiellement les script Gromacs
* simple_distance est un dossier qui contient quelque fichier de test
* 


