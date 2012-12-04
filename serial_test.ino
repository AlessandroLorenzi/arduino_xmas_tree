// sketch per studiare l uso della seriale

 


void setup(void){
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);

  Serial.println(0+1*100.00);
}

void loop(void){
 String readString;
 int convertedString;

 while (Serial.available()>0) {
  // read the incoming byte:
  delay (10);
  if( Serial.available()>0)
  {
     char c = Serial.read();
     readString += c;
  }
 }
 
  
 
 if(readString!=0)
 {
   convertedString = string_atoi(readString);
   if (convertedString < 100)
     digitalWrite(convertedString+2, HIGH);
   else
     digitalWrite(convertedString-100+2, LOW);

 }

  
}

int string_atoi(String inputstring)
{
   int converted=0;
   
   if (inputstring.length()>2) converted=1;

   for (int counter = 0 ; counter <= inputstring.length()-1 ; counter++ ) {
     char c = inputstring.charAt(counter);
     if (!isdigit(c)) return -1;
     c-=48;
     converted += c*(pow(10,inputstring.length()-counter-1));

   }
   
   return converted;

}
