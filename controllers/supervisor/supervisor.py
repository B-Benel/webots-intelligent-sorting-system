from controller import Supervisor
import random

supervisor = Supervisor()
timestep = int(supervisor.getBasicTimeStep())

receiver = supervisor.getDevice("receiver")
receiver.enable(timestep)

root = supervisor.getRoot()
children = root.getField("children")

# --- PARAMÈTRES (Alignés sur ton fichier .wbt fixe) ---
# Spawn au début du tapis (X négatif)
SPAWN_POS = [-0.6, 0, 0.2] 

# Bacs à la fin du tapis (X = 0.8 selon ton .wbt)
# J'ai mis Z=0.3 pour que ça tombe "dans" le bac
BIN_WATER = [ 0.8, -0.15, 0.3] 
BIN_SODA  = [ 0.8,  0.20, 0.3] 

current_obj_node = None

def spawn_object():
    global current_obj_node
    obj_type = random.choice(["WaterBottle", "Can"])
    
    # IMPORTANT : J'ai remis le boundingObject Box pour que 
    # le capteur de distance puisse "voir" l'objet (le rayon rebondit dessus)
    node_str = f"""
    DEF TARGET Solid {{
      translation {SPAWN_POS[0]} {SPAWN_POS[1]} {SPAWN_POS[2]}
      children [ DEF ITEM {obj_type} {{ }} ]
      name "{obj_type}"
      boundingObject Box {{ size 0.08 0.2 0.08 }}
      physics Physics {{ mass 0.2 }}
    }}
    """
    children.importMFNodeFromString(-1, node_str)
    current_obj_node = supervisor.getFromDef("TARGET")

# 1. On lance la première bouteille
spawn_object()

while supervisor.step(timestep) != -1:
    # 2. On attend sagement qu'un message arrive
    if receiver.getQueueLength() > 0:
        msg = receiver.getString()
        receiver.nextPacket()
        
        if current_obj_node:
            # 3. Téléportation INSTANTANÉE vers le bon bac
            if msg == "WATER":
                current_obj_node.getField("translation").setSFVec3f(BIN_WATER)
            else:
                current_obj_node.getField("translation").setSFVec3f(BIN_SODA)
            
            # 4. On attend 1 seconde pour voir l'objet dans le bac
            supervisor.step(1000) 
            
            # 5. On supprime l'ancienne bouteille
            current_obj_node.remove()
            current_obj_node = None 
            
            # 6. Et SEULEMENT MAINTENANT, on en fait apparaître une nouvelle
            spawn_object()
