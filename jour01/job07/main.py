import os

# Exécuter la commande mysqldump pour sauvegarder la base de données dans un fichier SQL
os.system('mysqldump -u [root] -p [LaPlateforme] > laplateforme.sql')