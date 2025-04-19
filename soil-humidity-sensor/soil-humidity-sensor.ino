char* buffer = new char[1];

void setup() {
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()){
    String s = Serial.readString();
    Serial.print(s);
    if(s == "?\n"){
      Serial.println(analogRead(A0));
    }
  }
}