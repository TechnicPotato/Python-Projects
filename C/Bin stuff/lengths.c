#include <stdio.h>

int main(void){
    int a  = 1;
    unsigned b = 2;
    long c = 321321;
    unsigned long d = 321421412;
    char e = 'a';
    char string[9] = "123456789";
    printf("Sizes of:\nInt: %ld\nUnsigned: %ld\nLong: %ld\n", sizeof(a), sizeof(b), sizeof(c));
    printf("Unsigned Long: %ld\nCharacter: %ld\nString with 9 characters: %ld\n", sizeof(d), sizeof(e), sizeof(string));
    return 0;
}
