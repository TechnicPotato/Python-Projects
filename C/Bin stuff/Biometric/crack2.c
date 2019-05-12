#include <stdio.h>
#include <string.h>
#include <assert.h>

typedef struct passport passport_t;

struct passport {
    char document_type;
    char last_name[32];
    char first_name[32];
    unsigned year;
    unsigned month;
    unsigned day;
    char country_code[3];
    char passport_code;
    char biometric_type;
    unsigned short junk;
    unsigned short a;
    unsigned short b;
    unsigned long checksum;
};

int main(int argc, char ** argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <passport_file>\n", argv[0]);
        return 1;
    }
    
    passport_t person;
    
    FILE* passport_file = fopen(argv[1], "rb");
    
    if (!passport_file) {
        fprintf(stderr, "Could not open passport file (%s) for reading\n", argv[1]);
        return 1;
    }
    // Reads into class, returns error if fails:
    if (fread(&person, sizeof(passport_t), 1, passport_file) !=1) {
        fprintf(stderr, "Error: Could not read passport bbinary file %s.\n", argv[1]);
         return 1;
    }
    // Add the null terminator to the person.country_code
    fclose(passport_file);
    printf("Document type: %c\nName: %s %s\n", person.document_type, person.first_name, person.last_name);
    printf("Birth data: %02u/%02u/%04u\n", person.day, person.month, person.year);
    printf("Country: %c%c%c\nPassport Code: %c\nChecksum: %lu\n", person.country_code[0], person.country_code[1], person.country_code[2], person.passport_code, person.checksum);
    printf("Biometric Type: %c\nBiometric Values: %u %u\n", person.biometric_type, person.a, person.b);
    return 0;

}

