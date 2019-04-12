# from Xc.items import XcItem
# from Xc.mysqlpileline.sql import Sql
#
# class Xcpipeline():
#
#     def process_item(self,item,spider):
#         if isinstance(item,XcItem):
#             ipaddress = item['ipaddress']
#             ret = Sql.select_name(ipaddress)
#             if ret[0] == 1:
#                 print('已经存在')
#             else:
#                 country = item['country']
#                 ipaddress = item['ipaddress']
#                 port = item['port']
#                 serveraddr = item['serveraddr']
#                 isanonymous = item['isanonymous']
#                 type = item['type']
#                 alivetime = item['alivetime']
#                 verifitime = item['verifitime']
#
#                 Sql.insert_db_xici(country,ipaddress,port,severaddr,isanonyumous,type,alivetime,verifitime)