import requests
from mysql import connector
import os


#open connection
db = connector.connect(
    host    = 'localhost',
    user    = 'root',
    passwd  = '',
    database= 'db_akademik_0577'
)


if db.is_connected():
    print('open connection successful')

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()

def options():
    print("1. Tampilkan Semua Data")
    print("2. Tampilkan Data Berdasarkan Limit")
    print("3. Cari Data Berdasarkan NIM")
    print("0. Keluar")
    x = input('Pilih Menu> ')
    if x == '1':
        showAllData()
    elif x == '2':
        limitData()
    elif x == '3':
        limitNim()

def insertDataMysql():
    baseURL = "https://api.abcfdab.cfd/students/"
    response = requests.get(baseURL)
    if response.status_code == requests.codes.ok:
        data = response.json()
        for out in data['data']:
            id = out['id']
            nim = out['nim']
            nama = out['nama']
            jk = out['jk']
            jurusan = out['jurusan']
            alamat = out['alamat']
            cur = db.cursor()
            cur.execute('INSERT INTO `tbl_students_0577` (no, nim, nama, jk, jurusan, alamat) VALUES (null, %s, %s, %s, %s, %s)', (nim, nama, jk, jurusan, alamat))
            db.commit()

def showAllData():
    clear()
    cur = db.cursor()
    cur.execute('SELECT * FROM `tbl_students_0577`')
    data = cur.fetchall()
    print('+-----+----------+----------------------------+----+-----------------------+-------------+')
    print('| No. |    NIM   |              NAMA          | JK  |        Jurusan       |    Alamat   |')
    print('+-----+----------+----------------------------+----+-----------------------+-------------+')
    for row in data:
        print("|", row[0],"|", row[1], "|", row[2]," "*(24-len(row[2])),"|", row[3]," "*(2-len(row[3])),"|", row[4]," "*(1-len(row[4])),"|", row[5],"|")
        print('+-----+----------+----------------------------+----+-----------------------+-------------+')   
    
    options()

def limitData():
    clear()
    x = input('Masukkan Limit : ')
    cur = db.cursor()
    cur.execute(f'SELECT * FROM `tbl_students_0577` LIMIT {x}')
    data = cur.fetchall()
    print('+-----+----------+----------------------------+----+-----------------------+-------------+')
    print('| No. |    NIM   |              NAMA          | JK  |        Jurusan       |    Alamat   |')
    print('+-----+----------+----------------------------+----+-----------------------+-------------+')
    for row in data:
        print("|", row[0],"|", row[1], "|", row[2]," "*(24-len(row[2])),"|", row[3]," "*(2-len(row[3])),"|", row[4]," "*(1-len(row[4])),"|", row[5],"|")
    print('+-----+----------+----------------------------+----+-----------------------+-------------+')     
    
    options()

def limitNim():
    clear()
    x = str(input('Masukkan NIM : '))
    cur = db.cursor()
    cur.execute(f'SELECT * FROM `tbl_students_0577` WHERE nim = "{x}" LIMIT 1')
    data = cur.fetchall()
    print('+-----+----------+----------------------------+----+-----------------------+-------------+')
    print('| No. |    NIM   |              NAMA          | JK  |        Jurusan       |    Alamat   |')
    print('+-----+----------+----------------------------+----+-----------------------+-------------+')
    for row in data:
        print("|", row[0],"|", row[1], "|", row[2]," "*(24-len(row[2])),"|", row[3]," "*(2-len(row[3])),"|", row[4]," "*(1-len(row[4])),"|", row[5],"|")
    print('+-----+----------+----------------------------+----+-----------------------+-------------+')     
    
    options()

if __name__ == '__main__':
    options()