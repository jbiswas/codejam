#include <stdio.h>
#include <string.h>

char *as_digits[26] = {"2",
                       "22",
                       "222",
                       "3",
                       "33",
                       "333",
                       "4",
                       "44",
                       "444",
                       "5",
                       "55",
                       "555",
                       "6",
                       "66",
                       "666",
                       "7",
                       "77",
                       "777",
                       "7777",
                       "8",
                       "88",
                       "888",
                       "9",
                       "99",
                       "999",
                       "9999"};


int main(void) {
	int N,i,j;
	char buffer[1000], c, last, *digits;
	scanf("%d", &N);
	getchar();
	for (i=0;i<N;i++) {
		printf("Case #%d: ", i+1);
		fgets(buffer, 1000, stdin);
		j=0;
		last = '\0';
		while ((c=buffer[j++]) != '\n') {
			if (c==' ') digits = "0";
			else digits = as_digits[c-97];
			if (last==digits[0]) printf(" ");
			printf("%s", digits);
			last = digits[0];
		}
		printf("\n");
	}
	return 0;
}	
