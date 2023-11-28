# Global-Solution-1-semestre
Projetos para a Global solution 1º semestre

Descrição do problema:

  A ausência de um sistema de contagem de pessoas em hospitais (entradas, salas de espera, pronto-soccoro), pode causar diversos problemas como:
  
Falta de gestão de Fluxo de Pacientes:
  Sem um sistema de contagem de pessoas, os hospitais podem ter dificuldade em gerenciar eficientemente o fluxo de pacientes, levando a congestionamentos e possíveis atrasos nos atendimentos.
  
Controle de Infecções:
  Em situações de surto de doenças contagiosas ou até mesmo pandemias, como a Covid-19, é essencial monitorar o número de pessoas presentes em um local, pois assim é possível tomar medidas, como a utilização de máscaras, para diminuir os riscos de contaminação dos pacientes e seus acompanhantes. 
  
Eficiência no Planejamento de Recursos:
  Um sistema de contagem de pessoas ajuda na gestão eficaz dos recursos hospitalares, permitindo a alocação adequada de pessoal, leitos e equipamentos conforme a demanda.


Solução: 

  Nossa proposta é um sistema baseado em Arduino projetado para monitorar e controlar o fluxo de pessoas que entram em um hospital. Ele busca otimizar o gerenciamento de dados relacionados à entrada de pacientes, acompanhantes, visitantes e funcionários, proporcionando uma solução eficiente e automatizada. Além disso, pode ser programado para soar alertas quando um a capacidade determinada de um local passe do indicado. Garantindo assim, que todos que frequentem os ambientes tenham a consiência dos riscos e recomendações de proteção que devem ser seguidas para evitar contaminações. Os dados gravados na memória interna do Arduino também podem ser recuperados e analisados. Por exemplo, no controle de pessoas que frequentam os hospitais, para depois concluirmos os dias da semanas com menos pessoas e tempo de espera e realizar uma logística melhor de atendimentos. 
  Um sistema de contagem de pessoas nos hospitais pode oferecer diversos benefícios em termos de eficiência operacional, segurança e qualidade do atendimento ao paciente.

Instruções:

Para utilizar o dispositivo, basta conectar o Arduino. O funcionamento é bastante intuitivo. Quando um objeto passa em frente ao sensor ultrassônico, este é detectado e a informação (quantidade de pessoas) é exibida no display de LED. A cada detecção, o sistema soma, exibe o total no visor e ascende o led. Ao atingir uma determinada quantidade crítica de pessoas em um ambiente (número pré definido de acordo com as necessidades), um buzzer é acionado para alertar todos que as taxas de contaminação são mais altas. Se desejar reiniciar a contagem, há um botão para isso, um simples clique reinicia o sistema, zerando os números e iniciando a contagem novamente.

Link Projeto:

https://www.tinkercad.com/things/453vZOZvMxK-contador-de-pessoas-gs-1-semestre?sharecode=T9zbAoFqD7RMqpOttFrz3fbFsKemJMCvWRSBlvWj1dw


Código fonte: 

#include <LiquidCrystal.h>

LiquidCrystal lcd(3, 2, 4, 5, 6, 7);
const int sinal = 8;
const int led_red = 9;
const int reset = 11;
const int buzzerPin = 10; // Substitua 10 pelo pino que você está usando para o buzzer
int cont = 0;
int x = 0;
int y = 0;

void setup() {
  pinMode(led_red, OUTPUT);
  pinMode(buzzerPin, OUTPUT); // Configurar o pino do buzzer como saída
  lcd.begin(16, 2);
  Serial.begin(9600);
  intro();
}

void loop() {
  pinMode(sinal, OUTPUT);
  digitalWrite(sinal, LOW);
  delayMicroseconds(2);
  digitalWrite(sinal, HIGH);
  delayMicroseconds(5);
  pinMode(sinal, INPUT);
  long duracao = pulseIn(sinal, HIGH);

  float dist_metros = duracao * 0.0001715;

  Serial.println(dist_metros);

  if (dist_metros >= 0.30 && dist_metros <= 3.0) {
    x = 1;
  } else {
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

  if (digitalRead(reset) == HIGH) {
    cont = 0;
  }
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

  if (cont >= 15) {
    // Ativar o buzzer
    tone(buzzerPin, 1000); // 1000 Hz
  } else {
    // Desativar o buzzer
    noTone(buzzerPin);
  }
}
