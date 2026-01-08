#include<stdio.h>

int main()
{
   char x[100] ;
   int i , j ;
   // freopen("result.txt","w",stdout);
   freopen("ch7.bin","r",stdin);
   scanf("%s",x);
   for (i=0 ; i < 20 ; i++)
   {
       printf("%d ",i);
       for(j=0 ; x[j] != 0 ; j++)
       {
           printf("%c",x[j]-i);
       }
       printf("\n") ;
   }
   return 0 ;

}
