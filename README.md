# Webots Automated Sorting System

Ce projet présente une preuve de concept (PoC) pour une ligne de tri industrielle automatisée intégrée dans l'environnement de simulation **Webots**. Le système repose sur l'architecture de détection en temps réel **YOLOv26** pour l'identification et la classification d'objets en mouvement.

## Architecture du Système

Le processus opérationnel est structuré autour d'une boucle de contrôle fermée impliquant trois composants principaux : la génération physique, la perception artificielle et l'actionneur logique.

### 1. Génération et Flux de Matériaux (Spawn Dynamique)

Le contrôleur `Supervisor` initialise la simulation en instanciant des objets (`WaterBottle` ou `Can`) de manière stochastique à l'origine du convoyeur. L'objet est soumis aux lois de la physique rigide (gravité et friction), lui permettant d'être entraîné par le tapis roulant vers la zone de détection.

<img width="1858" height="668" alt="image" src="https://github.com/user-attachments/assets/46115cc1-dc81-44a4-b7c0-10ce4cdbdb16" />

### 2. Perception et Analyse (Vision par Ordinateur)

Lorsqu'un objet pénètre dans le champ d'action du capteur de proximité (`DistanceSensor`), le sous-système de vision est activé :

* **Acquisition** : La caméra haute résolution capture une trame du flux vidéo.
* **Inférence** : Le modèle YOLOv26 traite l'image pour extraire les caractéristiques morphologiques et assigner une classe de probabilité. (Object Detection mais on peut le faire via Image classification ...)
* **Communication** : Le résultat (Water ou Soda) est encapsulé dans un paquet de données transmis via le protocole `Emitter/Receiver`.

<img width="1858" height="668" alt="Sans titre" src="https://github.com/user-attachments/assets/8edbb2f0-18d2-4b05-a75b-f6d001ea5bf9" />

### 3. Logique de Tri et Réinitialisation (Actionnement)

Dès réception du signal, le `Supervisor` exécute une translation instantanée des vecteurs de position de l'objet vers les bacs de collecte prédéfinis.

* **Validation** : L'objet est maintenu dans le bac durant un intervalle défini pour confirmer la réussite du tri.
* **Cycle** : Le nœud de l'objet est supprimé de l'arbre de scène avant qu'un nouveau cycle de génération ne soit amorcé, garantissant la pérennité des ressources de calcul de la simulation.

<img width="1858" height="668" alt="image" src="https://github.com/user-attachments/assets/bdfe32b5-6d5c-4993-972e-9449169825f4" />


## 🛠️ Installation

### 1. Environnement Python

Assurez-vous d'utiliser **Python 3.9 ou 3.10**.  
Installez les dépendances nécessaires via le terminal :

```powershell
pip install -r requirements.txt

### 2. Mise en place sur Webots
2.1 Ouvrir le monde
Lancez Webots et ouvrez le fichier présent dans worlds/sorting_line.wbt.

2.2 Installer les contrôleurs
Par défaut, un projet Webots contient un dossier controllers.
Remplacez le dossier controllers de votre projet par celui fourni dans ce dépôt Git.

2.3 Ajouter le modèle IA
Copiez le dossier models (contenant le fichier yolo26n.pt) depuis ce dépôt et collez-le à la racine de votre répertoire de projet Webots.

📦 Structure du répertoire
webots-vision-sorting-line/
├── controllers/      # Dossier à remplacer dans votre projet Webots
├── models/           # Contient le modèle YOLO (yolo26n.pt)
├── worlds/           # Fichier monde (.wbt)
├── requirements.txt  # Dépendances Python
└── README.md
Et voilà ! Vous êtes prêt·e à lancer la simulation.





