import mysql.connector
import xlrd

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="hindalcodb")

########################## for creating a table on the database #####################################################
cur=conn.cursor()
cur.execute("create table hindalcotb(datetime datetime,close float,high float,low float,open float,volume varchar(50),instrument varchar(50))")
cur.close()
conn.commit()
conn.close()


########################## inserting exel to mysql database #########################################################
cur=conn.cursor()
query = """INSERT INTO `hindalcotb`(`datetime`, `close`, `high`, `low`, `open`, `volume`, `instrument`) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
loc = ("hindalco.xla")

a=xlrd.open_workbook(loc)
sheet = a.sheet_by_name("HINDALCO")
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)

for i in range(1,sheet.nrows):
    datetime = sheet.cell(i,0).value
    close = sheet.cell(i,1).value
    high = sheet.cell(i,2).value
    low = sheet.cell(i,3).value
    open = sheet.cell(i,4).value
    volume = sheet.cell(i,5).value
    instrument = sheet.cell(i,6).value
    
    values = (datetime, close, high, low, open, volume, instrument)

    cur.execute(query, values)


cur.close()
conn.commit()
conn.close()




