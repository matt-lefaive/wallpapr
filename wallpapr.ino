const int buttonPin = 14; 
const int doorPin = 16;

int buttonState = 0;
int doorState = 0;

void setup() {
  // initialize the pushbutton pin and door sensor as input
  pinMode(buttonPin, INPUT);
  pinMode(doorPin, INPUT);
}

void loop() {
  // read the state of the button and sensor:
  buttonState = digitalRead(buttonPin);
  doorState = digitalRead(doorPin);

  // check if the push button is pressed. 
  if (buttonState == HIGH) {
    Serial.println("1");
  }

  // Check if the door sensor is open.
  if (doorState == HIGH) {
    Serial.println("2");
  }
}
