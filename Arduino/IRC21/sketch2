void Avoid_right(){
   Finish_init(); 
   Timer(1000); 
   Go_back(-5);
   Turn_left(-30);
   Timer(2000);
   judge4 = 1;
}

void Avoid_left(){
  Finish_init();
  Timer(1000); 
  Go_back(-5);
  Turn_right(30);
  Timer(2000);
  judge4 = 1;
}

void Adjust_line(){
    attachInterrupt(2, updateEncoderR, CHANGE);
    attachInterrupt(0, updateEncoderR, CHANGE);
    attachInterrupt(3, updateEncoderL, CHANGE);
    attachInterrupt(4, updateEncoderL, CHANGE);
    valR = 0;
    valL = 0;
    pulse = 0;
    pulse1 = 0;
    Go_back(-5);
    Turn_right(30);
    Timer(1500);
    nh.spinOnce();
}

/*[サービスボールのセット]*/
void Prepare(){
   for(ang2 = init_deg2; ang2 >= updeg; ang2 -=1){
    nh.spinOnce();    
    servo2.write(ang2);
    Timer(40);
  }
}

/*[サービスボールの投げ入れ]*/
void Serviceball(){
    distance = 10;
    servo2.write(updeg);      
    Go_straight(distance);
    /*アーム旋回*/
    for(ang1 = init_deg1; ang1 <= servicedeg; ang1 += 1){
      nh.spinOnce();    
      servo1.write(ang1);
      Timer(40);
    }
    Timer(1000);
    /*アーム下降*/
    for(ang2 = updeg; ang2 <= init_deg2; ang2 += 1){
      nh.spinOnce();    
      servo2.write(ang2);
      Timer(40);
    }
    /*アーム上昇*/
    for(ang2 = init_deg2; ang2 >= updeg; ang2 -=1){
      nh.spinOnce();    
      servo2.write(ang2);
      Timer(40);
    }
    /*アーム旋回*/
    for(ang1 = servicedeg; ang1 >= init_deg1; ang1 -=1){
      nh.spinOnce();    
      servo1.write(ang1);
      Timer(40);
    }  
    /*アーム下降*/
    for(ang2 = updeg; ang2 <= init_deg2; ang2 += 1){
      nh.spinOnce();    
      servo2.write(ang2);
      Timer(40);
    }
}

