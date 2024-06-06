#include <Servo.h>

Servo Servo1;  // Create a Servo object

const int servoPin1 = 39;       // The PWM pin connected to the servo

void setup() {
  Serial.begin(115200);
//  Servo1.attach(servoPin1); // Attach the servo to the specified pin
//  delay(1000); // Wait for servo to initialize (if needed)
}

void loop() {
//  Servo Close
  Servo1.attach(servoPin1);
  Servo1.write(178);
  delay(2000);
  Servo1.detach();

  Serial.println("3 Sec to open FLIPPER.");
  delay(3000);
  
  Servo1.attach(servoPin1);
  Servo1.write(78);
  delay(2000);
  Servo1.detach();
  
  Serial.println("3 sec to close FLIPPER.");
  delay(3000);
}
