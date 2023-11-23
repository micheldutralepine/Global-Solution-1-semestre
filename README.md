# Global-Solution-1-semestre
Projetos para a Global solution 1º semestre

Descrição do problema:



Solução: 

  Prosta é um sistema baseado em Arduino projetado para monitorar e controlar o fluxo de pessoas que entram em um hospital. Ele visa otimizar o gerenciamento de dados relacionados à entrada de pacientes, visitantes e funcionários, proporcionando uma solução eficiente e automatizada. Os dados gravados na memória interna do Arduino podem ser posteriormente recuperados e analisados. Por exemplo, no controle de pessoas que frequentam os hospitais para depois concluirmos os dias da semanas com menos pessoas e tempo de espera, pode usar um sistema de controle de dados para controlar o acesso a um determinado local. Entre outras diversas aplicações e controles poderiam ser feitos com este sistema. 

instruções:

Para utilizar o dispositivo, basta conectar o Arduino. O funcionamento é bastante intuitivo. Quando um objeto passa em frente ao sensor ultrassônico, este é detectado e a informação é exibida no display de LED. A cada detecção, o sistema soma e exibe o total no visor. Se desejar reiniciar a contagem, há um botão para isso. Um simples clique reinicia o sistema, zerando os números e iniciando a contagem novamente.

Link Projeto:

https://www.tinkercad.com/things/453vZOZvMxK-contador-de-pessoas-gs-1-semestre?sharecode=T9zbAoFqD7RMqpOttFrz3fbFsKemJMCvWRSBlvWj1dw


Código fonte: 

#include<LiquidCrystal.h>                                
LiquidCrystal lcd(3, 2, 4, 5, 6, 7);                   
int const sinal = 8;                                     
int const led_red = 9;                                     
int const reset = 11;                                     
int cont = 0, x = 0, y = 0, i = 0, m1 = 0, m2 = 0;       
long duracao;                                            
void setup()
{
  pinMode(led_red, OUTPUT);                                
  lcd.begin(16, 2);                                      
  Serial.begin(9600);                                   
  intro();                                               
}

void loop()
{
  pinMode(sinal, OUTPUT);                                
  digitalWrite(sinal, LOW);                              
  delayMicroseconds(2);                                 
  digitalWrite(sinal, HIGH);                             
  delayMicroseconds(5);                                  
  pinMode(sinal, INPUT);                                 
  duracao = pulseIn(sinal, HIGH);


  float dist_metros = duracao * .0001715;                

  Serial.println(dist_metros);                                                                   
  if (dist_metros >= 0.30 && dist_metros <= 3.0)         
    x = 1;                                               

  else {                                                 
    x = 0;                                               
    y = 1;                                               
    digitalWrite(led_red, LOW);                            
  }
  if (x == 1 && y == 1) {                                
    cont++;                                              
    y = 0;                                               
    digitalWrite(led_red, HIGH);                           
  }

  Serial.println(cont);                                  

  contador();                                            
                                           
  if (digitalRead(reset) == HIGH)                        
    cont = 0;                                            

}

void intro() {
  lcd.print("Conta Pessoas");
  delay(1000);
  lcd.clear();
}

void contador() {
  lcd.clear();
  lcd.setCursor(1, 0);
  lcd.print("Pessoas= ");
  lcd.setCursor(9, 0);
  lcd.print(cont);
}

