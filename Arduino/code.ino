#include <Servo.h>
#include <SPI.h>

#include <MFRC522.h>
long duration, distance, PET_Bin_Sensor, HDPE_Bin_Sensor, PP_Bin_Sensor, Right_Bin_Sensor2,Middle_Bin_Sensor2;

#define RST_PIN         5          // Configurable, see typical pin layout above
#define SS_PIN          53         // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);
#define trigPin1 6
#define echoPin1  7
#define capacitive 41

const int ledPins[] = {23,25,27,29}; // LED Pin for plastic type
const int numLeds = 4;

#define rfid_red_led 31 //rfid grant
#define rfid_green_led 33 // rfid denied 
bool account_bool = false;
int servoPin1 = 39;// flipper
int servoPin2 = 37;// bin
int servoPin3 = 35; //door 
Servo Servo1;
Servo Servo2;

Servo Servo3;

int defaultDeg = 90; // PP

void setup() {
  Servo1.attach(servoPin1);
  Servo1.write(178);
  delay(2000);
  Servo1.detach();
  
  SPI.begin(); 
  /* Initialise the RFID reader */
  mfrc522.PCD_Init();
  Serial.println("Initializing ....");
  delay(1000);
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(capacitive, INPUT);
  Serial.println("Start Now ....");
  Serial.println("Enter Plastic Type: ");
 
  
  Servo2.attach(servoPin2);
  Servo2.write(defaultDeg);
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

  
Serial.begin(115200);

//Servo2.write(90);

}

void loop() {
    int capacitiveValue = digitalRead(capacitive);
    Serial.println(capacitiveValue);
    Serial.print("CARD READ: ");
    Serial.println((mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()));
    if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
      // Show UID on serial monitor
      Serial.print("UID tag :");
      String content = "";
      for (byte i = 0; i < mfrc522.uid.size; i++) {
        Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
        Serial.print(mfrc522.uid.uidByte[i], HEX);
        content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
        content.concat(String(mfrc522.uid.uidByte[i], HEX));
      }
      Serial.println();
      Serial.print("Message : ");
      content.toUpperCase();
      if (content.substring(1) == "8A CF AD 1A"  ) {  // Change to match your tag's UID
        if (capacitiveValue == HIGH) {  // Change to match your tag's UID
          Serial.println("Authorized access but not Allowed");
          digitalWrite(rfid_red_led,HIGH);
          
          digitalWrite(rfid_red_led,LOW);
          Servo3.write(0); // Close
          delay(1000);
        } else { // OPEN
          account_bool = true;
          Serial.println("Authorized access");
          digitalWrite(rfid_green_led,HIGH);
          
          Servo3.write(120); // Open
          delay(1000);
          digitalWrite(rfid_green_led,LOW);
        }
     
      } else {
        account_bool = false;
        Serial.println("Unauthorized access");
        digitalWrite(rfid_red_led,HIGH);
        delay(1000);
        Servo3.write(0); // Close 
        digitalWrite(rfid_red_led,LOW);
      }

      
   // delay(1000); // Delay to avoid multiple readings
  }

  else {
    if(!account_bool || !(mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) || capacitiveValue){
//      Serial.println("READ?????????");
      Servo3.write(0); // Close
    } else if(account_bool && (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial())){
      Servo3.write(120); // Open
    }
    // delay(1000);
  }
      
 
    
 // Bin Detection if Full
    digitalWrite(trigPin1, LOW); 
    delayMicroseconds(2);
    digitalWrite(trigPin1, HIGH);  
    delayMicroseconds(10);
    digitalWrite(trigPin1, LOW);
    duration = pulseIn(echoPin1, HIGH);
    distance = duration * 0.034 / 2;
    int Bin_level_Sensor  = distance ;

   
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
  }
   else{
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
    else if (plastic_input.equals("OTHER"))
    {
      Serial.println("OTHER.");
     
      digitalWrite(ledPins[3], HIGH);
      delay(2000);
      digitalWrite(ledPins[3], LOW);  
      delay(2000);


      rotate(1050);
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
   delay(1000);
   Servo1.attach(servoPin1);
   Servo1.write(78);
   delay(2000);

   Servo1.detach();
   delay(2000);
   
   Servo1.attach(servoPin1);
   Servo1.write(178);
   delay(2000);
   Servo1.detach();
}
