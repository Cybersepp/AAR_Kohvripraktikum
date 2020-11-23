import RPi.GPIO as GPIO
import time

#Panen pinid paika
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setwarnings(False)

#Auto valgusfoori pinid
auto_punane = 12
auto_kollane = 16
auto_roheline = 18

#Jalakaija valgusfoori pinid
jala_punane = 22
jala_roheline = 15

#Sinise LED pin
sinine = 40

#Nupu pin
nupp = 38

#Panen paika nupu toevaartuse
nupp_toim = True

#Lulitab kindla LED'i sisse
def sisse(pin):
    GPIO.output(pin, GPIO.HIGH)

#Lulitab kindla LED'i valja
def valja(pin):
    GPIO.output(pin, GPIO.LOW)

#Paneb kindla LED'i vilkuma
def vilgu(pin):
    valja(pin)
    for i in range(4):
        time.sleep(1)
        sisse(pin)
        time.sleep(1)
        valja(pin)

#Muudab autofoori punaseks
def auto_valja():
    vilgu(auto_roheline)
    sisse(auto_kollane)
    time.sleep(1)
    valja(auto_kollane)
    sisse(auto_punane)

#Muudab autofoori roheliseks
def auto_sisse():
    sisse(auto_kollane)
    time.sleep(1)
    valja(auto_punane)
    valja(auto_kollane)
    sisse(auto_roheline)

#Muudab jalakaijafoori roheliseks
def jala_sisse():
    valja(jala_punane)
    sisse(jala_roheline)

#Muudab jalakaijafoori punaseks
def jala_valja():
    valja(jala_roheline)
    sisse(jala_punane)
    

try:
    while True:
        
        #Roheliseks autofoor ja punaseks jalakaijate oma
        sisse(auto_roheline)
        sisse(jala_punane)
        
        #Muudab vajutamisel nupu toevaartuse, et kaivitada foori muutmise tsukkel
        nupp_toim = GPIO.input(nupp)
        
        #Autofoori ja jalakaija foori tsukkel
        if nupp_toim == False:
            sisse(sinine)
            auto_valja()
            jala_sisse()
            valja(sinine)
            time.sleep(5)
            jala_valja()
            auto_sisse()
            
#Programmi lopetades kustutab LED'id
finally:
    GPIO.cleanup()