void Linetrace(){
/*ライントレース助走*/
  distance = 40;
  Go_straight(distance);
  detachInterrupt(2);
  detachInterrupt(0);
  detachInterrupt(3);
  detachInterrupt(4);
  detachInterrupt(1);
  detachInterrupt(5);
  judge1 = 0;
  judge2 = 0;
  valR = 0;
  valL = 0;
  Timer(1000);
/*ライントレース*/
  while(1){
    nh.spinOnce();
    val1 = digitalRead(pin11);
    val2 = digitalRead(pin12);
    val3 = digitalRead(pin13);
    val4 = digitalRead(pin14);
    val5 = digitalRead(pin15);
    val6 = digitalRead(pin16);
    val7 = digitalRead(pin17);
    if(val1 == 0 && val2 == 0 && val3 == 0 && val4 == 1 && val5 == 0 && val6 == 0 && val7 == 0){
      //center_black
      analogWrite(pin5,rstd-10); 
      analogWrite(pin6,0);
      analogWrite(pin7,lstd-10); 
      analogWrite(pin8,0); 
      Timer(10);
      flag = 0;
    }
    if(flag == 0 && val1 == 1 && val2== 1 && val3 == 1 && val4 == 1 ){
      //step_black
      flag = 1;
      analogWrite(pin5,rstd-20); 
      analogWrite(pin6,0); 
      analogWrite(pin7,lstd-20); 
      analogWrite(pin8,0); 
      count = count + 1;
      if(count == 3){
        analogWrite(pin5,0); 
        analogWrite(pin6,0); 
        analogWrite(pin7,0); 
        analogWrite(pin8,0);
        Timer(1000);
        break;
      }
    }
    else if(flag == 0 && val4 == 1 && val5 == 1 && val6 == 1 && val7 == 1){
      //step_black
      flag = 1;
      analogWrite(pin5,rstd-20); 
      analogWrite(pin6,0); 
      analogWrite(pin7,lstd-20); 
      analogWrite(pin8,0); 
      count = count + 1;
      if(count == 3){
        analogWrite(pin5,0); 
        analogWrite(pin6,0); 
        analogWrite(pin7,0); 
        analogWrite(pin8,0);
        Timer(1000);
        break;
      }
    }
    else if(flag == 0 && val1 == 1 && val3 == 1 && val5 == 1 && val7 == 1){
      //step_black
      flag = 1;
      analogWrite(pin5,rstd-20); 
      analogWrite(pin6,0); 
      analogWrite(pin7,lstd-20); 
      analogWrite(pin8,0); 
      count = count + 1;
      if(count == 3){
        analogWrite(pin5,0); 
        analogWrite(pin6,0); 
        analogWrite(pin7,0); 
        analogWrite(pin8,0);
        Timer(1000);
        break;
      }
    }
    else if(val1 == 0 && val2 == 0 && val3 == 0 && val4 == 0 && val5 == 0 && val6 == 0 && val7 == 0){
      //all_white
      flag = 0;
      analogWrite(pin5,rstd-20); 
      analogWrite(pin6,0); 
      analogWrite(pin7,lstd-20); 
      analogWrite(pin8,0); 
      Timer(10);
    }
    else if(val1 == 0 && val2 == 0 && val3 == 0 && val4 == 0 && val5 == 1 && val6 == 0 && val7 == 0){
      //turn_left_1
      flag = 0;
      analogWrite(pin5,rstd+10); //+10
      analogWrite(pin6,0); 
      analogWrite(pin7,lstd-10); //-10
      analogWrite(pin8,0); 
      Timer(10);
    }
    else if(val1 == 0 && val2 == 0 && val3 == 0 && val4 == 0 && val5 == 0 && val6 == 1 && val7 == 0){
      //turn_left_2
      flag = 0;
      analogWrite(pin5,rstd+20);//+20
      analogWrite(pin6,0); 
      analogWrite(pin7,lstd-10); //-10
      analogWrite(pin8,0); 
      Timer(10);
    }
    else if(val1 == 0 && val2 == 0 && val3 == 0 && val4 == 0 && val5 == 0 && val6 == 1 && val7 == 1){
      //turn_left_3
      flag = 0;
      analogWrite(pin5,rstd+100);
      analogWrite(pin6,0); 
      analogWrite(pin7,lstd);
      analogWrite(pin8,0); 
      Timer(20);
    }
    else if(val1 == 0 && val2 == 0 && val3 == 0 && val4 == 0 && val5 == 0 && val6 == 0 && val7 == 1){
      //turn_left_4
      flag = 0;
      analogWrite(pin5,rstd+110);
      analogWrite(pin6,0); 
      analogWrite(pin7,lstd);
      analogWrite(pin8,0); 
      Timer(50);  
    }
    else if(val1 == 0 && val2 == 0 && val3 == 1 && val4 == 0 && val5 == 0 && val6 == 0 && val7 == 0){
      //turn_right_1
      flag = 0;
      analogWrite(pin5,rstd-10); //-10
      analogWrite(pin6,0); 
      analogWrite(pin7,lstd+10); //+10
      analogWrite(pin8,0); 
      Timer(10);
    }
    else if(val1 == 0 && val2 == 1 && val3 == 0 && val4 == 0 && val5 == 0 && val6 == 0 && val7 == 0){
      //turn_right_2
      flag = 0;
      analogWrite(pin5,rstd-10); //-10
      analogWrite(pin6,0); 
      analogWrite(pin7,lstd+20);//+20
      analogWrite(pin8,0); 
      Timer(10);
    }
    else if(val1 == 1 && val2 == 1 && val3 == 0 && val4 == 0 && val5 == 0 && val6 == 0 && val7 == 0){
      //turn_right_3
      flag = 0;
      analogWrite(pin5,0); 
      analogWrite(pin6,rstd+50);
      analogWrite(pin7,lstd+50);
      analogWrite(pin8,0);   
      Timer(200);
    }
    else if(val1 == 1 && val2 == 0 && val3 == 0 && val4 == 0 && val5 == 0 && val6 == 0 && val7 == 0){
      //turn_right_4
      flag = 0;
      analogWrite(pin5,0);
      analogWrite(pin6,rstd+80); 
      analogWrite(pin7,lstd+80);
      analogWrite(pin8,0); 
      Timer(300);
    }
    else{
      analogWrite(pin5,rstd); 
      analogWrite(pin6,0); 
      analogWrite(pin7,lstd); 
      analogWrite(pin8,0);
    }
}
}

