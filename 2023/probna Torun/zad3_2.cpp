#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    // 1. znalezienie największej silni mniejszej lub równej N

    int najw_silnia = 1;
    int i = 1;
    while (najw_silnia <= N)
    {
        i++;
        najw_silnia *= i;
    }
    najw_silnia /= i;
    cout << najw_silnia << endl;

    int suma_silnia = najw_silnia;
    i--;

    while (suma_silnia < N && najw_silnia > 1)
    {
        najw_silnia /= i;
        suma_silnia += najw_silnia;
        i--;
    }

    if (N != suma_silnia)
    {
        cout << "NIE";
    }
    else
    {
        cout << "TAK";
    }

    // 2. Odejmowanie mniejszych silni od podanej liczby
    // jeżeli stwierdziliśmy, że najwyższa silnia mieszcząca się w naszej liczbie to 4!, wtedy musimy sprawdzić, czy 3!, 2! i 1! się mieszczą
    // jeżeli któaś z nich się mieści, to od razu ją odejmujemy

    // TAK / NIE
}