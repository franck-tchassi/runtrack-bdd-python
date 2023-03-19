import mysql.connector

# Créer une connexion à la base de données
connexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12Abcdef@",
  database="LaPlateforme"
)

# Vérifier si la connexion est réussie
if connexion.is_connected():
  print("Connexion réussie à la base de données 'LaPlateforme'")
else:
  print("La connexion à la base de données 'LaPlateforme' a échoué")

#récupère tous les noms et les capacités de la table “salles”
cursor = connexion.cursor()
query =  "SELECT nom, capacite FROM salles"
cursor.execute(query)
for row in cursor:
  print(row)



# Fermer la connexion et cursor
cursor.close()
connexion.close()