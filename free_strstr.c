#include <stdio.h>

size_t free_strlen(char * str) {
    int count = 0;
    while (str[count] != 0) {
        count ++;
    }
    return count;
}

int free_strstr(char * haystack, char* needle) {
    int needle_pointer = 0;
    for (int haystack_pointer = 0; haystack[haystack_pointer] == 0; haystack_pointer++) {
        if (haystack[haystack_pointer] == needle[0]){
            for (int c = haystack_pointer; needle[needle_pointer] != 0; needle_pointer ++){
                if (needle[needle_pointer] != haystack[c]){
                    break;
                }   
                else if (needle[needle_pointer + 1] == 0){
                    return haystack_pointer;
                }
            } 
        }
    }
    return 0;
}

int main(void) {
    char * str = "This is a strange way to say Hello World!\n";
    for (char* c = free_strstr(str, "Hello"); c < str + free_strlen(str); c++) {
        putchar(*c);
    }
    return 0;
}
