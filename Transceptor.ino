#include <SoftwareSerial.h>
SoftwareSerial HC05(3,10);

int option;
int a=0;
int r=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  HC05.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
   
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    option = Serial.read();
    Serial.println(option);

    
      if(option == 'A'){
        HC05.write(1);
        Serial.println("se mando");
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        }

      if(option == 'B'){
        HC05.write(2);
        delay(50);
        }  
      if(option == 'C'){
        HC05.write(3);
        delay(50);
        }

      if(option == 'D'){
        HC05.write(4);
        delay(50);
        } 
      if(option == 'E'){
        HC05.write(5);
          delay(50);
        }

      if(option == 'F'){
        
        HC05.write(6);
        delay(50);
        }  
      if(option == 'G'){
          HC05.write(7);
          delay(50);
        }

      if(option == 'H'){
          HC05.write(8);
          delay(50);
        }
      if(option == 'I'){
          HC05.write(9);
          delay(50);
        }
      if(option == 'U'){
          HC05.write(10);
          delay(50);
        }      
        
   
    if(option == 'Z'){
      HC05.write(11);
      digitalWrite(LED_BUILTIN, LOW);
    }
    
    if(option == 'Y'){
      HC05.write(12);
    }
    if(option == 'X'){
      HC05.write(13);
    }
    
    if(option == 'W'){
      HC05.write(14);
    }
    if(option == 'V'){
      HC05.write(15);
    }
  }
}
