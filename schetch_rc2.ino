#define ENABLE_A  10  // on pwm 10
#define IN1_A  9   
#define IN2_A  8   
#define ENABLE_B  5  // on PWM 5
#define IN3_B  7   
#define IN4_B  6   
  
byte speedDC = 255;  
  
void setup()  
{  
  pinMode(ENABLE_A,OUTPUT);  
  pinMode(IN1_A,OUTPUT);  
  pinMode(IN2_A,OUTPUT);  
   pinMode(ENABLE_B,OUTPUT);  
  pinMode(IN3_B,OUTPUT);  
  pinMode(IN4_B,OUTPUT);  
}  
  
void motor_speed(int spd)  
{  
  analogWrite(ENABLE_A,spd);  
  analogWrite(ENABLE_B,spd);  
}  
  
void motor_dir(int dir)  
{  
  if ( dir == 0 ) {  // forward   
     digitalWrite(IN1_A,HIGH);  
     digitalWrite(IN2_A,LOW);  
     digitalWrite(IN3_B,HIGH);  
     digitalWrite(IN4_B,LOW);  
  }  
  else if ( dir == 1 ) { // turn right  
     digitalWrite(IN1_A,HIGH);  
     digitalWrite(IN2_A,LOW);  
     digitalWrite(IN3_B,LOW);  
     digitalWrite(IN4_B,HIGH);  
  }  
  else if ( dir == 2 ) { // turn left  
     digitalWrite(IN1_A,LOW);  
     digitalWrite(IN2_A,HIGH);  
     digitalWrite(IN3_B,HIGH);  
     digitalWrite(IN4_B,LOW);  
  }    
  else if ( dir == 4 ) { // backward  
     digitalWrite(IN1_A,LOW);  
     digitalWrite(IN2_A,HIGH);  
     digitalWrite(IN3_B,LOW);  
     digitalWrite(IN4_B,HIGH);  
  }     
}  
  
void loop()  
{  
  motor_dir(0);  
  for ( int i = 0; i < 100; i++ ) {  
      motor_speed(i);  
      delay(100);  
  }  
  motor_speed(30);  
  motor_dir(1);  
  delay(500);  
  motor_dir(0);  
  delay(3000);   
}  
