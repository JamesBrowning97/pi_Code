import urllib.request
import json
import RPi.GPIO as GPIO
import time
#import the relevant libraries you need

#setting up servo
servoPIN = 17
FAN_PIN1 = 8
FAN_PIN2 = 10
FAN_PIN3 = 12
FAN_PIN4 = 16

#set up servo output
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) #GPIO 17 for PWM with 50hmz
p.start(0) #set initial duty cycle

#define api url
url = 'http://magicseaweed.com/api/cde8fb2381336a1d44665a44182e5513/forecast/?spot_id=167'
#get the response
req = urllib.request.Request('http://magicseaweed.com/api/cde8fb2381336a1d44665a44182e5513/forecast/?spot_id=167')

##parsing response
r = urllib.request.urlopen(req).read()
#load json into array
data = json.loads(r.decode('utf-8'))

#set the day you want 0 = tpoday
x = 6

while True: #Run forever
    day = data[x] #get the day set from line 22
    height = day['swell']['components']['combined']['height'] #api get data
    wind = day['wind']['compassDirection']#, day['wind']['speed']
    tide = day['swell']['absMinBreakingHeight']
    print("day=","new Height,", "new Wind,", "new Tide") #print new height to the terminal
    print(height, wind, tide) #print to terminal to get it working 
    
    #WIND
    #if wind == '':
        #print("The wind is coming from the ") North, CLockwise.
    if wind == 'N':
        print("The wind is coming from the North.")
        
    if wind == 'NNE':
        print("The wind is coming from the North North East.")
    if wind == 'NE':
        print("The wind is coming from the North East")
    if wind == 'ENE':
        print("The wind is coming from the East North East.")
    
    if wind == 'E':
        print("The wind is coming from the East.")
    
    if wind == 'ESE':
        print("The wind is coming from the East South East.")
    if wind == 'SE':
        print("The wind is coming from the South East")
    if wind == 'SSE':
        print("The wind is coming from the South South East")
    
    if wind == 'S':
        print("The wind is coming from the South")
    
    if wind == 'SSW':
        print("The wind is coming from the South South West")
    if wind == 'SW':
        print("The wind is coming from the South West")
    if wind == 'WSW':
        print("The wind is coming from the West South West")
    
    if wind == 'W':
        print("The wind is coming from the West")
    
    if wind == 'WNW':
        print("The wind is coming from the West North West")
    if wind == 'NW':
        print("The wind is coming from the North West")
    if wind == 'NNW':
        print("The wind is coming from the North North West")
    
    #SWELL
    if 0 < height <= 2:
        print("Swell is less than 2, pulsing once.")
        p.ChangeDutyCycle(7.5)
        time.sleep(5)
        p.ChangeDutyCycle(2.5)
        time.sleep(5)
    
    if 2 < height <= 4:
        print("Swell is less than 4, pulsing twice.")
        p.ChangeDutyCycle(7.5)
        time.sleep(2.5)
        p.ChangeDutyCycle(2.5)
        time.sleep(2.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(2.5)
        p.ChangeDutyCycle(2.5)
        time.sleep(2.5)
    
    if 4 < height <= 6:
        print("Swell is less than 6, pulsing thrice.")
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(2)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(2)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(3)
        
    if 6 < height <= 8:
        print("Swell is less than 8, pulsing max (four).")
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(1.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(1.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(1.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(1.5)
        
    #WIND - FAN CONTROL
    if wind == 'N':
        print("North fan is ON.")
        FAN_PIN1 = 8
        GPIO.setup(FAN_PIN, GPIO.OUT)
        GPIO.output(FAN_PIN1, True)
        GPIO.output(FAN_PIN2, False)
        GPIO.output(FAN_PIN3, False)
        GPIO.output(FAN_PIN4, False)
        
    if wind == 'E':
        print("East fan is ON.")
        FAN_PIN2 = 10
        GPIO.setup(FAN_PIN, GPIO.OUT)
        GPIO.output(FAN_PIN1, False)
        GPIO.output(FAN_PIN2, True)
        GPIO.output(FAN_PIN3, False)
        GPIO.output(FAN_PIN4, False)
        
    if wind == 'S':
        print("South fan is ON.")
        FAN_PIN3 = 12
        GPIO.setup(FAN_PIN, GPIO.OUT)
        GPIO.output(FAN_PIN1, False)
        GPIO.output(FAN_PIN2, False)
        GPIO.output(FAN_PIN3, True)
        GPIO.output(FAN_PIN4, False)
        
    if wind == 'W':
        print("West fan is ON.")
        FAN_PIN4 = 16
        GPIO.setup(FAN_PIN, GPIO.OUT)
        GPIO.output(FAN_PIN1, False)
        GPIO.output(FAN_PIN2, False)
        GPIO.output(FAN_PIN3, False)
        GPIO.output(FAN_PIN4, True)
        
time.sleep(10) #sleep for 10 seconds and start loop again

    
