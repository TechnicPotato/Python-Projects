#include <stdio.h>
// Buffers and stuff
char buf[32];
int count = 0;
int int_array[20];
// Shitty string copier
int copystr(char* dest, char* source){
    

// Passport Check Function
int passport_check(char *string){
    char code;
    int danger_level
    code = getchar();
    if (code == EOF){
        return 0;
        }
    else if (code == 'O'){
        danger_level = getchar() - '0';
        if (danger_level > 4){
            string = "Get Lost!"
            }
        }
    return 1;
    }
// Reading Age Function
int read_age(void){
    int c;
    char age[10];
    int age_position = 0;
    // Loop to read int from stdin
    do {
        c = getchar();   
        if (c!= 10){
            age[age_position] = c;
            age_position++;
            }
        } while (c != 10);
    age[age_position] = '\0';
    // Loop that converts age into int
    int i = 0;
    int n = 0;
    while(age[i] >= '0' && age[i] <= '9'){
        n = n * 10 + (age[i] - '0');
        i ++; 
        }
    age[i] = '\0';
    return n;
    }
// Averaging function
void calculate_average(){
    int c = 0;
    int n = 0;
    while (c < count){
        n += int_array[c];
        c++;
        }
    double average;
    average = (double) n/count;
    printf("Average age: %02f (from %d passports)\n",average, count);
    }
// Main Function
int main(){  
    int age;
    int conditional;
    int i = 0;
    char buf2[32];
    while (conditional == 1){
        conditional = passport_check(buf2);
        age = read_age();
        int_array[count] = age;
        count ++;
        printf("Your age is %d.\n", age);
        i++;
        }
    calculate_average();
    printf("Done!\n");
    return 0;
    }
