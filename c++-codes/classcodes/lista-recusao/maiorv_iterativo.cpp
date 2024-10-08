#include <stdio.h>
#include <stdlib.h>
int maior_elemento(int * vector, int n){
    int m_elemento = vector[0];
    for(int i = 0; i < n; i++){
        if(m_elemento < vector[i]){
            m_elemento = vector[i];
        }
    }
    return m_elemento;
}
int main(){

    int n, *vector;
    scanf("%d", &n);
    
    vector = (int *) malloc(n*sizeof(int));

    for(int i = 0; i < n; i++){
        scanf("%d", &vector[i]);
    }

    printf("O maior elemento entre os valores informados é %d.\n", maior_elemento(vector, n));

    return 0;
}