/*[ボールに近づく]*/
void Approach(int distance, int degree){
  valR = 0;
  valL = 0;
  pulse = 0;
  pulse1 = 0;

/*旋回*/
  if(degree >= 0) {
    if(degree < 3){
      degree = 3;
    }
    Turn_right(degree);
  }  
  else if(degree < 0){
    if(degree > -3){
      degree = -3;
    }
    Turn_left(degree);
  }

/*前進・後退*/
  if(distance >= 0){
    if(distance < 3){
      distance = 3;
    }
    Go_straight(distance);
  }
  else if(distance < 0){
    if(distance > -3){
      distance = 0;
    }
    Go_back(distance);
  }
}


/*ゴール方向への左旋回*/
void Turnadd_left(int goal){
  theta = 135 - goal;
  if(theta > 175){
    degree = theta - 175;
    degree = -degree;
    Turn_left(degree);
    theta = 175;
  } 
   for(ang1 = init_deg1; ang1 <= theta; ang1 += 1){
    nh.spinOnce();
    servo1.write(ang1);
    Timer(40);
  }
}

/*ゴール方向への右旋回ver2*/
void Turnadd_right2(int goal){
  diff = -goal - 180;
  theta = 135 - 180 + diff;
  degree = -theta + 5;
  theta = 5;
  Turn_right(degree);
   for(ang1 = init_deg1; ang1 >= theta; ang1 -= 1){
    nh.spinOnce();
    servo1.write(ang1);
    Timer(40);
   }
}

/*ゴール方向への右旋回*/
void Turnadd_right(int goal){
  theta = 135 - goal;
  if(theta < 5){
    degree = -theta + 5;
    theta = 5;
    Turn_right(degree);
  }
  for(ang1 = init_deg1; ang1 >= theta; ang1 -= 1){
    nh.spinOnce();
    servo1.write(ang1);
    Timer(40);
  }
 }
 
/*[ボールを射出]*/
void Shoot(){
    degS=355, pulseS=0;
    pulseS = degS * 11500 / 360; //11500[ppr]
    servo1.detach();
    while(1){
        nh.spinOnce();
        if(valS >= pulseS){
          digitalWrite(shoot,LOW);
          degS=0;
          valS=0; 
          pulseS=0;
          Timer(1000);
          break;
        }
        else{
          digitalWrite(shoot,HIGH);
          Timer(10);
        }
      }
}

/*[射出動作]*/
void Arm_turning(int goal,int area){
  attachInterrupt(1, updateEncoderS, CHANGE);
  attachInterrupt(5, updateEncoderS, CHANGE);
  theta = 0;
  nh.spinOnce();
  if(goal >= 0){
    Turnadd_right(goal);
  }else if(goal <= -135){
    Turnadd_right2(goal);
  }else if(goal < 0){
    Turnadd_left(goal);
  }
  Timer(1000);

  if(area == 1){
    for(ang2 = updeg; ang2 >= updeg -5; ang2 -= 1){
    nh.spinOnce();
    servo2.write(ang2);
    Timer(40);
    }
  }
  
  Shoot();
  
  servo1.attach(5);
  Timer(500);
  nh.spinOnce();

  /*アームを正面に戻す*/
  if(theta <= init_deg1){
    for(ang1 = theta; ang1 <= init_deg1; ang1 +=1){
      nh.spinOnce();
      servo1.write(ang1);
      Timer(40);
    }  
  }else if(theta > init_deg1){
    for(ang1 = theta; ang1 >= init_deg1; ang1 -=1){
      nh.spinOnce();;
      servo1.write(ang1);
      Timer(40);
    }  
  }
  
  Timer(500);
  /*アーム下降*/
  if(area == 1){
     for(ang2 = updeg -5; ang2 <= init_deg2; ang2 += 1){
      nh.spinOnce();
      servo2.write(ang2);
      Timer(40);
    }
  }
  else if(area == 0){
    for(ang2 = updeg; ang2 <= init_deg2; ang2 += 1){
      nh.spinOnce();
      servo2.write(ang2);
      Timer(40);
    }
  }
  
}

