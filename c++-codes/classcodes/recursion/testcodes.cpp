#include <stdio.h>
int Fatorial (int n)
{
int fat =1; int i;
for (i =1; i <= n; i++)
fat = fat * i;
return fat;
}
int main()
{
int res, n = 5;
// chamada externa
res = Fatorial(n);
printf("%d ", res);
}