#include <OneButton.h>
int LED_red = 4;
int LED_green = 5;
boolean button_pressed = false;
OneButton button(A1, false);
 
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  
  pinMode(LED_red, OUTPUT);
  pinMode(LED_green, OUTPUT);
  button.attachClick(singleClick);
  
}

// the loop function runs over and over again forever
void loop() {
  button.tick();
  
  digitalWrite(LED_green, HIGH);
  
  delay(20);
} 

void singleClick() {
  while(true){  
    digitalWrite(LED_green, LOW);
    digitalWrite(LED_red, HIGH); 
    tone(3, 2000, 500);
    delay(500);                       // wait for a second
    digitalWrite(LED_red, LOW);    // turn the LED off by making the voltage LOW
    delay(500);  
  }
} 
