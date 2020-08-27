import sqlite3


conn = sqlite3.connect('PythonAssignmentStep171.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFileName( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()
conn.close()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('PythonAssignmentStep171.db')

for file in fileList:
    if file.endswith(".txt"):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_txtFileName(col_fileName) \
            VALUES(?)",(file,))
            print(file)
            conn.commit()
conn.close()
            
