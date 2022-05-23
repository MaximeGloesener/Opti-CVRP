### Explication du problème
Un marchand de poisson veut optimiser sa livraison de poisson à tous ses clients.   
Sur la carte, on peut identifier les différents clients par des points bleus et les points rouges correspondent à des endroits où le marchand de poisson peut installer son dépôt.   
Chaque client a besoin d'une quantité de poissons x et la camionnette du marchand de poisson peut livrer au maximum un poids y de poisson. 
Il faut résoudre 2 problèmes :
- identifier pour un dépôt, le chemin optimal de livraison, c'est-à-dire, celui qui va minimiser la distance parcourue, tout en respectant la contrainte de poids que la camionnette ne peut pas dépasser
- identifier le nombre de dépôts et l'endroit idéal des dépôts, c'est-à-dire les dépôts qui permettront au marchand de poisson de parcourir une distance minimale pour faire ses livraisons 



NB: Dans le cadre de ce mini-projet, l'objectif était de tester le solver docplex. Les données sont donc générées aléatoirement en fonction des paramètres rentrés par l'utilisateur.
Dans un cas réel, il suffirait de rentrer les vraies positions des clients et des dépôts potentiels, les quantités demandées par chaque client et la capacité de la camionnette du marchand.


### Comment tester le programme ?
1) Rentrer les paramètres
- capacité de la camionnette du marchand de poisson
- nombre de clients
- nombre de dépôts possibles
- bornes inférieure/supérieure des demandes des clients
2) Lancer le solver 
3) Visualiser les résultats


### Monitoring
Le notebook nommé monitoring est présent car il permet de montrer comment monitorer un modèle docplex. Cela nous permet de visualiser l'évolution du gap et de la fonction objective au cours du temps et de l'exploration des différents noeuds. (Méthode utilisée = Mixed integer programming -> méthode exacte qui utilise un branch and cut)
