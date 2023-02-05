#include<stdio.h>
#include<stdlib.h>
#define MAX_typeA 20
#define MAX_typeB 40
#define MAX_typeC 60
int curr_A=0;
int curr_B=0;
int curr_C=0;

struct guest
{
    /* data */
    char name[50];
    int Adults;
    int room_no;
    char room_type;
    int floor;
    int start_day;
    int end_day;
    int amount;
};
typedef struct guest G;

G Enter_dets(){

}
int check(int n){
    if (n==1){
        if (curr_A <= MAX_typeA) return 1;
        else return 0;
    }
    if (n==2){
        if (curr_A <= MAX_typeB) return 1;
        else return 0;
    }
    if (n==3){
        if (curr_A <= MAX_typeC) return 1;
        else return 0;
    }
}

void main(){
    int ch=1,choice;
    char pref;
    while(ch){
        printf("Menu\n1.Add guest\t2.Add comment\nEnter choice:");
        scanf("%d",&choice);
        switch(choice){
            case 1:
                if (check())
        }

    }
}