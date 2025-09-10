#include <stdio.h>
#include <locale.h>

int main() {
	
	setlocale(LC_ALL, "portuguese");
	
    int a, b, temp;

    printf("Digite o primeiro número: ");
    scanf("%d", &a);
    printf("Digite o segundo número: ");
    scanf("%d", &b);

    while (b != 0) {
        temp = b;
        b = a % b;
        a = temp;
    }

    printf("O máximo divisor comum é: %d\n", a);

    return 0;
}