/*[リミットセンサが反応しアームを上昇]*/
void Rising(){
  /*アームを正面に戻す*/
  if(ang1 <= init_deg1){
    for(ang1 = ang1; ang1 <= init_deg1; ang1 +=1){
      nh.spinOnce();
      servo1.write(ang1);
      Timer(40);
    }  
  }else if(ang1 > init_deg1){
    for(ang1 = ang1; ang1 >= init_deg1; ang1 -=1){
      nh.spinOnce();
      servo1.write(ang1);
      Timer(40);
    }  
  }
  
  Timer(500);
  /*アーム上昇*/
  for(ang2 = downdeg; ang2 >= updeg; ang2 -=1){
    nh.spinOnce();
    servo2.write(ang2);
    Timer(40);
  }
  digitalWrite(vacuum,LOW);
  nh.spinOnce();
}


void Limit(){
  //int KKK;
      while(1){
      nh.spinOnce();
      val8 = digitalRead(limit);
      if (val8 == 1){
          judge3 = 1;
          Timer(500);
          val8 = 0;
          countV = 0;
          nh.spinOnce();
    
          Rising();
          k = 1;
          //KKK = 1;
          break;
        }else{
          Timer(5);
          judge3 = 0;
          countV = countV + 1;
          if(countV == 20){
            countV = 0;
            break;
          }
          //KKK=0;
        }
      }
      //return KKK;
}

void Press(){
  for(ang2 = ang2; ang2 >= init_deg2; ang2 -=1){
    nh.spinOnce();
    servo2.write(ang2);
    Timer(40);
  }
  distance = -5;
  Go_back(distance);
  Timer(2000);
  temporary.data = COLOR;
  stand_by2.publish(&temporary); 
}
   

/*[吸引動作]*/
void Suction(){
  nh.spinOnce();
  val_press = 300;
  for(ang2 = init_deg2; ang2 <= downdeg -10; ang2 +=1){
    nh.spinOnce();
    servo2.write(ang2);
    val_press = analogRead(pres);
    if(val_press == 0){
          countP = countP + 1;
          if(countP == 5){
            Press();
            Timer(1000);
            countP = 0;
          }
        }
    Timer(40);
   }
   for(ang2 = downdeg -10; ang2 <= downdeg; ang2 += 1){
        nh.spinOnce();
        servo2.write(ang2);
        Timer(40);
    }
  digitalWrite(vacuum,HIGH);
  /*アームを左に首振り*/
  for(ang1 = init_deg1; ang1 <= init_deg1+10; ang1 +=1){
      nh.spinOnce();
      servo1.write(ang1);
      Limit();
      if (k == 1){
      goto label;
      }
  }
   /*アームを右に首振り*/
   for(ang1 = init_deg1+10; ang1 >= init_deg1-10; ang1 -=1){
      nh.spinOnce();
      servo1.write(ang1);
       Limit();
      if (k == 1){
      goto label;
      }
  }

  /*アームを正面に戻す*/
  for(ang1 = init_deg1-10; ang1 <= init_deg1; ang1 +=1){
      nh.spinOnce();
      servo1.write(ang1);
       Limit();
      if (k == 1){
      goto label;
      }
  }
  digitalWrite(vacuum,LOW);
 
  /*アーム上昇*/
  for(ang2 = downdeg; ang2 >= init_deg2; ang2 -=1){
        nh.spinOnce();
        servo2.write(ang2);
        Timer(40); 
   }

 label:
  if (k == 1){
    judge3 =1;
     k =0;
     rotation.data = 1;
     stand_by3.publish(&rotation);
  }
  else {
    judge3  = 0;
  }
   
}


