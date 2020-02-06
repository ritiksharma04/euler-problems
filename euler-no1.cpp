#include<iostream>
#include<conio.h>

using namespace std;

void get_no()
{
    int sum = 0;
    for(int i = 1;i<1000;i++)
    {
        if(i%3 == 0 ||i%5 == 0)

            sum = sum +i;

    }
    cout<<"sum is = \n "<<sum;
}
int main()
{

    get_no();
    return 0;
}


