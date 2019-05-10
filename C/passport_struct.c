#include <stdio.h>

typedef struct passport passport_t;

struct passport {
    char[31] first_name;
    char[31] last_name;
    // Age shouldn't have a sign
    unsigned age;
    
};
