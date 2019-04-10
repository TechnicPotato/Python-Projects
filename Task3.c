#include <stdio.h>
// Buffers and stuff
char buf[32];
int count = 0;
int int_array[20];
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
    int i = 0;
    while (i < 5){
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
