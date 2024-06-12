#include <Servo.h>

long duration, distance, PET_Bin_Sensor, HDPE_Bin_Sensor, PP_Bin_Sensor, Right_Bin_Sensor2,Middle_Bin_Sensor2;

const int ledPins[] = {23,25,27,29}; // LED Pin for plastic type
const int numLeds = 4;

#define rfid_red_led 31 //rfid grant
#define rfid_green_led 33 // rfid denied 
#define trigPin1 6
#define echoPin1  7

int servoPin1 = 31; // flipper
int servoPin2 = 37; // bin
int servoPin3 = 39; //door 
Servo Servo1;
Servo Servo2;
Servo Servo3;

int defaultDeg = 90; // PP

int default_flip_deg = 178;
int open_flip_deg = 100;

void setup() {
    Serial.begin(115200);
    Serial.println("Initializing ....");
    
//    180
//    Servo1.attach(servoPin1);
//    Servo1.write(178);
//    delay(1000);
//    Servo1.detach();

    Serial.println("FLIPPER DEFAULT CLOSE");
    Servo1.attach(servoPin1);  // attaches the servo on pin 9 to the servo object
    Servo1.write(default_flip_deg);
    delay(2000);
    Servo1.detach();

    Serial.println("Start Now ....");
    Serial.println("Enter Plastic Type: ");
    
    
    Servo2.attach(servoPin2);
    Servo2.write(defaultDeg);
    delay(2000);
    Servo2.detach();

    Servo3.attach(servoPin3);
    Servo3.write(0); //door close
  
  
    for (int i = 0; i < numLeds; i++) {
        pinMode(ledPins[i], OUTPUT);
    }

    for (int i = 0; i < numLeds; i++) {
        digitalWrite(ledPins[i], LOW);
    }

    bin_light_initializing();
    pinMode(rfid_red_led, OUTPUT);
    pinMode(rfid_green_led, OUTPUT);

    digitalWrite(rfid_red_led, LOW);
    digitalWrite(rfid_green_led, LOW);

    //Servo2.write(90);
}

void loop() {
    // Bin Detection if Full
    digitalWrite(trigPin1, LOW); 
    delayMicroseconds(2);
    digitalWrite(trigPin1, HIGH);  
    delayMicroseconds(10);
    digitalWrite(trigPin1, LOW);
    duration = pulseIn(echoPin1, HIGH);
    distance = duration * 0.034 / 2;
    int Bin_level_Sensor  = distance ;
    // Serial.println(Bin_level_Sensor);
   
    if (Bin_level_Sensor <= 10 && Bin_level_Sensor >= 5){
        Serial.println("Bin is already Full!");
        Serial.println(Bin_level_Sensor);

        for (int i = 0; i < numLeds; i++) {
            digitalWrite(ledPins[i], HIGH);
        }
        delay(500);

        for (int i = 0; i < numLeds; i++) {
            digitalWrite(ledPins[i], LOW);
        }
        delay(500);

        digitalWrite(ledPins[0,1,2,3], LOW);  
        delay(500);

    } else {
        digitalWrite(ledPins[0], LOW);
        delay(500);
    }
  
  
  if(Serial.available() > 0){
    String plastic_input = Serial.readStringUntil('\n');
    
    if (plastic_input.equals("PET"))
    {
      Serial.println("PET.");
      digitalWrite(ledPins[0], HIGH);
      delay(1000);
      digitalWrite(ledPins[0], LOW);  
      delay(1000);

      rotate(0);
    }
    else if (plastic_input.equals("HDPE"))
    {
      Serial.println("HDPE.");
    
      digitalWrite(ledPins[1], HIGH);
      delay(1000);
      digitalWrite(ledPins[1], LOW);  
      delay(1000);

      rotateCounter(1100);
    }
    else if (plastic_input.equals("PP"))
    {
      Serial.println("PP.");
 
      digitalWrite(ledPins[2], HIGH);
      delay(2000);
      digitalWrite(ledPins[2], LOW);  
      delay(2000);


      PProtate(2100);
    }
    else if (plastic_input.equals("OTHERS"))
    {
      Serial.println("OTHERS.");
     
      digitalWrite(ledPins[3], HIGH);
      delay(2000);
      digitalWrite(ledPins[3], LOW);  
      delay(2000);


      rotate(1050);
    } else if (plastic_input.equals("OPEN")){
//      180
      Serial.println("OPEN DOOR.");
      Servo3.attach(servoPin3);
      Servo3.write(120); // Open
      delay(2000);
      Servo3.detach();
      
    } else if (plastic_input.equals("CLOSE")){
//      180
      Serial.println("CLOSE DOOR.");
      Servo3.attach(servoPin3);
      Servo3.write(0); // Open
      delay(2000);
      Servo3.detach();
    }
  }
}


