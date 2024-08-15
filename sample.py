#! /usr/bin/python3
import requests
from bs4 import BeautifulSoup
import psycopg2
from datetime import datetime
conn=psycopg2.connect(database="postgres",user='postgres',password='pavani',host='localhost',port='5432')
cursor = conn.cursor()
sql='DROP TABLE IF EXISTS interviewbit'
cursor.execute(sql)
sql = '''CREATE TABLE interviewbit(id  SERIAL NOT NULL,name varchar(30) not null,date varchar(30) not null)'''
cursor.execute(sql)
Url="https://www.interviewbit.com/contests/"
headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
r=requests.get(url=Url,headers=headers);
soup=BeautifulSoup(r.content,'html.parser')
table=soup.findAll('div',attrs={'class':'col-xs-12 col-sm-12 col-md-6 contest-card'})[0].find('a')
table1=soup.findAll('div',attrs={'class':'col-xs-12 col-sm-12 col-md-6 contest-card'})[0].find('div',attrs={'class':'info-value'})
d=[]
c=[]
for row in table:
 d.append(row.get_text().strip())
for row in table1:
 c.append(row.get_text().strip())
a=[]
for i in range(len(d)):
 x=[]
 x.append(d[i])
 x.append(c[i])
 a.append((x))
for b in a:
 cursor.execute("INSERT into interviewbit(name,date) VALUES (%s,%s)", b)
conn.commit()
sql='DROP TABLE IF EXISTS hackerearth'
cursor.execute(sql)
sql = '''CREATE TABLE hackerearth(id  SERIAL NOT NULL,name varchar(50) not null,date varchar(50) not null)'''
cursor.execute(sql)
Url="https://www.hackerearth.com/challenges/"
headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
r=requests.get(url=Url,headers=headers);
soup=BeautifulSoup(r.content,'html.parser')
table=soup.find('div',attrs={'class':'upcoming challenge-list'}).findAll('span',attrs={'class':'challenge-list-title challenge-card-wrapper'})
table2=soup.find('div',attrs={'class':'upcoming challenge-list'}).findAll('div',attrs={'class':'date less-margin dark'})
d=[]
c=[]
for row in table:
 d.append(row.text)
for row in table2:
 c.append(row.text)
a=[]
for i in range(len(d)):
 x=[]
 x.append(d[i])
 x.append(c[i])
 a.append((x))
for b in a:
 cursor.execute("INSERT into hackerearth(name,date) VALUES (%s,%s)", b)
conn.commit()
 
sql='DROP TABLE IF EXISTS leetcode'
cursor.execute(sql)
sql = '''CREATE TABLE leetcode(id  SERIAL NOT NULL,name varchar(50) not null,date varchar(50) not null)'''
cursor.execute(sql) 
Url="https://leetcode.com/contest/"
headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
r=requests.get(url=Url,headers=headers);
soup=BeautifulSoup(r.content,'html.parser')
table=soup.find('div',attrs={'class':'swiper-wrapper'}).findAll('span',attrs={'class':'transition-colors group-hover:text-blue-s dark:group-hover:text-dark-blue-s'})
table3=soup.find('div',attrs={'class':'swiper-wrapper'}).findAll('div',attrs={'class':'flex items-center text-[14px] leading-[22px] text-label-2 dark:text-dark-label-2'})
d=[]
c=[]
for row in table:
 d.append(row.text)
for row in table3:
 c.append(row.text)
a=[]
for i in range(len(d)):
 x=[]
 x.append(d[i])
 x.append(c[i])
 a.append((x))
for b in a:
 cursor.execute("INSERT into leetcode(name,date) VALUES (%s,%s)", b)
conn.commit()
  
sql='DROP TABLE IF EXISTS hackerearth1'
cursor.execute(sql)
sql = '''CREATE TABLE hackerearth1(id  SERIAL NOT NULL,name varchar(100) not null)'''
cursor.execute(sql)
Url="https://www.hackerearth.com/challenges/"
headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
r=requests.get(url=Url,headers=headers);
soup=BeautifulSoup(r.content,'html.parser')
table=soup.find('div',attrs={'class':'ongoing challenge-list'}).findAll('span',attrs={'class':'challenge-list-title challenge-card-wrapper'})
d=[]
for row in table:
 d.append(row.text)
