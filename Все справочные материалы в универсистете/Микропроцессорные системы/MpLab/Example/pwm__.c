/*

Краткий курс AVR - первые шаги  http://avr123.nm.ru

Генерация ШИМ на ножке PD5  ATmega16
  
project for testing PWM code for PD5 ATmega16 with VMLAB simulation

==============================       

UART  115200   8N1  out PD1

Chip type           : ATmega16
Program type        : Application
Clock frequency     : 7,37 MHz
Memory model        : Small
External SRAM size  : 0
Data Stack size     : 256 
*/

#include <mega16.h> 
#include <m8_128.h> //   http://avr123.nm.ru/m8_128.h 
#include <delay.h>
#include <stdio.h>  



// Declare your global variables here 

char pwm = 10; // Величина ШИМ начальная PWM в %

u32 pwm_val; // для хранения величины ШИМ PWM в  1/1024

// unsigned long int pwm_val; если у вас нет файла: w/o  m8_128.h

void main(void)
{
// Declare your local variables here

// Input/Output Ports initialization
PORTA=0x00;
DDRA=0x00;

PORTB=0x00;  
DDRB=0x00;

PORTC=0x00;
DDRC=0x00;

// Port D initialization
PORTD=0x00;
DDRD=0x20; // 0010 0000   PD5 (OC1A) - PWM Timer1 OUT  

// Timer/Counter 0 initialization
// Clock source: 
// Clock value: 
TCCR0=0x00;  
TCNT0=0x00;
OCR0=0x00;
                

//PWM 

//TIMER1 initialize - prescale:1
// WGM: 7) PWM 10bit fast, TOP=0x03FF
// actual value: 7200,000Hz (100,0%)

 TCCR1B = 0x00; //stop Timer
 
 TCNT1H = 0xFC; //setup
 TCNT1L = 0x01; 
 
 //  +++++++++++++++++++++++++++++++++++++
 OCR1AH = 0x03; // PWM(PD5) = OCR1A / 10.23  (%) 
 OCR1AL = 0xFF; 
 //  +++++++++++++++++++++++++++++++++++++
 
 OCR1BH = 0x03;
 OCR1BL = 0xFF;

 ICR1H  = 0x03;
 ICR1L  = 0xFF;  
 
 TCCR1A = 0x83; 
 
 TCCR1B = 0x09; //start Timer


// USART initialization
// Communication Parameters: 8 Data, 1 Stop, No Parity
// USART Receiver: Off
// USART Transmitter: On
// USART Mode: Asynchronous
// USART Baud rate: 115200      7.37 MHz
UCSRA=0x00;
UCSRB=0x08;
UCSRC=0x86;
UBRRH=0x00;
UBRRL=0x03;



// Timer/Counter 2 initialization
// Clock source: System Clock
// Clock value: Timer 2 Stopped
// Mode: Normal top=FFh
// OC2 output: Disconnected
ASSR=0x00;
TCCR2=0x00;
TCNT2=0x00;
OCR2=0x00;

// External Interrupt(s) initialization
// INT0: Off
// INT1: Off
// INT2: Off
MCUCR=0x00;
MCUCSR=0x00;

// Timer(s)/Counter(s) Interrupt(s) initialization
TIMSK=0x00;

// Analog Comparator initialization
// Analog Comparator: Off
// Analog Comparator Input Capture by Timer/Counter 1: Off
ACSR=0x80;
SFIOR=0x00;


// Global enable interrupts
// #asm("sei") 
// эта программа не использует прервания.

while (1){

      // Place your code here 
      
if (pwm > 102) { //если ШИМ уже более 100 %
       pwm = 0;  // обнулить величину ШИМ
               }; 
               
               
////////////////////////////////////////   

pwm_val = ((1023 * (u32)pwm)/100); 
// перевели % в 1024-е доли

printf("PWM %u %c\n",pwm,'%');
// вывели новое значение ШИМ в %

// ОБРАТИТЕ ВНИМАНИЕ КАК вывести символ % в printf
 
//  +++++++++++++++++++++++++++++++++++++
// PWM(PD5) = OCR1A / 10.23 
OCR1AH = (char)(pwm_val>>8);
OCR1AL = (char)pwm_val;        

pwm += 10; //увеличим ШИМ на 10% 
   
delay_ms(20); // пауза    

      };  // закрывающая скобка для while(1) 
      
}
