import sqlite3

dirDB = 'res/programa1.db'

def createDB():
    conn = sqlite3.connect(dirDB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            alias char(10) PRIMARY KEY NOT NULL,
            nombre char(30) NOT NULL,
            primer_apellido char(20) NOT NULL,
            segundo_apellido char(20),
            razon_social text NOT NULL,
            rfc char(13) NOT NULL,
            telefono char(10) NOT NULL,
            correo char(50) NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sec(
            id int PRIMARY KEY NOT NULL,
            descr char(20) NOT NULL,
            value char(50) NOT NULL
        );
    """)
    conn.commit()
    conn.close()

def isKey():
    conn = sqlite3.connect(dirDB)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM sec
    """)
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        return False
    else:
        return True 

def setKey(key):
    conn = sqlite3.connect(dirDB)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sec(id, descr, value)
        VALUES(1, "key", ?)
    """, (key,))
    conn.commit()
    conn.close()
    return True

def checkKey(key):
    conn = sqlite3.connect(dirDB)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM sec WHERE descr='key'
    """)
    row = cursor.fetchone()
    conn.close()
    return row[2] == key

def add_client(client):
    conn = sqlite3.connect(dirDB)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE alias = ?', (client[0],))
    entry = cursor.fetchone()
    if entry is None:
        cursor.execute("""
            INSERT INTO clients(alias, nombre, primer_apellido, segundo_apellido, razon_social, rfc, telefono, correo)
            VALUES(?,?,?,?,?,?,?,?)
        """, client)
        conn.commit()
        conn.close()
        return True
    else: return False

def update_client(alias, client):
    conn = sqlite3.connect(dirDB)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE alias = ?', (alias,))
    entry = cursor.fetchone()
    if entry is not None:
        lista =  list(client)
        for x in range(len(lista)-1):
            if lista[x]=="":
                lista[x] = entry[x+1]
        client = tuple(lista)
        cursor.execute("""
            UPDATE clients SET nombre=?,
                primer_apellido=?,
                segundo_apellido=?,
                razon_social=?,
                rfc=?,
                telefono=?,
                correo=? WHERE alias=?
        """, client)
        conn.commit()
        conn.close()
        return True
    else: return False

def get_all():
    conn = sqlite3.connect(dirDB)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete_client(alias):
    conn = sqlite3.connect(dirDB)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clients WHERE alias=?', (alias,))
    conn.commit()
    conn.close()
    return True