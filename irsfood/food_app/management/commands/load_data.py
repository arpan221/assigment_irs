import mysql.connector
from django.core.management.base import BaseCommand
import time 
import math
# import numpy as np

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="8504KANUsharma@@",
  database="food_data",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
mycursor.execute('set GLOBAL max_allowed_packet=67108864')


class Command(BaseCommand):
	help = 'This Command Use For Upload Data...'

	def add_arguments(self, parser):
		parser.add_argument('file_name')

	
	def handle(self, *args, **options):
		data_val = []
		all_values = []
		val = 0
		file_name = options['file_name']
		with open(file_name,'r+',encoding='latin-1') as f:
			read_file = f.read()
			for i in read_file.split("\n"):
				if i != '':
					coloumn_name_start = i.find("/")
					coloumn_name_end = i.find(":")
					coloumn_name = i[coloumn_name_start+1:coloumn_name_end]
					if coloumn_name_start !=  -1 and coloumn_name_end != -1:
						data = i[coloumn_name_end+1:]
						data_val.append(data)
						val+=1
						if val == 8:
							all_values.append(tuple(data_val))
							data_val = []
							val = 0
			#Here File is fix so i have taken int number like 1lac , if file changeable then we use input section for this
			
			insert_len = len(all_values)/100000
			x = math.trunc(insert_len)
			y = 0
			z = 100000
			for i in range(x+1):
				if x == i:
					new_val = all_values[y:]
				else:
					new_val = all_values[y:z]
					y+=100000
					z+=100000
				sql = "INSERT INTO food_app_food (productId,userId,profileName,helpfulness,score,time,summary,text) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
				mycursor.executemany(sql,new_val)
				mydb.commit()
				print(mycursor.rowcount, "record was inserted.")
				