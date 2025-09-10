#include <locale.h>
#include <stdio.h>

	
	long long fatorial(int num) {
    long long fat = 1;
    int i; 

    for (i = 1; i <= num; ++i) {
        fat *= i;
    }
    return fat;
}

int main() {
	setlocale(LC_ALL, "portuguese");
	
    int n, k;
    long long combinatoria;

    printf("Digite o valor de n: ");
    scanf("%d", &n);
    printf("Digite o valor de k: ");
    scanf("%d", &k);

    if (n < k || n < 0 || k < 0) {
        printf("Entrada inválida. n deve ser maior ou igual a k e ambos devem ser não-negativos.\n");
    } else {
        combinatoria = fatorial(n) / (fatorial(k) * fatorial(n - k));
        printf("A combinatória de %d tomados %d a %d é: %lld\n", n, k, k, combinatoria);
    }

    return 0;
}

