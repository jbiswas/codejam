#include <stdio.h>
#include <string.h>

int main(void) {
  int N, i, j;
  char buffer[50000];
  char *words[1000];

  scanf("%d\n", &N);

  for (i=0; i<N; i++) {
    fgets(buffer, 50000, stdin);
    j = 0;
    words[j] = strtok(buffer, " \n");
    while (words[++j] = strtok(NULL, " \n")) ;
    printf("Case #%d: ", i+1);
    for (j--; j>=0; j--)
      printf("%s%s", words[j], j==0? "\n" : " ");
  }
  return 0;
}
