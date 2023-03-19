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


#À l’aide d’une requête, calculer la somme des capacités des salles
cursor = connexion.cursor()
query =  "SELECT CONCAT('la capacité de toutes les salles est de : ', SUM(capacite)) AS resultat FROM salles"
cursor.execute(query)


resultat = cursor.fetchone()[0]
print(resultat)



# Fermer la connexion et cursor
cursor.close()
connexion.close()
