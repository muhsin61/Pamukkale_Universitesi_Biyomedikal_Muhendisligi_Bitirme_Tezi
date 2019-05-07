#include <WiFi.h>//Wifi kütüphanesi eklendi

const int analogIn = A0; //pot pini
bool sicaklik = true; // sıcaklık pot ve led değerinin bir kere göndermesi için tanımlandı.
bool pot = true;
bool led = true;

int RawValue= 0;  //lm35 ölçümü için değişkenler.
double Voltage = 0;
double tempC = 0;
double tempF = 0;


const char* ssid = "TURKSAT-KABLONET-B958-2.4G";
const char* password =  "6e570198"; //wifi sağı ismi ve şifresi
 
const uint16_t port = 8090;
const char * host = "192.168.0.34"; // bağlanılacak yerel ağ ve portu

int id;//serino için
String giden;

#define buton 35//led pini
void setup()
{
 
  Serial.begin(115200); // Seri port haberleşmesi esp32 genelde 115200 kullanılır.
 
  WiFi.begin(ssid, password);        //wifi bağlantı kodları.
  while (WiFi.status() != WL_CONNECTED) {
  delay(500);
  Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());
  
  pinMode(35,INPUT);//buton pini
  pinMode(22,OUTPUT);//WİFİ ışığı
  digitalWrite(22, HIGH);//wifi bağlandığında yanması için.

}
 
void loop()
{
    WiFiClient client;//
////////////////buton
    if (digitalRead(buton) == 1){
      delay(1000);
      id=14187001;
      Serial.print("Butona basıldı.");
      Serial.print("Sicaklik: ");
      gonder(id,100);
    }
/////////////sıcaklık
  RawValue = analogRead(analogIn); //lm35 ölçümü
  Voltage = (RawValue / 2048.0) * 3300; 
  tempC = Voltage * 0.1;

  Serial.print("\t Temperature in C = ");
  Serial.println(tempC,1);

  delay(100);
  if ((tempC >= 40) && (sicaklik==true)){
      sicaklik=false;
      id = 14187002;
      Serial.print("Sicaklik: ");
      Serial.println(tempC);
      delay(10);
   
      gonder(id,tempC);
    
    }


//////////////////pot
  int sensorValue = analogRead(32);
  Serial.println(sensorValue);
  if ((sensorValue >= 3000) && (pot==true)){
      pot=false;
      id = 14187003;
      Serial.print("Sicaklik: ");
      Serial.println(sensorValue);
      delay(10);
   
   gonder(id,sensorValue);
    }
//////////////////led
  int led1 = analogRead(33);
  Serial.println(led1);
  if ((led1 >= 3000) && (led==true)){
      led=false;
      id = 14187000;
      Serial.print("Sicaklik: ");
      Serial.println(led1);
      delay(10);
   
   gonder(id,led1);
    }
/////////////////////////
 
}
  int gonder(int id, int veri){
    WiFiClient client; // wiVeri göndermeyi başlatmak için.
    giden=id;
    giden +=",";
    giden +=veri;
    Serial.println(giden);
    if (!client.connect(host, port)) {
          Serial.println("Soket baglanamadi.");
          delay(100); 
    }
 
    Serial.println("Baglanti basarili.");
    client.print(giden);
    Serial.println("Kapatiliyor...");
    client.stop();//veri gönderildikten sonra soket kapatılır.
}

