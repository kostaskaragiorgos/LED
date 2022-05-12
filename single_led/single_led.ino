int redledPin = 9;
int delaytime =  1000;
int fromp;
void setup() {
  Serial.begin(9600);
  pinMode(redledPin,OUTPUT);

}

void loop() {
 if (Serial.available()>0){
  fromp = Serial.read();
  if (fromp == 'H'){
    digitalWrite(redledPin,HIGH);
    Serial.print(HIGH);
  }
  if(fromp == 'L')
  {
    digitalWrite(redledPin,LOW);
    Serial.print(LOW);
  }
 }
  delay(delaytime);

}
