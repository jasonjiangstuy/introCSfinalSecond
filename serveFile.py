#! /usr/bin/python
import cgi

import cgitb
cgitb.enable(display=0, logdir='../www/logdir')

data = cgi.FieldStorage()

# catch post request to server
stopRoute = False
isRequest = data.getfirst('cookieRequest')

if isRequest:
   if 'HTTP_COOKIE' in os.environ.keys():
	   cookie_set = os.environ['HTTP_COOKIE']
	   cookies = cookie_set.split(';')
	   for acookie in cookies:
         #test
   	   print(acookie.strip())

         # if cookie matches a file, return that file

   else:
	   print('Not Done')
