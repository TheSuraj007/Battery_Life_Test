const int analogInPin = A0; // Analog pin for battery voltage
const int baudRate = 9600;  // UART baud rate

void setup()
{
    Serial.begin(baudRate);
}

void loop()
{
    int sensorValue = analogRead(analogInPin);
    float voltage = sensorValue * (5.0 / 1023.0); // Convert ADC value to voltage
    Serial.print("Voltage: ");
    Serial.print(voltage);
    Serial.println(" V");
    delay(1000); // Delay for stability, adjust as needed
}
