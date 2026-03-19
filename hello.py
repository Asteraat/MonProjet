# Simulation d'une IA Azure Cognitive Services
confiance = 0.85

print("--- Analyse d'image IA ---")
if confiance > 0.80:
    print("Résultat : L'IA est sûre qu'il s'agit d'un chat !")
elif confiance<81 & confiance>65:
    print("Résultat : L’IA hesite encore")
else:
    print("Résultat : Ce n est probablement pas un chat")

# Exercice : Change la valeur de 'confiance' sur ton PC 
# et fais un 'git pull' sur ton tel pour voir le résultat changer !

