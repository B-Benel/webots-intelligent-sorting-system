# 🤖 Webots Vision Sorting Line (YOLOv8)

Ce projet simule un prototype "1rst Try" d'une ligne de tri industrielle automatisée utilisant **Webots** et **YOLOv8**. 
Un Supervisor génère des objets (canettes, bouteilles), un robot de vision les identifie en temps réel, 
et ils sont instantanément téléportés dans leurs bacs respectifs.

## 🚀 Fonctionnement
- **Spawn Dynamique** : Génération aléatoire d'objets sur un tapis roulant.
- <img width="1858" height="668" alt="image" src="https://github.com/user-attachments/assets/46115cc1-dc81-44a4-b7c0-10ce4cdbdb16" />

- **Vision IA** : Détection via YOLOv8 (Ultralytics).
- <img width="1904" height="926" alt="image" src="https://github.com/user-attachments/assets/101829d2-de16-47c4-bab4-a944beed78e3" />

- **Tri Instantané** : Téléportation vers les bacs cibles après détection.
<img width="1899" height="654" alt="image" src="https://github.com/user-attachments/assets/bdfe32b5-6d5c-4993-972e-9449169825f4" />

- **Communication** : Utilisation des Emitters/Receivers Webots.

## 🛠️ Installation

1. **Cloner le projet** :
   ```bash
   git clone [https://github.com/ton-pseudo/webots-vision-sorting-line.git](https://github.com/ton-pseudo/webots-vision-sorting-line.git)
   cd webots-vision-sorting-line
   
Process : 










