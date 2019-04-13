#include <stdio.h>
int main(int argc, char** argv) {
    // Initialise a buffer for passport file
    char buffer[50];
    // Read second argument from command line
    char *file_name = argv[1];
    FILE *fp;
    char first[31], last[31], cc[2];
    char passcode;
    // Write everything into the buffer
    fp = fopen(file_name, "r");
    fgets(buffer, 50, fp);
    // %2[^<] read 2 characters that aren't < into buffer
    sscanf(buffer, "P<%2[^<]<<<%31[^<]<%31[^<]<<<%c<<<00", cc, first, last, passcode);
    printf("Name: %s %s\n", first, last);
    printf("Passport Code: %c\n", passcode);
    printf("Country Code: %s\n", cc);
    return 0;
}