void order1(const std_msgs::Int16 &message){
  const int Separation = message.data;
  if(Separation == 0){
   Prepare();
  }
  else if(Separation == 1){
    Serviceball();
    Linetrace();
    Adjust_line();
    Timer(2000);
    nh.spinOnce();
    Timer(1000);
    nh.spinOnce();
    wait_ball.data = 1;
    stand_by1.publish(&wait_ball);
  }
}

void order2(const geometry_msgs::Twist &message){
  const int special_distance = message.linear.x;
  const int special_color = message.linear.z;
  const int special_degree = message.angular.z;
  COLOR = special_color;  
  Approach(special_distance, special_degree);

  Timer(2000);
  temporary.data = special_color;
  stand_by2.publish(&temporary); 
  nh.spinOnce();
                       
  if (judge4 == 0){
  Suction();
  }
  
  if(judge3 == 0 || judge4 == 1){
    judge4 = 0;
    wait_ball.data = 1;
    stand_by1.publish(&wait_ball);
  }
}

void order3(const geometry_msgs::Twist &message){
  const int Turn_angle = message.linear.x;
  const int special_area = message.angular.x;
  judge3 = 0;
  
  Arm_turning(Turn_angle,special_area);
  
  Timer(2000);
  nh.spinOnce();
  wait_ball.data = 1;
  stand_by1.publish(&wait_ball);
}

ros::Subscriber<std_msgs::Int16> signal_to_start("/control", &order1);
ros::Subscriber<geometry_msgs::Twist> Destination("/ball_xy", &order2);
ros::Subscriber<geometry_msgs::Twist> Turn("/goal_theta", &order3);

void setup(){
  pinMode(pin1, INPUT);
  pinMode(pin2, INPUT);
  pinMode(pin3, INPUT);
  pinMode(pin4, INPUT);
  pinMode(enA, INPUT);
  pinMode(enB, INPUT);
  pinMode(pin5,OUTPUT); 
  pinMode(pin6,OUTPUT); 
  pinMode(pin7,OUTPUT); 
  pinMode(pin8,OUTPUT); 
  attachInterrupt(0, updateEncoderR, CHANGE);
  attachInterrupt(2, updateEncoderR, CHANGE);
  attachInterrupt(4, updateEncoderL, CHANGE);
  attachInterrupt(3, updateEncoderL, CHANGE);
  attachInterrupt(1, updateEncoderS, CHANGE);
  attachInterrupt(5, updateEncoderS, CHANGE);  
  digitalWrite(pin1, HIGH);
  digitalWrite(pin2, HIGH);
  digitalWrite(pin3, HIGH);
  digitalWrite(pin4, HIGH);
  digitalWrite(enA, HIGH);
  digitalWrite(enB, HIGH);
  pinMode(pin11,INPUT); 
  pinMode(pin12,INPUT); 
  pinMode(pin13,INPUT); 
  pinMode(pin14,INPUT); 
  pinMode(pin15,INPUT);
  pinMode(pin16,INPUT); 
  pinMode(pin17,INPUT);
  servo1.attach(5);  //方位角
  servo2.attach(8);  //仰角  
  servo1.write(init_deg1);
  servo2.write(init_deg2);   
  pinMode(vacuum,OUTPUT); //vacuum
  pinMode(limit,INPUT_PULLUP);
  pinMode(shoot,OUTPUT);  //shoot
  nh.initNode();
  nh.advertise(stand_by1);
  nh.advertise(stand_by2);
  nh.advertise(stand_by3);
  nh.subscribe(Destination);
  nh.subscribe(signal_to_start);
  nh.subscribe(Turn);
}

void loop(){
  nh.spinOnce();
  Timer(1);
}
