
async_mode = None

from flask import Flask, render_template
import socketio
import cv2
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)



IA=False
sio = socketio.Server(logger=True, async_mode=async_mode)
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)
app.config['SECRET_KEY'] = 'secret!'
thread = None


def prenderfoco1():
    ser.write(b'A')
    return False

def prenderfoco2():
    ser.write(b'B')
    return False

def prendercontacto1():
    ser.write(b'C')
    return False

def prendercontacto2():
    ser.write(b'D')
    return False

def prendertiraled():
    ser.write(b'I')
    return False

def prendermotor():
    ser.write(b'E')
    return False

def apagarfoco1():
    ser.write(b'Z')
    return False

def apagarfoco2():
    ser.write(b'Y')
    return False

def apagarcontacto1():
    ser.write(b'X')
    return False

def apagarcontacto2():
    ser.write(b'W')
    return False

def apagarmotor():
    ser.write(b'V')
    return False

def apagartiraLed():
    ser.write(b'U')
    return False

def apagarIA():
    return IA
    
def apagar():
    return True


def prenderIA(mient):
    global IA
 #   rostros_cascada2 = cv2.CascadeClassifier('haarcascade_eye.xml')
 #   rostros_cascada = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gesto_1 = cv2.CascadeClassifier('cascade.xml')
    gesto_2 = cv2.CascadeClassifier('cascade9.xml')
    sio.emit('my_response', {'data': 'Encenderia'})
    captura = cv2.VideoCapture(0)
    print("funcionando")
    IA=False
    g=0
    g1=0
    g0=0
    while True:
        _, img = captura.read()

        gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #    rostros = rostros_cascada.detectMultiScale(gris, 1.2, 10)
     #   rostros2 = rostros_cascada2.detectMultiScale(gris, 1.2, 10)
        gesto1 = gesto_1.detectMultiScale(gris, 5, 35)
        gesto2= gesto_2.detectMultiScale(gris,
                                           scaleFactor=8,
                                           minNeighbors=90,
                                           minSize=(70, 120))


        for (x, y, w, h) in gesto1:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, 'mano cerrada', (x, y - 10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
            g=g+1
            if(g==50):
                prenderfoco1()
                sio.emit('my_response', {'data': 'pf1'})
                time.sleep(0.5)
                prenderfoco2()
                sio.emit('my_response', {'data': 'pf2'})
                g=0
        for (x, y, w, h) in gesto2:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, 'mano', (x, y - 10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
            g=g+1
            if(g==50):
                apagarcontacto1()
                sio.emit('my_response', {'data': 'af1'})
                time.sleep(1)
                apagarcontacto2()
                sio.emit('my_response', {'data': 'af2'})
                time.sleep(1)
                apagarfoco1()
              #  sio.emit('my_response', {'data': 'ac1'})
                time.sleep(1)
                apagarfoco2()
              #  sio.emit('my_response', {'data': 'ac2'})
                g=0
      
       
        cv2.imshow('Inteligencia', img)
        mient=apagarIA()
        if ((cv2.waitKey(10) & 0xFF == 27) or mient):
            sio.emit('my_response', {'data': 'apagaria'})
            break
 
    captura.release()
    



def background_thread():
    count = 0
    while True:
        sio.sleep(10)
        count += 1
        sio.emit('my_response', {'data': 'Server generated event'})


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = sio.start_background_task(background_thread)
    return render_template('index.html')

car=False

@sio.event
def my_event(sid, message):
    #print(message)
    print(message['data'])
    if(message['data']=='foco1'):
            prenderfoco1()
            message['data']='pf1'
    elif(message['data']=='foco2'):
            prenderfoco2()
            message['data']='pf2'
    elif(message['data']=='IA'):
            prenderIA(False)
            
    elif(message['data']=='contacto1'):
            prendercontacto1()
            message['data']='pc1'
    elif(message['data']=='contacto2'):
            prendercontacto2()
            message['data']='pc2'
    elif(message['data']=='motor'):
            prendermotor()
            message['data']='pm'
    elif(message['data']=='led'):
            prendertiraled()
            message['data']='pl'
    sio.emit('my_response', {'data': message['data']}, room=sid)

@sio.event
def my_broadcast_event(sid, message):
    global IA
    print(message['data'])
    if(message['data']=='foco1'):
            car=apagarfoco1()
            message['data']='af1'
    elif(message['data']=='foco2'):
            car=apagarfoco2()
            message['data']='af2'
    elif(message['data']=='contacto1'):
            car=apagarcontacto1()
            message['data']='ac1'
    elif(message['data']=='contacto2'):
            car=apagarcontacto2()
            message['data']='ac2'
    elif(message['data']=='motor'):
            car=apagarmotor()
            message['data']='am'
    elif(message['data']=='led'):
            car=apagartiraLed()
            message['data']='al'
    elif(message['data']=='apagar'):
            apagartiraLed()
            apagarmotor()
            apagarcontacto1()
            apagarfoco1()
            apagarcontacto2()
            apagarfoco2()
            IA=apagar()
            message['data']='all'            
    elif(message['data']=='IA'):
            IA=apagar()
            
    sio.emit('my_response', {'data': message['data']})


if __name__ == '__main__':
    if sio.async_mode == 'threading':
      
        app.run(threaded=True)
    elif sio.async_mode == 'eventlet':
       
        import eventlet
        import eventlet.wsgi
        eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
    elif sio.async_mode == 'gevent':
      
        from gevent import pywsgi
        try:
            from geventwebsocket.handler import WebSocketHandler
            websocket = True
        except ImportError:
            websocket = False
        if websocket:
            pywsgi.WSGIServer(('', 5000), app,
                              handler_class=WebSocketHandler).serve_forever()
        else:
            pywsgi.WSGIServer(('', 5000), app).serve_forever()
    elif sio.async_mode == 'gevent_uwsgi':
        print('Start the application through the uwsgi server. Example:')
        print('uwsgi --http :5000 --gevent 1000 --http-websockets --master '
              '--wsgi-file app.py --callable app')
    else:
       print('Unknown async_mode: ' + sio.async_mode)
