#include <stdio.h>
#include <locale.h>

int main() {
	
	setlocale(LC_ALL, "portuguese");
	
    int numero;
    int i; 

    printf("Digite um número inteiro: ");
    scanf("%d", &numero);

    printf("Os divisores de %d são: \n", numero);

   
    for (i = 1; i <= numero; ++i) {
        if (numero % i == 0) {
            printf("%d\n", i);
        }
    }

    return 0;
}
