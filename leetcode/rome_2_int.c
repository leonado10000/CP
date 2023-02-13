#include<stdio.h>
#include<str.h>
int romanToInt(char  s);
void main()
{   
    int i=0;
    char s[10];
    printf("enter number");
    for(i;i<10;i++)
        scanf("%d",&s[i]);
    romanToInt(char  s);
}
int romanToInt(char  s)
{
    int i,z1,z2,z3,t=0;
    for (i=0;i<=strlen(s);i++)
    {   
        if (s[i]=='M')
        {
            z1=7;
        }
        if (s[i]=='D')
        {
            z1=6;
        }
        if (s[i]=='C')
        {
            z1=5;
        }
        if (s[i]=='L')
        {
            z1=4;
        }
        if (s[i]=='X')
        {
            z1=3;
        }
        if (s[i]=='V')
        {
            z1=2;        
        }
        if (s[i]=='I')
        {
            z1=1;
        }
        if (s[i+1]=='M')
        {
            z2=7;
        }
        if (s[i+1]=='D')
        {
            z2=6;
        }
        if (s[i+1]=='C')
        {
            z2=5;
        }
        if (s[i+1]=='L')
        {
            z2=4;
        }
        if (s[i+1]=='X')
        {
            z2=3;
        }
        if (s[i+1]=='V')
        {
            z2=2;        
        }
        if (s[i+1]=='I')
        {
            z2=1;
        }
        if(z1<z2)
        {
            if (s[i]=='M')
            {
                z3=1000;
            }
            if (s[i]=='D')
            {
                z3=500;
            }
            if (s[i]=='C')
            {
                z3=100;
            }
            if (s[i]=='L')
            {
                z3=50;
            }
            if (s[i]=='X')
            {
                z3=10;
            }
            if (s[i]=='V')
            {
                z3=5;        
            }
            if (s[i]=='I')
            {
                z3=1;
            }
            t=t-z3;
        }
        else
        {
            if (s[i]=='M')
            {
                z3=1000;
            }
            if (s[i]=='D')
            {
                z3=500;
            }
            if (s[i]=='C')
            {
                z3=100;
            }
            if (s[i]=='L')
            {
                z3=50;
            }
            if (s[i]=='X')
            {
                z3=10;
            }
            if (s[i]=='V')
            {
                z3=5;        
            }
            if (s[i]=='I')
            {
                z3=1;
            }
            t=t+z3;
        }
      
    }
}