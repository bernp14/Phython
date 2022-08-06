import sqlite3

fichierDonnees="C:/Users/Bern Pac/Downloads/test.db"

cur =conn.cursor()

#cur.execute("CREATE TABLE membres (age INTEGER, nom TEXT, taille REAL)")
#cur.execute("INSERT INTO membres(age,nom,taille) VALUES(21,'Dupont',1.83)")
#cur.execute("INSERT INTO membres(age,nom,taille) VALUES(15,'Blumâr',1.57)")
#cur.execute("INSERT Into membres(age,nom,taille) VALUES(18,'Özémir',1.69)")

conn.commit()

cur.close()
conn.close()