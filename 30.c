#include<stdio.h>
int main(void)
{
	int a,b,c,d,a1,a2,t,n1,n2;
	scanf("%d%d",&a,&b);
	scanf("%d%d",&c,&d);
	a1=a*60+b;
	a2=c*60+d;
	if(a1>a2)
	{
		t=a1-a2;
		n1=t/60;
		n2=t%60;
		printf("%d %d",n1,n2);
	}
	else
	{
		t=a2-a1;
		n1=t/60;
		n2=t%60;
		printf("%d %d",n1,n2);
	}
}	
