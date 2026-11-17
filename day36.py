// ME25C04 Makerspace Lab - LM35 Temperature Sensor

const int tempPin = A0; // LM35 output connected to A0

void setup() {
  Serial.begin(9600); // Start serial communication
}

void loop() {
  int analogValue = analogRead(tempPin); // Read ADC value (0-1023)
  
  float voltage = analogValue * (5.0 / 1023.0); // Convert to voltage
  
  float temperature = voltage * 100.0; // LM35: 10mV per °C, so Temp = Voltage * 100
  
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");
  
  delay(1000); // Wait 1 second
}
