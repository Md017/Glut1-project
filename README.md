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
## Dossiers du projets
Les données de ce projet sont réparties dans quatre dossiers principaux :
## GROMACS_simulations-folder
Ce dossier comporte 5 sous dossier dont:
* com_coord_for_sites : contient les coordonnées des centre de masses pour differents sites
* coordonnes_without-COM : contient les coordonnées de chaque atoms d'un site donnée
* index file: contient le fichier index dans lequel nous avons créé des groupes d'atomes qui composent chaque site
* main file : contient les fichiers necessaires pour nos simulations gromacs dont wt_start.pdb la structure protéique, wt_rep.tpr le fichier de topologie et wt_rep-100ps.xtc la trajectoire 
* pairdist : contient les fichiers de distances Cl-site et le script python plot_distances.py pour identifier les chlores et reprénter les distances
Le script python permet de:
  - d'identifier les chlores par leurs ID et ainsi que les frames correspondantes
  - afficher ces information
  - Visualiser graphiquement les différentes distances pour chaque chlore 
* script_folder contient essnetiellement les script Gromacs
* simple_distance est un dossier qui contient quelque fichier de test
## fragments_trajectoires_pour_chaque_chlore
ce dossier contient les fraguement de trajectoires que l'on a extrait pour chaque ions chlore identifiés ainsi que les fichiers mywt_rep_dry.tpr et glut1+glc_in_bilayer_new.top que l'on a créé en modifiant les origrinaux( enlever tous les atoms non protéiques) pour lancer la simulation sur gRINN
## gRinn_results 
Ce dossier contient les résulats obtenu de gRINN pour chaque ions chlore identifié et comporte 7 sous-dossier dont les 6 contiennent pour chacun les résultats pour un ion donné. 
le dernier dossier csv_files contient les fichiers csv conentant des informations sur le réseau de la protéine pour chaque ion chlore ainsi qu'un script network_analysis.ipyp qui permet de :
* visualiser les données métriques issues des résultats network analysis de gRINN
* Afficher le Top n des résidues avec les valeurs de BC et/ou de CC les plus élevées pour chaque fragment de trajectoire à l'aide de la fonction top_n_highest_BC_AND_CC(data, n) et de les visualiser graphiquement à l'aide plot_bar(data, title, image_title)
* faire pareil pour chaque site 
## Comment visualiser les données ?
Il suffit de télécharger d'abord le dossier. 
Pour la visualisation de l'ensemble des résultats des simulations sur gRINN, il faut:
1. Télécharger gRINN à partir du site https://grinn.readthedocs.io/en/latest/download.html en ayant préalablement téléchargé Gromacs si vous ne l'avez pas
2. Ouvrir un terminal dans le dossier grINN que vous avez téléchargé et décompressé, taper ./grinn puis  cliquer sur View results une fois lancé
3. selectionner le dossier gRinn_results
4. choisir un des dossiers nommés du style ClXXX_siteN
Pour visualiser les données métriques du réseau, aller dans le dossier csv_files, ouvrir le fichier network_analysis.ipyp et enfin lancer vos simulations selon le site que vous voulez visualiser.






