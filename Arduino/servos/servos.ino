#include <Servo.h>
long duration, distance, Right_Bin_Sensor,Middle_Bin_Sensor,Left_Bin_Sensor, Right_Bin_Sensor2,Middle_Bin_Sensor2;

int servoPin = 35; 
Servo Servo1;
Servo Servo2;

void setup() {
Serial.begin(115200);
Serial.println("Enter Plastic Type: ");
//Servo1.write(90);
Servo2.write(0);
Servo2.attach(servoPin);
}

void loop() {
 if(Serial.available() > 0){
    String plastic_input = Serial.readStringUntil('\n');

    if (plastic_input.equals("PP"))
    {
      Serial.println("PP OPEN DOOR ");
      Servo2.write(0);
      delay(2000); 
      Servo2.write(120);
      delay(3000);
      Servo2.write(0);
    
     
    }
    else if (plastic_input.equals("PET"))
    {
      Servo2.write(0);
      delay(4000); 
      Servo2.write(120);
      delay(3000);
     
    }
    else if (plastic_input.equals("HDPE"))
    {
      Servo2.write(0);
      delay(4000); 
      Servo2.write(120);
      delay(3000);
      
    }
    else if (plastic_input.equals("UNKNOWN"))
    {
      Servo2.write(0);
      delay(4000); 
      Servo2.write(120);
      delay(3000);
      
    }
 }
}
