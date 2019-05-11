#include <stdio.h>

typedef struct passport passport_t;

struct passport {
    char first_name[31];
    char last_name[31];
    char country_code[3];
    
    char passport_code;
    // Age shouldn't have a sign
    unsigned age;
    unsigned checksum;
};

void print_passport(passport_t* ptr){
   printf("Name: %s %s\n", ptr->first_name, ptr->last_name);
   printf("Country Code: %s\nPassport Code: %c\n", ptr->country_code, ptr->passport_code);
   printf("Age: %d\nChecksum: %d\n", ptr->age, ptr->checksum);
}

int main(void) {
    passport_t simon = {
        .first_name = "Simon",
        .last_name = "Yeahnahmate",
        .country_code = "AU",
        .passport_code = 'O',
        .age = 25,
        .checksum = 51};
    passport_t * simonptr = &simon;
    print_passport(simonptr);
    return 0;
}
