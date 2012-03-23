#include <stdio.h>

int main(void) {
  int nb_test_cases, C, I, P[1000], nb_elts = 0;
  int test_counter = 1, elt_counter = 0;

  int solved = 0;
  int out[2];

  scanf("%d", &nb_test_cases);
  while (nb_test_cases - test_counter >= 0) {
    scanf("%d", &C);
    scanf("%d", &I);

    nb_elts = 0;
    while (nb_elts < I) {
      scanf("%d", &P[nb_elts++]);
    }


    while (I-- > 0 && !solved) {
      out[0] = --nb_elts;
      while (nb_elts > 0 && !solved) {
        out[1] = --nb_elts;
        //printf("\n%d + %d = %d", P[out[0]], P[out[1]], P[out[0]] + P[out[1]]);
        if(P[out[0]] + P[out[1]] == C) {
          printf("Case #%d: %d %d\n", test_counter, out[1]+1, out[0]+1);
          solved = 1;
        }
      }
      nb_elts = I;
      elt_counter++;
    }
    solved = 0;
    test_counter++;
  }
}
