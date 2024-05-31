#include <Servo.h>
long duration, distance, Right_Bin_Sensor,Middle_Bin_Sensor,Left_Bin_Sensor, Right_Bin_Sensor2,Middle_Bin_Sensor2;

int servoPin = 9; 
int servoPin2 = 11;
Servo Servo1;
Servo Servo2;

void setup() {
Serial.begin(9600);
Serial.println("Enter Plastic Type: ");
//Servo1.write(90);
Servo1.write(178);
}

void loop() {
 flip();
 if(Serial.available() > 0){
    String plastic_input = Serial.readStringUntil('\n');

    if (plastic_input.equals("PP"))
    {
      Servo2.write(180);
      delay(2000); 
      Servo2.write(90);
      delay(3000);
      flip();
    }
    else if (plastic_input.equals("PET"))
    {
      Servo2.write(180);
      delay(4000); 
      Servo2.write(90);
      delay(3000);
      flip();
    }
    else if (plastic_input.equals("HDPE"))
    {
      Servo2.write(0);
      delay(4000); 
      Servo2.write(90);
      delay(3000);
      flip();
    }
    else if (plastic_input.equals("UNKNOWN"))
    {
      Servo2.write(0);
      delay(4000); 
      Servo2.write(90);
      delay(3000);
      flip();
    }
 }
}

 void flip(){
     Servo1.attach(servoPin);
     Servo1.write(100);
     delay(3000);
     Servo1.write(178);
     delay(5000);
     }
