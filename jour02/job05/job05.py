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
query =  "SELECT CONCAT ('La superficie de La Plateforme est de ', SUM(superficie), ' m2') AS resultat FROM etage"
cursor.execute(query)

resultat = cursor.fetchone()[0]
print(resultat)




# Fermer la connexion et cursor
cursor.close()
connexion.close()














