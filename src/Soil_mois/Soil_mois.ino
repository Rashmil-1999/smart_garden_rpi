const int AirValue1 = 505;
const int AirValue2 = 515;
const int AirValue3 = 504;
const int AirValue4 = 514;  //you need to replace this value with Value_1
const int WaterValue1 = 237;
const int WaterValue2 = 249;
const int WaterValue3 = 236;
const int WaterValue4 = 251;//you need to replace this value with Value_2

int soilMoistureValue1 = 0;
int soilMoistureValue2 = 0;
int soilMoistureValue3 = 0;
int soilMoistureValue4 = 0;

int soilmoisturepercent1 =0;
int soilmoisturepercent2 =0;
int soilmoisturepercent3 =0;
int soilmoisturepercent4 =0;

void setup() {
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
}
void loop() {
  soilMoistureValue1 = analogRead(A5);
  soilMoistureValue2= analogRead(A4); 
  soilMoistureValue3 = analogRead(A3); 
  soilMoistureValue4= analogRead(A2); //put Sensor insert into soil
  
//  Serial.println("Raw Values in order 0->1->2->3");
//  Serial.println("Soil Moisture % values\nA0:%d\tA1:%d\tA2:%d\tA3:%d\t",soilMoistureValue0, soilMoistureValue1, soilMoistureValue2, soilMoistureValue3);
//  Serial.println("###################");
//  Serial.println(soilMoistureValue1);
//  Serial.println(soilMoistureValue2);
//  Serial.println(soilMoistureValue3);
//  Serial.println(soilMoistureValue4);
//  Serial.println(AirValue1);
//  Serial.println(WaterValue1);
  
  
  soilmoisturepercent1 = map(soilMoistureValue1, AirValue1, WaterValue1, 0, 100);
  soilmoisturepercent2 = map(soilMoistureValue2, AirValue2, WaterValue2, 0, 100);
  soilmoisturepercent3 = map(soilMoistureValue3, AirValue3, WaterValue3, 0, 100);
  soilmoisturepercent4 = map(soilMoistureValue4, AirValue4, WaterValue4, 0, 100);

//  Serial.println("Soil Moisture % values\nA0:%d\tA1:%d\tA2:%d\tA3:%d\t",soilmoisturepercent0,soilmoisturepercent1,soilmoisturepercent2,soilmoisturepercent3);
  Serial.println(soilmoisturepercent1);
//  Serial.println("###################");
//  Serial.println(soilmoisturepercent1);
//  Serial.println(soilmoisturepercent2);
//  Serial.println(soilmoisturepercent3);

  if (Serial.available() > 0){
      String data = Serial.readStringUntil('\n');
       if(data == "moisture"){
//          Serial.println((String)"ch_1:"+soilmoisturepercent1+":ch_2:"+soilmoisturepercent2+":ch_3:"+soilmoisturepercent3+":ch_4:"+soilmoisturepercent4);
          Serial.println((String)"ch_1:"+soilmoisturepercent1);
       }
       else if(data == "testing"){
          Serial.println((String)"ch_1:"+soilMoistureValue1+":ch_2:"+soilMoistureValue2+":ch_3:"+soilMoistureValue3+":ch_4:"+soilMoistureValue4); 
       }
    }

  delay(2000);
}
