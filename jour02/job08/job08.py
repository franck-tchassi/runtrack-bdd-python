import mysql.connector

connexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12Abcdef@",
    database = "zoo"
)

if connexion.is_connected:
    print("connexion succefull on DATABASE")
else:
   print("connexion failled on your DATABASE")

cursor = connexion.cursor()
#cursor.execute('''CREATE TABLE animal
#                  (id INT AUTO_INCREMENT PRIMARY KEY,
#                   nom VARCHAR(255) NOT NULL,
#                  race VARCHAR(255) NOT NULL,
#                  id_cage INT NOT NULL,
#                   date_naissance DATE NOT NULL,
#                   pays_origine VARCHAR(255) NOT NULL) ''')


#cursor.execute('''CREATE TABLE cage
#                  (id INT AUTO_INCREMENT PRIMARY KEY,
#                   nb_animaux INT NOT NULL,
#                   superficie FLOAT NOT NULL,
#                   capacite_max INT NOT NULL) ''') 




#                 fonction qui ajoute les animaux et cage 
def ajoute_animaux():
    nom = input("nom de l'animal:")
    race = input("race de l'animal:")
    id_cage = input("id_cage de l'animal:")
    date_naissance = input("date_naissance de l'animal yyyy/mm/dd:")
    pays_origine = input("pays origine de l'animal:")

    #cursor2 = connexion.cursor()
    sql = "INSERT INTO animal(nom, race, id_cage, date_naissance, pays_origine) VALUE(%s, %s, %s, %s, %s)"
    val = (nom, race, id_cage, date_naissance, pays_origine)
    cursor.execute(sql, val)

    connexion.commit()
    print(cursor.rowcount, "animal ajouté.")



def ajoute_cage():
    nb_animaux = input("nombres animaux:")
    superficie = input("superficie de l'animal:")
    capacite_max = input("capacite_max de l'animal:")

    #cursor3 = connexion.cursor()
    sql = "INSERT INTO cage(nb_animaux, superficie, capacite_max) VALUE(%s, %s, %s)"
    val = (nb_animaux, superficie, capacite_max)
    cursor.execute(sql, val)

    connexion.commit()
    print(cursor.rowcount, "cage ajouté.")


#                    fonction qui supprimer les animaux et les cage 
def supprimer_animaux(id):
    sql = "DELETE FROM animal WHERE id=%s"
    val = (id)
    cursor.execute(sql, val)

    connexion.commit()
    print(cursor.rowcount, "animal supprimé.")
    


def supprimer_cage(id):
    sql = "DELETE FROM cage WHERE id=%s"
    val = [id]
    cursor.execute(sql, val)

    connexion.commit()
    print(cursor.rowcount, "cage supprimé.")


#                    fonction qui modifie les animaux et les cages
def modifier_animaux(id, nom, race, id_cage, date_naissance, pays_origine):
    sql = "UPDATE animaux SET nom=%s race=%s id_cage=%s date_naissance=%s pays_origine=%s WHERE id=%s"
    val= (nom, race, id_cage, date_naissance, pays_origine, id)
    cursor.execute(sql, val)

    connexion.commit()
    print(cursor.rowcount, "animal modifier.")

    

def modifier_cage(id, nb_animaux, superficie, capacite_max):
    sql = "UPDATE animaux SET nb_animaux=%s superficie=%s capacite_max=%s  WHERE id=%s"
    val= (nb_animaux, superficie, capacite_max, id)
    cursor.execute(sql, val)

    connexion.commit()
    print(cursor.rowcount, "cage modifier.")

# animaux present dans le zoo
sql = "SELECT nom FROM animal"
cursor.execute(sql)
for row in cursor:
  print(row)
# liste animaux presants dans les cages:
sql= ("SELECT animal.nom, animal.race, animal.id_cage, animal.date_naissance, animal.pays_origine AS cage "
          "FROM animal "
          "JOIN cage ON animal.id_cage = cage.id;")
cursor.execute(sql)
for row in cursor:
  print(row)

# superficie total des de la table cage:
#sql = "SELECT SUM(superficie) FROM cage"
#cursor.execute(sql)

#ajoute_animaux()
#ajoute_cage()
#supprimer_cage(2)

cursor.close()
connexion.close()