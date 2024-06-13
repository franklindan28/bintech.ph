#include <Servo.h>
int servoPin1 = 31;       // The PWM pin connected to the servo
Servo Servo1;
void setup() {
  Serial.begin(115200);
  Servo1.attach(servoPin1);
  Servo1.write(178);
  delay(2000);
  Servo1.detach();
  Serial.println("Enter Command: ");
//  Servo1.write(90);
//  delay(2000);
//  Servo1.attach(servoPin1); // Attach the servo to the specified pin
//  delay(1000); // Wait for servo to initialize (if needed)
}

void loop() {
  if(Serial.available() > 0){
    String plastic_input = Serial.readStringUntil('\n');

    if (plastic_input.equals("OPEN")) {
      
      Serial.println("OPEN FLIPPER.");
      Servo1.attach(servoPin1);
      Servo1.write(1);
      delay(3000);
      Servo1.detach();
      
    } else if(plastic_input.equals("CLOSE")) {
      
      Serial.println("CLOSE FLIPPER.");
      Servo1.attach(servoPin1);
      Servo1.write(180);
      delay(3000);
      Servo1.detach();
    }
  }
    
}