a=[]
for i in range(len(d)):
 x=[]
 x.append(d[i])
 a.append((x))
for b in a:
 cursor.execute("INSERT into hackerearth1(name) VALUES (%s)", b)
conn.commit() 

sql='DROP TABLE IF EXISTS atcoder'
cursor.execute(sql)
sql = '''CREATE TABLE atcoder(id  SERIAL NOT NULL,name varchar(100) not null,date varchar(100) not null)'''
cursor.execute(sql)
Url="https://atcoder.jp/contests/"
headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
r=requests.get(url=Url,headers=headers);
soup=BeautifulSoup(r.content,'html.parser')
table=soup.find('div',attrs={'id':'contest-table-upcoming'}).findAll('time',attrs={'class':'fixtime-full'})
table4=soup.find('div',attrs={'id':'contest-table-upcoming'}).findAll('a')
d=[]
c=[]
for row in table:
 c.append(row.text)
for row in table4:
 d.append(row.text)
a=[]
j=1
for i in range(len(c)):
 x=[]
 x.append(d[j])
 x.append(c[i])
 a.append((x))
 j=j+2
for b in a:
 cursor.execute("INSERT into atcoder(name,date) VALUES (%s,%s)", b)
conn.commit()

sql='DROP TABLE IF EXISTS toph'
cursor.execute(sql)
sql = '''CREATE TABLE toph(id  SERIAL NOT NULL,name varchar(100) not null,date varchar(100) not null)'''
cursor.execute(sql)
Url="https://toph.co/contests/current"
headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
r=requests.get(url=Url,headers=headers);
soup=BeautifulSoup(r.content,'html.parser')
table=soup.find('div',attrs={'class':'col-md-9'}).findAll('span',attrs={'class':'text'})
table5=soup.find('div',attrs={'class':'col-md-9'}).findAll('a')
d=[]
c=[]
for row in table:
 c.append(row.text)
for row in table5:
 d.append(row.text)
a=[]
for i in range(len(c)):
 x=[]
 x.append(d[i])
 x.append(c[i])
 a.append((x))
for b in a:
 cursor.execute("INSERT into toph(name,date) VALUES (%s,%s)", b)
conn.commit()

sql='DROP TABLE IF EXISTS icpc'
cursor.execute(sql)
sql = '''CREATE TABLE icpc(id  SERIAL NOT NULL,name varchar(100) not null,date varchar(100) not null)'''
cursor.execute(sql)
Url="https://u.icpc.global/events/"
headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
r=requests.get(url=Url,headers=headers);
soup=BeautifulSoup(r.content,'html.parser')
table=soup.find('div',attrs={'class':'et_pb_row et_pb_row_1'}).findAll('p')
table6=soup.find('div',attrs={'class':'et_pb_row et_pb_row_1'}).findAll('h2')
d=[]
c=[]
for row in table:
 d.append(row.text)
for row in table6:
 c.append(row.text)
a=[]
j=1
for i in range(len(c)):
 x=[]
 x.append(c[i])
 x.append(d[j])
 a.append((x))
 j=j+2
for b in a:
 cursor.execute("INSERT into icpc(name,date) VALUES (%s,%s)", b)
conn.commit()

sql='DROP TABLE IF EXISTS spoj'
cursor.execute(sql)
sql = '''CREATE TABLE spoj(id  SERIAL NOT NULL,name varchar(100) not null,sdate varchar(100) not null,edate varchar(100) not null)'''
cursor.execute(sql)
Url="https://www.spoj.com/contests/"
headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
r=requests.get(url=Url,headers=headers);
soup=BeautifulSoup(r.content,'html.parser')
table=soup.findAll('table',attrs={'class':'table table-condensed'})[0].findAll('a')
table7=soup.findAll('table',attrs={'class':'table table-condensed'})[0].findAll('span')
d=[]
c=[]
for row in table:
 d.append(row.text)
for row in table7:
 c.append(row.text)
a=[]
j=0
for i in range(len(d)):
 x=[]
 x.append(d[i])
 x.append(c[j])
 j=j+1
 x.append(c[j])
 j=j+1
 a.append((x))
for b in a:
 cursor.execute("INSERT into spoj(name,sdate,edate) VALUES (%s,%s,%s)", b)
conn.commit() 
conn.close()