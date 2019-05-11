#include <stdio.h>
#include <string.h>
#include <assert.h>

typedef struct passport passport_t;

struct passport {
    char first_name[32];
    char last_name[32];
    char passport_code;
    char country_code[3];
    unsigned age;
    unsigned checksum;
};

int main(int argc, char ** argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <passport_file>\n", argv[0]);
        return 1;
    }
    
    passport_t person;
    passport_t * personptr = &person;
    
    FILE* passport_file = fopen(argv[1], "r");
    
    if (!passport_file) {
        fprintf(stderr, "Could not open passport file (%s) for reading\n", argv[1]);
        return 1;
    }

    if (
            fscanf(
                passport_file,
                "P<%2[^<]<<<%31[^<]<%31[^<]<<<%u<<<%c<<<%u",
                person.country_code, person.first_name, person.last_name,
                &person.age, &person.passport_code, &person.checksum
            ) != 6) {
        fprintf(stderr, "Passport format invalid: could not read %s\n", argv[1]);
        return 1;
    }
    
    fclose(passport_file);

    printf("Name: %s %s\nAge: %d\nPassport Code: %c\nCountry Code: %s\nChecksum: %d\n",
        personptr->first_name, personptr->last_name, personptr->age, personptr->passport_code, 
        personptr->country_code, personptr->checksum);
    
    // Creates a file name name
    char newfile[1024];
    strcpy(newfile, argv[1]);
    int arglen = strlen(argv[1]);
    char append[] = ".memdump.bin";
    int i = 0;
    while (i < strlen(".memdump.bin")){
        newfile[arglen + i] = append[i];
        i++;
    }
    newfile[arglen + i] = 0;
    
    // Write to a binary
    FILE * write_file = fopen(newfile, "ab");
    fwrite(&person, sizeof(person), 1, write_file);
    fclose(write_file);

    return 0;

}

