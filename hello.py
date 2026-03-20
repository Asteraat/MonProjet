import time
# Simulation d'une IA Azure Cognitive Services

# On boucle "pour toujours" jusqu'à ce qu'on décide de sortir
while True:
    confiance = float(input("Valeur de confiance (0 à 1) : "))
    
    if 0 <= confiance <= 1:
        break # <--- On sort de la boucle ici car la valeur est BONNE
    
    print("Mauvaise valeur, réessayez...")
    time.sleep(1)

# Le reste du code s'exécute après le break
print("--- Analyse d'image IA ---")

if confiance > 0.80:
    print("Résultat : L'IA est sûre qu'il s'agit d'un chat !")
elif confiance<0.81 and  confiance>0.65:
    print("Résultat : L’IA hesite encore")
else:
    print("Résultat : Ce n est probablement pas un chat")

# Exercice : Change la valeur de 'confiance' sur ton PC 
# et fais un 'git pull' sur ton tel pour voir le résultat changer !

data = open("data.txt" , "r")
print("contenu du fichier: \n" + data.read())
