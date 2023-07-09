#include <LiquidCrystal.h>
#include <SoftwareSerial.h>

const int rs = 12, en = 11, d4 = 6, d5 = 5, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

SoftwareSerial HC06(10,4);

int motor = 46;
int Foco1 = 47;
int libre1 = 48;
int Foco2 = 49;
int libre2 = 50;
int contacto1= 51;
int libre3 = 52;
int contacto2= 53;
int option;
int a=0;
int r=0;
int TRled=7;
int TGled=8;
int TBled=9;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  HC06.begin(9600);
  pinMode(Foco1, OUTPUT);
  pinMode(Foco2, OUTPUT);
  pinMode(contacto1, OUTPUT);
  pinMode(contacto2, OUTPUT);
  pinMode(libre1, OUTPUT);
  pinMode(libre2, OUTPUT);
  pinMode(motor, OUTPUT);
  pinMode(libre3, OUTPUT);
  pinMode(TRled, OUTPUT);
  pinMode(TGled, OUTPUT);
  pinMode(TBled, OUTPUT); 
  pinMode(LED_BUILTIN, OUTPUT);
  lcd.begin(16, 2); 
}

void loop() {

  if (HC06.available() > 0){
    option = HC06.read();
    Serial.println(option);
    lcd.clear();
    
      if(option == 1){
     
        lcd.write("    encendido   ");
        lcd.setCursor(0,1);
        lcd.write("      foco1     ");
        digitalWrite(Foco1, LOW);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        }

      if(option == 2){
        lcd.write("    encendido   ");
        lcd.setCursor(0,1);
        lcd.write("      foco2     ");
        digitalWrite(Foco2, LOW);
        delay(50);
        }  
      if(option == 3){
        lcd.write("    encendido   ");
        lcd.setCursor(0,1);
        lcd.write("    contacto1   ");
        digitalWrite(contacto1, LOW);
        delay(50);
        }

      if(option == 4){
        lcd.write("    encendido   ");
        lcd.setCursor(0,1);
        lcd.write("    contacto2   ");
        digitalWrite(contacto2, LOW);
        delay(50);
        } 
      if(option == 5){
        lcd.write("    encendido   ");
        lcd.setCursor(0,1);
        lcd.write("      motor     ");
          digitalWrite(motor, LOW);
          delay(50);
        }

      if(option == 6){
        
        digitalWrite(libre1, LOW);
        delay(50);
        }  
      if(option == 7){
          digitalWrite(libre2, LOW);
          delay(50);
        }

      if(option == 8){
          digitalWrite(libre3, LOW);
          delay(50);
        }
      if(option == 9){
          lcd.write("    encendido   ");
          lcd.setCursor(0,1);
          lcd.write("    tira led    ");
          analogWrite(TRled, random(0,255));
          analogWrite(TGled, random(0,255));
          analogWrite(TBled, random(0,255));
          delay(50);
        }
      if(option == 10){
          lcd.write("     apagado    ");
          lcd.setCursor(0,1);
          lcd.write("    tira led    ");
          analogWrite(TRled, 0);
          analogWrite(TGled, 0);
          analogWrite(TBled, 0);
        }      
        
   
    if(option == 11){
      lcd.write("     apagado    ");
      lcd.setCursor(0,1);
      lcd.write("      foco1     ");
      digitalWrite(Foco1, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    
    if(option == 12){
      lcd.write("     apagado    ");
      lcd.setCursor(0,1);
      lcd.write("      foco2     ");
      digitalWrite(Foco2, HIGH);
    }
    if(option == 13){
      lcd.write("     apagado    ");
      lcd.setCursor(0,1);
      lcd.write("    contacto1   ");
      digitalWrite(contacto1, HIGH);
    }
    
    if(option == 14){
      lcd.write("     apagado    ");
      lcd.setCursor(0,1);
      lcd.write("    contacto2   ");
      digitalWrite(contacto2, HIGH);
    }
    if(option == 15){
      lcd.write("     apagado    ");
      lcd.setCursor(0,1);
      lcd.write("      motor     ");
      digitalWrite(motor, HIGH);
    }
  }
}
