void setup(){
      pinMode( 2, OUTPUT);
      pinMode( 3, OUTPUT);
      pinMode( 4, OUTPUT);
      pinMode( 5, OUTPUT);
      pinMode( 6, OUTPUT);
      pinMode( 7, OUTPUT);
      pinMode( 8, OUTPUT);
      pinMode( 9, OUTPUT);
      pinMode(10, OUTPUT);
      pinMode(11, OUTPUT);
}

void loop(){
  int n, a;
  n = random(2,12);
  a = random(0,2);
  /*if (a){
    digitalWrite(n,HIGH);
  }else{
    digitalWrite(n,LOW);
  }*/
  
  digitalWrite(n,a);
  
  delay(300);
}
