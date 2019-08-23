#include<iostream>
#include<cstdlib>

int main(){
int n,l;
int x[10];
cin >> n >> l;
for(int i=0; i<n; i++){
    cin >> x[i];
}
int a=0;
for(int i=0;i<n-1;i++){
    for(int j=i+1;j<=n-1;j++){
        if(abs(x[i]-x[j])<=l){
            a++;
        }
    }
}
cout << a << endl;
}