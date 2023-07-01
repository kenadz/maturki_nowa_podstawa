#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    fstream plik("Dane_2105/instrukcje.txt", ios::in);
    if (!(plik.is_open() && plik.good()))
    {
        cout << "Blad";
        return 1;
    }

    string napis;
    string instrukcja;
    char parametr;

    int max_dl = 0, aktualna_dl = 0;
    string max_instr, poprzednia_instr;

    int litery[26] = {};

    for (int i = 0; i < 2000; i++)
    {
        plik >> instrukcja;
        plik >> parametr;

        if (instrukcja == poprzednia_instr)
        {
            aktualna_dl++;
            if (aktualna_dl > max_dl)
            {
                max_dl = aktualna_dl;
                max_instr = poprzednia_instr;
            }
        }
        else
        {
            aktualna_dl = 1;
            poprzednia_instr = instrukcja;
        }

        if (instrukcja == "DOPISZ")
        {
            litery[parametr - 'A']++;
            /*
            A 65
            65 - 65 = 3
            {1,0,1,1,0....}
            */
            napis += parametr;
        }
        else if (instrukcja == "ZMIEN")
        {
            napis.back() = parametr;
        }
        else if (instrukcja == "USUN")
        {
            napis.pop_back();
        }
        else if (instrukcja == "PRZESUN")
        {
            int index = napis.find(parametr);
            if (index != -1) // jeżeli znalazło
            {
                if (napis[index] == parametr)
                {
                    napis[index]++;
                    if (napis[index] > 'Z')
                    {
                        napis[index] -= 26;
                    }
                }
            }
            /*
            for(int j = 0; j < napis.size(); j++)
            {
                if(napis[j] == parametr)
                {
                    napis[j]++;
                    if(napis[j] > 'Z')
                    {
                        napis[j] -= 26;
                    }
                    break;
                }
            }
            */
        }
    }

    plik.close();

    cout << napis << endl;
    cout << napis.size() << endl;
    cout << max_instr << " " << max_dl << endl;

    int najwiecej_razy = 0;
    char litera;
    for(int i = 0; i < 26; i++)
    {
        if(litery[i]>najwiecej_razy)
        {
            najwiecej_razy = litery[i];
            litera = i + 'A';
        }
    }

    cout << najwiecej_razy << " " << litera;

    // wypisać do pliku

    plik.open("wyniki.txt", ios::out); // otwarcie pliku wynikowego
    plik << 4.1 << endl;
    plik << napis.size() << endl;
    plik << 4.2 << endl;
    plik << max_instr << " " << max_dl << endl;
    plik << 4.3 << endl;
    plik << najwiecej_razy << " " << litera << endl;
    plik << 4.4 << endl;
    plik << napis;
    // wypisanie danych


    plik.close();
}
