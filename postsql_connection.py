#coding:utf-8

import psycopg2.extras
import sys


def main():
	conn_string = "host='localhost' dbname='dbname' user='postgres' password='secret'"

	print "Connecting to database\n -> %s" % (conn_string)

	conn = psycopg2.connect(conn_string)

	cursor = conn.cursor()
	#this is Cursor for controlling the Dict.
	#cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	cursor.execute("SELECT * FROM actor")
	#query 
	rows = cursor.fetchall()

	#for re in records:
	#	print "%s %s %s" %(re['actor_id'], re['first_name'], re['last_name'])

	for row in rows:
		print row

if __name__ == "__main__":
	main()
