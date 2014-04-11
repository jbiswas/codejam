#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char googlerese[] = 
 "ejp mysljylc kd kxveddknmc re jsicpdrysi"
 "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
 "de kr kd eoya kw aej tysr re ujdr lkgc jv aozq";

char plain_text[] =
 "our language is impossible to understand"
 "there are twenty six factorial possibilities"
 "so it is okay if you want to just give up yeqz";


void translate(char* input, size_t len) {
  int i = 0;
  char * pch = 0;
  pch = strchr(input, '\n');
  while(i < pch - input && input[i] != '\n') {
    input[i] = plain_text[ strchr(googlerese, input[i]) - googlerese];
    i++;
  }
}

int main() {
  char *line;
  int nb_test_cases = 0, counter = 0;
  size_t length;

  line = malloc(10000);
  scanf("%d\n", &nb_test_cases);

  while(counter < nb_test_cases) {
    getline(&line, &length, stdin);
    translate(line, length);
    printf("Case #%d: %s", ++counter, line);
  }
  free(line);
  return 0;
}
