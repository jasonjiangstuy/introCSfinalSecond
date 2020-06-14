#! /usr/bin/python
print('Content-type: text/html\n')

import os
import StuyTools
StuyTools.PWS_startup()

#backup paths
root = '/home/students/2022/jjiang20/public_html/introCSfinalSecond/'
outsideRoot =  '~/jjiang20/introCSfinalSecond/'

#testing
# for param in os.environ.keys():
#     print("<b>%20s</b>: %s<\br>" % (param, os.environ[param]))

# if 'SCRIPT_FILENAME' in os.environ.keys():
#     path = str(os.environ['SCRIPT_FILENAME'])
#     #print(path.split('/')[1:])
#     outsideRoot = path.replace('main.py', '')
#     print(outsideRoot)
if 'SCRIPT_NAME' in os.environ.keys():
    path = str(os.environ['SCRIPT_NAME']) 
    #print(path.split('/')[1:])
    # path for the current directory, used to get the path for images and what not
    outsideRoot = path.replace('main.py', '') 

   #  print(outsideRoot)

import cgi

import cgitb
cgitb.enable(display=0, logdir='../www/logdir')




#functions -------------------------------
def render_template(filename, **kwargs): #root = root
    #given filename in this directory
   #  print('Where are we: ' + str(os.getcwd()))
    os.chdir('templates')
   #  print('How About Now: ' + str(os.getcwd()))
    try:
        f = open(filename, 'r')
        myFile = f.read()
        f.close()
        # print(myFile)
    except:
        print('filename '+ filename + ' not found in ' + os.getcwd())
        raise ValueError('filename '+ filename + ' not found in ' + os.getcwd())
    #include root for files
    myFile = myFile.replace('{{root}}', str(outsideRoot))

    for key, value in kwargs.items():
        print(key,value)
        if type(key) == type('String'):
            myFile = myFile.replace('{{' + key + '}}', str(value))
        else:
            print('404 Known Internal Server Error')
            raise(ValueError('Key value pair for templates must be strings'))

    #includes for first level embedded templates
    while True:
        if '{{include' in myFile:
            Before, throw, save = myFile.partition('{{include')
            save, throw, After = save.partition('}}')
            save = save.strip(" '") 
            # print(save)
            try:
                f = open(save, 'r')
                include = f.read()
                f.close()
            except:
                print('includes:' + 'filename '+ save + ' not found in ' + os.getcwd())
                raise ValueError('includes:' + 'filename '+ save + ' not found in ' + os.getcwd())
            include = include.replace('{{root}}', str(outsideRoot))
            myFile = Before + include + After
        else:
            break
            
    print(myFile)

data = cgi.FieldStorage()

# catch post request to server
stopRoute = False
isRequest = data.getfirst('submit')
# print(isRequest)
if isRequest:
   #post request
   stopRoute = True
   myImg = data.getfirst('myImg')
   markerColor = data.getfirst('markerColor')
   backgroundColor = data.getfirst('backgroundColor')
   
   # test that non of them are None type
   if not(myImg and markerColor and backgroundColor):
      #fails
      print('Bad Request, Missing Part of Request')
   else:
      # print(myImg, markerColor, backgroundColor)
      #print(markerColor, backgroundColor)
      # credits
      import io
      buf = io.BytesIO(myImg)
      #base 64 -> file object that is ready for PIL
      import handwriting

      #do proccessing
      finalProccessed = handwriting.removeHandwriting(buf)

      #convert PIL image to base 64
      import base64
      buffered = BytesIO()


      finalProccessed.save(buffered, format="JPEG")
      img_str = base64.b64encode(buffered.getvalue())
      print(img_str)
      


#routes
if 'PATH_INFO' in os.environ.keys() and not stopRoute:
   path = str(os.environ['PATH_INFO'])
   #print(path.split('/')[1:])
   pathParts = path.split('/')[1:]
   if len(pathParts) > 0:
      if pathParts[0] == 'login':
         render_template('login.html')
      elif pathParts[0] == 'go':
         render_template('goclean.html')
      elif pathParts[0] == 'works':
         render_template('about.html')
      else:
         render_template('home.html')
   else:
      render_template('home.html')
else:
   if not stopRoute:
      render_template('home.html')

