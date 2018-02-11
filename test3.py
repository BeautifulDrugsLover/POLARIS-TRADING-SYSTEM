import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='mcx202PX@P',
                             db='nse_500',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



try:
    with connection.cursor() as cursor:
        sql = "SELECT nse_500.companies.name FROM nse_500.companies"
        cursor.execute(sql)
        data=cursor.fetchall()


finally:
    connection.close()
sk=[]

for i in range (0,len(data)):
    s=str(data[i].values())
    s=s.lstrip("dict_values(['")
    s=s.rstrip("'])")
    sk=sk+[s.lower().strip().replace(" ","")]
sk2=[]
import csv
with open('equity_list.csv','r') as f:
    obj = csv.reader(f)
    for i in obj:
        sk2=sk2+[i[1].lower().strip().replace(" ","")]

a=set(sk)
b=set(sk2)
tem=[]
for i in sk:
    for j in sk2:
        if i in j:
            print(i,j)
        if j in i:
            print(j,i)





