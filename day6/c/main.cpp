#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int array[301] = {0};

int getChildren(int number, int days){
    if (number == 0){
        return 0;
    }
    if (days-number < 0){return 1;}
    if (number == 7) {
        return getChildren(6, days-1);
    }else if (number == 8){
        return getChildren(6, days-2);
    }else{
        if (days-number == 0){return 1;}
        return getChildren(6, days-number-1) + getChildren(8, days-number-1);
    }
}

void populateArray(){
    FILE *myFile;
    myFile = fopen("../file.txt", "r");
    if (myFile == NULL){
        printf("Error Reading File\n");
        exit (0);
    }
    for (int i = 0; i < 301; i++){
        fscanf(myFile, "%d,", &array[i] );
    }
    //for (int i = 0; i < 301; i++){printf("Number is: %d\n\n", array[i]);}
    fclose(myFile);
}

int main() {
    int memory[6] = {0};
    int size = sizeof(array);
    long final_result = 0;

    populateArray();

    clock_t begin = clock();
    for(int i=0; i< size; i++) {
        if (array[i] != 0){
            if (memory[array[i]] == 0) {
                memory[array[i]] = getChildren(array[i], 256);
                final_result += memory[array[i]];

            }else if (array[i]>0 and array[i]<6){
                final_result += memory[array[i]];
            }
        }
        
    }
    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Execution time: %f",time_spent);
    printf("Final result: %lu",final_result);
    return 0;
}