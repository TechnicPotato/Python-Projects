#include <stdio.h>
// Buffers and stuff
int count = 0;
int int_array[20];
char buf[32];

// Shitty string copier
int copystr(char* dest, const char* source){
	int count = 0;
	while (source[count]!=0){
		dest[count] = source[count];
		count ++;
	}
	dest[count] = 0;
	return count;
}

// Passport Check Function
int passport_check(char *string){
	char code;
	int danger_level;
	char buf[32];
	char c;
	int counter=0;
	do{
		c = getchar();
		buf[counter] = c;
		counter++;
	} while(c != '\n' && c != EOF);
	if(c==EOF){
		return 0;
	}
	code = buf[0];
	danger_level = buf[1];
	if (code == 'O'){
		if ((danger_level - '0') > 4){
		copystr(string,"Sorry, Visa denied.");
        }
		else {
		copystr(string,"Hello World!");
	}
    	}
    	else if (code == 'A'){
	    	copystr(string, "Glory to Arstotzka!");
    	}
    	else if (code == 'R'){
	    	copystr(string, "Go Away!");
    	}
    	else{
	    	copystr(string, "INVALID PASSPORT");
    	}
    	return 1;
}

// Reading Age Function
int read_age(void){
//void read_age(){
	int c;
	char age[11];
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
	printf("Average age: %.02f (from %d passports)\n",average, count);
}

// Name parsing
void read_name(){
	int c;
	int count2 = 0;
	do{
		c = getchar();
		if (c == 10){
			break;
		}
		buf[count2] = c;
		count2 ++;
	} while(c != 10);
	buf[count2] = 0;
}
// Main Function
int main(){
	int age;
	int conditional = 1;
	int i = 0;
	char buf2[32];
	while (conditional == 1){
		printf("Please enter passport (code, age, name in that order):\n");
        	conditional = passport_check(buf2);
			if(conditional == 0){
				continue;
			}
		age = read_age();
		read_name();
		int_array[count] = age;
		count ++;
		printf("Dear %s, %s\n",buf,buf2);
	//	printf("Your age is %d.\n", age);
		i++;
	}
	calculate_average();
	printf("Done!\n");
	return 0;
}
