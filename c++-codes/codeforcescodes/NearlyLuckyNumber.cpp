    #include<bits/stdc++.h>
    using namespace std;
     
    int main(){
    	char ch;
    	int num=0;
    	while((ch=getchar())!='\n'){
    		if(ch=='4'||ch=='7')
    			num++;
    	}
    	cout<<(num==4||num==7? "YES":"NO");
    }