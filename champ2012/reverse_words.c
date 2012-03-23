#include <stdio.h>
#include <string.h>

int main(void) {
  int nb_test_cases, nb_elts = 0, word_size = 0;
  int test_counter = 1, elt_counter = 0;

  char *line;
  char words[1000][50];

  int solved = 0;

  line = (char *)calloc(50000, 1);
  scanf("%d", &nb_test_cases);
  while (nb_test_cases - test_counter >= 0) {
    nb_elts = 0;
    word_size = 0;
    memset(line, '\0', 50000);
    memset(words, '\0', 50000);
    fgets(line, 50000, stdin);

    if(strlen(line) > 1) {
      do {
        sscanf(line + word_size, "%s", words[nb_elts]);
        word_size += strlen(words[nb_elts]) + 1;
        nb_elts++;
      } while (strlen(words[nb_elts-1]) >= 1);
      printf("Case #%d:", test_counter);
      test_counter++;
      while (nb_elts-- > 0) {
          printf("%s ", words[nb_elts]);
      }
      printf("\n");
      nb_elts = 0;
    }
  }
}
