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

cursor = connexion.cursor()
query =  "SELECT * FROM employes WHERE salaire>3000.00"

query1 = ("SELECT employes.nom, employes.prenom, employes.salaire, services.nom AS service "
          "FROM employes "
          "JOIN services ON employes.id_service = services.id;")

cursor.execute(query)
for row in cursor:
  print(row)
  
cursor.execute(query1)
for row in cursor:
  print(row)




# Fermer la connexion et cursor
cursor.close()
connexion.close()