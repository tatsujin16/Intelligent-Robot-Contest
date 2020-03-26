#include<MsTimer2.h>
#include<Servo.h>
#include<Arduino.h>
#include<ros.h>
#include<geometry_msgs/Twist.h>
ros::NodeHandle nh;
Servo servo1,servo2;
volatile boolean tim1msF = false;
int count_time=0, count=0, n;
int pin5 = 11;
int pin6 = 12;
int pin7 = 6;
int pin8 = 7;
int shoot = 14;
int vacuum = 15;
int a,b,c,d;
int e = 0, f = 0, g = 0, h = 0;
int flag1 = 0, flag2 = 0;
int ang1,ang2;
int updeg = 75;
int downdeg = 143;
int goal = 50;
int init_deg1 = 135;
int init_deg2 = 100;

/*[タイマー割込み(n秒)]*/
void timer1mS(){
  tim1msF = true;
}
int Timer(int n){
  MsTimer2::set(1, timer1mS);
  MsTimer2::start();
  while(count_time <= n){
    if(tim1msF){
      count_time = count_time + 1;
      tim1msF = false;
    }
  }
  MsTimer2::stop();
  tim1msF = false;
  count_time = 0;
  return 0;
}

void Move_front(int a, int b){
  a = a - 105;
  b = b - 100;
  analogWrite(pin5,a);
  analogWrite(pin6,0);
  analogWrite(pin7,b);
  analogWrite(pin8,0); 
  Timer(5); 
}

void Move_back(int a, int b){
  a = -a - 105;
  b = -b - 100;
  analogWrite(pin5,0);
  analogWrite(pin6,a);
  analogWrite(pin7,0);
  analogWrite(pin8,b); 
  Timer(5); 
}

void Turn_right(int c, int d){
  c = -c ;
  d = -d ;
  analogWrite(pin5,0);
  analogWrite(pin6,c);
  analogWrite(pin7,d);
  analogWrite(pin8,0); 
  Timer(5); 
}

void Turn_left(int c, int d){
  c = c - 50;
  d = d - 50;
  analogWrite(pin5,c);
  analogWrite(pin6,0);
  analogWrite(pin7,0);
  analogWrite(pin8,d); 
  Timer(5); 
}

void Stop(){
  analogWrite(pin5,0);
  analogWrite(pin6,0);
  analogWrite(pin7,0);
  analogWrite(pin8,0); 
  Timer(50); 
}

void Arm_turn(){
  for(ang1 = init_deg1; ang1 >= goal; ang1 -= 1){
    nh.spinOnce();
    servo1.write(ang1);
    Timer(40);
  }
  flag1 = 1;
}

void Arm_return(){
  for(ang1 = goal; ang1 <= init_deg1; ang1 += 1){
    nh.spinOnce();
    servo1.write(ang1);
    Timer(40);
  }
  flag1 = 0;
}

void Arm_up(){
  for(ang2 = init_deg2; ang2 >= updeg; ang2 -= 1){
    nh.spinOnce();
    servo2.write(ang2);
    Timer(40);
  }
  flag2 = 1;
}

void Arm_down(){
  for(ang2 = updeg; ang2 <= init_deg2; ang2 += 1){
    nh.spinOnce();
    servo2.write(ang2);
    Timer(40);
  }
  flag2 = 0;
}

void Vacuum_on(){
   digitalWrite(vacuum,HIGH);
}

void Vacuum_off(){
  digitalWrite(vacuum,LOW);
}

void Shoot_on(){
  digitalWrite(shoot,HIGH);
}

void Shoot_off(){
  digitalWrite(shoot,LOW);
}



void order1(const geometry_msgs::Twist &message){
  const float front_back = message.linear.x;
  const int servo_updown = message.linear.y;
  const int servo_turn = message.angular.x;
  const int servo_return = message.angular.y;
  const float right_left = message.angular.z;
  
  nh.spinOnce();
  a = front_back;
  b = front_back;
  c = right_left;
  d = right_left; 
  e = servo_turn;
  f = servo_return;
  g = servo_updown;
  
  if(front_back > 0){
    Move_front(a,b);
    }
  else if(front_back < 0){
    Move_back(a,b);
    }
  else if(right_left < 0){
    Turn_right(c,d);
    }
  else if(right_left > 0){
    Turn_left(c,d);
    }
  else {
    Stop();
    }
    
  if(e == 1 && flag1 == 0){
    Arm_turn();
  }
  else if(f == 1 && flag1 == 1){
    Arm_return();
  }
  else if(g == 1 && flag2 == 0){
    Arm_up();
  }
  else if(g == -1 && flag2 == 1){
    Arm_down();
  }
  
  nh.spinOnce();
}
ros::Subscriber<geometry_msgs::Twist> Destination("/control", &order1);
void setup() {
   pinMode(pin5,OUTPUT);
   pinMode(pin6,OUTPUT);
   pinMode(pin7,OUTPUT);
   pinMode(pin8,OUTPUT);
   pinMode(shoot,OUTPUT);
   pinMode(vacuum,OUTPUT);
   servo1.attach(5);  //方位角
   servo2.attach(8);  //仰角  
   servo1.write(init_deg1);
   servo2.write(init_deg2);
   nh.initNode(); 
   nh.subscribe(Destination);
}

void loop() {
  nh.spinOnce();
  Timer(1);
}