void bin_light_initializing(){
    for (int i = 0; i < numLeds; i++) {
        digitalWrite(ledPins[i], HIGH); 
        delay(500);
        digitalWrite(ledPins[i], LOW); 
    }
    
    for (int i = numLeds - 1; i >= 0; i--) {
        digitalWrite(ledPins[i], HIGH); 
        delay(500);
        digitalWrite(ledPins[i], LOW); 
    }
    
    for (int i = 0; i < numLeds; i++) {
        digitalWrite(ledPins[i], HIGH); 
    }
    
    delay(1000);
    
    for (int i = 0; i < numLeds; i++) {
        digitalWrite(ledPins[i], LOW); 
    }
}


void rotate(int delaySec){
    Serial.println("ROTATING");
    Servo2.attach(servoPin2);
    Servo2.write(360);

    delay(delaySec); // waiting time

    Servo2.detach();
    Serial.println("WAITINGS");
    flip();
    delay(2000); // WAITINGS NA MAFALL SIYA

    Serial.println("ROTATE BACK");
    Servo2.attach(servoPin2);

    Servo2.write(10);
    delay(delaySec);
    Servo2.detach();
}

void rotateCounter(int delaySec){
    Serial.println("ROTATING");
    Servo2.attach(servoPin2);
    Servo2.write(10);

    delay(delaySec); // waiting time

    Servo2.detach();
    Serial.println("WAITINGS");
    flip();
    delay(2000); // WAITINGS NA MAFALL SIYA

    Serial.println("ROTATE BACK");
    Servo2.attach(servoPin2);

    Servo2.write(360);
    delay(delaySec);
    Servo2.detach();
}

void PProtate(int delaySec){
    Serial.println("ROTATING");
    Servo2.attach(servoPin2);
    Servo2.write(360);

    delay(delaySec); // waiting time

    Servo2.detach();
    Serial.println("WAITINGS");
    flip();
    delay(2000); // WAITINGS NA MAFALL SIYA

    Serial.println("ROTATE BACK");
    Servo2.attach(servoPin2);

    Servo2.write(10);
    delay(delaySec-100);
    Servo2.detach();
}

void flip(){
//    delay(1000);
//    180
    Serial.println("OPEN FLIPPER.");
//    Servo1.attach(servoPin1);
//    Servo1.write(78);
//    delay(2000);
    Servo1.attach(servoPin1);
    for (int pos = default_flip_deg; pos >= open_flip_deg; pos -= 1) { // goes from 180 degrees to 0 degrees
      Servo1.write(pos);              // tell servo to go to position in variable 'pos'
      delay(20);                       // waits 15ms for the servo to reach the position
    }
    Servo1.detach();

    delay(2000);

    Serial.println("CLOSE FLIPPER.");
//    Servo1.attach(servoPin1);
//    Servo1.write(178);
//    delay(2000);
//    Servo1.detach();
    Servo1.attach(servoPin1);
    for (int pos = open_flip_deg; pos <= default_flip_deg; pos += 1) { // goes from 180 degrees to 0 degrees
      Servo1.write(pos);              // tell servo to go to position in variable 'pos'
      delay(20);                       // waits 15ms for the servo to reach the position
    }
    Servo1.detach();

//  360
//    Serial.println("OPEN FLIPPER.");
//    Servo1.write(0);
//    delay(350);
//     
//    Servo1.write(90);
//    delay(2000);
//
//    Serial.println("CLOSE FLIPPER.");
//    Servo1.write(360);
//    delay(350);
//
//    Servo1.write(90);
}
