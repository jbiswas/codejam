#include <stdio.h>

int main() {
  int nb_test_cases, test_counter = 1;
  char message[1001], this_letter;
  int last_digit = -1;



  scanf("%d^\n", &nb_test_cases);

  getchar();
  while(nb_test_cases - test_counter >= 0) {
    printf("Case #%d: ", test_counter);

    while((this_letter = getchar()) != EOF) {
      if(this_letter != '\n'){
        switch(this_letter) {
        case 97:
          if(last_digit == 2) printf(" 2");
          else printf("2");
          last_digit = 2;
          break;
        case 98:
          if(last_digit == 2) printf(" 22");
          else printf("22");
          last_digit = 2;
          break;
        case 99:
          if(last_digit == 2) printf(" 222");
          else printf("222");
          last_digit = 2;
          break;
        case 100:
          if(last_digit == 3) printf(" 3");
          else printf("3");
          last_digit = 3;
          break;
        case 101:
          if(last_digit == 3) printf(" 33");
          else printf("33");
          last_digit = 3;
          break;
        case 102:
          if(last_digit == 3) printf(" 333");
          else printf("333");
          last_digit = 3;
          break;
        case 103:
          if(last_digit == 4) printf(" 4");
          else printf("4");
          last_digit = 4;
          break;
        case 104:
          if(last_digit == 4) printf(" 44");
          else printf("44");
          last_digit = 4;
          break;
        case 105:
          if(last_digit == 4) printf(" 444");
          else printf("444");
          last_digit = 4;
          break;
        case 106:
          if(last_digit == 5) printf(" 5");
          else printf("5");
          last_digit = 5;
          break;
        case 107:
          if(last_digit == 5) printf(" 55");
          else printf("55");
          last_digit = 5;
          break;
        case 108:
          if(last_digit == 5) printf(" 555");
          else printf("555");
          last_digit = 5;
          break;
        case 109:
          if(last_digit == 6) printf(" 6");
          else printf("6");
          last_digit = 6;
          break;
        case 110:
          if(last_digit == 6) printf(" 66");
          else printf("66");
          last_digit = 6;
          break;
        case 111:
          if(last_digit == 6) printf(" 666");
          else printf("666");
          last_digit = 6;
          break;
        case 112:
          if(last_digit == 7) printf(" 7");
          else printf("7");
          last_digit = 7;
          break;
        case 113:
          if(last_digit == 7) printf(" 77");
          else printf("77");
          last_digit = 7;
          break;
        case 114:
          if(last_digit == 7) printf(" 777");
          else printf("777");
          last_digit = 7;
          break;
        case 115:
          if(last_digit == 7) printf(" 7777");
          else printf("7777");
          last_digit = 7;
          break;
        case 116:
          if(last_digit == 8) printf(" 8");
          else printf("8");
          last_digit = 8;
          break;
        case 117:
          if(last_digit == 8) printf(" 88");
          else printf("88");
          last_digit = 8;
          break;
        case 118:
          if(last_digit == 8) printf(" 888");
          else printf("888");
          last_digit = 8;
          break;
        case 119:
          if(last_digit == 9) printf(" 9");
          else printf("9");
          last_digit = 9;
          break;
        case 120:
          if(last_digit == 9) printf(" 99");
          else printf("99");
          last_digit = 9;
          break;
        case 121:
          if(last_digit == 9) printf(" 999");
          else printf("999");
          last_digit = 9;
          break;
        case 122:
          if(last_digit == 9) printf(" 9999");
          else printf("9999");
          last_digit = 9;
          break;
        case 32:
          if(last_digit == 0) printf(" 0");
          else printf("0");
          last_digit = 0;
          break;
        default:
          printf("What?");
        }
      } else {
        printf("\n");
        test_counter++;
        if(test_counter <= nb_test_cases)
          printf("Case #%d: ", test_counter);
      }
    }

  }

  return 0;
}
