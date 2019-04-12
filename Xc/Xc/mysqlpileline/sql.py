# import pymysql
# from Xc import settings
#
# MYSQL_HOST = settings.MYSQL_HOST
# MYSQL_USER = settings.MYSQL_USER
# MYSQL_PASSWORD = settings.MYSQL_PASSWORD
# MYSQL_PORT = settings.MYSQL_PORT
# MYSQL_DB = settings.MYSQL_DB
#
# db = pymysql.connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOST,port=MYSQL_PORT,database=MYSQL_DB,charset='utf8')
#
# cursor = db.cursor()
#
# class Sql():
#     @classmethod
#     def insert_db_xici(cls,country,ipaddress,port,severaddr,isanonyumous,type,alivetime,verifitime):
#         sql = 'insert into xicidaili(country,ipaddress,port,severaddr,isanonyumous,type,alivetime,verifitime) VALUES (%(country)s,%(ipaddress)s,%(port)s,%(severaddr)s,%(isanonyumous)s,%(type)s,%(alivetime)s,%(verifitime)s)'
#         value = {
#             'country':country,
#             'ipaddress':ipaddress,
#             '':,
#             '':,
#             '':,
#             '':,
#             '':,
#             '':,
#         }
#         try:
#             cursor.execute(sql,value)
#             db.commit()
#         except Exception as e:
#             print('插入失败',e)
#             db.rollback()
#
#     #去重
#     @classmethod
#     def select_name(cls,ipaddress):
#         sql =