import web 
from web import form 
from bin import map

urls= (
     '/game' , 'GameEngine',
    '/' , 'Index' ,
    '/upload' , 'Upload' ,
    )
      
app= web.application(urls, globals())

render = web.template.render('templates/', base="layout")

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                  initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session




class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        session.room = map.START
        web.seeother("/game")
        
class Upload(object):
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return render.upload()
        
    def POST(self):
        x= web.input(myfile={})
        filedir= "C:/Users/tejas/Documents/filesave"
        if 'myfile' in x:
            fout = open(filedir + '/' + 'myfile.jpg', 'wb') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete
            return "Success! Your image has been saved in the given folder."
            raise web.seeother('/upload')
        


class GameEngine(object):

    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        
        if session.room and form.action:
            session.room = session.room.go(form.action)
        else:
            session.room= None
        
        web.seeother("/game")



        

if __name__=="__main__":
    
    app.run()
    
    