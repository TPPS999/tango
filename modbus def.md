Protokół MODBUS
Wersja sterownika: 1.5.3.x
Data wydania: 20.12.2020
str. 2
Spis treści
1 Pomiary ............................................................................................................................................ 3
1.1 Pomiary bieżące....................................................................................................................... 3
1.2 Pomiary wartości MinMax ..................................................................................................... 11
1.3 Pomiary konfigurowalne ....................................................................................................... 11
2 Nastawy ......................................................................................................................................... 13
2.1 Konfiguracja kart I/O ............................................................................................................. 13
2.2 Zestaw aktywnych zabezpieczeń ........................................................................................... 14
2.3 Parametry ogólne .................................................................................................................. 15
2.4 Parametry komunikacji .......................................................................................................... 22
2.5 Banki nastaw zabezpieczeń ................................................................................................... 26
3 Sterowania ..................................................................................................................................... 39
4 Zdarzenia ....................................................................................................................................... 41
5 Synchronizacja czasu ..................................................................................................................... 49
6 Identyfikacja .................................................................................................................................. 49
7 Kody błędów .................................................................................................................................. 50
8 Odczyt rejestratora zakłóceń ......................................................................................................... 50
8.1 Parametry rejestratora (funkcja 3, offset 0x25C0) ................................................................ 51
8.2 Lista przebiegów (funkcja 3, offset 0x2580) .......................................................................... 52
8.3 Wybór bloku do odczytu (funkcja 16, offset 0x2570) ........................................................... 53
8.4 Odczyt bloku .......................................................................................................................... 53
8.5 Problemy w trakcie odczytu .................................................................................................. 54
9 Odczyt rejestratora kryterialnego ................................................................................................. 54
9.1 Parametry rejestratora (funkcja 3, offset 0x2620) ................................................................ 55
9.2 Lista rejestracji (funkcja 3, offset 0x25E0) ............................................................................. 56
9.3 Wybór bloku do odczytu (funkcja 16, offset 0x25D0) ........................................................... 56
9.4 Odczyt bloku .......................................................................................................................... 57
9.5 Problemy w trakcie odczytu .................................................................................................. 57
10 Komunikacja ETHERNET ............................................................................................................ 58
str. 3
1 Pomiary
Nastawy wejść przesyłane są następująco:
Najbardziej znaczący bit - negacja wejścia 1 - wejście zanegowane (tylko oznaczone wejścia)
Dolna połówka rejestru - numer slotu 1÷15 odpowiadający karcie A÷N
Górna połówka rejestru - numer wejścia 1÷8 dla karty 8 wejść, 1÷12 dla karty 12 wejść
Nastawy wyjść przesyłane są następująco:
Dolna połówka rejestru - numer slotu 1÷15 odpowiadający karcie A÷W
Górna połówka rejestru - numer wyjścia 1÷8 dla karty 8 wyjść
1.1 Pomiary bieżące
Pomiary wartości bieżących
Odczyt funkcją 4
Brak ograniczenia co do ilości odczytywanych rejestrów.
bajty wartości 1-rejestrowych B1*28 + B2 przesyłane w kolejności B1, B2
bajty wartości 2-rejestrowych B1*224 + B2*216 + B3*28 + B4*20 przesyłane w kolejności: B3, B4, B1, B2
wartości zmiennoprzecinkowe (float) w formacie IEEE-754 single
Adres bazowy: 0x0000 Adres HEX Typ Skrót Opis Jednostka
+0x000
float
I1
Wartość prądu I1
A
+0x002
float
I2
Wartość prądu I2
A
+0x004
float
I3
Wartość prądu I3
A
+0x006
float
U12
Wartość napięcia U12
V
+0x008
float
U23
Wartość napięcia U23
V
+0x00A
float
U31
Wartość napięcia U31
V
+0x00C
float
f
Wartość częstotliwości
Hz
+0x00E
float
P
Wartość mocy czynnej
W
+0x010
float
Q
Wartość mocy biernej
var
+0x012
float
S
Wartość mocy pozornej
VA
+0x014
float
cos(φ)
Wartość cos(φ)
+0x016
float
tg(φ)
Wartość tg(φ)
+0x018
float
Ec+
Licznik energii czynnej dodatniej
Wh
+0x01A
float
Ec-
Licznik energii czynnej ujemnej
Wh
+0x01C
float
Eb+
Licznik energii biernej dodatniej
varh
+0x01E
float
Eb-
Licznik energii biernej ujemnej
varh
+0x020
float
I0
Wartość prądu I0
A
+0x022
float
U0
Wartość napięcia U0
V
str. 4
+0x024
float
Y0
Wartość admitancji Y0
S
+0x026
float
φ0
Kąt między U0 a I0
°
+0x028
float
Ig
Wartość prądu wew. baterii kondensatorów Ig
A
+0x02A
float
I1_1h
Wartość I harmonicznej prądu I1
A
+0x02C
float
I2_1h
Wartość I harmonicznej prądu I2
A
+0x02E
float
I3_1h
Wartość I harmonicznej prądu I3
A
+0x030
float
U1
Wartość napięcia U1
V
+0x032
float
U2
Wartość napięcia U2
V
+0x034
float
U3
Wartość napięcia U3
V
+0x036
float
P1
Wartość mocy czynnej P1
W
+0x038
float
P2
Wartość mocy czynnej P2
W
+0x03A
float
P3
Wartość mocy czynnej P3
W
+0x03C
float
Q1
Wartość mocy biernej Q1
var
+0x03E
float
Q2
Wartość mocy biernej Q2
var
+0x040
float
Q3
Wartość mocy biernej Q3
var
+0x042
float
φ1
Kąt między U1 a I1
°
+0x044
float
φ2
Kąt między U2 a I2
°
+0x046
float
φ3
Kąt między U3 a I3
°
+0x048
float
φU1_2
Kąt między U1 a U2
°
+0x04A
float
φU1_3
Kąt między U1 a U3
°
+0x04C
float
I_s1
Składowa zgodna prądu
A
+0x04E
float
I_s2
Składowa przeciwna prądu
A
+0x050
float
U_s1
Składowa zgodna napięcia
V
+0x052
float
U_s2
Składowa przeciwna napięcia
V
+0x054
uint16
%I_2h
Max. zawartość II harmonicznej prądu
%
+0x055
P420 (uint16)
Kier.I
Kierunek prądów
+0x056
float
U_SYN
Napięcie synchronizacji dla funkcji synchrocheck
V
+0x058
float
ΔU_SYN
Różnica napięć dla funkcji synchrocheck
V
+0x05A
float
Δf_SYN
Różnica częstotliwości napięć dla funkcji synchrocheck
Hz
+0x05C
float
Δφ_SYN
Przesunięcie kątowe napięć dla funkcji synchrocheck
°
+0x05E
float
MinA_Uf
Minimalna wartość średnia 10min napięć fazowych
V
+0x060
float
MaxA_Uf
Maksymalna wartość średnia 10min napięć fazowych
V
+0x062
float
MinA_Up
Minimalna wartość średnia 10min napięć przewodowych
V
+0x064
float
MaxA_Up
Maksymalna wartość średnia 10min napięć przewodowych
V
+0x066
float
MinA_UfnN
Minimalna wartość średnia 10min napięć fazowych strona nN
V
+0x068
float
MaxA_UfnN
Maksymalna wartość średnia 10min napięć fazowych strona nN
V
+0x06A
float
MinA_UpnN
Minimalna wartość średnia 10min napięć przewodowych strona nN
V
+0x06C
float
MaxA_UpnN
Maksymalna wartość średnia 10min napięć przewodowych strona nN
V
+0x06E
float
Zapas
Zarezerwowane
+0x070
float
Zapas
Zarezerwowane
+0x072
float
Zapas
Zarezerwowane
+0x074
float
Zapas
Zarezerwowane
+0x076
float
I1_nN
Wartość prądu I1 nN
A
+0x078
float
I2_nN
Wartość prądu I2 nN
A
+0x07A
float
I3_nN
Wartość prądu I3 nN
A
+0x07C
float
U12_nN
Wartość napięcia U12 nN
V
+0x07E
float
U23_nN
Wartość napięcia U23 nN
V
+0x080
float
U31_nN
Wartość napięcia U31 nN
V
+0x082
float
f_nN
Wartość częstotliwości nN
Hz
+0x084
float
I0_nN
Wartość prądu I0 nN
A
+0x086
float
U0_nN
Wartość napięcia U0 nN
V
+0x088
float
Y0_nN
Wartość admitancji Y0 nN
S
+0x08A
float
φ0_nN
Kąt między U0 a I0 nN
°
+0x08C
float
I1_1h_nN
Wartość I harmonicznej prądu I1 nN
A
+0x08E
float
I2_1h_nN
Wartość I harmonicznej prądu I2 nN
A
+0x090
float
I3_1h_nN
Wartość I harmonicznej prądu I3 nN
A
+0x092
float
U1_nN
Wartość napięcia U1 nN
V
+0x094
float
U2_nN
Wartość napięcia U2 nN
V
+0x096
float
U3_nN
Wartość napięcia U3 nN
V
str. 5
+0x098
float
φ1_nN
Kąt między U1 a I1 nN
°
+0x09A
float
φ2_nN
Kąt między U2 a I2 nN
°
+0x09C
float
φ3_nN
Kąt między U3 a I3 nN
°
+0x09E
float
φU1_2_nN
Kąt między U1 a U2 nN
°
+0x0A0
float
φU1_3_nN
Kąt między U1 a U3 nN
°
+0x0A2
uin32
PZab1
Sygnały pobudzeń zabezpieczeń 1
+0x0A4
uin32
PZab2
Sygnały pobudzeń zabezpieczeń 2
+0x0A6
uin32
PZab3
Sygnały pobudzeń zabezpieczeń 3
+0x0A8
uin32
PZab4
Sygnały pobudzeń zabezpieczeń 4
+0x0AA
uin32
ZZab1
Sygnały zadziałań zabezpieczeń 1
+0x0AC
uin32
ZZab2
Sygnały zadziałań zabezpieczeń 2
+0x0AE
uin32
ZZab3
Sygnały zadziałań zabezpieczeń 3
+0x0B0
uin32
ZZab4
Sygnały zadziałań zabezpieczeń 4
+0x0B2
uin32
ZZabZ1
Sygnały zadziałań zabezpieczeń z zatrzaskiem 1
+0x0B4
uin32
ZZabZ2
Sygnały zadziałań zabezpieczeń z zatrzaskiem 2
+0x0B6
uin32
ZZabZ3
Sygnały zadziałań zabezpieczeń z zatrzaskiem 3
+0x0B8
uin32
ZZabZ4
Sygnały zadziałań zabezpieczeń z zatrzaskiem 4
+0x0BA
P453 (uint16)
Ster.
Miejsce sterowania
+0x0BB
P450 (uint16)
SPZ
Stan automatyki SPZ
+0x0BC
P450 (uint16)
SCO
Stan automatyki SCO
+0x0BD
P450 (uint16)
SCOw
Stan automatyki SCO człon wykonawczy
+0x0BE
P450 (uint16)
SPZW
Stan automatyki SPZ od zab. wyspowych
+0x0BF
uint16
Zapas
Zarezerwowane
+0x0C0
uint16
Zapas
Zarezerwowane
+0x0C1
P450 (uint16)
SPZ/SCOw
Stan automatyki SPZ/SCO człon wykonawczy
+0x0C2
uint16
we/wyA
Stan wejść/wyjść karty w slocie A
+0x0C3
uint16
we/wyB
Stan wejść/wyjść karty w slocie B
+0x0C4
uint16
we/wyC
Stan wejść/wyjść karty w slocie C
+0x0C5
uint16
we/wyD
Stan wejść/wyjść karty w slocie D
+0x0C6
uint16
we/wyE
Stan wejść/wyjść karty w slocie E
+0x0C7
uint16
we/wyF
Stan wejść/wyjść karty w slocie F
+0x0C8
uint16
we/wyG
Stan wejść/wyjść karty w slocie G
+0x0C9
uint16
we/wyH
Stan wejść/wyjść karty w slocie H
+0x0CA
uint16
we/wyI
Stan wejść/wyjść karty w slocie I
+0x0CB
uint16
we/wyJ
Stan wejść/wyjść karty w slocie J
+0x0CC
uint16
we/wyK
Stan wejść/wyjść karty w slocie K
+0x0CD
uint16
we/wyL
Stan wejść/wyjść karty w slocie L
+0x0CE
uint16
we/wyM
Stan wejść/wyjść karty w slocie M
+0x0CF
uint16
we/wyN
Stan wejść/wyjść karty w slocie N
+0x0D0
uint16
we/wyZ
Stan wejść/wyjść złącza W
+0x0D1
uint16
we/wyZ
Stan LED RED 1_16
+0x0D2
uint16
we/wyZ
Stan LED RED 17_22
+0x0D3
uint16
we/wyZ
Stan LED GREEN 1_16
+0x0D4
uint16
we/wyZ
Stan LED GREEN 17_22
+0x0D5
P452 (uint16)
StanL1
Stan łącznika 1
+0x0D6
P452 (uint16)
StanL2
Stan łącznika 2
+0x0D7
P452 (uint16)
StanL3
Stan łącznika 3
+0x0D8
P452 (uint16)
StanL4
Stan łącznika 4
+0x0D9
P452 (uint16)
StanL5
Stan łącznika 5
+0x0DA
P452 (uint16)
StanL6
Stan łącznika 6
+0x0DB
P452 (uint16)
StanL7
Stan łącznika 7
+0x0DC
P452 (uint16)
StanL8
Stan łącznika 8
+0x0DD
P452 (uint16)
StanL9
Stan łącznika 9
+0x0DE
P452 (uint16)
StanL10
Stan łącznika 10
+0x0DF
P452 (uint16)
StanL11
Stan łącznika 11
+0x0E0
P452 (uint16)
StanL12
Stan łącznika 12
+0x0E1
uint16
New_Ev
Ilość nowych zdarzeń
+0x0E2
uint16
New_Rec1
Ilość nowych rejestracji zakłóceń
+0x0E3
uint16
New_Rec2
Ilość nowych rejestracji kryterialnych
str. 6
+0x0E4
uint16
Zapas
Zarezerwowane
+0x0E5
uint16
Zapas
Zarezerwowane
+0x0E6
uint16
nWYL
Pozostała ilość wyłączeń (kontrola zużycia styków wyłącznika)
+0x0E7
uint16
BANK
Aktywny bank nastaw zabezpieczeń
+0x0E8
uint16
Q I>INV
Poziom zabezpieczenia nadprądowego zależnego
%
+0x0E9
uint16
Q TH
Stopień nagrzania zabezpieczenia cieplnego
%
+0x0EA
uint16
WZ
Licznik udanych cykli SPZ 1-krotnego
+0x0EB
uint16
WZWZ
Licznik udanych cykli SPZ 2-krotnego
+0x0EC
uint16
WZWZWZ
Licznik udanych cykli SPZ 3-krotnego
+0x0ED
uint16
WZW
Licznik nieudanych cykli SPZ 1-krotnego
+0x0EE
uint16
WZWZW
Licznik nieudanych cykli SPZ 2-krotnego
+0x0EF
uint16
WZWZWZW
Licznik nieudanych cykli SPZ 3-krotnego
+0x0F0
uint16
L.1
Licznik użytkownika 1
+0x0F1
uint16
L.2
Licznik użytkownika 2
+0x0F2
uint16
L.3
Licznik użytkownika 3
+0x0F3
uint16
L.4
Licznik użytkownika 4
+0x0F4
uint16
L.5
Licznik użytkownika 5
+0x0F5
uint16
L.6
Licznik użytkownika 6
+0x0F6
uint16
L.7
Licznik użytkownika 7
+0x0F7
uint16
L.8
Licznik użytkownika 8
+0x0F8
int16
TPT1
Temperatura PT1 (karta PT)
°C
+0x0F9
int16
TPT2
Temperatura PT2 (karta PT)
°C
+0x0FA
int16
TPT3
Temperatura PT3 (karta PT)
°C
+0x0FB
int16
TPT4
Temperatura PT4 (karta PT)
°C
+0x0FC
int16
TPT5
Temperatura PT5 (karta PT)
°C
+0x0FD
int16
TPT6
Temperatura PT6 (karta PT)
°C
+0x0FE
float
An.1
Wejście analogowe 1 (karta AIN)
+0x100
float
An.2
Wejście analogowe 2 (karta AIN)
+0x102
float
An.3
Wejście analogowe 3 (karta AIN)
+0x104
float
An.4
Wejście analogowe 4 (karta AIN)
+0x106
float
kI1
Wartość prądu I1
Ib
+0x108
float
kI2
Wartość prądu I2
Ib
+0x10A
float
kI3
Wartość prądu I3
Ib
+0x10C
float
kU12
Wartość napięcia U12
Ub
+0x10E
float
kU23
Wartość napięcia U23
Ub
+0x110
float
kU31
Wartość napięcia U31
Ub
+0x112
float
kU1
Wartość napięcia U1
Ub
+0x114
float
kU2
Wartość napięcia U2
Ub
+0x116
float
kU3
Wartość napięcia U3
Ub
+0x118
uint16
Zapas
Zarezerwowane
+0x119
uint16
Zapas
Zarezerwowane
+0x11A
P500 (uint16)
K.UZ1
Komunikat użytkownika 1 (sygnał logiki COMM1)
+0x11B
uint16
Time_YM
Czas bieżący - rok,mies
+0x11C
uint16
Time_DH
Czas bieżący - dzień,godzina
+0x11D
uint16
Time_MS
Czas bieżący - minuta,sekunda
+0x11E
float
In
Prąd znamionowy
A
+0x120
float
Un
Napięcie znamionowe
V
+0x122
uint16
BitUserIn
Wejściowe sygnały logiki
+0x123
uint16
BitUserOut
Wyjściowe sygnały logiki
+0x124
float
TRP_I0
Wartość I0 przy zadziałaniu zab.
A
+0x126
float
TRP_U0
Wartość U0 przy zadziałaniu zab.
V
+0x128
float
TRP_φ0
Wartość φ0 przy zadziałaniu zab.
°
+0x12A
uint16
Zapas
Zarezerwowane
+0x12B
uint16
Zapas
Zarezerwowane
+0x12C
uint16
Zapas
Zarezerwowane
+0x12D
uint16
Krot.SPZ
Krotność SPZ
+0x12E
P454 (uint16)
LRW
Stan automatyki LRW
+0x12F
P454 (uint16)
ZS
Stan automatyki ZS
str. 7
Formaty dla pomiarów Format Opis
P12
Czas pracy w sekundach
P20
Kierunek prądu b0 = 1 - kierunek dodatni fazy L1 b1 = 1 - kierunek dodatni fazy L2 b2 = 1 - kierunek dodatni fazy L3 b4 = 1 - kierunek ujemny fazy L1 b5 = 1 - kierunek ujemny fazy L2 b6 = 1 - kierunek ujemny fazy L3 b0 i b4 = 0 - kierunek niemożliwy do ustalenia dla fazy L1 b1 i b5 = 0 - kierunek niemożliwy do ustalenia dla fazy L2 b2 i b6 = 0 - kierunek niemożliwy do ustalenia dla fazy L3
P450
0 = Odst/Zabl 1 = Odst/Odbl 2 = Nast/Zabl 3 = Nast/Odbl
P451
0 = Stop 1 = Praca 2 = Rozruch
P452
0 = ? 1 = Otwarty 2 = Zamknięty 3 = Błąd stanu
P453
0 = -- 1 = Lokalne 2 = Zdalne 3 = Lok./zd.
P454
0 = Odst. 1 = 2 = Nast. 3 =
P500
Kierunek prądu b0 - komunikat użytkownika z logiki 1 b1 - komunikat użytkownika z logiki 2 b2 - komunikat użytkownika z logiki 3 b3 - komunikat użytkownika z logiki 4 b4 - komunikat użytkownika z logiki 5 b5 - komunikat użytkownika z logiki 6 b6 - komunikat użytkownika z logiki 7 b7 - komunikat użytkownika z logiki 8 b8,b9 - komunikat użytkownika z logiki 9 b10,b11 - komunikat użytkownika z logiki 10 b12,b13 - komunikat użytkownika z logiki 11 b14,b15 - komunikat użytkownika z logiki 12
Bity pobudzeń zabezpieczeń PZab1, zadziałań zabezpieczeń ZZab1 i zadziałań zabezpieczeń z zatrzaskiem ZZabZ1:
bit
Zabezpieczenie
0
zwarciowe I>>
1
nadprądowe 1 I>1
2
nadprądowe 2 I>2
3
nadprądowe 3 I>3
4
nadprądowe zależne I>INV
5
cieplne THERM
6
cieplne alarm THERM
7
nadprądowe zależne I>INV alarm
8
9
10
ziemnozwarciowe 1 I0>1
str. 8
11
ziemnozwarciowe 2 I0>2
12
ziemnozwarciowe kierunkowe I0>d
13
admitancyjne Y0>
14
admitancyjne kierunkowe 1 Y0>d1
15
admitancyjne kierunkowe 2 Y0>d2
16
ziemnozwarciowe nadnapięciowe 1 U0>1
17
ziemnozwarciowe nadnapięciowe 2 U0>2
18
podnapięciowe 1 U<1
19
podnapięciowe 2 U<2
20
nadnapięciowe 1 U>1
21
nadnapięciowe 2 U>2
22
zwrotnomocowe P P>
23
zwrotnomocowe Q Q>
24
od asymetrii obciążenia ASIM
25
podprądowe I<
26
od utyku wirnika RLOCK
27
czasu rozruchu silnika
28
prądu wewnętrznego baterii kondensatorów Ig>
29
różnicowe silnika DIFM
30
od wypadnięcia z synchronizmu Iss>
31
Bity pobudzeń zabezpieczeń PZab2, zadziałań zabezpieczeń ZZab2 i zadziałań zabezpieczeń z zatrzaskiem ZZabZ2:
bit
Zabezpieczenie
0
podczęstotliwościowe 1 f<1
1
podczęstotliwościowe 2 f<2
2
podczęstotliwościowe 3 f<3
3
podczęstotliwościowe 4 f<4
4
nadczęstotliwościowe 1 f>1
5
nadczęstotliwościowe 2 f>2
6
dU/dt
7
8
9
10
11
12
13
str. 9
14
15
ZS zabezpieczenie szyn
16
temperaturowe 1
17
temperaturowe 2
18
gazowo-przepływowe trafo I stopnia
19
gazowo-przepływowe trafo II stopnia
20
gazowo-przepływowe dławika I stopnia
21
gazowo-przepływowe dławika II stopnia
22
gazowo-przepływowe przełącznika zaczepów
23
LRW
24
kontrola zbrojenia napędu wyłącznika
25
kontrola 2-bitowych stanów łączników
26
kontrola COW1
27
kontrola COW2
28
kontrola COZ
29
różnicowe zewnętrzne
30
odległościowe zewnętrzne
31
zewnętrzne
Bity pobudzeń zabezpieczeń PZab3, zadziałań zabezpieczeń ZZab3 i zadziałań zabezpieczeń z zatrzaskiem ZZabZ3:
bit
Zabezpieczenie
0
I0> automatyki AWSC
1
U0> automatyki AWSC
2
łukoochronne pola własnego
3
łukoochronne z pola zewnętrznego
4
kontrola trwałości wyłącznika
5
kontrola przekładników prądowych
6
kontrola przekładników napięciowych
7
zadziałanie bezpieczników w obwodach pomiaru U
8
zadziałanie bezpieczników w obwodach pomiaru U0
9
wyjście LRW
10
zadziałanie bezpieczników w obwodach pomiaru Us
11
zadziałanie bezpieczników w obwodach pomiaru USZR
12
13
14
termiczne PT czujnik 1 poziom alarmowy
str. 10
Bity pobudzeń zabezpieczeń PZab4, zadziałań zabezpieczeń ZZab4 i zadziałań zabezpieczeń z zatrzaskiem ZZabZ4:
bit
Zabezpieczenie
0
technologiczne 1
1
technologiczne 2
2
technologiczne 3
3
technologiczne 4
4
technologiczne 5
5
technologiczne 6
6
technologiczne 7
7
technologiczne 8
8
technologiczne 9
9
technologiczne 10
10
technologiczne 11
11
technologiczne 12
12
technologiczne 13
13
technologiczne 14
14
technologiczne 15
15
technologiczne 16
16
Nadprądowe 4
17
Nadprądowe 5
15
termiczne PT czujnik 2 poziom alarmowy
16
termiczne PT czujnik 3 poziom alarmowy
17
termiczne PT czujnik 4 poziom alarmowy
18
termiczne PT czujnik 5 poziom alarmowy
19
termiczne PT czujnik 6 poziom alarmowy
20
termiczne PT czujnik 1
21
termiczne PT czujnik 2
22
termiczne PT czujnik 3
23
termiczne PT czujnik 4
24
termiczne PT czujnik 5
25
termiczne PT czujnik 6
26
błąd czujnika zabezpieczeń termicznych PT
27
28
19
30
31
str. 11
18
Ziemnozwarciowe niskiego napięcia
19
Ziemnozwarciowe nadnapięciowe niskiego napięcia
20
Nadnapięciowe 3
21
Podnapięciowe 3
22
Nadnapięciowe średnie 10 minutowe
23
24
25
26
27
28
29
30
31
1.2 Pomiary wartości MinMax
Wartości min i max pomiarów od ostatniego odczytu.
Wartości są wyliczane jeśli parametr „Akt. MinMax COM1”, „Akt. MinMax COM2”, „Akt. MinMax ETH1”, „Akt. MinMax ETH2” (Komunikacja | Parametry Modbus) dla odpowiedniego portu ustawiony jest na „Tak”.
Odczyt funkcją 4
Adres bazowy 0x5050 Adres HEX Typ Skrót Opis Jednostka
+0x000
float
Max I1RMS
Wartość maksymalna prądu I1 od ostatniego odczytu
A
+0x002
float
Max I2RMS
Wartość maksymalna prądu I2 od ostatniego odczytu
A
+0x004
float
Max I3RMS
Wartość maksymalna prądu I3 od ostatniego odczytu
A
+0x006
float
Max U12
Wartość maksymalna napięcia U12 od ostatniego odczytu
V
+0x008
float
Max U23
Wartość maksymalna napięcia U23 od ostatniego odczytu
V
+0x00A
float
Max U31
Wartość maksymalna napięcia U31 od ostatniego odczytu
V
+0x00C
float
Max P
Wartość maksymalna mocy czynnej od ostatniego odczytu
W
+0x00E
float
Max Q
Wartość maksymalna mocy biernej od ostatniego odczytu
var
+0x010
float
Min I1RMS
Wartość minimalna prądu I1 od ostatniego odczytu
A
+0x012
float
Min I2RMS
Wartość minimalna prądu I2 od ostatniego odczytu
A
+0x014
float
Min I3RMS
Wartość minimalna prądu I3 od ostatniego odczytu
A
+0x016
float
Min U12
Wartość minimalna napięcia U12 od ostatniego odczytu
V
+0x018
float
Min U23
Wartość minimalna napięcia U23 od ostatniego odczytu
V
+0x01A
float
Min U31
Wartość minimalna napięcia U31 od ostatniego odczytu
V
+0x01C
float
Min P
Wartość minimalna mocy czynnej od ostatniego odczytu
W
+0x01E
float
Min Q
Wartość minimalna mocy biernej od ostatniego odczytu
var
1.3 Pomiary konfigurowalne
str. 12
12 wartości 2-rejestrowych i 16 wartości 1-rejestrowych do dowolnego skonfigurowania. W konfiguracji pomiarów konfigurowalnych ustalane adresy wartości pomiarów bieżących, które mają być skopiowane do przestrzeni pomiarów konfigurowalnych.
Pomiary konfigurowalne są wspólne dla wszystkich portów komunikacyjnych.
Obszar pomiarów jest aktywny jeśli parametr „Akt. konfig. pom.” (Konfiguracja | Parametry komunikacji | Parametry Modbus) ustawiony jest na „Tak”.
Konfiguracja pomiarów konfigurowalnych:
Odczyt funkcją 3
Zapis funkcją 16
Adres bazowy: 0x5000 Adres HEX Typ Skrót Opis
+0x000
uint16
Ad_2rej1
Adres wartości 2-rejestrowej 1
+0x001
uint16
Ad_2rej2
Adres wartości 2-rejestrowej 2
+0x002
uint16
Ad_2rej3
Adres wartości 2-rejestrowej 3
+0x003
uint16
Ad_2rej4
Adres wartości 2-rejestrowej 4
+0x004
uint16
Ad_2rej5
Adres wartości 2-rejestrowej 5
+0x005
uint16
Ad_2rej6
Adres wartości 2-rejestrowej 6
+0x006
uint16
Ad_2rej7
Adres wartości 2-rejestrowej 7
+0x007
uint16
Ad_2rej8
Adres wartości 2-rejestrowej 8
+0x008
uint16
Ad_2rej9
Adres wartości 2-rejestrowej 9
+0x009
uint16
Ad_2rej10
Adres wartości 2-rejestrowej 10
+0x00A
uint16
Ad_2rej11
Adres wartości 2-rejestrowej 11
+0x00B
uint16
Ad_2rej12
Adres wartości 2-rejestrowej 12
+0x00C
uint16
Ad_1rej1
Adres wartości 1-rejestrowej 1
+0x00D
uint16
Ad_1rej2
Adres wartości 1-rejestrowej 2
+0x00E
uint16
Ad_1rej3
Adres wartości 1-rejestrowej 3
+0x00F
uint16
Ad_1rej4
Adres wartości 1-rejestrowej 4
+0x010
uint16
Ad_1rej5
Adres wartości 1-rejestrowej 5
+0x011
uint16
Ad_1rej6
Adres wartości 1-rejestrowej 6
+0x012
uint16
Ad_1rej7
Adres wartości 1-rejestrowej 7
+0x013
uint16
Ad_1rej8
Adres wartości 1-rejestrowej 8
+0x014
uint16
Ad_1rej9
Adres wartości 1-rejestrowej 9
+0x015
uint16
Ad_1rej10
Adres wartości 1-rejestrowej 10
+0x016
uint16
Ad_1rej11
Adres wartości 1-rejestrowej 11
+0x017
uint16
Ad_1rej12
Adres wartości 1-rejestrowej 12
+0x018
uint16
Ad_1rej13
Adres wartości 1-rejestrowej 13
+0x019
uint16
Ad_1rej14
Adres wartości 1-rejestrowej 14
+0x01A
uint16
Ad_1rej15
Adres wartości 1-rejestrowej 15
+0x01B
uint16
Ad_1rej16
Adres wartości 1-rejestrowej 16
Pomiary konfigurowalne:
Odczyt funkcją 4
Adres bazowy: 0x5000 Adres HEX Typ Skrót Opis
+0x000
uint32/float
Pom_2rej1
Pomiar 2-rejestrowy 1
+0x002
uint32/float
Pom_2rej2
Pomiar 2-rejestrowy 2
+0x004
uint32/float
Pom_2rej3
Pomiar 2-rejestrowy 3
+0x006
uint32/float
Pom_2rej4
Pomiar 2-rejestrowy 4
+0x008
uint32/float
Pom_2rej5
Pomiar 2-rejestrowy 5
str. 13
+0x00A
uint32/float
Pom_2rej6
Pomiar 2-rejestrowy 6
+0x00C
uint32/float
Pom_2rej7
Pomiar 2-rejestrowy 7
+0x00E
uint32/float
Pom_2rej8
Pomiar 2-rejestrowy 8
+0x010
uint32/float
Pom_2rej9
Pomiar 2-rejestrowy 9
+0x012
uint32/float
Pom_2rej10
Pomiar 2-rejestrowy 10
+0x014
uint16
Pom_2rej11
Pomiar 2-rejestrowy 11
+0x015
uint16
Pom_2rej12
Pomiar 2-rejestrowy 12
+0x016
uint16
Pom_1rej1
Pomiar 1-rejestrowy 1
+0x017
uint16
Pom_1rej2
Pomiar 1-rejestrowy 2
+0x018
uint16
Pom_1rej3
Pomiar 1-rejestrowy 3
+0x019
uint16
Pom_1rej4
Pomiar 1-rejestrowy 4
+0x01A
uint16
Pom_1rej5
Pomiar 1-rejestrowy 5
+0x01B
uint16
Pom_1rej6
Pomiar 1-rejestrowy 6
+0x01C
uint16
Pom_1rej7
Pomiar 1-rejestrowy 7
+0x01D
uint16
Pom_1rej8
Pomiar 1-rejestrowy 8
+0x01E
uint16
Pom_1rej9
Pomiar 1-rejestrowy 9
+0x01F
uint16
Pom_1rej10
Pomiar 1-rejestrowy 10
+0x020
uint16
Pom_1rej11
Pomiar 1-rejestrowy 11
+0x021
uint16
Pom_1rej12
Pomiar 1-rejestrowy 12
+0x022
uint16
Pom_1rej13
Pomiar 1-rejestrowy 13
+0x023
uint16
Pom_1rej14
Pomiar 1-rejestrowy 14
+0x024
uint16
Pom_1rej15
Pomiar 1-rejestrowy 15
+0x025
uint16
Pom_1rej16
Pomiar 1-rejestrowy 16
2 Nastawy
Odczyt funkcją 3 Zapis funkcją 16
Brak ograniczenia co do ilości odczytywanych rejestrów.
bajty wartości 1-rejestrowych B1*28 + B2 przesyłane w kolejności B1, B2
2.1 Konfiguracja kart I/O
Adres bazowy: 0x1200 Adres HEX Parametr Opis Zakres wartości
+0x000
Slot A
Karta w slocie A
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
+0x001
Slot B
Karta w slocie B
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
+0x002
Slot C
Karta w slocie C
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
+0x003
Slot D
Karta w slocie D
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
+0x004
Slot E
Karta w slocie E
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
+0x005
Slot F
Karta w slocie F
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
str. 14
+0x006
Slot G
Karta w slocie G
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
+0x007
Slot H
Karta w slocie H
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
+0x008
Slot I
Karta w slocie I
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
+0x009
Slot J
Karta w slocie J
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
+0x00A
Slot K
Karta w slocie K
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
+0x00B
Slot L
Karta w slocie L
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
+0x00C
Slot M
Karta w slocie M
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
+0x00D
Slot N
Karta w slocie N
0 = Pusty
1 = 8IN
2 = 12IN
3 = 8OUT
4 = PT
5 = AI20
6 = AI10
7 = AO20
8 = AO10
9 = ARC
10 = ARP
11 = TRR
12 = TMP
2.2 Zestaw aktywnych zabezpieczeń
Adres bazowy: 0x1300 Adres HEX Parametr Opis Zakres wartości
+0x000
NAST_W
Nastawy wspólne zabezpieczeń
0 = Nie
1 = Tak
+0x001
I>>
Zab. zwarciowe
0 = Nie
1 = Tak
+0x002
I>1
Zab. nadprądowe 1
0 = Nie
1 = Tak
+0x003
I>2
Zab. nadprądowe 2
0 = Nie
1 = Tak
+0x004
I>3
Zab. nadprądowe 3
0 = Nie
1 = Tak
+0x005
I>INV
Zab. nadprądowe zależne
0 = Nie
1 = Tak
+0x006
I0>1
Zab. ziemnozwarciowe 1
0 = Nie
1 = Tak
+0x007
I0>2
Zab. ziemnozwarciowe 2
0 = Nie
1 = Tak
+0x008
I0>d
Zab. ziemnozwarciowe kierunkowe
0 = Nie
1 = Tak
+0x009
Y0>
Zab. admitancyjne
0 = Nie
1 = Tak
+0x00A
Y0>d1
Zab. admitancyjne kierunkowe 1
0 = Nie
1 = Tak
+0x00B
Y0>d2
Zab. admitancyjne kierunkowe 2
0 = Nie
1 = Tak
+0x00C
U0>1
Zab. nadnapięciowe U0 1
0 = Nie
1 = Tak
+0x00D
U0>2
Zab. nadnapięciowe U0 2
0 = Nie
1 = Tak
+0x00E
U<1
Zab. podnapięciowe 1
0 = Nie
1 = Tak
+0x00F
U<2
Zab. podnapięciowe 2
0 = Nie
1 = Tak
+0x010
U>1
Zab. nadnapięciowe 1
0 = Nie
1 = Tak
+0x011
U>2
Zab. nadnapięciowe 2
0 = Nie
1 = Tak
+0x012
ΔU
Zab. od zmiany napięcia
0 = Nie
1 = Tak
+0x013
f<>
Zab. częstotliwościowe
0 = Nie
1 = Tak
+0x014
P>
Zab. zwrotnomocowe P
0 = Nie
1 = Tak
+0x015
Q>
Zab. zwrotnomocowe Q
0 = Nie
1 = Tak
+0x016
THERM
Zab. cieplne
0 = Nie
1 = Tak
+0x017
ASIM
Zab. od asymetrii
0 = Nie
1 = Tak
+0x018
RLOCK
Zab. od zablokowania wirnika
0 = Nie
1 = Tak
+0x019
tST>
Zab. czasu rozruchu silnika
0 = Nie
1 = Tak
str. 15
+0x01A
nST>
Blokada od częst. rozruchów silnika
0 = Nie
1 = Tak
+0x01B
I<
Zab. podprądowe
0 = Nie
1 = Tak
+0x01C
DIF.M
Zab. różnicowe silnika
0 = Nie
1 = Tak
+0x01D
Iss>
Zab. od wypadnięcia z synchronizmu
0 = Nie
1 = Tak
+0x01E
Ig>
Zab. prądu wew. baterii kond.
0 = Nie
1 = Tak
+0x01F
GAZ-PP
Zab. gazowo-przepływowe
0 = Nie
1 = Tak
+0x020
TEMP
Zab. temperaturowe
0 = Nie
1 = Tak
+0x021
ZEWN
Zab. zewnętrzne dwustanowe
0 = Nie
1 = Tak
+0x022
PT
Zab. termiczne PT
0 = Nie
1 = Tak
+0x023
ARC
Zab. łukoochronne
0 = Nie
1 = Tak
+0x024
SYNCHK
Synchrocheck
0 = Nie
1 = Tak
+0x025
ZS
Automatyka ZS
0 = Nie
1 = Tak
+0x026
LRW
Automatyka LRW
0 = Nie
1 = Tak
+0x027
SPZ
Automatyka SPZ
0 = Nie
1 = Tak
+0x028
SCO
Automatyka SCO
0 = Nie
1 = Tak
+0x029
SCOw
Automatyka SCO człon wykonawczy
0 = Nie
1 = Tak
+0x02A
AWSC
Automatyka AWSC
0 = Nie
1 = Tak
+0x02B
AZBKw
Automatyka AZBK człon wykonawczy
0 = Nie
1 = Tak
+0x02C
SZRw
Automatyka SZR człon wykonawczy
0 = Nie
1 = Tak
+0x02D
SPZW
Automatyka SPZ od zab. wyspowych
0 = Nie
1 = Tak
2.3 Parametry ogólne
Adres bazowy: 0x1000 Adres HEX Parametr Opis Zakres wartości Parametry przekładników
+0x000
In strona pierw. SN
Prąd znamionowy przekładnika prądowego po stronie pierwotnej SN
1÷5000 [A]
+0x001
In strona wtórna SN
Prąd znamionowy przekładnika prądowego po stronie wtórnej SN
0 = 1 [A]
1 = 5 [A]
+0x002
Un strona pierw. SN
Napięcie znamionowe przewodowe po stronie pierwotnej SN
1÷1300 [*0.1kV]
+0x003
Un strona wtórna SN
Napięcie znamionowe przewodowe po stronie wtórnej SN
58÷110 [V]
+0x004
Przekładnia I0 SN
Przekładnia dla pomiaru prądu I0 SN
1÷5000 [A/A]
+0x005
Przekładnia U0 SN
Przekładnia dla pomiaru napięcia U0 SN
1÷1300 [V/V]
+0x006
In strona pierw. nN
Prąd znamionowy przekładnika prądowego po stronie pierwotnej nN
1÷5000 [A]
+0x007
In strona wtórna nN
Prąd znamionowy przekładnika prądowego po stronie wtórnej nN
0 = 1 [A]
1 = 5 [A]
+0x008
Un strona pierw. nN
Napięcie znamionowe przewodowe po stronie pierwotnej nN
1000÷10000 [*0.1V]
+0x009
Un strona wtórna nN
Napięcie znamionowe przewodowe po stronie wtórnej nN
1000÷4000 [*0.1V]
+0x00A
Przekładnia I0 nN
Przekładnia dla pomiaru prądu I0 nN
1÷5000 [A/A]
+0x00B
Przekładnia U0 nN
Przekładnia dla pomiaru napięcia U0 nN
1÷1300 [V/V]
+0x00C
We bezp. U SN
Wejście zadziałania bezpieczników w obw. pomiaru napięcia
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x00D
We bezp. U0 SN
Wejście zadziałania bezpieczników w obw. pomiaru napięcia U0
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x00E
We bezp. Us SN
Wejście zadziałania bezpieczników w obw. pomiaru napięcia Us
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x00F
We bezp. Uszr SN
Wejście zadziałania bezpieczników w obw. pomiaru napięcia USZR
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
Pomiary
+0x010
Konf. przekładników U SN
Konfiguracja podłączenia przekładników napięciowych SN
0 = Gwiazda
1 = Układ V
+0x011
Konf. we I0 SN
Konfiguracja wejścia pomiaru I0 SN
0 = Niewykorzystane
1 = Pomiar I0
+0x012
Konf. we U0 SN
Konfiguracja wejścia pomiaru U0 SN
0 = Niewykorzystane
1 = Pomiar U0
2 = Pomiar U12synch
str. 16
+0x013
Konf. przekładników U nN
Konfiguracja podłączenia przekładników napięciowych nN
0 = Gwiazda
1 = Układ V
+0x014
Konf. we I0 nN
Konfiguracja wejścia pomiaru I0 nN
0 = Niewykorzystane
1 = Pomiar I0
+0x015
Konf. we U0 nN
Konfiguracja wejścia pomiaru U0 nN
0 = Niewykorzystane
1 = Pomiar U0
+0x016
Zmiana znaku I SN
Zmiana znaku próbek prądu SN
0 = Nie
1 = Tak
+0x017
Zmiana znaku U SN
Zmiana znaku próbek napięcia SN
0 = Nie
1 = Tak
+0x018
Zmiana znaku P,Q SN
Zmiana znaku mocy SN
0 = Nie
1 = Tak
+0x019
Zmiana znaku I0 SN
Zmiana znaku próbek prądu I0 SN
0 = Nie
1 = Tak
+0x01A
Zmiana znaku U0 SN
Zmiana znaku próbek napięcia U0 SN
0 = Nie
1 = Tak
+0x01B
Zmiana znaku I nN
Zmiana znaku próbek prądu nN
0 = Nie
1 = Tak
+0x01C
Zmiana znaku U nN
Zmiana znaku próbek napięcia nN
0 = Nie
1 = Tak
Zasilanie
+0x01D
Zasilanie na Z12 i Z34
Podwójne zasilanie sterownika
0 = Nie
1 = Tak
Logika
+0x01E
Aktywność
Aktywność logiki
0 = Nie
1 = Tak
+0x01F
Pamięć RS
Stany przerzutników RS podtrzymywane po zaniku zasilania
0 = Nie
1 = Tak
Współpraca z wyłącznikiem SN
+0x020
Sterowanie
Typ sterowania
0 = Cewki ZAM,OTW
1 = Cewka ZAM
+0x021
We zam. wył.
Wejście zamknięcia operacyjnego
Lo(nr_we)
Hi(nr_slot)
+0x022
We otw. wył.
Wejście otwarcia operacyjnego
Lo(nr_we)
Hi(nr_slot)
+0x023
We zam. z tele.
Wejście zamknięcia operacyjnego z telemechaniki
Lo(nr_we)
Hi(nr_slot)
+0x024
We otw. z tele.
Wejście otwarcia operacyjnego z telemechaniki
Lo(nr_we)
Hi(nr_slot)
+0x025
We kas. z tele.
Wejście kasowania z telemechaniki
Lo(nr_we)
Hi(nr_slot)
+0x026
Podtrzymanie impulsu otw.
Podtrzymanie impulsu otwarcia po zadziałaniu zabezpieczenia
0 = Nie
1 = Tak
+0x027
takt PDZ
Czas aktywności PDZ po operacyjnym zamknięciu wyłącznika
0÷60000 [*0.01s]
+0x028
We RN
Wejście - rozbrojenie napędu wyłącznika
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x029
t RN
Max. czas zbrojenia napędu wyłącznika
1÷120 [s]
+0x02A
We COW1
Wejście kontroli ciągłości obwodu 1 wyłączania wyłącznika
Lo(nr_we)
Hi(nr_slot)
+0x02B
We COW2
Wejście kontroli ciągłości obwodu 2 wyłączania wyłącznika
Lo(nr_we)
Hi(nr_slot)
+0x02C
We COZ
Wejście kontroli ciągłości obwodu załączania wyłącznika
Lo(nr_we)
Hi(nr_slot)
+0x02D
t COW/COZ
Czas zwłoki kontroli COW1,COW2,COZ
1÷5 [s]
+0x02E
Blk. od stanu wyłącznika
Blokada kontroli w zależności od stanu wyłącznika
0 = Nie
1 = Tak
+0x02F
We blokady COZ
Dodatkowe wejście blokady kontroli COZ
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
Współpraca z wyłącznikiem nN
+0x030
Nr łacz nN
Wybór nr łącznika który jest wył. nN
0 = Q2
1 = Q3
2 = Q4
3 = Q5
4 = Q6
5 = Q7
6 = Q8
+0x031
We RN nN
Wejście - rozbrojenie napędu wyłącznika nN
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x032
t RN nN
Max. czas zbrojenia napędu wyłącznika nN
1÷120 [s] Sygnalizacja AW/UP/AL
+0x033
AW
Działanie sygnalizacji AW
0 = Sygnał
1 = Impuls
+0x034
UP
Działanie sygnalizacji UP
0 = Sygnał
1 = Impuls
2 = Autokasowanie
+0x035
t imp. AW/UP
Czas impulsu AW/UP
1÷60000 [*0.01s]
+0x036
Autokasowanie AL
Automatyczne kasowanie sygnalizacji AL
0 = Nie
1 = Tak
+0x037
Kas. zad. z zatrz.
Kasowanie zadziałań zabezpieczeń z zatrzaskiem
0 = Nie
1 = Tak
Kontrola zużycia styków wyłącznika SN
+0x038
Aktywność
Aktywność kontroli zużycia styków wyłącznika
0 = Nie
1 = Tak
+0x039
Ir
Prąd znamionowy wyłącznika
100÷60000 [A]
+0x03A
NIr
Trwałość mechaniczna wyłącznika
1÷60000
+0x03B
Isc
Prąd zwarciowy wyłączalny wyłącznika
1000÷60000 [A]
+0x03C
NIsc
Trwałość przy prądzie zwarciowym wyłączalnym wyłącznika
1÷60000
+0x03D
Ityp
Typowy prąd zwarcia
100÷60000 [A]
+0x03E
NItyp
Alarmowa ilość pozostałych wyłączeń dla typowego prądu zwarcia
1÷200 Kontrola przekł. prądowych
+0x03F
Aktywność
Aktywność kontroli przekładników prądowych
0 = Nie
1 = Tak
str. 17
+0x040
Imax>
Prąd maksymalny
1÷200 [*0.01*In]
+0x041
Imin<
Prąd minimalny
1÷200 [*0.01*In]
+0x042
t
Czas zwłoki
1÷60000 [*0.01] Kontrola przekł. napięciowych
+0x043
Aktywność
Aktywność kontroli przekładników napięciowych
0 = Nie
1 = Tak
+0x044
Uneg>
Napięcie składowej przeciwnej
1÷100 [*0.01*Un]
+0x045
Ineg<
Prąd składowej przeciwnej
1÷100 [*0.01*In]
+0x046
t
Czas zwłoki
1÷60000 [*0.01] Sterowanie zdalne/lokalne
+0x047
Aktywność
Aktywność wyboru miejsca sterowania
0 = Nie
1 = Tak
+0x048
Tryb
Tryb działania
0 = Lok./Zdalne
1 = Zdalne
+0x049
We ster. lokalne
Wejście - sterowanie lokalne
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x04A
We przeł. st. lokalne
Wejście przełączenia na sterowanie lokalne
Lo(nr_we)
Hi(nr_slot)
+0x04B
We przeł. st. zdalne
Wejście przełączenia na sterowanie zdalne
Lo(nr_we)
Hi(nr_slot)
+0x04C
Pamięć stanu
Pamięć stanu sterowania po zaniku zasilania
0 = Nie
1 = Tak
Synchronizacja czasu
+0x04D
Tryb
Tryb synchronizacji czasu RTC
0 = Nieaktywna
1 = Master wy
2 = Slave we
3 = Master COM
+0x04E
Wy master
Wyjście synchronizacji dla trybu Master we/wy
Lo(nr_wy)
Hi(nr_slot)
+0x04F
We slave
Wejście synchronizacji dla trybu Slave we/wy
Lo(nr_we)
Hi(nr_slot)
+0x050
COM master
Port COM synchronizacji dla trybu Master COM
1÷2 Wyjścia sygnalizacyjne
+0x051
Wy syg. 1
Wyjście sygnalizacyjne 1
Lo(nr_wy)
Hi(nr_slot)
+0x052
Działanie wy. syg. 1
Działanie wyjścia sygnalizacyjnego 1
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x053
Wy syg. 2
Wyjście sygnalizacyjne 2
Lo(nr_wy)
Hi(nr_slot)
+0x054
Działanie wy. syg. 2
Działanie wyjścia sygnalizacyjnego 2
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x055
Wy syg. 3
Wyjście sygnalizacyjne 3
Lo(nr_wy)
Hi(nr_slot)
+0x056
Działanie wy. syg. 3
Działanie wyjścia sygnalizacyjnego 3
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
str. 18
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x057
Wy syg. 4
Wyjście sygnalizacyjne 4
Lo(nr_wy)
Hi(nr_slot)
+0x058
Działanie wy. syg. 4
Działanie wyjścia sygnalizacyjnego 4
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x059
Wy syg. 5
Wyjście sygnalizacyjne 5
Lo(nr_wy)
Hi(nr_slot)
+0x05A
Działanie wy. syg. 5
Działanie wyjścia sygnalizacyjnego 5
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x05B
Wy syg. 6
Wyjście sygnalizacyjne 6
Lo(nr_wy)
Hi(nr_slot)
+0x05C
Działanie wy. syg. 6
Działanie wyjścia sygnalizacyjnego 6
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x05D
Wy syg. 7
Wyjście sygnalizacyjne 7
Lo(nr_wy)
Hi(nr_slot)
+0x05E
Działanie wy. syg. 7
Działanie wyjścia sygnalizacyjnego 7
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x05F
Wy syg. 8
Wyjście sygnalizacyjne 8
Lo(nr_wy)
Hi(nr_slot)
+0x060
Działanie wy. syg. 8
Działanie wyjścia sygnalizacyjnego 8
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
str. 19
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
LED sygnalizacyjne
+0x061
Działanie LED1
Działanie LED1
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x062
Kolor LED1
Kolor LED1
0 = Czerwony
1 = Czerwony/Zielony
2 = Żółty
3 = R-Zad,Y-Pob
4 = R-Zad,Y-Pob.podt.
+0x063
Działanie LED2
Działanie LED2
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x064
Kolor LED2
Kolor LED2
0 = Czerwony
1 = Czerwony/Zielony
2 = Żółty
3 = R-Zad,Y-Pob
4 = R-Zad,Y-Pob.podt.
+0x065
Działanie LED3
Działanie LED3
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x066
Kolor LED3
Kolor LED3
0 = Czerwony
1 = Czerwony/Zielony
2 = Żółty
3 = R-Zad,Y-Pob
4 = R-Zad,Y-Pob.podt.
+0x067
Działanie LED4
Działanie LED4
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
str. 20
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x068
Kolor LED4
Kolor LED4
0 = Czerwony
1 = Czerwony/Zielony
2 = Żółty
3 = R-Zad,Y-Pob
4 = R-Zad,Y-Pob.podt.
+0x069
Działanie LED5
Działanie LED5
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x06A
Kolor LED5
Kolor LED5
0 = Czerwony
1 = Czerwony/Zielony
2 = Żółty
3 = R-Zad,Y-Pob
4 = R-Zad,Y-Pob.podt.
+0x06B
Działanie LED6
Działanie LED6
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x06C
Kolor LED6
Kolor LED6
0 = Czerwony
1 = Czerwony/Zielony
2 = Żółty
3 = R-Zad,Y-Pob
4 = R-Zad,Y-Pob.podt.
+0x06D
Działanie LED7
Działanie LED7
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x06E
Kolor LED7
Kolor LED7
0 = Czerwony
1 = Czerwony/Zielony
2 = Żółty
3 = R-Zad,Y-Pob
4 = R-Zad,Y-Pob.podt.
+0x06F
Działanie LED8
Działanie LED8
0 = Brak
1 = Al - alarm
2 = AW - zad. zab. otw.
3 = UP - zad. zab. syg.
4 = Zad. zab. analog.
5 = Pob. zab. analog.
6 = Zadziałanie ogólne
7 = Pobudzenie ogólne
8 = Zab. I>
9 = Zab. I0>
10 = Zab. U>
11 = Zab. U<
12 = Rozbrojenie napędu
13 = Blokada zamknięcia
14 = Rozbrojenie nap. nN
15 = Blokada zamkn. nN
str. 21
16 = Zab. I>>
17 = Zab. I>1
18 = Zab. I>2
19 = Zab. I>3
20 = Zab. I>4
21 = Zab. I>5
22 = Zab. I>12345
23 = Zab. U0>
24 = Zab. U0>nN
25 = Zab. f>
26 = Zab. f<
27 = Zab. ΔU
28 = Zab. U>sr
+0x070
Kolor LED8
Kolor LED8
0 = Czerwony
1 = Czerwony/Zielony
2 = Żółty
3 = R-Zad,Y-Pob
4 = R-Zad,Y-Pob.podt.
Przyciski funkcyjne F1..F4
+0x071
Działanie F1
Działanie przycisku F1
0 = Brak
1 = Aut. SPZ
2 = Aut. SCO
3 = Aut. SCOw
4 = Bank 1/2
5 = Ster.Lok/Zd
6 = Aut. SPZW
7 = SPZ/SCOw
+0x072
Działanie F2
Działanie przycisku F2
0 = Brak
1 = Aut. SPZ
2 = Aut. SCO
3 = Aut. SCOw
4 = Bank 1/2
5 = Ster.Lok/Zd
6 = Aut. SPZW
7 = SPZ/SCOw
+0x073
Działanie F3
Działanie przycisku F3
0 = Brak
1 = Aut. SPZ
2 = Aut. SCO
3 = Aut. SCOw
4 = Bank 1/2
5 = Ster.Lok/Zd
6 = Aut. SPZW
7 = SPZ/SCOw
+0x074
Działanie F4
Działanie przycisku F4
0 = Brak
1 = Aut. SPZ
2 = Aut. SCO
3 = Aut. SCOw
4 = Bank 1/2
5 = Ster.Lok/Zd
6 = Aut. SPZW
7 = SPZ/SCOw
Gorąca rezerwa
+0x075
Zapis nastaw
Zapis nastaw na pendrive gorącej rezerwy (w USB2)
0 = Nie
1 = Tak
+0x076
Zapis danych
Zapis danych na pendrive gorącej rezerwy (w USB2)
0 = Nie
1 = Tak
Parametry panelu
+0x077
Czas wylogowania
Czas wylogowania
1÷60 [min]
+0x078
Czas powr. do ekr. podst.
Czas powrotu do ekranu głównego
1÷60 [min]
+0x079
Wyświetlanie zdarzeń
Wyświetlanie bieżących zdarzeń
0 = Nie
1 = Tak
+0x07A
Sterowanie
Sterowanie łącznikami z panelu
0 = Nieaktywne
1 = Z potwierdzeniem
2 = Bez potwierdzenia
+0x07B
Kas. bieżącego zdarzenia
Kasowanie z panelu najpierw bieżącego zdarzenia
0 = Nie
1 = Tak
Rejestrator zakłóceń
+0x07C
Częstotliwość próbkowania
Częstotliwość próbkowania dla kanałów rejestratora
0 = 1.6kHz
1 = 3.2kHz
+0x07D
Ilość rejestracji
Ilość rejestracji przechowywana w pamięci
1÷39
+0x07E
Wyzw. rej. od zamkn. wył.
Wyzwolenie rejestratora zakłóceń od zamkn. wył,
0 = Nie
1 = Tak
+0x07F
%t rej. po wyzw. od zamkn. wył.
Czas rejestracji po wyzwoleniu rej. od zamkn. wył,
0÷100 [%]
+0x080
Wyzw. rej. z logiki
Wyzwolenie rejestratora zakłóceń z logiki
0 = Nie
1 = Tak
+0x081
%t rej. po wyzw. z logiki
Czas rejestracji po wyzwoleniu rej. z logiki
0÷100 [%]
+0x082
Rejestracja próbek I1
Zezwolenie na rejestrację próbek z kanału I1
0 = Nie
1 = Tak
+0x083
Rejestracja próbek I2
Zezwolenie na rejestrację próbek z kanału I2
0 = Nie
1 = Tak
+0x084
Rejestracja próbek I3
Zezwolenie na rejestrację próbek z kanału I3
0 = Nie
1 = Tak
+0x085
Rejestracja próbek U1
Zezwolenie na rejestrację próbek z kanału U1
0 = Nie
1 = Tak
+0x086
Rejestracja próbek U2
Zezwolenie na rejestrację próbek z kanału U2
0 = Nie
1 = Tak
+0x087
Rejestracja próbek U3
Zezwolenie na rejestrację próbek z kanału U3
0 = Nie
1 = Tak
+0x088
Rejestracja próbek I0
Zezwolenie na rejestrację próbek z kanału I0
0 = Nie
1 = Tak
+0x089
Rejestracja próbek U0
Zezwolenie na rejestrację próbek z kanału U0
0 = Nie
1 = Tak
+0x08A
Rejestracja próbek Ig
Zezwolenie na rejestrację próbek z kanału Ig
0 = Nie
1 = Tak
+0x08B
Rejestracja próbek I1 nN
Zezwolenie na rejestrację próbek z kanału I1 nN
0 = Nie
1 = Tak
+0x08C
Rejestracja próbek I2 nN
Zezwolenie na rejestrację próbek z kanału I2 nN
0 = Nie
1 = Tak
+0x08D
Rejestracja próbek I3 nN
Zezwolenie na rejestrację próbek z kanału I3 nN
0 = Nie
1 = Tak
+0x08E
Rejestracja próbek I1 nN
Zezwolenie na rejestrację próbek z kanału U1 nN
0 = Nie
1 = Tak
+0x08F
Rejestracja próbek I2 nN
Zezwolenie na rejestrację próbek z kanału U2 nN
0 = Nie
1 = Tak
+0x090
Rejestracja próbek I3 nN
Zezwolenie na rejestrację próbek z kanału U3 nN
0 = Nie
1 = Tak
+0x091
Kanał niedostępny
0 = Nie
1 = Tak
str. 22
Rejestrator kryterialny
+0x092
Ilość rejestracji
Ilość rejestracji przechowywana w pamięci
1÷40
+0x093
Wyzw. rej. od przekr. I
Wyzwolenie rejestratora kryterialnego od przekroczenia I
0 = Nie
1 = Tak
+0x094
Is
Próg wyzwolenia rejestratora od przekroczenia I
20÷3000 [*0.01*Ib]
+0x095
tI>
Czas zwłoki wyzwolenia rejestratora od przekroczenia I
0÷60000 [*0.01s]
+0x096
Wyzw. rej. od przekr. Up
Wyzwolenie rejestratora kryterialnego od przekroczenia Up
0 = Nie
1 = Tak
+0x097
Ups
Próg wyzwolenia rejestratora od przekroczenia Up
50÷120 [*0.01*Ub]
+0x098
tUp>
Czas zwłoki wyzwolenia rejestratora od przekroczenia Up
0÷60000 [*0.01s]
+0x099
Wyzw. rej. od przekr. I0
Wyzwolenie rejestratora kryterialnego od przekroczenia I0
0 = Nie
1 = Tak
+0x09A
I0s
Próg wyzwolenia rejestratora od przekroczenia I0 (po stronie wtórnej)
5÷5000 [mA]
+0x09B
tI0>
Czas zwłoki wyzwolenia rejestratora od przekroczenia I0
0÷60000 [*0.01s]
+0x09C
Wyzw. rej. od przekr. U0
Wyzwolenie rejestratora kryterialnego od przekroczenia U0
0 = Nie
1 = Tak
+0x09D
U0s
Próg wyzwolenia rejestratora od przekroczenia U0 (po stronie wtórnej)
40÷1200 [*0.1V]
+0x09E
tU0>
Czas zwłoki wyzwolenia rejestratora od od przekroczenia U0
0÷60000 [*0.01s]
+0x09F
Wyzw. rej. od zamkn. wył.
Wyzwolenie rejestratora zakłóceń od zamkn. wył,
0 = Nie
1 = Tak
+0x0A0
Wyzw. rej. z logiki
Wyzwolenie rejestratora zakłóceń z logiki
0 = Nie
1 = Tak
+0x0A1
Rejestracja pomiaru I1
Zezwolenie na rejestrację pomiaru I1
0 = Nie
1 = Tak
+0x0A2
Rejestracja pomiaru I2
Zezwolenie na rejestrację pomiaru I2
0 = Nie
1 = Tak
+0x0A3
Rejestracja pomiaru I3
Zezwolenie na rejestrację pomiaru I3
0 = Nie
1 = Tak
+0x0A4
Rejestracja pomiaru U1
Zezwolenie na rejestrację pomiaru U1
0 = Nie
1 = Tak
+0x0A5
Rejestracja pomiaru U2
Zezwolenie na rejestrację pomiaru U2
0 = Nie
1 = Tak
+0x0A6
Rejestracja pomiaru U3
Zezwolenie na rejestrację pomiaru U3
0 = Nie
1 = Tak
+0x0A7
Rejestracja pomiaru I0
Zezwolenie na rejestrację pomiaru I0
0 = Nie
1 = Tak
+0x0A8
Rejestracja pomiaru U0
Zezwolenie na rejestrację pomiaru U0
0 = Nie
1 = Tak
+0x0A9
Rejestracja pomiaru φ0
Zezwolenie na rejestrację pomiaru φ0
0 = Nie
1 = Tak
+0x0AA
Rejestracja pomiaru I1 nN
Zezwolenie na rejestrację pomiaru I1 nN
0 = Nie
1 = Tak
+0x0AB
Rejestracja pomiaru I2 nN
Zezwolenie na rejestrację pomiaru I2 nN
0 = Nie
1 = Tak
+0x0AC
Rejestracja pomiaru I3 nN
Zezwolenie na rejestrację pomiaru I3 nN
0 = Nie
1 = Tak
+0x0AD
Rejestracja pomiaru U1 nN
Zezwolenie na rejestrację pomiaru U1 nN
0 = Nie
1 = Tak
+0x0AE
Rejestracja pomiaru U2 nN
Zezwolenie na rejestrację pomiaru U2 nN
0 = Nie
1 = Tak
+0x0AF
Rejestracja pomiaru U3 nN
Zezwolenie na rejestrację pomiaru U3 nN
0 = Nie
1 = Tak
Rejestrator profilu mocy
+0x0B0
Krok rejestracji
Krok rejestracji profilu mocy
0 = 1
1 = 2
2 = 3
3 = 4
4 = 5
5 = 6
6 = 10
7 = 12
8 = 15
9 = 20
10 = 30
11 = 60
Rejestrator jakości energii
+0x0B1
Krok rejestracji
Krok rejestracji
0 = 1
1 = 2
2 = 3
3 = 4
4 = 5
5 = 6
6 = 10
7 = 12
8 = 15
9 = 20
10 = 30
11 = 60
Kompatybilność
+0x0B2
Maska
Maska bitowa
0÷65535
2.4 Parametry komunikacji
Adres bazowy: 0x1100
str. 23
Adres HEX Parametr Opis Zakres wartości Parametry portu COM 1
+0x000
Protokół
Protokół
0 = MODBUS
1 = IEC103
2 = DNP
3 = CANBUS
4 = PROFIBUS
+0x001
Baud
Prędkość transmisji
0 = 4800
1 = 9600
2 = 19200
3 = 38400
4 = 57600
5 = 115200
+0x002
Param.
Parametry
0 = 8N1
1 = 8E1
2 = 8O1
3 = 8N2
4 = 8E2
5 = 8O2
+0x003
Timeout
Dodatkowy timeout międzyznakowy
0÷100 [ms] Parametry portu COM 2
+0x004
Protokół
Protokół
0 = MODBUS
1 = IEC103
2 = DNP
3 = CANBUS
4 = PROFIBUS
+0x005
Baud
Prędkość transmisji
0 = 4800
1 = 9600
2 = 19200
3 = 38400
4 = 57600
5 = 115200
+0x006
Param.
Parametry
0 = 8N1
1 = 8E1
2 = 8O1
3 = 8N2
4 = 8E2
5 = 8O2
+0x007
Timeout
Dodatkowy timeout międzyznakowy
0÷100 [ms] Parametry ETHERNET
+0x008
Aktywność
Aktywność portu ETHERNET
0 = Nie
1 = Tak
+0x009
IP1
Adres IP1
0÷255
+0x00A
IP2
Adres IP2
0÷255
+0x00B
IP3
Adres IP3
0÷255
+0x00C
IP4
Adres IP4
0÷255
+0x00D
MSK1
Maska IP1
0÷255
+0x00E
MSK2
Maska IP2
0÷255
+0x00F
MSK3
Maska IP3
0÷255
+0x010
MSK4
Maska IP4
0÷255 Parametry MODBUS
+0x011
Adres Modbus
Adres e2TANGO w protokole MODBUS
1÷199
+0x012
Akt. MinMax COM1
Aktywność obszaru pomiarów MinMax dla COM1
0 = Nie
1 = Tak
+0x013
Akt. MinMax COM2
Aktywność obszaru pomiarów MinMax dla COM2
0 = Nie
1 = Tak
+0x014
Akt. MinMax ETH1
Aktywność obszaru pomiarów MinMax dla łącza ETH1 (porty 502, 10503)
0 = Nie
1 = Tak
+0x015
Akt. MinMax ETH2
Aktywność obszaru pomiarów MinMax dla łącza ETH2 (porty 10502, 10504)
0 = Nie
1 = Tak
+0x016
Akt. konfig. pom.
Aktywność obszaru pomiarów konfigurowalnych
0 = Nie
1 = Tak
+0x017
Adr. 2R1 k. pom.
Adres pomiaru 2-rejestrowego 1 obszaru pomiarów konfigurowalnych
0÷250
+0x018
Adr. 2R2 k. pom.
Adres pomiaru 2-rejestrowego 2 obszaru pomiarów konfigurowalnych
0÷250
+0x019
Adr. 2R3 k. pom.
Adres pomiaru 2-rejestrowego 3 obszaru pomiarów konfigurowalnych
0÷250
+0x01A
Adr. 2R4 k. pom.
Adres pomiaru 2-rejestrowego 4 obszaru pomiarów konfigurowalnych
0÷250
+0x01B
Adr. 2R5 k. pom.
Adres pomiaru 2-rejestrowego 5 obszaru pomiarów konfigurowalnych
0÷250
+0x01C
Adr. 2R6 k. pom.
Adres pomiaru 2-rejestrowego 6 obszaru pomiarów konfigurowalnych
0÷250
+0x01D
Adr. 2R7 k. pom.
Adres pomiaru 2-rejestrowego 7 obszaru pomiarów konfigurowalnych
0÷250
+0x01E
Adr. 2R8 k. pom.
Adres pomiaru 2-rejestrowego 8 obszaru pomiarów konfigurowalnych
0÷250
+0x01F
Adr. 2R9 k. pom.
Adres pomiaru 2-rejestrowego 9 obszaru pomiarów konfigurowalnych
0÷250
+0x020
Adr. 2R10 k. pom.
Adres pomiaru 2-rejestrowego 10 obszaru pomiarów konfigurowalnych
0÷250
+0x021
Adr. 2R11 k. pom.
Adres pomiaru 2-rejestrowego 11 obszaru pomiarów konfigurowalnych
0÷250
+0x022
Adr. 2R12 k. pom.
Adres pomiaru 2-rejestrowego 12 obszaru pomiarów konfigurowalnych
0÷250
+0x023
Adr. 1R1 k. pom.
Adres pomiaru 1-rejestrowego 1 obszaru pomiarów konfigurowalnych
0÷250
str. 24
+0x024
Adr. 1R2 k. pom.
Adres pomiaru 1-rejestrowego 2 obszaru pomiarów konfigurowalnych
0÷250
+0x025
Adr. 1R3 k. pom.
Adres pomiaru 1-rejestrowego 3 obszaru pomiarów konfigurowalnych
0÷250
+0x026
Adr. 1R4 k. pom.
Adres pomiaru 1-rejestrowego 4 obszaru pomiarów konfigurowalnych
0÷250
+0x027
Adr. 1R5 k. pom.
Adres pomiaru 1-rejestrowego 5 obszaru pomiarów konfigurowalnych
0÷250
+0x028
Adr. 1R6 k. pom.
Adres pomiaru 1-rejestrowego 6 obszaru pomiarów konfigurowalnych
0÷250
+0x029
Adr. 1R7 k. pom.
Adres pomiaru 1-rejestrowego 7 obszaru pomiarów konfigurowalnych
0÷250
+0x02A
Adr. 1R8 k. pom.
Adres pomiaru 1-rejestrowego 8 obszaru pomiarów konfigurowalnych
0÷250
+0x02B
Adr. 1R9 k. pom.
Adres pomiaru 1-rejestrowego 9 obszaru pomiarów konfigurowalnych
0÷250
+0x02C
Adr. 1R10 k. pom.
Adres pomiaru 1-rejestrowego 10 obszaru pomiarów konfigurowalnych
0÷250
+0x02D
Adr. 1R11 k. pom.
Adres pomiaru 1-rejestrowego 11 obszaru pomiarów konfigurowalnych
0÷250
+0x02E
Adr. 1R12 k. pom.
Adres pomiaru 1-rejestrowego 12 obszaru pomiarów konfigurowalnych
0÷250
+0x02F
Adr. 1R13 k. pom.
Adres pomiaru 1-rejestrowego 13 obszaru pomiarów konfigurowalnych
0÷250
+0x030
Adr. 1R14 k. pom.
Adres pomiaru 1-rejestrowego 14 obszaru pomiarów konfigurowalnych
0÷250
+0x031
Adr. 1R15 k. pom.
Adres pomiaru 1-rejestrowego 15 obszaru pomiarów konfigurowalnych
0÷250
+0x032
Adr. 1R16 k. pom.
Adres pomiaru 1-rejestrowego 16 obszaru pomiarów konfigurowalnych
0÷250 Parametry IEC103
+0x033
Adres IEC103
Adres e2TANGO w protokole IEC103
1÷254
+0x034
Tmax synch. t
Maksymalny okres synchronizacji zegarów
1÷600 [s]
+0x035
ASDU pomiarów
ASDU telemetryczne
0 = Brak
1 = 3.1
2 = 3.2
3 = 3.3
4 = 3.4
5 = 9
6 = 9 nstd.
+0x036
INF ASDU9 nstd.
INF ASDU9 niestandardowego
149÷159
+0x037
T pomiarów
Okres ASDU telemetrycznych
1÷600 [s]
+0x038
I1 w ASDU9 nstd.
Pomiar I1 w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x039
I2 w ASDU9 nstd.
Pomiar I2 w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x03A
I3 w ASDU9 nstd.
Pomiar I3 w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x03B
I0 w ASDU9 nstd.
Pomiar I0 w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x03C
U1 w ASDU9 nstd.
Pomiar U1 w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x03D
U2 w ASDU9 nstd.
Pomiar U2 w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x03E
U3 w ASDU9 nstd.
Pomiar U3 w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x03F
U0 w ASDU9 nstd.
Pomiar U0 w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x040
U12 w ASDU9 nstd.
Pomiar U12 w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x041
U23 w ASDU9 nstd.
Pomiar U23 w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x042
U31 w ASDU9 nstd.
Pomiar U31 w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x043
P w ASDU9 nstd.
Pomiar P w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x044
Q w ASDU9 nstd.
Pomiar Q w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x045
f w ASDU9 nstd.
Pomiar f w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x046
Us w ASDU9 nstd.
Pomiar Us w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x047
cos w ASDU9 nstd.
Pomiar cos w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x048
tg w ASDU9 nstd.
Pomiar tg w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x049
I1nN w ASDU9 nstd.
Pomiar I1 str. nN w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x04A
I2nN w ASDU9 nstd.
Pomiar I2 str. nN w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x04B
I3nN w ASDU9 nstd.
Pomiar I3 str. nN w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x04C
U1nN w ASDU9 nstd.
Pomiar U1 str. nN w ASDU9 niestandardowym
0 = Nie
1 = Tak
str. 25
+0x04D
U2nN w ASDU9 nstd.
Pomiar U2 str. nN w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x04E
U3nN w ASDU9 nstd.
Pomiar U3 str. nN w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x04F
U12nN w ASDU9 nstd.
Pomiar U12 str. nN w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x050
U23nN w ASDU9 nstd.
Pomiar U23 str. nN w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x051
U31nN w ASDU9 nstd.
Pomiar U31 str. nN w ASDU9 niestandardowym
0 = Nie
1 = Tak
+0x052
ASDU pom. energii
Przesyłanie ASDU telemetrycznych energii
0 = Nie
1 = Tak
+0x053
T pomiarów energii
Okres ASDU telemetrycznych energii
1÷600 [s]
+0x054
Stan łączników
Sposób przesyłania ASDU stanu łączników
0 = 1-BIT
1 = 2-BIT
2 = 2-BIT(2)
+0x055
ASDU4 po otw.
ASDU4 po otwarciu wyłącznika
0 = Nie
1 = Tak
+0x056
ASDU zabezpieczeń
ASDU zadziałania zabezpieczeń
1÷2
+0x057
Skala pomiarów
Skalowanie pomiarów
0 = *1.2
1 = *2.4
Parametry DNP
+0x058
Adres DNP
Adres e2TANGO w protokole DNP3.0
1÷65534
+0x059
Tmax synch. t
Maksymalny okres synchronizacji zegarów
1÷600 [s]
+0x05A
SBO Timeout
Select-Operate timeout
1÷600 [s]
+0x05B
ΔI
Zmiana dla I1, I2, I3
5÷100 [*0.01*In]
+0x05C
ΔU
Zmiana dla U12, U23, U31
5÷100 [*0.01*Un]
+0x05D
ΔI0
Zmiana dla I0 (str. wtórna przekładników)
5÷1000 [mA]
+0x05E
ΔU0
Zmiana dla U0 (str. wtórna przekładników)
1÷100 [V]
+0x05F
ΔP,Q
Zmiana dla P, Q
5÷100 [*0.01*Sn]
+0x060
Δf
Zmiana dla f
1÷100 [*0.01Hz] Parametry CANBUS
+0x061
Adres Canbus
Adres e2TANGO w protokole CANBUS
160÷255
+0x062
Offset meldunków
Offset numerów serii meldunkowych normalnych i szybkich
0÷240
+0x063
Meldunki I
Przesyłanie meldunków I1, I2, I3 (serie 0,1,2)
0 = Nie
1 = Tak
+0x064
Meldunki U
Przesyłanie meldunków U1, U2, U3 (serie 3,4,5)
0 = Nie
1 = Tak
+0x065
Meldunki LOG
Przesyłanie meldunków stanu sygnałów logiki 1-32 (serie 6,7)
0 = Nie
1 = Tak
+0x066
Meldunki ZAB/LOG
Przesyłanie meldunków zabezpieczeń / logiki 33-64 (serie 8,9)
0 = NIE
1 = TAK(ZAB)
2 = TAK(LOG)
+0x067
Meldunki SW
Przesyłanie meldunków stanów łączników (seria 10), (kolejność bitów w serii)
0 = NIE
1 = TAK(OTW,ZAM)
2 = TAK(ZAM,OTW)
Parametry PROFIBUS
+0x068
Adres Profibus
Adres e2TANGO w protokole Profibus
1÷126
+0x069
Adres obszaru 1
Adres początku danych mapy Modbus dla obszaru 1
0÷65535
+0x06A
Ilość słów ob. 1
Ilość słów obszaru 1
0÷64
+0x06B
Adres obszaru 2
Adres początku danych mapy Modbus dla obszaru 2
0÷65535
+0x06C
Ilość słów ob. 2
Ilość słów obszaru 2
0÷64
+0x06D
Adres obszaru 3
Adres początku danych mapy Modbus dla obszaru 3
0÷65535
+0x06E
Ilość słów ob. 3
Ilość słów obszaru 3
0÷64
+0x06F
Adres obszaru 4
Adres początku danych mapy Modbus dla obszaru 4
0÷65535
+0x070
Ilość słów ob. 4
Ilość słów obszaru 4
0÷64
+0x071
Adres obszaru 5
Adres początku danych mapy Modbus dla obszaru 5
0÷65535
+0x072
Ilość słów ob. 5
Ilość słów obszaru 5
0÷64
+0x073
Adres obszaru 6
Adres początku danych mapy Modbus dla obszaru 6
0÷65535
+0x074
Ilość słów ob. 6
Ilość słów obszaru 6
0÷64
+0x075
Adres obszaru 7
Adres początku danych mapy Modbus dla obszaru 7
0÷65535
+0x076
Ilość słów ob. 7
Ilość słów obszaru 7
0÷64
+0x077
Adres obszaru 8
Adres początku danych mapy Modbus dla obszaru 8
0÷65535
+0x078
Ilość słów ob. 8
Ilość słów obszaru 8
0÷64
str. 26
2.5 Banki nastaw zabezpieczeń
Adres bazowy: Bank 1: 0x0000, Bank 2: 0x0400, Bank 3: 0x0800, Bank 4: 0x0C00 Adres HEX Parametr Opis Zakres wartości Nastawy wspólne
+0x000
Ib
Prąd znamionowy dla zabezpieczeń po stronie pierwotnej (prąd bazowy) SN
10÷50000 [*0.1A]
+0x001
Ub
Napięcie znamionowe przewodowe dla zabezpieczeń po stronie pierwotnej SN
1÷1300 [*0.1kV]
+0x002
Dział.kier.?
Działanie zab. kierunkowych przy braku pomiaru kierunku
0 = Nie
1 = Tak
+0x003
Ib_nN
Prąd znamionowy dla zabezpieczeń nN po stronie pierwotnej (prąd bazowy)
10÷50000 [*0.1A]
+0x004
Ub_nN
Napięcie znamionowe przewodowe dla zabezpieczeń nN po stronie pierwotnej
1000÷30000 [*0.1V] Parametry zab. I>>
+0x005
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x006
Kryterium
Wielkość kryterialna działania zabezpieczenia
0 = SN I harm.
1 = SN RMS
+0x007
Kierunek działania
Kierunek działania zabezpieczenia
0 = Bezkier.
1 = Dodatnia
2 = Ujemna
+0x008
Is
Próg zadziałania zabezpieczenia
10÷3000 [*0.01*Ib]
+0x009
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x00A
k odpadu
Współczynnik odpadu zabezpieczenia
50÷99 [*0.01]
+0x00B
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x00C
Blokada 2h
Próg blokady działania od II harmonicznej (0 - bez blokady)
0÷100 [%]
+0x00D
Akt. PDZ
Aktywność PDZ
0 = Nie
1 = Tak
+0x00E
t PDZ
Czas zwłoki przy PDZ
0÷600 [*0.01s]
+0x00F
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x010
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. I>1
+0x011
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x012
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x013
Kryterium
Wielkość kryterialna działania zabezpieczenia
0 = SN I harm.
1 = SN RMS
2 = nN I harm.
3 = nN RMS
+0x014
Kierunek działania
Kierunek działania zabezpieczenia
0 = Bezkier.
1 = Dodatnia
2 = Ujemna
+0x015
Is
Próg zadziałania zabezpieczenia
5÷3000 [*0.01*Ib]
+0x016
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x017
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x018
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x019
Blokada 2h
Próg blokady działania od II harmonicznej (0 - bez blokady)
0÷100 [%]
+0x01A
Akt. PDZ
Aktywność PDZ
0 = Nie
1 = Tak
+0x01B
t PDZ
Czas zwłoki przy PDZ
0÷600 [*0.01s]
+0x01C
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x01D
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. I>2
+0x01E
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x01F
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x020
Kryterium
Wielkość kryterialna działania zabezpieczenia
0 = SN I harm.
1 = SN RMS
2 = nN I harm.
3 = nN RMS
+0x021
Kierunek działania
Kierunek działania zabezpieczenia
0 = Bezkier.
1 = Dodatnia
2 = Ujemna
+0x022
Is
Próg zadziałania zabezpieczenia
5÷3000 [*0.01*Ib]
+0x023
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x024
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x025
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x026
Blokada 2h
Próg blokady działania od II harmonicznej (0 - bez blokady)
0÷100 [%]
+0x027
Akt. PDZ
Aktywność PDZ
0 = Nie
1 = Tak
str. 27
+0x028
t PDZ
Czas zwłoki przy PDZ
0÷600 [*0.01s]
+0x029
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x02A
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. I>3
+0x02B
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x02C
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x02D
Kryterium
Wielkość kryterialna działania zabezpieczenia
0 = SN I harm.
1 = SN RMS
2 = nN I harm.
3 = nN RMS
+0x02E
Kierunek działania
Kierunek działania zabezpieczenia
0 = Bezkier.
1 = Dodatnia
2 = Ujemna
+0x02F
Is
Próg zadziałania zabezpieczenia
5÷3000 [*0.01*Ib]
+0x030
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x031
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x032
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x033
Blokada 2h
Próg blokady działania od II harmonicznej (0 - bez blokady)
0÷100 [%]
+0x034
Akt. PDZ
Aktywność PDZ
0 = Nie
1 = Tak
+0x035
t PDZ
Czas zwłoki przy PDZ
0÷600 [*0.01s]
+0x036
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x037
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. I>4
+0x038
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x039
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x03A
Kryterium
Wielkość kryterialna działania zabezpieczenia
0 = SN I harm.
1 = SN RMS
2 = nN I harm.
3 = nN RMS
+0x03B
Kierunek działania
Kierunek działania zabezpieczenia
0 = Bezkier.
1 = Dodatnia
2 = Ujemna
+0x03C
Is
Próg zadziałania zabezpieczenia
5÷3000 [*0.01*Ib]
+0x03D
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x03E
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x03F
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x040
Blokada 2h
Próg blokady działania od II harmonicznej (0 - bez blokady)
0÷100 [%]
+0x041
Akt. PDZ
Aktywność PDZ
0 = Nie
1 = Tak
+0x042
t PDZ
Czas zwłoki przy PDZ
0÷600 [*0.01s]
+0x043
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x044
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. I>5
+0x045
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x046
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x047
Kryterium
Wielkość kryterialna działania zabezpieczenia
0 = SN I harm.
1 = SN RMS
2 = nN I harm.
3 = nN RMS
+0x048
Kierunek działania
Kierunek działania zabezpieczenia
0 = Bezkier.
1 = Dodatnia
2 = Ujemna
+0x049
Is
Próg zadziałania zabezpieczenia
5÷3000 [*0.01*Ib]
+0x04A
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x04B
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x04C
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x04D
Blokada 2h
Próg blokady działania od II harmonicznej (0 - bez blokady)
0÷100 [%]
+0x04E
Akt. PDZ
Aktywność PDZ
0 = Nie
1 = Tak
+0x04F
t PDZ
Czas zwłoki przy PDZ
0÷600 [*0.01s]
+0x050
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x051
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. I>INV
+0x052
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x053
Kryterium
Wielkość kryterialna działania zabezpieczenia
0 = SN I harm.
1 = SN RMS
2 = nN I harm.
3 = nN RMS
+0x054
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x055
Charakterystyka
Charakterystyka działania zabezpieczenia
0 = Inverse
1 = Very inv.
2 = Ext. inv.
3 = IEEE Mod.
str. 28
4 = IEEE Very
5 = IEEE Ext.
6 = Użytkow.
+0x056
Is
Próg zadziałania zabezpieczenia
100÷200 [*0.01*Ib]
+0x057
tm
Mnożnik czasu charakterystyk standardowych
1÷500 [*0.1]
+0x058
t I=1.1Is
Czas zadziałania zabezpieczenia dla I=1.1Is charakterystyki użytkownika
1÷18000 [s]
+0x059
t I=1.2Is
Czas zadziałania zabezpieczenia dla I=1.2Is charakterystyki użytkownika
1÷18000 [s]
+0x05A
t I=1.5Is
Czas zadziałania zabezpieczenia dla I=1.5Is charakterystyki użytkownika
1÷18000 [s]
+0x05B
t I=2.0Is
Czas zadziałania zabezpieczenia dla I=2.0Is charakterystyki użytkownika
1÷1800 [s]
+0x05C
t I=3.0Is
Czas zadziałania zabezpieczenia dla I=3.0Is charakterystyki użytkownika
1÷180 [s]
+0x05D
t I=6.0Is
Czas zadziałania zabezpieczenia dla I=6.0Is charakterystyki użytkownika
1÷180 [*0.1s]
+0x05E
tr
Czas odpadu dla charakterystyk IEC i użytkownika
0÷18000 [s]
+0x05F
Qalarm
Poziom alarmowy (pobudzenia UP)
10÷100 [%]
+0x060
Qblk
Poziom blokowania zamknięcia wyłącznika
10÷100 [%]
+0x061
We Reset
Wejście kasowania liczników zabezpieczenia
Lo(nr_we)
Hi(nr_slot)
+0x062
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x063
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. I0>1
+0x064
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x065
I0s
Próg I0 działania zabezpieczenia (po stronie wtórnej)
5÷5000 [mA]
+0x066
t
Czas zwłoki działania zabezpieczenia
0÷6000 [*0.01s]
+0x067
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x068
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x069
Stabilizacja U0
Aktywność progu napięcia U0
0 = Nie
1 = Tak
+0x06A
U0 min.
Próg U0 działania zabezpieczenia (po stronie wtórnej)
40÷1000 [*0.1V]
+0x06B
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x06C
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. I0>2
+0x06D
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x06E
I0s
Próg I0 działania zabezpieczenia (po stronie wtórnej)
5÷5000 [mA]
+0x06F
t
Czas zwłoki działania zabezpieczenia
0÷6000 [*0.01s]
+0x070
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x071
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x072
Stabilizacja U0
Aktywność progu napięcia U0
0 = Nie
1 = Tak
+0x073
U0 min
Próg U0 działania zabezpieczenia (po stronie wtórnej)
40÷1000 [*0.1V]
+0x074
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x075
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. I0>nN
+0x076
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x077
I0s
Próg I0 działania zabezpieczenia (po stronie wtórnej)
5÷5000 [mA]
+0x078
t
Czas zwłoki działania zabezpieczenia
0÷6000 [*0.01s]
+0x079
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x07A
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x07B
Stabilizacja U0
Aktywność progu napięcia U0
0 = Nie
1 = Tak
+0x07C
U0 min
Próg U0 działania zabezpieczenia (po stronie wtórnej)
40÷1000 [*0.1V]
+0x07D
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x07E
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. I0>d
+0x07F
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
str. 29
+0x080
Typ
Typ zabezpieczenia
0 = Kąt φ0
1 = Czynnomocowe
2 = Biernomocowe
+0x081
I0s
Próg I0 działania zabezpieczenia (po stronie wtórnej)
5÷5000 [mA]
+0x082
φ
Kąt charakterystyczny zabezpieczenia
0÷359 [°]
+0x083
t
Czas zwłoki działania zabezpieczenia
0÷6000 [*0.01s]
+0x084
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x085
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x086
U0 min
Próg U0 działania zabezpieczenia (po stronie wtórnej)
40÷1000 [*0.1V]
+0x087
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x088
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. Y0>
+0x089
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x08A
Y0s
Próg Y0 działania zabezpieczenia (po stronie wtórnej)
5÷5000 [*0.01mS]
+0x08B
t
Czas zwłoki działania zabezpieczenia
0÷6000 [*0.01s]
+0x08C
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x08D
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x08E
U0 min
Próg U0 działania zabezpieczenia (po stronie wtórnej)
40÷1000 [*0.1V]
+0x08F
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x090
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. Y0>d1
+0x091
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x092
Typ
Typ zabezpieczenia
0 = Kąt φ0
1 = Kondukt.
2 = Suscept.
+0x093
Kierunkowość
Kierunkowość zabezpieczenia
0 = Bezkier.
1 = Dodatnia
2 = Ujemna
+0x094
Y0s
Próg Y0 działania zabezpieczenia (po stronie wtórnej)
5÷5000 [*0.01mS]
+0x095
φ
Kąt charakterystyczny zabezpieczenia
0÷359 [°]
+0x096
t
Czas zwłoki działania zabezpieczenia
0÷6000 [*0.01s]
+0x097
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x098
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x099
U0 min
Próg U0 działania zabezpieczenia (po stronie wtórnej)
40÷1000 [*0.1V]
+0x09A
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x09B
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. Y0>d2
+0x09C
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x09D
Typ
Typ zabezpieczenia
0 = Kąt φ0
1 = Kondukt.
2 = Suscept.
+0x09E
Kierunkowość
Kierunkowość zabezpieczenia
0 = Bezkier.
1 = Dodatnia
2 = Ujemna
+0x09F
Y0s
Próg Y0 działania zabezpieczenia (po stronie wtórnej)
5÷5000 [*0.01mS]
+0x0A0
φ
Kąt charakterystyczny zabezpieczenia
0÷359 [°]
+0x0A1
t
Czas zwłoki działania zabezpieczenia
0÷6000 [*0.01s]
+0x0A2
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x0A3
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x0A4
U0 min
Próg U0 działania zabezpieczenia (po stronie wtórnej)
40÷1000 [*0.1V]
+0x0A5
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x0A6
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. U0>1
+0x0A7
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x0A8
U0s
Próg U0 działania zabezpieczenia (po stronie wtórnej)
40÷1000 [*0.1V]
+0x0A9
t
Czas zwłoki działania zabezpieczenia
0÷6000 [*0.01s]
+0x0AA
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x0AB
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x0AC
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x0AD
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. U0>2
+0x0AE
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
str. 30
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x0AF
U0s
Próg U0 działania zabezpieczenia (po stronie wtórnej)
40÷1000 [*0.1V]
+0x0B0
t
Czas zwłoki działania zabezpieczenia
0÷6000 [*0.01s]
+0x0B1
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x0B2
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x0B3
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x0B4
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. U0>nN
+0x0B5
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x0B6
U0s
Próg U0 działania zabezpieczenia (po stronie wtórnej)
40÷1000 [*0.1V]
+0x0B7
t
Czas zwłoki działania zabezpieczenia
0÷6000 [*0.01s]
+0x0B8
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x0B9
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x0BA
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x0BB
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. U<1
+0x0BC
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x0BD
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x0BE
Typ
Typ zabezpieczenia
0 = Uf 1-faz SN
1 = Uf 3-faz SN
2 = Up 1-faz SN
3 = Up 3-faz SN
4 = Uf 1-faz nN
5 = Uf 3-faz nN
6 = Up 1-faz nN
7 = Up 3-faz nN
+0x0BF
Us
Próg zadziałania zabezpieczenia
20÷100 [*0.01*Ub]
+0x0C0
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x0C1
k odpadu
Współczynnik odpadu zabezpieczenia
101÷120 [*0.01]
+0x0C2
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x0C3
Blk. otw. wył.
Blokady zabezpieczenia przy otwartym wyłączniku
0 = Nie
1 = Tak
+0x0C4
We. blokady
Wejście blokady zabezpieczenia
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x0C5
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x0C6
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. U<2
+0x0C7
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x0C8
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x0C9
Typ
Typ zabezpieczenia
0 = Uf 1-faz SN
1 = Uf 3-faz SN
2 = Up 1-faz SN
3 = Up 3-faz SN
4 = Uf 1-faz nN
5 = Uf 3-faz nN
6 = Up 1-faz nN
7 = Up 3-faz nN
+0x0CA
Us
Próg zadziałania zabezpieczenia
20÷100 [*0.01*Ub]
+0x0CB
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x0CC
k odpadu
Współczynnik odpadu zabezpieczenia
101÷120 [*0.01]
+0x0CD
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x0CE
Blk. otw. wył.
Blokady zabezpieczenia przy otwartym wyłączniku
0 = Nie
1 = Tak
+0x0CF
We. blokady
Wejście blokady zabezpieczenia
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x0D0
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x0D1
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. U<3
+0x0D2
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x0D3
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x0D4
Typ
Typ zabezpieczenia
0 = Uf 1-faz SN
1 = Uf 3-faz SN
2 = Up 1-faz SN
3 = Up 3-faz SN
4 = Uf 1-faz nN
5 = Uf 3-faz nN
6 = Up 1-faz nN
7 = Up 3-faz nN
+0x0D5
Us
Próg zadziałania zabezpieczenia
20÷100 [*0.01*Ub]
+0x0D6
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x0D7
k odpadu
Współczynnik odpadu zabezpieczenia
101÷120 [*0.01]
+0x0D8
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x0D9
Blk. otw. wył.
Blokady zabezpieczenia przy otwartym wyłączniku
0 = Nie
1 = Tak
str. 31
+0x0DA
We. blokady
Wejście blokady zabezpieczenia
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x0DB
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x0DC
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. U>1
+0x0DD
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x0DE
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x0DF
Typ
Typ zabezpieczenia
0 = Uf 1-faz SN
1 = Uf 3-faz SN
2 = Up 1-faz SN
3 = Up 3-faz SN
4 = Uf 1-faz nN
5 = Uf 3-faz nN
6 = Up 1-faz nN
7 = Up 3-faz nN
8 = Upos SN
9 = Uneg SN
+0x0E0
Us
Próg zadziałania zabezpieczenia
50÷120 [*0.01*Ub]
+0x0E1
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x0E2
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x0E3
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x0E4
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x0E5
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. U>2
+0x0E6
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x0E7
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x0E8
Typ
Typ zabezpieczenia
0 = Uf 1-faz SN
1 = Uf 3-faz SN
2 = Up 1-faz SN
3 = Up 3-faz SN
4 = Uf 1-faz nN
5 = Uf 3-faz nN
6 = Up 1-faz nN
7 = Up 3-faz nN
8 = Upos SN
9 = Uneg SN
+0x0E9
Us
Próg zadziałania zabezpieczenia
50÷120 [*0.01*Ub]
+0x0EA
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x0EB
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x0EC
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x0ED
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x0EE
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. U>3
+0x0EF
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x0F0
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x0F1
Typ
Typ zabezpieczenia
0 = Uf 1-faz SN
1 = Uf 3-faz SN
2 = Up 1-faz SN
3 = Up 3-faz SN
4 = Uf 1-faz nN
5 = Uf 3-faz nN
6 = Up 1-faz nN
7 = Up 3-faz nN
8 = Upos SN
9 = Uneg SN
+0x0F2
Us
Próg zadziałania zabezpieczenia
50÷120 [*0.01*Ub]
+0x0F3
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x0F4
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x0F5
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x0F6
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x0F7
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. U>sr
+0x0F8
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x0F9
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x0FA
Typ
Typ zabezpieczenia
0 = Uf 1-faz SN
1 = Uf 3-faz SN
2 = Up 1-faz SN
3 = Up 3-faz SN
4 = Uf 1-faz nN
5 = Uf 3-faz nN
6 = Up 1-faz nN
7 = Up 3-faz nN
8 = Upos SN
9 = Uneg SN
+0x0FB
Us
Próg zadziałania zabezpieczenia
50÷120 [*0.01*Ub]
+0x0FC
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x0FD
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x0FE
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x0FF
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x100
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. ΔU
+0x101
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
str. 32
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x102
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x103
Typ zabezpieczenia
Typ zabezpieczenia
0 = dU/dt
1 = U<+dU/dt
2 = U<+ΔU/Δt
+0x104
Kryterium
Wielkość kryterialna działania zabezpieczenia
0 = SN
1 = nN
+0x105
Charakter zmian
Wykrywanie wzrostu lub spadku napięcia
0 = Spadek
1 = Wzrost
2 = Spadek lub wzrost
+0x106
Upmin
Minimalne napięcie przewodowe
20÷100 [*0.01*Ub]
+0x107
Uakt
Napięcie przewodowe poniżej którego aktywowane są U<+dU/dt oraz U<+ΔU/Δt
20÷120 [*0.01*Ub]
+0x108
dU/dt
Prędkość zmiany napięcia dla dU/dt oraz U<+dU/dt
5÷500 [*0.01*Ub/s]
+0x109
t
Czas zwłoki dla dU/dt oraz U<+dU/dt
10÷6000 [*0.01s]
+0x10A
ΔU
Zmiana napięcia dla typu działania U<+ΔU/Δt
5÷1000 [*0.01*Ub]
+0x10B
Δt
Czas zmiany napięcia dla typu działania U<+ΔU/Δt
10÷6000 [*0.01s]
+0x10C
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x10D
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. f<>
+0x10E
Aktywność
Aktywność zabezpieczeń częstotliwościowych
0 = Nie
1 = Tak
+0x10F
Wybór wyłącznika
Wybór wyłącznika, na który działa zabezpieczenie
0 = SN
1 = nN
2 = SN i nN
+0x110
Źródło pomiaru
Źródło pomiaru dla zabezpieczenia
0 = SN
1 = nN
+0x111
Upmin
Minimalne napięcie przewodowe
20÷100 [*0.01*Ub]
+0x112
Blk.Uf
Blokada od minimalnego napięcia fazowego
0 = Nie
1 = Tak
+0x113
Ufmin
Minimalne napięcie fazowe w 3 fazach
20÷100 [*0.01*Ub]
+0x114
Blk.U0
Blokada od napięcia U0
0 = Nie
1 = Tak
+0x115
U0max
Maksymalne napięcie U0 (strona wtórna)
100÷1000 [*0.1V]
+0x116
Działanie f<1
Sposób działania zabezpieczenia f<1
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
7 = Aut. SCO
+0x117
Typ f<1
Typ działania zabezpieczenia f<1
0 = f<
1 = f<+df/dt
2 = f<+Δf/Δt
3 = df/dt
4 = Δf/Δt
+0x118
f f<1
Próg częstotliwości dla typu działania f<
4500÷5000 [*0.01Hz]
+0x119
t f<1
Czas zwłoki dla typu działania f<
3÷60000 [*0.01s]
+0x11A
df/dt f<1
Prędkość zmiany częstotliwości dla typu działania df/dt
10÷1000 [*0.01Hz/s]
+0x11B
tdf/dt f<1
Czas zwłoki dla typu działania df/dt
3÷6000 [*0.01s]
+0x11C
fΔf/Δt f<1
Próg częstotliwości dla typu działania Δf/Δt
4500÷5000 [*0.01Hz]
+0x11D
Δf f<1
Zmiana częstotliwości dla typu działania Δf/Δt
1÷500 [*0.01Hz]
+0x11E
Δt f<1
Czas zmiany częstotliwości dla typu działania Δf/Δt
5÷6000 [*0.01s]
+0x11F
Działanie f<2
Sposób działania zabezpieczenia f<2
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
7 = Aut. SCO
+0x120
Typ f<2
Tryb działania zabezpieczenia f<2
0 = f<
1 = f<+df/dt
2 = f<+Δf/Δt
3 = df/dt
4 = Δf/Δt
+0x121
f f<2
Próg częstotliwości dla typu działania f<
4500÷5000 [*0.01Hz]
+0x122
t f<2
Czas zwłoki dla typu działania f<
3÷60000 [*0.01s]
+0x123
df/df f<2
Prędkość zmiany częstotliwości dla typu działania df/dt
10÷1000 [*0.01Hz/s]
+0x124
tdf/dt f<2
Czas zwłoki dla typu działania df/dt
3÷6000 [*0.01s]
+0x125
fΔf/Δt f<2
Próg częstotliwości dla typu działania Δf/Δt
4500÷5000 [*0.01Hz]
+0x126
Δf f<2
Zmiana częstotliwości dla typu działania Δf/Δt
1÷500 [*0.01Hz]
+0x127
Δt f<2
Czas zmiany częstotliwości dla typu działania Δf/Δt
5÷6000 [*0.01s]
+0x128
Działanie f<3
Sposób działania zabezpieczenia f<3
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
7 = Aut. SCO
+0x129
Typ f<3
Tryb działania zabezpieczenia f<3
0 = f<
1 = f<+df/dt
2 = f<+Δf/Δt
3 = df/dt
4 = Δf/Δt
+0x12A
f f<3
Próg częstotliwości dla typu działania f<
4500÷5000 [*0.01Hz]
+0x12B
t f<3
Czas zwłoki dla typu działania f<
3÷60000 [*0.01s]
+0x12C
df/dt f<3
Prędkość zmiany częstotliwości dla typu działania df/dt
10÷1000 [*0.01Hz/s]
+0x12D
tdf/dt f<3
Czas zwłoki dla typu działania df/dt
3÷6000 [*0.01s]
+0x12E
fΔf/Δt f<3
Próg częstotliwości dla typu działania Δf/Δt
4500÷5000 [*0.01Hz]
+0x12F
Δf f<3
Zmiana częstotliwości dla typu działania Δf/Δt
1÷500 [*0.01Hz]
+0x130
Δt f<3
Czas zmiany częstotliwości dla typu działania Δf/Δt
5÷6000 [*0.01s]
+0x131
Działanie f<4
Sposób działania zabezpieczenia f<4
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
str. 33
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
7 = Aut. SCO
+0x132
Typ f<4
Tryb działania zabezpieczenia f<4
0 = f<
1 = f<+df/dt
2 = f<+Δf/Δt
3 = df/dt
4 = Δf/Δt
+0x133
f f<4
Próg częstotliwości dla typu działania f<
4500÷5000 [*0.01Hz]
+0x134
t f<4
Czas zwłoki dla typu działania f<
3÷60000 [*0.01s]
+0x135
df/dt f<4
Prędkość zmiany częstotliwości dla typu działania df/dt
10÷1000 [*0.01Hz/s]
+0x136
tdf/dt f<4
Czas zwłoki dla typu działania df/dt
3÷6000 [*0.01s]
+0x137
fΔf/Δt f<4
Próg częstotliwości dla typu działania Δf/Δt
4500÷5000 [*0.01Hz]
+0x138
Δf f<4
Zmiana częstotliwości dla typu działania Δf/Δt
1÷500 [*0.01Hz]
+0x139
Δt f<4
Czas zmiany częstotliwości dla typu działania Δf/Δt
5÷6000 [*0.01s]
+0x13A
Działanie f>1
Sposób działania zabezpieczenia f>1
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
7 = Aut. SCO
+0x13B
Typ f>1
Tryb działania zabezpieczenia f>1
0 = f>
1 = f>+df/dt
2 = f>+Δf/Δt
3 = df/dt
4 = Δf/Δt
+0x13C
f f>1
Próg częstotliwości dla typu działania f>1
4900÷5500 [*0.01Hz]
+0x13D
t f>1
Czas zwłoki dla typu działania f>1
1÷18000 [*0.1s]
+0x13E
df/dt f>1
Prędkość zmiany częstotliwości dla typu działania df/dt
10÷1000 [*0.01Hz/s]
+0x13F
tdf/dt f>1
Czas zwłoki dla typu działania df/dt
3÷6000 [*0.01s]
+0x140
fΔf/Δt f>1
Próg częstotliwości dla typu działania Δf/Δt
4900÷5500 [*0.01Hz]
+0x141
Δf f>1
Zmiana częstotliwości dla typu działania Δf/Δt
1÷500 [*0.01Hz]
+0x142
Δt f>1
Czas zmiany częstotliwości dla typu działania Δf/Δt
5÷6000 [*0.01s]
+0x143
Działanie f>2
Sposób działania zabezpieczenia f>2
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
7 = Aut. SCO
+0x144
Typ f>2
Tryb działania zabezpieczenia f>2
0 = f>
1 = f>+df/dt
2 = f>+Δf/Δt
3 = df/dt
4 = Δf/Δt
+0x145
f f>2
Próg częstotliwości dla typu działania f>2
4900÷5500 [*0.01Hz]
+0x146
t f>2
Czas zwłoki dla typu działania f>2
1÷18000 [*0.1s]
+0x147
df/dt f>2
Prędkość zmiany częstotliwości dla typu działania df/dt
10÷1000 [*0.01Hz/s]
+0x148
tdf/dt f>2
Czas zwłoki dla typu działania df/dt
3÷6000 [*0.01s]
+0x149
fΔf/Δt f>2
Próg częstotliwości dla typu działania Δf/Δt
4900÷5500 [*0.01Hz]
+0x14A
Δf f>2
Zmiana częstotliwości dla typu działania Δf/Δt
1÷500 [*0.01Hz]
+0x14B
Δt f>2
Czas zmiany częstotliwości dla typu działania Δf/Δt
5÷6000 [*0.01s] Parametry zab. P>
+0x14C
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x14D
Kierunkowość
Kierunek działania
0 = Bezkier.
1 = Dodatnia
2 = Ujemna
+0x14E
Ps
Próg zadziałania zabezpieczenia
1÷200 [*0.01*Sn]
+0x14F
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x150
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x151
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x152
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x153
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. Q>
+0x154
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x155
Kierunkowość
Kierunek działania
0 = Bezkier.
1 = Dodatnia
2 = Ujemna
+0x156
Qs
Próg zadziałania zabezpieczenia
1÷200 [*0.01*Sn]
+0x157
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x158
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x159
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x15A
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x15B
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. THERM
+0x15C
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x15D
q_neg
Współczynnik uwzględnienia składowej przeciwnej
0÷10
+0x15E
Imax
Maksymalny prąd długotrwały
100÷200 [*0.01*Ib]
str. 34
+0x15F
Tg1
Stała czasowa grzania dla I<2*In
1÷480 [min]
+0x160
Tg2
Stała czasowa grzania dla I>=2*In
1÷480 [min]
+0x161
Ts
Stała czasowa stygnięcia
1÷480 [min]
+0x162
Aktywacja Tg2
Sposób aktywacji stałej czasowej Tg2
0 = Nieaktywna
1 = Ieq > 2Ib
2 = We 2-stan.
+0x163
We akt. Tg2
Wejście aktywacji stałej czasowej Tg2 (dla Aktywacja TG2 = Wejście 2-stan.)
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x164
Qalarm
Alarmowy stopień nagrzania
10÷100 [%]
+0x165
Qblk
Stopień nagrzania blokowania zamknięcia wyłącznika
10÷100 [%]
+0x166
We Reset
Wejście kasowania stopnia nagrzania
Lo(nr_we)
Hi(nr_slot)
Parametry zab. ASIM
+0x167
Sposób działania
Sposób działania zabezpieczenia
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x168
Tryb działania
Tryb działania zabezpieczenia
0 = Asym. I
1 = Skł. przeciwna
+0x169
Typ zwłoki
Typ zwłoki czasowej
0 = Niezależna
1 = Zależna
+0x16A
k
Asymetria zadziałania zabezpieczenia
1÷100 [*0.01]
+0x16B
t
Czas zwłoki działania zabezpieczenia
0÷60000 [*0.01s]
+0x16C
k odpadu
Współczynnik odpadu zabezpieczenia
80÷99 [*0.01]
+0x16D
t odpadu
Czas odpadu zabezpieczenia
0÷600 [*0.01s]
+0x16E
Wyzw. rej. zakł.
Wyzwolenie rejestratora zakłóceń
0 = Brak
1 = Pob. Zab.
2 = Zad. Zab.
+0x16F
%t rej. zakł.
Czas rejestracji po wyzwoleniu rejestratora
0÷100 [%] Parametry zab. gaz-przepł.
+0x170
We BTQ
Wejście zab. gaz.-przepł. trafo I stopnia
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x171
We BTV
Wejście zab. gaz.-przepł. trafo II stopnia
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x172
We BDQ
Wejście zab. gaz.-przepł. dławika I stopnia
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x173
We BDV
Wejście zab. gaz.-przepł. dławika II stopnia
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x174
We BPZ
Wejście zab. gaz.-przepł. przełącznika zaczepów
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x175
LRW
Pobudzenie LRW dla zabezpieczeń otwierających wyłącznik
0 = Nie
1 = Tak
Parametry zab. temperaturowych
+0x176
Sp.dział. TEMP 1
Sposób działania zabezpieczenia temperaturowego 1
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
+0x177
We TEMP 1
Wejście zabezpieczenia temperaturowego 1
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x178
t TEMP 1
Czas zwłoki działania zabezpieczenia temperaturowego 1
0÷60000 [*0.01s]
+0x179
Sp.dział. TEMP 2
Sposób działania zabezpieczenia temperaturowego 2
0 = Odstawione
1 = Sygnal. UP
2 = Otw,LRW,Blk
3 = Otw,LRW
4 = Otw,Blk
5 = Otw
6 = Logika
7 = Log. bez zd.
+0x17A
We TEMP 2
Wejście zabezpieczenia temperaturowego 2
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x17B
t TEMP 2
Czas zwłoki działania zabezpieczenia temperaturowego 2
0÷60000 [*0.01s] Parametry zab. termicznych PT
+0x17C
Ilość czujników
Ilość czujników
0÷6
+0x17D
Temp. UP PT1
Temperatura pobudzenia UP od czujnika PT1 (200 - odstawione)
20÷200 [°C]
+0x17E
Temp. AW PT1
Temperatura otwarcia wyłącznika od czujnika PT1 (200 - odstawione)
20÷200 [°C]
+0x17F
Temp. UP PT2
Temperatura pobudzenia UP od czujnika PT2 (200 - odstawione)
20÷200 [°C]
+0x180
Temp. AW PT2
Temperatura otwarcia wyłącznika od czujnika PT2 (200 - odstawione)
20÷200 [°C]
+0x181
Temp. UP PT3
Temperatura pobudzenia UP od czujnika PT3 (200 - odstawione)
20÷200 [°C]
+0x182
Temp. AW PT3
Temperatura otwarcia wyłącznika od czujnika PT3 (200 - odstawione)
20÷200 [°C]
+0x183
Temp. UP PT4
Temperatura pobudzenia UP od czujnika PT4 (200 - odstawione)
20÷200 [°C]
+0x184
Temp. AW PT4
Temperatura otwarcia wyłącznika od czujnika PT4 (200 - odstawione)
20÷200 [°C]
+0x185
Temp. UP PT5
Temperatura pobudzenia UP od czujnika PT5 (200 - odstawione)
20÷200 [°C]
+0x186
Temp. AW PT5
Temperatura otwarcia wyłącznika od czujnika PT5 (200 - odstawione)
20÷200 [°C]
+0x187
Temp. UP PT6
Temperatura pobudzenia UP od czujnika PT6 (200 - odstawione)
20÷200 [°C]
str. 35
+0x188
Temp. AW PT6
Temperatura otwarcia wyłącznika od czujnika PT6 (200 - odstawione)
20÷200 [°C]
+0x189
LRW
Pobudzenie LRW dla zabezpieczeń otwierających wyłącznik
0 = Nie
1 = Tak
Parametry zab. łukoochronnego
+0x18A
Aktywność
Aktywność zabezpieczenia
0 = Nie
1 = Tak
+0x18B
Typ pola
Typ pola
0 = ODP. 1S
1 = ZAS. 1S
2 = SP. L 1S
3 = SP. R 1S
4 = POM. 1S
5 = ODP. 2S
6 = ZAS. 2S
7 = SP.POP. 2S
8 = SP.POD. 2S
9 = SP.PP. 2S
10 = POM.A 2S
11 = POM.B 2S
+0x18C
Numer pola
Numer pola
1÷60
+0x18D
Sekcja
Sekcja
1÷4
+0x18E
Ilość sekcji
Ilość sekcji
1÷4
+0x18F
Poł. pierścieniowe
Połączenie pierścieniowe sekcji (dla rozdzielni 1-systemowych)
0 = Nie
1 = Tak
+0x190
Nr pola sprzęgła
Numer pola sprzęgła sekcji sąsiedniej (dla rozdzielni 1-systemowych)
0÷60
+0x191
Nap. sekcji własne
Kontrola napięcia własnego
0 = Nie
1 = Tak
+0x192
Wy otw. rozdz. nad.
Wyjście otwarcia rozdzielni nadrzędnej
Lo(nr_wy)
Hi(nr_slot)
+0x193
We odł. systemu A
Wejście stanu zamknięcia odłącznika systemu A (dla rozdzielni 2-systemowych)
Lo(nr_we)
Hi(nr_slot)
+0x194
We odł. systemu B
Wejście stanu zamknięcia odłącznika systemu B (dla rozdzielni 2-systemowych)
Lo(nr_we)
Hi(nr_slot)
+0x195
Info U<
Wysyłanie informacji o zaniku napięcia
0 = Nie
1 = Tak
+0x196
Kontrola CAN
Kontrola magistrali CANBUS
0 = Nie
1 = Tak
+0x197
Czujnik 1
Działanie czujnika 1
0 = Odst.
1 = Std.
+0x198
Czujnik 2
Działanie czujnika 2
0 = Odst.
1 = Std.
+0x199
Czujnik 3
Działanie czujnika 3
0 = Odst.
1 = Std.
+0x19A
Czujnik 4
Działanie czujnika 4
0 = Odst.
1 = Std.
2 = Czujnik 1
3 = Czujnik 2
4 = Czujnik 3
+0x19B
Czujnik 5
Działanie czujnika 5
0 = Odst.
1 = Std.
2 = Czujnik 1
3 = Czujnik 2
4 = Czujnik 3
+0x19C
Czujnik 6
Działanie czujnika 6
0 = Odst.
1 = Std.
2 = Czujnik 1
3 = Czujnik 2
4 = Czujnik 3
+0x19D
Czujnik 7
Działanie czujnika 7
0 = Odst.
1 = Std.
2 = Czujnik 1
3 = Czujnik 2
4 = Czujnik 3
5 = Czujnik 4
6 = Czujnik 5
7 = Czujnik 6
+0x19E
Czujnik 8
Działanie czujnika 8
0 = Odst.
1 = Std.
2 = Czujnik 1
3 = Czujnik 2
4 = Czujnik 3
5 = Czujnik 4
6 = Czujnik 5
7 = Czujnik 6
+0x19F
Czujnik 9
Działanie czujnika 9
0 = Odst.
1 = Std.
2 = Czujnik 1
3 = Czujnik 2
4 = Czujnik 3
5 = Czujnik 4
6 = Czujnik 5
7 = Czujnik 6
+0x1A0
Czujnik 10
Działanie czujnika 10
0 = Odst.
1 = Std.
2 = Czujnik 1
3 = Czujnik 2
4 = Czujnik 3
5 = Czujnik 4
6 = Czujnik 5
7 = Czujnik 6
+0x1A1
Czujnik 11
Działanie czujnika 11
0 = Odst.
1 = Std.
2 = Czujnik 1
3 = Czujnik 2
4 = Czujnik 3
5 = Czujnik 4
6 = Czujnik 5
7 = Czujnik 6
+0x1A2
Czujnik 12
Działanie czujnika 12
0 = Odst.
1 = Std.
2 = Czujnik 1
3 = Czujnik 2
4 = Czujnik 3
5 = Czujnik 4
6 = Czujnik 5
7 = Czujnik 6
+0x1A3
Wy otw. pól
Wyjście otwarcia pól sekcji
Lo(nr_wy)
Hi(nr_slot)
+0x1A4
Godzina aut.testu
Godzina przeprowadzania aut. testu czujników (0-testy odstawione)
0÷23
+0x1A5
Wy testu czujników
Wyjście testowania czujników
Lo(nr_wy)
Hi(nr_slot)
Parametry synchrocheck
+0x1A6
Aktywność
Aktywność synchrocheck
0 = Nie
1 = Tak
str. 36
+0x1A7
Umin str. C
Minimalne napięcie strony czynnej
50÷100 [*0.01*Ub]
+0x1A8
Umax str. N
Maksymalne napięcie strony nieczynnej
0÷50 [*0.01*Ub]
+0x1A9
t C<->N
Zwłoka czasowa przełączenia stanu strony
0÷6000 [*0.01s]
+0x1AA
We U12_BP
Wejście niesprawności pomiaru napięcia strony U12
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x1AB
We Us_BP
Wejście niesprawności pomiaru napięcia strony Us
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x1AC
Zamknięcie N/N
Zamknięcie przy obu stronach nieczynnych
0 = Nie
1 = Tak
+0x1AD
Zamknięcie N/C
Zamknięcie przy stronie pomiaru U12 nieczynnej, stronie pomiaru Us czynnej
0 = Nie
1 = Tak
+0x1AE
Zamknięcie C/N
Zamknięcie przy stronie pomiaru U12 czynnej, stronie pomiaru Us nieczynnej
0 = Nie
1 = Tak
+0x1AF
Zamknięcie C/C
Zamknięcie przy obu stronach czynnych - z synchrocheck
0 = Nie
1 = Tak
+0x1B0
Max ΔU
Maksymalna różnica napięć
1÷30 [*0.01*Ub]
+0x1B1
Max Δf
Maksymalna różnica częstotliwości
1÷100 [*0.01Hz]
+0x1B2
Max Δφ
Maksymalna różnica kątowa
0÷60 [°]
+0x1B3
tsyn
Minimalny czas spełnienia warunków przed załączeniem
0÷100 [*0.01s]
+0x1B4
tw zam.
Czas własny zamknięcia wyłącznika
0÷300 [ms]
+0x1B5
tgr
Czas graniczny oczekiwania na synchronizm
0÷12000 [*0.01s]
+0x1B6
We blokady
Wejście blokady sprawdzania warunków synchronizmu
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
Parametry automatyki ZS
+0x1B7
Wy ZS1
Wyjście 1 automatyki ZS
Lo(nr_wy)
Hi(nr_slot)
+0x1B8
Wy ZS2
Wyjście 2 automatyki ZS
Lo(nr_wy)
Hi(nr_slot)
+0x1B9
Krt.pob.wy.
Kryterium pobudzenia wyjść automatyki ZS
0 = Is>
1 = Pob. I>>
2 = Pob. I>1
3 = Pob. I>2
4 = Pob. I>3
+0x1BA
Is
Próg prądu pobudzenia wyjścia automatyki ZS
20÷3000 [*0.01*Ib]
+0x1BB
We ZS1
Wejście 1 automatyki ZS
Lo(nr_we)
Hi(nr_slot)
+0x1BC
We ZS2
Wejście 2 automatyki ZS
Lo(nr_we)
Hi(nr_slot)
+0x1BD
Blokada I>>
Blokada zabezpieczenia zwarciowego
0 = Nie
1 = Tak
+0x1BE
Blokada I>1
Blokada zabezpieczenia nadprądowego 1
0 = Nie
1 = Tak
+0x1BF
Blokada I>2
Blokada zabezpieczenia nadprądowego 2
0 = Nie
1 = Tak
+0x1C0
Blokada I>3
Blokada zabezpieczenia nadprądowego 3
0 = Nie
1 = Tak
+0x1C1
Blokada I>4
Blokada zabezpieczenia nadprądowego 4
0 = Nie
1 = Tak
+0x1C2
Blokada I>4
Blokada zabezpieczenia nadprądowego 5
0 = Nie
1 = Tak
+0x1C3
We odst.
Wejście odstawienia automatyki ZS
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
Parametry automatyki LRW
+0x1C4
Wy LRW1
Wyjście 1 automatyki LRW
Lo(nr_wy)
Hi(nr_slot)
+0x1C5
Wy LRW2
Wyjście 2 automatyki LRW
Lo(nr_wy)
Hi(nr_slot)
+0x1C6
t wy
Czas zwłoki pobudzenia wyjść automatyki LRW
0÷100 [*0.01s]
+0x1C7
Kryt. odwzbudzenia
Kryterium odwzbudzenia wyjść automatyki LRW
0 = Odwzb. zab.
1 = Otw. + I<
2 = Otw.
3 = I<
+0x1C8
Imin wy
Próg działania wyjść automatyki LRW
0÷3000 [*0.01*Ib]
+0x1C9
We LRW1
Wejście 1 automatyki LRW
Lo(nr_we)
Hi(nr_slot)
+0x1CA
We LRW2
Wejście 2 automatyki LRW
Lo(nr_we)
Hi(nr_slot)
+0x1CB
t we
Czas zwłoki wejść automatyki LRW
0÷100 [*0.01s]
+0x1CC
Imin we
Próg działania wejść automatyki LRW
0÷3000 [*0.01*Ib]
+0x1CD
Blokada zam.
Blokada zamknięcia po zadziałaniu LRW
0 = Nie
1 = Tak
+0x1CE
We odst.
Wejście odstawienia automatyki LRW
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
Parametry automatyki SPZ
+0x1CF
Aktywność
Aktywność automatyki SPZ
0 = Nie
1 = Tak
+0x1D0
Krotność
Krotność automatyki SPZ
1÷3
+0x1D1
Pob. SPZ I>>
Pobudzenie SPZ od zab. zwarciowego
0 = Nie
1 = Tak
+0x1D2
Pob. SPZ I>1
Pobudzenie SPZ od zab. nadprądowego 1
0 = Nie
1 = Tak
+0x1D3
Pob. SPZ I>2
Pobudzenie SPZ od zab. nadprądowego 2
0 = Nie
1 = Tak
+0x1D4
Pob. SPZ I>3
Pobudzenie SPZ od zab. nadprądowego 3
0 = Nie
1 = Tak
+0x1D5
Pob. SPZ I0>1
Pobudzenie SPZ od zab. ziemnozwarciowego 1
0 = Nie
1 = Tak
+0x1D6
Pob. SPZ I0>2
Pobudzenie SPZ od zab. ziemnozwarciowego 2
0 = Nie
1 = Tak
+0x1D7
Pob. SPZ I0>d
Pobudzenie SPZ od zab. ziemnozwarciowego kierunkowego
0 = Nie
1 = Tak
+0x1D8
Pob. SPZ Y0>
Pobudzenie SPZ od zab. ziemnozwarciowego admitancyjnego
0 = Nie
1 = Tak
+0x1D9
Pob. SPZ Y0>d1
Pobudzenie SPZ od zab. ziemnozwarciowego admitancyjnego kierunkowego 1
0 = Nie
1 = Tak
str. 37
+0x1DA
Pob. SPZ Y0>d2
Pobudzenie SPZ od zab. ziemnozwarciowego admitancyjnego kierunkowego 2
0 = Nie
1 = Tak
+0x1DB
Pob. SPZ TECH1
Pobudzenie SPZ od zab. technologicznego 1
0 = Nie
1 = Tak
+0x1DC
t blk. po zam
Czas blokady SPZ po zamknięciu operacyjnym wyłącznika
0÷6000 [*0.01s]
+0x1DD
t SPZ1
Czas przerwy beznapięciowej 1
5÷6000 [*0.01s]
+0x1DE
t powrotu 1
Czas powrotu SPZ po I załączeniu
5÷6000 [*0.01s]
+0x1DF
t SPZ2
Czas przerwy beznapięciowej 2
5÷6000 [*0.01s]
+0x1E0
t powrotu 2
Czas powrotu SPZ po II załączeniu
5÷6000 [*0.01s]
+0x1E1
t SPZ3
Czas przerwy beznapięciowej 3
5÷6000 [*0.01s]
+0x1E2
t powrotu 3
Czas powrotu SPZ po III załączeniu
5÷6000 [*0.01s]
+0x1E3
Akt. PDZ0
Przyspieszenia PDZ przed cyklem SPZ
0 = Nie
1 = Tak
+0x1E4
Akt. PDZ1
Przyspieszenia PDZ po I cyklu SPZ
0 = Nie
1 = Tak
+0x1E5
Akt. PDZ2
Przyspieszenia PDZ po II cyklu SPZ
0 = Nie
1 = Tak
+0x1E6
Akt. PDZ3
Przyspieszenia PDZ po III cyklu SPZ
0 = Nie
1 = Tak
+0x1E7
Akt. PDZ I>>
Aktywność PDZ dla zab. zwarciowego
0 = Nie
1 = Tak
+0x1E8
Akt. PDZ_I>1
Aktywność PDZ dla zab. nadprądowego 1
0 = Nie
1 = Tak
+0x1E9
Akt. PDZ I>2
Aktywność PDZ dla zab. nadprądowego 2
0 = Nie
1 = Tak
+0x1EA
Akt. PDZ I>3
Aktywność PDZ dla zab. nadprądowego 3
0 = Nie
1 = Tak
+0x1EB
Blk. U
Blokada SPZ przy obecności napięcia na linii
0 = Brak
1 = U
2 = Us
3 = We
+0x1EC
We Blk. U
Wejście blokady SPZ przy obecności nap. na linii
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x1ED
We nastawienia
Wejście nastawienia automatyki
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x1EE
We odblokowania
Wejście odblokowania automatyki
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x1EF
We zablokowania
Wejście zablokowania automatyki
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x1F0
Pamięć stanu
Pamięć stanu automatyki po zaniku zasilania
0 = Nie
1 = Tak
Parametry automatyki SCO
+0x1F1
Aktywność
Aktywność automatyki
0 = Nie
1 = Tak
+0x1F2
Wy SCO1
Wyjście SCO1
Lo(nr_wy)
Hi(nr_slot)
+0x1F3
Wy SCO2
Wyjście SCO2
Lo(nr_wy)
Hi(nr_slot)
+0x1F4
Wy SCO3
Wyjście SCO3
Lo(nr_wy)
Hi(nr_slot)
+0x1F5
Wy SCO4
Wyjście SCO4
Lo(nr_wy)
Hi(nr_slot)
+0x1F6
Wy SPZ/SCO
Wyjście SPZ/SCO
Lo(nr_wy)
Hi(nr_slot)
+0x1F7
We nastawienia
Wejście nastawienia automatyki
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x1F8
We odblokowania
Wejście odblokowania automatyki
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x1F9
We zablokowania
Wejście zablokowania automatyki
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x1FA
We nast.SPZ/SCO
Wejście nastawienia automatyki SPZ/SCO
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x1FB
Pamięć stanu
Pamięć stanu automatyki po zaniku zasilania
0 = Nie
1 = Tak
Parametry automatyki SCOw
+0x1FC
Aktywność
Aktywność automatyki
0 = Nie
1 = Tak
+0x1FD
Typ
Typ automatyki
0 = Wejścia
1 = Zab. f<>
+0x1FE
Stopień SCO
Stopień automatyki
0 = 1
1 = 2
2 = 3
3 = 4
4 = 1,2
5 = 1,3
6 = 1,4
7 = 2,3
8 = 2,4
9 = 3,4
10 = 1,2,3
11 = 1,2,4
12 = 1,3,4
13 = 2,3,4
14 = 1,2,3,4
+0x1FF
We SCO1
Wejście SCO1
Lo(nr_we)
Hi(nr_slot)
+0x200
We SCO2
Wejście SCO2
Lo(nr_we)
Hi(nr_slot)
+0x201
We SCO3
Wejście SCO3
Lo(nr_we)
Hi(nr_slot)
+0x202
We SCO4
Wejście SCO4
Lo(nr_we)
Hi(nr_slot)
+0x203
AW po SCO
Sygnalizacja AW
0 = Nie
1 = Tak
+0x204
We SPZ/SCO
Wejście SPZ/SCO
Lo(nr_we)
Hi(nr_slot)
+0x205
t SPZ/SCO
Zwłoka czasowa SPZ/SCO
0÷600 [*0.01s]
+0x206
We nastawienia
Wejście nastawienia automatyki
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x207
We odblokowania
Wejście odblokowania automatyki
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x208
We zablokowania
Wejście zablokowania automatyki
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x209
We nast.SPZ/SCO
Wejście nastawienia automatyki SPZ/SCO
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x20A
Odb/zab.SPZ/SCO
Aktywność odblokowania/zablokowania automatyki SPZ/SCO
0 = Nie
1 = Tak
+0x20B
We odb. SPZ/SCO
Wejście odblokowania automatyki SPZ/SCO
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x20C
We zab. SPZ/SCO
Wejście zablokowania automatyki SPZ/SCO
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x20D
Pamięć stanu
Pamięć stanu automatyki po zaniku zasilania
0 = Nie
1 = Tak
Parametry automatyki SZRw
str. 38
+0x20E
Aktywność
Aktywność członu wykonawczego automatyki SZR
0 = Nie
1 = Tak
+0x20F
We otwarcia
Wejście otwarcia z SZR
Lo(nr_we)
Hi(nr_slot)
+0x210
We zamknięcia
Wejście zamknięcia z SZR
Lo(nr_we)
Hi(nr_slot)
+0x211
Tryb blk.trwałej
Tryb działania wyjścia blokady trwałej
0 = Zad. zab.
1 = LRW,ZS,ARC
+0x212
Wy blk. trwałej
Wyjście blokady trwałej SZR
Lo(nr_wy)
Hi(nr_slot)
+0x213
We1 b. przejśc.
Wejście 1 blokady przejściowej SZR
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x214
We2 b. przejśc.
Wejście 2 blokady przejściowej SZR
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x215
Wy b. przejść
Wyjście blokady przejściowej SZR
Lo(nr_wy)
Hi(nr_slot)
Parametry automatyki SPZW
+0x216
Aktywność
Aktywność automatyki SPZW
0 = Nie
1 = Tak
+0x217
wyłącznik
Wybór wyłącznika dla którego ma działać SPZW
0 = SN
1 = nN
+0x218
Pob. SPZW U<1
Pobudzenie SPZW od zab. U<1
0 = Nie
1 = Tak
+0x219
Pob. SPZW U<2
Pobudzenie SPZW od zab. U<2
0 = Nie
1 = Tak
+0x21A
Pob. SPZW U<3
Pobudzenie SPZW od zab. U<3
0 = Nie
1 = Tak
+0x21B
Pob. SPZW U>1
Pobudzenie SPZW od zab. U>1
0 = Nie
1 = Tak
+0x21C
Pob. SPZW U>2
Pobudzenie SPZW od zab. U>2
0 = Nie
1 = Tak
+0x21D
Pob. SPZW U>3
Pobudzenie SPZW od zab. U>3
0 = Nie
1 = Tak
+0x21E
Pob. SPZW U>śr
Pobudzenie SPZW od zab. U>śr
0 = Nie
1 = Tak
+0x21F
Pob. SPZW U0>1
Pobudzenie SPZW od zab. U0>1
0 = Nie
1 = Tak
+0x220
Pob. SPZW U0>2
Pobudzenie SPZW od zab. U0>2
0 = Nie
1 = Tak
+0x221
Pob. SPZW U0>nN
Pobudzenie SPZW od zab. U0>nN
0 = Nie
1 = Tak
+0x222
Pob. SPZW f<1
Pobudzenie SPZW od zab. f<1
0 = Nie
1 = Tak
+0x223
Pob. SPZW f<2
Pobudzenie SPZW od zab. f<2
0 = Nie
1 = Tak
+0x224
Pob. SPZW f<3
Pobudzenie SPZW od zab. f<3
0 = Nie
1 = Tak
+0x225
Pob. SPZW f<4
Pobudzenie SPZW od zab. f<4
0 = Nie
1 = Tak
+0x226
Pob. SPZW f>1
Pobudzenie SPZW od zab. f>1
0 = Nie
1 = Tak
+0x227
Pob. SPZW f>2
Pobudzenie SPZW od zab. f>2
0 = Nie
1 = Tak
+0x228
Pob. SPZW ΔU
Pobudzenie SPZW od zab. ΔU
0 = Nie
1 = Tak
+0x229
Jednokrotna
Jednokrotność automatyki SPZW
0 = Nie
1 = Tak
+0x22A
t SPZW
Czas SPZW
1÷60000 [*0.1s]
+0x22B
We nastawienia
Wejście nastawienia automatyki
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x22C
We odblokowania
Wejście odblokowania automatyki
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x22D
We zablokowania
Wejście zablokowania automatyki
Lo(nr_we)
Hi(nr_slot)
MSB(neg)
+0x22E
Pamięć stanu
Pamięć stanu automatyki po zaniku zasilania
0 = Nie
1 = Tak
str. 39
3 Sterowania
Zapis: Funkcja 5 Adres Dana = 0x0000 Dana = 0xFF00
0x0001
Otwarcie łącznika 1
Zamknięcie łącznika 1
0x0002
Otwarcie łącznika 2
Zamknięcie łącznika 2
0x0003
Otwarcie łącznika 3
Zamknięcie łącznika 3
0x0004
Otwarcie łącznika 4
Zamknięcie łącznika 4
0x0005
Otwarcie łącznika 5
Zamknięcie łącznika 5
0x0006
Otwarcie łącznika 6
Zamknięcie łącznika 6
0x0007
Otwarcie łącznika 7
Zamknięcie łącznika 7
0x0008
Otwarcie łącznika 8
Zamknięcie łącznika 8
0x0009
Otwarcie łącznika 9
Zamknięcie łącznika 9
0x000A
Otwarcie łącznika 10
Zamknięcie łącznika 10
0x000B
Otwarcie łącznika 11
Zamknięcie łącznika 11
0x000C
Otwarcie łącznika 12
Zamknięcie łącznika 12
0x0010
--
Kasowanie sygnalizacji
0x0020
--
Zmiana banku nastaw zabezpieczeń na Bank 1
0x0021
--
Zmiana banku nastaw zabezpieczeń na Bank 2
0x0022
--
Zmiana banku nastaw zabezpieczeń na Bank 3
0x0023
--
Zmiana banku nastaw zabezpieczeń na Bank 4
0x0050
Zablokowanie automatyki SPZ
Odblokowanie automatyki SPZ
0x0051
Zablokowanie automatyki SCO
Odblokowanie automatyki SCO
0x0052
Zablokowanie układu współpracy z automatyką SCO (SCOw)
Odblokowanie układu współpracy z automatyką SCO (SCOw)
0x0053
Zablokowanie automatyki AWSC
Odblokowanie automatyki AWSC
0x0054
Zablokowanie automatyki AZBK
Odblokowanie automatyki AZBK
0x0055
Zablokowanie układu współpracy z automatyką AZBK (AZBKw)
Odblokowanie układu współpracy z automatyką AZBK (AZBKw)
0x2200
Ustawienie bitu logiki 1
Skasowanie bitu logiki 1
0x2201
Ustawienie bitu logiki 2
Skasowanie bitu logiki 2
0x2202
Ustawienie bitu logiki 3
Skasowanie bitu logiki 3
0x2203
Ustawienie bitu logiki 4
Skasowanie bitu logiki 4
str. 40
0x2204
Ustawienie bitu logiki 5
Skasowanie bitu logiki 5
0x2205
Ustawienie bitu logiki 6
Skasowanie bitu logiki 6
0x2206
Ustawienie bitu logiki 7
Skasowanie bitu logiki 7
0x2207
Ustawienie bitu logiki 8
Skasowanie bitu logiki 8
0x2208
Ustawienie bitu logiki 9
Skasowanie bitu logiki 9
0x2209
Ustawienie bitu logiki 10
Skasowanie bitu logiki 10
0x220A
Ustawienie bitu logiki 11
Skasowanie bitu logiki 11
0x220B
Ustawienie bitu logiki 12
Skasowanie bitu logiki 12
0x220C
Ustawienie bitu logiki 13
Skasowanie bitu logiki 13
0x220D
Ustawienie bitu logiki 14
Skasowanie bitu logiki 14
0x220E
Ustawienie bitu logiki 15
Skasowanie bitu logiki 15
0x220F
Ustawienie bitu logiki 16
Skasowanie bitu logiki 16
0x2210
--
Generacja impulsu 1s na bicie logiki 1
0x2211
--
Generacja impulsu 1s na bicie logiki 2
0x2212
--
Generacja impulsu 1s na bicie logiki 3
0x2213
--
Generacja impulsu 1s na bicie logiki 4
0x2214
--
Generacja impulsu 1s na bicie logiki 5
0x2215
--
Generacja impulsu 1s na bicie logiki 6
0x2216
--
Generacja impulsu 1s na bicie logiki 7
0x2217
--
Generacja impulsu 1s na bicie logiki 8
0x2218
--
Generacja impulsu 1s na bicie logiki 9
0x2219
--
Generacja impulsu 1s na bicie logiki 10
0x221A
--
Generacja impulsu 1s na bicie logiki 11
0x221B
--
Generacja impulsu 1s na bicie logiki 12
0x221C
--
Generacja impulsu 1s na bicie logiki 13
0x221D
--
Generacja impulsu 1s na bicie logiki 14
0x221E
--
Generacja impulsu 1s na bicie logiki 15
0x221F
--
Generacja impulsu 1s na bicie logiki 16
str. 41
4 Zdarzenia
Odczyt: Funkcja 4
Przed odczytem zdarzeń należy odczytać rejestr ilości nowych zdarzeń. Powoduje to zamrożenie aktualnej listy zdarzeń, tak aby nowe zdarzenia pojawiające się w czasie odczytu nie powodowały przesuwania się bufora. Możliwy jest odczyt niezależny obydwu rejestrów, lub odczyt obu rejestrów na raz.
Rejestr 0x0501 - ilość nowych zdarzeń Rejestr 0x0502 - ilość wszystkich zdarzeń Odczyt zdarzeń
Odczyt zdarzeń może być dowolnie dzielony (odczytywanie zdarzeń porcjami). Należy podać numer zdarzenia początkowego jako adres spod, którego chcemy odczytywać natomiast jako ilość rejestrów do odczytania należy podać ilość zdarzeń do odczytania * 8. Ilość rejestrów do odczytu musi być podzielna przez 8.
Adres zdarzenia musi się mieścić w przedziale 0x1000 <= Rejestr <= 0x13FF, gdzie rejestr 0x1000 zawiera najnowsze zdarzenie
Dla łącza ethernetowego w jednej paczce możliwy jest odczyt maksymalnie 60 zdarzeń (60*8 rejestrów). Dla łącza szeregowego ilość odczytywanych zdarzeń nie jest limitowana.
Schemat jednego zdarzenia Numer rejestru Opis
0
Kod zdarzenia
1
Wartość: Lo(Int1), Hi(Int2)
2,3
Wartość float
4
Lo(miesiąc), Hi(końcówka roku)
5
Lo(godzina), Hi(dzień)
6
Lo(sekunda), Hi(minuta)
7
milisekundy
Kody zdarzeń
4.1.1.1.1 Kody zdarzeń Kod Opis Wartość Int1 Wartość Int2 Wartość float
10
ODWZB. ZAB. ZWARCIOWEGO
11
POB. ZAB. ZWARCIOWEGO
Z1000
Imax [A]
12
ZAB. ZWARCIOWE
Z1000
Imax [A]
14
BLK. ZAB. ZWARCIOWEGO
Z1001
15
ODBLK. ZAB. ZWARCIOWEGO
20
ODWZB. ZAB. NADPRĄDOWEGO 1
21
POB. ZAB. NADPRĄDOWEGO 1
Z1000
Imax [A]
22
ZAB. NADPRĄDOWE 1
Z1000
Imax [A]
24
BLK. ZAB. NADPRĄDOWEGO 1
Z1001
25
ODBLK. ZAB. NADPRĄDOWEGO 1
30
ODWZB. ZAB. NADPRĄDOWEGO 2
31
POB. ZAB. NADPRĄDOWEGO 2
Z1000
Imax [A]
32
ZAB. NADPRĄDOWE 2
Z1000
Imax [A]
str. 42
34
BLK. ZAB. NADPRĄDOWEGO 2
Z1001
35
ODBLK. ZAB. NADPRĄDOWEGO 2
40
ODWZB. ZAB. NADPRĄDOWEGO 3
41
POB. ZAB. NADPRĄDOWEGO 3
Z1000
Imax [A]
42
ZAB. NADPRĄDOWE 3
Z1000
Imax [A]
44
BLK. ZAB. NADPRĄDOWEGO 3
Z1001
45
ODBLK. ZAB. NADPRĄDOWEGO 3
50
ODWZB. ZAB. NADPR. ZALEŻNEGO
51
POB. ZAB. NADPR. ZALEŻNEGO
Z1000
Imax [A]
52
ZAB. NADPRĄDOWE ZALEŻNE
Z1000
Imax [A]
54
BLK. ZAB. NADPR. ZALEŻNEGO
Z1001
55
ODBLK. ZAB. NADPR. ZALEŻNEGO
56
SKASOWANIE ZAB. NADPR. ZALEŻNEGO
Z1002
57
ZAB. NADPR. ZALEŻNE - ALARM
58
ODWZB. ZAB. NADPR. ZAL. ALARM
60
ODWZB. ZAB. CIEPLNEGO
61
POB. ZAB. CIEPLNEGO
Z1000
Imax [A]
62
ZAB. CIEPLNE
Z1000
Imax [A]
66
ZAB. CIEPLNE - ALARM
67
SKASOWANIE ZAB. CIEPLNEGO
Z1002
68
ODWZB. ZAB. CIEPLNEGO ALARM
70
ODWZB. ZAB. ZIEMNOZWARCIOWEGO 1
71
POB. ZAB. ZIEMNOZWARCIOWEGO 1
Z1000
I0 [A]
72
ZAB. ZIEMNOZWARCIOWE 1
Z1000
I0 [A]
74
BLK. ZAB. ZIEMNOZWARCIOWEGO 1
Z1001
75
ODBLK. ZAB. ZIEMNOZWARCIOWEGO 1
80
ODWZB. ZAB. ZIEMNOZWARCIOWEGO 2
81
POB. ZAB. ZIEMNOZWARCIOWEGO 2
Z1000
I0 [A]
82
ZAB. ZIEMNOZWARCIOWE 2
Z1000
I0 [A]
84
BLK. ZAB. ZIEMNOZWARCIOWEGO 2
Z1001
85
ODBLK. ZAB. ZIEMNOZWARCIOWEGO 2
90
ODWZB. ZAB. ZIEMNOZW. KIERUNKOWEGO
91
POB. ZAB. ZIEMNOZW. KIERUNKOWEGO
Z1000
I0d [A]
92
ZAB. ZIEMNOZWARCIOWE KIERUNKOWE
Z1000
I0d [A]
94
BLK. ZAB. ZIEMNOZW. KIERUNKOWEGO
Z1001
95
ODBLK. ZAB. ZIEMNOZW. KIERUNKOWEGO
100
ODWZB. ZAB. ADMITANCYJNEGO
101
POB. ZAB. ADMITANCYJNEGO
Z1000
Y0 [S]
102
ZAB. ADMITANCYJNE
Z1000
Y0 [S]
104
BLK. ZAB. ADMITANCYJNEGO
Z1001
105
ODBLK. ZAB. ADMITANCYJNEGO
110
ODWZB. ZAB. ADMIT. KIERUNKOWEGO 1
111
POB. ZAB. ADMIT. KIERUNKOWEGO 1
Z1000
Y0d [S]
112
ZAB. ADMITANCYJNE KIERUNKOWE 1
Z1000
Y0d [S]
114
BLK. ZAB. ADMIT. KIERUNKOWEGO 1
Z1001
115
ODBLK. ZAB. ADMIT. KIERUNKOWEGO 1
120
ODWZB. ZAB. ADMIT. KIERUNKOWEGO 2
121
POB. ZAB. ADMIT. KIERUNKOWEGO 2
Z1000
Y0d [S]
122
ZAB. ADMITANCYJNE KIERUNKOWE 2
Z1000
Y0d [S]
124
BLK. ZAB. ADMIT. KIERUNKOWEGO 2
Z1001
125
ODBLK. ZAB. ADMIT. KIERUNKOWEGO 2
130
ODWZB. ZAB. NADNAPIĘCIOWEGO U0 1
131
POB. ZAB. NADNAPIĘCIOWEGO U0 1
Z1000
U0 [V]
132
ZAB. NADNAPIĘCIOWE U0 1
Z1000
U0 [V]
134
BLK. ZAB. NADNAPIĘCIOWEGO U0 1
Z1001
135
ODBLK. ZAB. NADNAPIĘCIOWEGO U0 1
140
ODWZB. ZAB. NADNAPIĘCIOWEGO U0 2
141
POB. ZAB. NADNAPIĘCIOWEGO U0 2
Z1000
U0 [V]
142
ZAB. NADNAPIĘCIOWE U0 2
Z1000
U0 [V]
str. 43
144
BLK. ZAB. NADNAPIĘCIOWEGO U0 2
Z1001
145
ODBLK. ZAB. NADNAPIĘCIOWEGO U0 2
150
ODWZB. ZAB. NADNAPIĘCIOWEGO 1
151
POB. ZAB. NADNAPIĘCIOWEGO 1
Z1000
Umax [V]
152
ZAB. NADNAPIĘCIOWE 1
Z1000
Umax [V]
154
BLK. ZAB. NADNAPIĘCIOWEGO 1
Z1001
155
ODBLK. ZAB. NADNAPIĘCIOWEGO 1
160
ODWZB. ZAB. NADNAPIĘCIOWEGO 2
161
POB. ZAB. NADNAPIĘCIOWEGO 2
Z1000
Umax [V]
162
ZAB. NADNAPIĘCIOWE 2
Z1000
Umax [V]
164
BLK. ZAB. NADNAPIĘCIOWEGO 2
Z1001
165
ODBLK. ZAB. NADNAPIĘCIOWEGO 2
170
ODWZB. ZAB. PODNAPIĘCIOWEGO 1
171
POB. ZAB. PODNAPIĘCIOWEGO 1
Z1000
Umin [V]
172
ZAB. PODNAPIĘCIOWE 1
Z1000
Umin [V]
174
BLK. ZAB. PODNAPIĘCIOWEGO 1
Z1001
175
ODBLK. ZAB. PODNAPIĘCIOWEGO 1
180
ODWZB. ZAB. PODNAPIĘCIOWEGO 2
181
POB. ZAB. PODNAPIĘCIOWEGO 2
Z1000
Umin [V]
182
ZAB. PODNAPIĘCIOWE 2
Z1000
Umin [V]
184
BLK. ZAB. PODNAPIĘCIOWEGO 2
Z1001
185
ODBLK. ZAB. PODNAPIĘCIOWEGO 2
190
ODWZB. ZAB. ZWROTNOMOCOWEGO P
191
POB. ZAB. ZWROTNOMOCOWEGO P
Z1000
P [W]
192
ZAB. ZWROTNOMOCOWE P
Z1000
P [W]
194
BLK. ZAB. ZWROTNOMOCOWEGO P
Z1001
195
ODBLK. ZAB. ZWROTNOMOCOWEGO P
200
ODWZB. ZAB. ZWROTNOMOCOWEGO Q
201
POB. ZAB. ZWROTNOMOCOWEGO Q
Z1000
Q [var]
202
ZAB. ZWROTNOMOCOWE Q
Z1000
Q [var]
204
BLK. ZAB. ZWROTNOMOCOWEGO Q
Z1001
205
ODBLK. ZAB. ZWROTNOMOCOWEGO Q
210
ODWZB. ZAB. PODPRĄDOWEGO
211
POB. ZAB. PODPRĄDOWEGO
Z1000
Imin [A]
212
ZAB. PODPRĄDOWE
Z1000
Imin [A]
214
BLK. ZAB. PODPRĄDOWEGO
Z1001
215
ODBLK. ZAB. PODPRĄDOWEGO
220
ODWZB. ZAB. OD ZABL. WIRNIKA
221
POB. ZAB. OD ZABL. WIRNIKA
Z1000
Imax [A]
222
ZAB. OD ZABL. WIRNIKA
Z1000
Imax [A]
224
BLK. ZAB. OD ZABL. WIRNIKA
Z1001
225
ODBLK. ZAB. OD ZABL. WIRNIKA
230
ODWZB. ZAB. OD ASYMETRII
231
POB. ZAB. OD ASYMETRII
Z1000
Ias [A]
232
ZAB. OD ASYMETRII
Z1000
Ias [A]
234
BLK. ZAB. OD ASYMETRII
Z1001
235
ODBLK. ZAB. OD ASYMETRII
241
ROZRUCH SILNIKA
242
PRZEKROCZENIE CZASU ROZRUCHU SILNIKA
250
ODWZB. ZAB. PRĄDU WEW. BATERII
251
POB. ZAB. PRĄDU WEW. BATERII
Z1000
Ig [A]
252
ZAB. PRĄDU WEW. BATERII
Z1000
Ig [A]
254
BLK. ZAB. PRĄDU WEW. BATERII
Z1001
255
ODBLK. ZAB. PRĄDU WEW. BATERII
260
ODWZB. ZAB. f<1
261
POB. ZAB. f<1
Z1000
f [Hz]
262
ZAB. f<1
Z1000
f [Hz]
264
BLK. ZAB. f<1
Z1001
265
ODBLK. ZAB. f<1
str. 44
270
ODWZB. ZAB. f<2
271
POB. ZAB. f<2
Z1000
f [Hz]
272
ZAB. f<2
Z1000
f [Hz]
274
BLK. ZAB. f<2
Z1001
275
ODBLK. ZAB. f<2
280
ODWZB. ZAB. f<3
281
POB. ZAB. f<3
Z1000
f [Hz]
282
ZAB. f<3
Z1000
f [Hz]
284
BLK. ZAB. f<3
Z1001
285
ODBLK. ZAB. f<3
290
ODWZB. ZAB. f<4
291
POB. ZAB. f<4
Z1000
f [Hz]
292
ZAB. f<4
Z1000
f [Hz]
294
BLK. ZAB. f<4
Z1001
295
ODBLK. ZAB. f<4
300
ODWZB. ZAB. f>1
301
POB. ZAB. f>1
Z1000
f [Hz]
302
ZAB. f>1
Z1000
f [Hz]
304
BLK. ZAB. f>1
Z1001
305
ODBLK. ZAB. f>1
310
ODWZB. ZAB. f>2
311
POB. ZAB. f>2
Z1000
f [Hz]
312
ZAB. f>2
Z1000
f [Hz]
314
BLK. ZAB. f>2
Z1001
315
ODBLK. ZAB. f>2
320
ODWZB. ZAB. RÓŻN. SILNIKA
321
POB. ZAB. RÓŻN. SILNIKA
Z1000
Ir [A]
322
ZAB. RÓŻNICOWE SILNIKA
Z1000
Ir [A]
324
BLK. ZAB. RÓŻN SILNIKA
Z1001
325
ODBLK. ZAB. RÓŻN. SILNIKA
330
ODWZB. ZAB. OD WYP. Z SYNCH.
331
POB. ZAB. OD WYP. Z SYNCH.
332
ZAB. OD WYP. Z SYNCH.
334
BLK. OD WYP. Z SYNCH.
335
ODBLK. ZAB. OD WYP. Z SYNCH.
340
ODWZB. ZAB. OD ZMIANY NAP.
341
POB. ZAB. OD ZMIANY NAP. U =
[V]
342
ZAB. OD ZMIANY NAP. U =
[V]
344
BLK. ZAB. OD ZMIANY NAP.
345
ODBLK. ZAB. OD ZMIANY NAP.
500
ODWZB. ZAB. NADPRĄDOWEGO 4
501
POB. ZAB. NADPRĄDOWEGO 4
Z1000
Imax [A]
502
ZAB. NADPRĄDOWE 4
Z1000
Imax [A]
504
BLK. ZAB. NADPRĄDOWEGO 4
Z1001
505
ODBLK. ZAB. NADPRĄDOWEGO 4
510
ODWZB. ZAB. NADPRĄDOWEGO 5
511
POB. ZAB. NADPRĄDOWEGO 5
Z1000
Imax [A]
512
ZAB. NADPRĄDOWE 5
Z1000
Imax [A]
514
BLK. ZAB. NADPRĄDOWEGO 5
Z1001
515
ODBLK. ZAB. NADPRĄDOWEGO 5
520
ODWZB. ZAB. ZIEMNOZWARCIOWEGO 3
521
POB. ZAB. ZIEMNOZWARCIOWEGO 3
Z1000
I0 [A]
522
ZAB. ZIEMNOZWARCIOWE 3
Z1000
I0 [A]
524
BLK. ZAB. ZIEMNOZWARCIOWEGO 3
Z1001
525
ODBLK. ZAB. ZIEMNOZWARCIOWEGO 3
530
ODWZB. ZAB. NADNAPIĘCIOWEGO U0 3
531
POB. ZAB. NADNAPIĘCIOWEGO U0 3
Z1000
U0 [V]
532
ZAB. NADNAPIĘCIOWE U0 3
Z1000
U0 [V]
534
BLK. ZAB. NADNAPIĘCIOWEGO U0 3
Z1001
str. 45
535
ODBLK. ZAB. NADNAPIĘCIOWEGO U0 3
560
ODWZB. ZAB. NADNAPIĘCIOWEGO 3
561
POB. ZAB. NADNAPIĘCIOWEGO 3
Z1000
Umax [V]
562
ZAB. NADNAPIĘCIOWE 3
Z1000
Umax [V]
564
BLK. ZAB. NADNAPIĘCIOWEGO 3
Z1001
565
ODBLK. ZAB. NADNAPIĘCIOWEGO 3
570
ODWZB. ZAB. PODNAPIĘCIOWEGO 3
571
POB. ZAB. PODNAPIĘCIOWEGO 3
Z1000
Umin [V]
572
ZAB. PODNAPIĘCIOWE 3
Z1000
Umin [V]
574
BLK. ZAB. PODNAPIĘCIOWEGO 3
Z1001
575
ODBLK. ZAB. PODNAPIĘCIOWEGO 3
580
ODWZB. ZAB. NADNAPIĘCIOWEGO ŚREDNIEGO
581
POB. ZAB. NADNAPIĘCIOWE Uśr
Z1000
Umin [V]
582
ZAB. NADNPIĘCIOWE Uśr
Z1000
Umin [V]
584
BLK. ZAB. NADNAPIĘCIOWEGO Uśr
Z1001
585
ODBLK. ZAB. NADNAPIĘCIOWEGO Uśr
1002
ROZBROJENIE NAPĘDU WYŁĄCZNIKA
1012
BRAK COW1
1022
BRAK COW2
1032
BRAK COZ
1042
OTWARCIE Z LRW
1043
LRW
1052
ZAB. TEMPERATUROWE 1
1062
ZAB. TEMPERATUROWE 2
1072
ZAB. GAZ.-PRZEPŁ. TRAFO I ST.
1082
ZAB. GAZ.-PRZEPŁ. TRAFO II ST.
1092
ZAB. GAZ.-PRZEPŁ. DŁAWIKA I ST.
1102
ZAB. GAZ.-PRZEPŁ. DŁAWIKA II ST.
1112
ZAB. GAZ.-PRZEPŁ. PRZEŁ. ZACZEPÓW
1122
ZAB. RÓŻNICOWE ZEWNĘTRZNE
1132
ZAB. ODLEGŁOŚCIOWE ZEWNĘTRZNE
1142
ZAB. ZEWNĘTRZNE
1150
ODWZB. ZAB. PT CZUJNIK:
uint8
1152
ZAB. PT CZUJNIK:
uint8
1153
BŁĄD CZUJNIKA PT
1154
ZAB. PT UP CZUJNIK:
uint8
1155
ODWZB. ZAB. PT UP CZUJNIK:
uint8
1162
ZUŻYCIE STYKÓW WYŁĄCZNIKA N=
uint8
[]
1172
USZKODZENIE PRZEKŁADNIKÓW PRĄDOWYCH
1182
USZKODZENIE PRZEKŁADNIKÓW NAPIĘCIOWYCH
1192
ZADZIAŁANIE BEZPIECZNIKÓW W OBW. U
1193
ZADZIAŁANIE BEZPIECZNIKÓW W OBW. U0
1194
ZADZIAŁANIE BEZPIECZNIKÓW W OBW. Us
1195
ZADZIAŁANIE BEZPIECZNIKÓW W OBW. USZR
1200
ZAB. ŁUKOOCHR. CZUJNIK:
uint8
1201
OTW. Z ZAB. ŁUKOOCHR. POLE:
uint8
1202
ZAB. ŁUKOOCHR. BRAK ZAREJ. POLA
uint8
1203
ZAB. ŁUKOOCHR. BRAK ODCZYTU NAPIĘCIA
Z1006
1204
ODWZB. ZAB. ŁUKOOCHR. CZUJNIK:
uint8
1205
TEST ZAB. ŁUKOOCHR. POZYTYWNY
uint8
1206
TEST ZAB. ŁUKOOCHR. NEGATYWNY CZUJNIK:
uint8
2000
ODWZB. ZAB. TECHNOLOGICZNEGO
uint8
2001
POB. ZAB. TECHNOLOGICZNEGO
uint8
2002
ZAB. TECHNOLOGICZNE
uint8
2012
ROZBROJENIE NAPĘDU WYŁĄCZNIKA nN
2080
ZDARZENIE UŻYTKOWNIKA
uint8
2101
ZAMKNIĘCIE OPERACYJNE ŁĄCZNIKA
Z1005
Z1002
2102
OTWARCIE OPERACYJNE ŁĄCZNIKA
Z1005
Z1002
2103
ZAMKNIĘCIE ZEWNĘTRZNE ŁĄCZNIKA
Z1005
str. 46
2104
OTWARCIE ZEWNĘTRZNE ŁĄCZNIKA
Z1005
2105
BŁĄD STEROWANIA ŁĄCZNIKA
Z1005
2106
BŁĄD STANU ŁĄCZNIKA
Z1005
2200
ODWZB. WE
uint8
Z1003
2201
POB. WE
uint8
Z1003
2900
ZABLOKOWANIE AUTOMATYKI SPZ
Z1002
2901
ODBLOKOWANIE AUTOMATYKI SPZ
Z1002
2902
ZAŁĄCZENIE SPZ1
2903
ZAŁĄCZENIE SPZ2
2904
ZAŁĄCZENIE SPZ3
2905
NIEUDANE ZAŁĄCZENIE SPZ
2906
DEFINITYWNE WYŁĄCZENIE SPZ
2920
ODSTAWIENIE AUTOMATYKI SPZ
Z1002
2921
NASTAWIENIE AUTOMATYKI SPZ
Z1002
3000
ZABLOKOWANIE AUTOMATYKI SCO
Z1002
3001
ODBLOKOWANIE AUTOMATYKI SCO
Z1002
3002
AUTOMATYKA SCO
Z1000
f [Hz]
3003
AUTOMATYKA SCO 1 ST.
Z1000
f [Hz]
3004
AUTOMATYKA SCO 2 ST.
Z1000
f [Hz]
3005
AUTOMATYKA SCO 3 ST.
Z1000
f [Hz]
3006
AUTOMATYKA SCO 4 ST.
Z1000
f [Hz]
3007
AUTOMATYKA SPZ/SCO
Z1000
f [Hz]
3020
ODSTAWIENIE AUTOMATYKI SCO
Z1002
3021
NASTAWIENIE AUTOMATYKI SCO
Z1002
3100
ZABLOKOWANIE AUTOMATYKI SCOw
Z1002
3101
ODBLOKOWANIE AUTOMATYKI SCOw
Z1002
3102
OTWARCIE Z AUTOMATYKI SCO ST:
uint8
3103
ZAMKNIĘCIE Z AUTOMATYKI SCO
3104
OTWARCIE Z AUTOMATYKI SCO
Z1000
f [Hz]
3105
ZAMKNIĘCIE Z AUTOMATYKI SCO
Z1000
f [Hz]
3120
ODSTAWIENIE AUTOMATYKI SCOw
Z1002
3121
NASTAWIENIE AUTOMATYKI SCOw
Z1002
3130
ZABLOKOWANIE AUT. SPZ/SCOw
Z1002
3131
ODBLOKOWANIE AUT. SPZ/SCOw
Z1002
3132
ODSTAWIENIE AUT. SPZ/SCOw
Z1002
3133
NASTAWIENIE AUT. SPZ/SCOw
Z1002
3200
ZABLOKOWANIE AUTOMATYKI AWSC
Z1002
3201
ODBLOKOWANIE AUTOMATYKI AWSC
Z1002
3202
ZAMKNIĘCIE STYCZNIKA Z AWSC
3203
OTWARCIE STYCZNIKA Z AWSC
3204
OTWARCIE WYŁĄCZNIKA Z AWSC
3205
POB. ZAB. NADPRĄDOWEGO I0 AWSC
Z1000
I0 [A]
3206
ZAB. NADPRĄDOWE I0 AWSC
Z1000
I0 [A]
3207
ODWZB. ZAB. NADPRĄDOWEGO I0 AWSC
Z1000
3208
POB. ZAB. NADNAPIĘCIOWEGO U0 AWSC
Z1000
U0 [V]
3209
ZAB. NADNAPIĘCIOWE U0 AWSC
Z1000
U0 [V]
3210
ODWZB. ZAB. NADNAPIĘCIOWEGO U0 AWSC
Z1000
3220
ODSTAWIENIE AUTOMATYKI AWSC
Z1002
3221
NASTAWIENIE AUTOMATYKI AWSC
Z1002
3400
ZABL. UKŁ. WSP. Z AZBK
Z1002
3401
ODBL. UKŁ. WSP. Z AZBK
Z1002
3402
OTWARCIE Z AUTOMATYKI AZBK
3403
ZAMKNIĘCIE Z AUTOMATYKI AZBK
3420
ODST. UKŁ. WSP. Z AZBK
Z1002
3421
NAST. UKŁ. WSP. Z AZBK
Z1002
3500
OTWARCIE Z AUTOMATYKI SZR
3501
ZAMKNIĘCIE Z AUTOMATYKI SZR
3600
OCZEKIWANIE NA SYNCHRONIZACJĘ
3601
SYNCHRONIZACJA NIEUDANA
Z1007
str. 47
3700
ZABLOKOWANIE AUTOMATYKI SPZW
Z1002
3701
ODBLOKOWANIE AUTOMATYKI SPZW
Z1002
3702
ZAŁĄCZENIE SPZW
3705
NIEUDANE ZAŁĄCZENIE SPZW
3706
DEFINITYWNE WYŁĄCZENIE SPZW
3720
ODSTAWIENIE AUTOMATYKI SPZW
Z1002
3721
NASTAWIENIE AUTOMATYKI SPZW
Z1002
8000
RESTART e2TANGO
8001
BRAK NAPIĘCIA ZASILANIA Z12
8002
BRAK NAPIĘCIA ZASILANIA Z34
8003
ZMIANA PARAMETRÓW:
Z1004
Z1002
8004
BRAK NAPIĘCIA ZASILANIA
8005
PODANIE NAPIĘCIA ZASILANIA
8100
SKASOWANIE ZDARZEŃ
Z1002
8101
SKASOWANIE REJESTRATORA ZAKŁÓCEŃ
Z1002
8102
SKASOWANIE REJESTRATORA KRYT.
Z1002
8103
ZMIANA BANKU NASTAW NA BANK:
uint8
Z1002
8104
SKASOWANIE PROFILU MOCY.
Z1002
8105
SKASOWANIE REJESTRATORA JAOŚCI ENERGII.
Z1002
9000
BŁĄD NASTAW - WPROWADZONO WARTOŚCI DOMYŚLNE
Z1004
9001
BŁĄD PROCESORA DSP NR:
uint8
uint16
9002
BŁĄD KARTY W SLOCIE:
Z1003
9003
BATERIA ROZŁADOWANA
9010
KALIBRACJA DSP:
uint8
9011
BŁĄD KALIBRACJI DSP:
Z1008
Z1009
9012
KALIBRACJA DSP OK:
uint8
uint16
9013
UTRATA PAMIĘCI RAM:
uint8
9014
ZMIANA WERSJI FIRMWARE'U
9015
BŁĄD PRZERWANIA
uint8
uint16
9016
RESET e2TANGO
uint8
uint16
9098
WYZWOLENIE REJESTRATORA OD ZAM. WYŁ.
9099
WYZWOLENIE REJESTRATORA OD LOGIKI
4.1.1.2 Formaty dla zdarzeń Format Opis
Z1000
0 = 1 = faza: 1 2 = faza: 2 3 = faza: 12 4 = faza: 3 5 = faza: 13 6 = faza: 23 7 = faza: 123 8 = symulacja
Z1001
0 = 1 = II harm. 2 = Zab.szyn 3 = Logika 4 = Odstawienie 5 = I0 AWSC 6 = Bezp. U
Z1002
0 = 1 = We.dwust. 2 = Telester. 3 = Logika 4 = 5 = COM1 6 = COM2 7 = ETH1
str. 48
8 = ETH2 9 = 10 = Panel 11 = Panel Oper1 12 = Panel Oper2 13 = Panel Oper3 14 = Panel Oper4 15 = Panel Oper5 16 = Panel Oper6 17 = Panel Oper7 18 = Panel Oper8 19 = Panel Admin 20 = TStudio 21 = TStudio Oper1 22 = TStudio Oper2 23 = TStudio Oper3 24 = TStudio Oper4 25 = TStudio Oper5 26 = TStudio Oper6 27 = TStudio Oper7 28 = TStudio Oper8 29 = TStudio Admin
Z1003
0 = 1 = A 2 = B 3 = C 4 = D 5 = E 6 = F 7 = G 8 = H 9 = I 10 = J 11 = K 12 = L 13 = M 14 = N
Z1004
0 = 1 = BANK 1 2 = BANK 2 3 = BANK 3 4 = BANK 4 5 = NASTAWY OGÓLNE 6 = ZESTAW ZABEZP. 7 = KOMUNIKACJA 8 = KONFIG. KART 9 = SYMULACJA 10 = LOGIKA 11 = SCHEMAT 12 = ETYKIETY 13 = UST. WIDGETÓW 14 = PLIK STER. 15 = UPRAWNIENIA 16 = HASŁA
Z1005
0 = Q1 1 = Q2 2 = Q3 3 = Q4 4 = Q5 5 = Q6 6 = Q7 7 = Q8 8 = Q9 9 = Q10 10 = Q11 11 = Q12
Z1006
0 = SEK.1 1 = SEK.2 2 = SEK.3 3 = SEK.4 4 = SYST.A 5 = SYST.B1 6 = SYST.B2
str. 49
Z1007
0 = 1 = ΔU 2 = Δf 3 = Δf,ΔU 4 = Δφ 5 = Δφ,ΔU 6 = Δφ,Δf 7 = Δφ,Δf,ΔU
Z1008
0 = U 1 = Im 2 = Id 3 = I0m 4 = I0d 5 = U0 6 = Ig 7 = Ir 8 = Umn 9 = P 10 = Q 11 = EEPROM
Z1009
0 = 1 = AMP 2 = PHA
5 Synchronizacja czasu
Odczyt funkcją 3, zapis funkcją 16
Zapis lub odczyt tylko kompletu rejestrów.
Adres bazowy: 0x1620
Adres
Opis
Zakres wartości
+0x0000
Końcówka roku
0 - 99
+0x0001
Miesiąc
1 - 12
+0x0002
Dzień
1 - 31
+0x0003
Godzina
0 - 23
+0x0004
Minuta
0 - 59
+0x0005
Sekunda
0 - 59
+0x0006
Milisekunda
0 - 999
6 Identyfikacja
Odczyt funkcją 3
Adres bazowy: 0x1600
Adres
Opis
+0x0000
MSB - wersja 1 jednostki centralnej, LSB - wersja 2 jednostki centralnej
+0x0001
MSB - wersja 3 jednostki centralnej, LSB - wersja 4 jednostki centralnej
+0x0002
Ilość dostępnych slotów (6, 10, 14)
+0x0003
Wersja 4 pliku sterownika
+0x0004
nr seryjny 1 jednostki centralnej
+0x0005
nr seryjny 2 jednostki centralnej
+0x0006
MSB - wersja 1 panela, LSB - wersja 2 panela
+0x0007
MSB - wersja 3 panela, LSB - wersja 4 panela
+0x0008
wersja sprzętowa panela (600, 800, 1000, 1200)
str. 50
+0x0009
+0x000A
nr seryjny 1 panela
+0x000B
nr seryjny 2 panela
7 Kody błędów
Kod
Opis
0x01
Niedozwolona funkcja
0x02
Niedozwolony numer rejestru
0x06
Urządzenie zajęte
0x0A
Odmowa sterowania - blokady
0x0B
Odmowa dostępu – brak uprawnień
8 Odczyt rejestratora zakłóceń
OSTRZEŻENIE!
Poniższy dokument opisuje protokół pobierania rejestratorów obowiązujący dla wszystkich nowych sterowników e²TANGO. Niektóre starsze urządzenia mogą nie być kompatybilne. Oprogramowanie e²TANGO-Studio oraz firmware panelu zachowują zgodność z wszystkimi sterownikami. W wypadku oprogramowania firm trzecich zaleca się aktualizację urządzenia.
Rejestrator zakłóceń przechowuje określoną liczbę ostatnio zarejestrowanych przebiegów. Długość pojedynczego przebiegu zależy od konfiguracji (ilość pamiętanych przebiegów, ilość rejestrowanych kanałów, częstotliwość próbkowania itp.). Przebiegi numerowane są kolejnymi liczbami naturalnymi. Numery resetowane są do zera gdy lista jest czyszczona poleceniem kasowania lub wskutek zmiany nastaw. Numery rosną do wartości 0xFFFF po czym numeracja zaczyna się od początku. Numer danego przebiegu nigdy się nie zmienia. Numery nie powtarzają się wśród aktualnie pamiętanych przebiegów. Każdy przebieg składa się z serii bloków opisujących stan sieci w ciągu ostatnich 10 milisekund. Rejestrator pamięta dwa rodzaje kanałów.
Kanały pomiarowe zapamiętują wartość RMS rejestrowanej wartości fizycznej. Wartość RMS zapamiętywana jest co 10ms. Każdy blok zawiera jedną liczbę typu float dla każdego kanału pomiarowego. Liczba ta bezpośrednio przekłada się na wartość pomiaru.
Kanały próbkowane zapamiętują wartość chwilową, pochodzącą bezpośrednio z przetwornika. Próbki rejestrowane są z częstotliwością 1.6kHz lub 3.2kHz w zależności od nastawy. Każdy blok zawiera odpowiedni 16 lub 32 próbki dla każdego rejestrowanego kanału próbkowanego.
Konfiguracja rejestratora odbywa się w sekcji "Konfiguracja → Nastawy ogólne → Rejestrator zakłóceń". Możemy decydować o częstotliwości rejestracji próbek. Wybór częstotliwości 1,6kHz daje 16 próbek na kanał na blok, zaś 3.2kHz daje 32 próbki na kanał na blok. W sekcji tej możemy również wyłączyć rejestrację próbek w niektórych kanałach co pozwala zaoszczędzić miejsce i wydłużyć czas rejestracji. W transmisji Modbus pojawiają się tylko aktywne kanały w tej samej kolejności, w jakiej figurują w opcjach. W obecnej wersji oprogramowania nie można wyłączyć kanałów pomiarowych w rejestratorze zakłóceń. Rejestrowane kanały pomiarowe to:
 I1
str. 51
 I2
 I3
 U1
 U2
 U3
 I0
 U0
 I1R
 I2R
 I3R
 f
OSTRZEŻENIE!
Dokładna ilość danych pobieranych z urządzenia zależy od konfiguracji rejestratora. Przed odczytem upewnij się, że twój system zna wszystkie odpowiednie parametry. Zmiana parametrów w urządzeniu spowoduje skasowanie dotychczas zarejestrowanych przebiegów.
Adresy rejestratora zakłóceń:
 0x0620 (funkcja 4) - aktualnie odczytywany blok
 0x2570 (funkcja 16) - kontrola aktualnie odczytywanego bloku
 0x25C0 (funkcja 3) - parametry rejestratora
 0x2580 (funkcja 3) - lista zarejestrowanych przebiegów
Aby odczytać rejestrator zakłóceń postępuj według następującej procedury:
1. Odczytaj parametry rejestratora (0x25C0 f. 3)
2. Odczytaj listę zarejestrowanych przebiegów (0x2580 f. 3)
3. Wybierz blok do odczytu (0x2570 f. 16)
4. Odczytaj blok (0x0620 f. 4)
5. Powtarzaj punkty 3. oraz 4. aż odczytasz wszystkie interesujące przebiegi
8.1 Parametry rejestratora (funkcja 3, offset 0x25C0)
Liczba rejestrów: 4 + 4*n + 4*m gdzie:
 n - liczba rejestrowanych kanałów pomiarowych
 m - liczba rejestrowanych kanałów próbkowanych
Pierwszy rejestr
Ostatni rejestr
Liczba rejestrów
Opis
+0
+0
1
suma CRC bloku (nieistotne)
+1
+1
1
wartość zarezerwowana
+3
+3
1
liczba bloków w każdym przebiegu
+3
+3
1
rozmiar bloku (w rejestrach)
+4
+4+4∙n-1
4∙n
parametry przekładników dla kanałów pomiarowych
(po dwie liczby stałoprzecinkowe uint32 –
strona pierwotna i strona wtórna)
str. 52
+4+4∙n
+4+4∙n+4∙m-1
4∙m
parametry przekładników dla kanałów próbkowanych
(j. w.)
8.2 Lista przebiegów (funkcja 3, offset 0x2580)
Liczba rejestrów: 26 * 40
Każdy zarejestrowany przebieg opisany jest przez jeden rekord o rozmiarze 26 słów. Lista przebiegów może zwierać do 40 wpisów. Należy odczytywać całe rekordy lub ich wielokrotności.
Kolejne rekordy w tabeli ułożone są w przestrzeni adresowej Modbus co 1 rejestr. Przykłady tego, jak odczytywać kolejne wpisy, przedstawiono w tabeli poniżej. Ze względu na specyfikę protokołu Modbus RTU, oraz górne ograniczenie rozmiaru ramki w protokole Ethernet nie zaleca się czytania więcej niż 10 wpisów jednym zapytaniem.
wpisy do odczytania
offset
liczba rejestrów
0
0x2580
26
1
0x2581
26
2
0x2582
26
4,5,6
0x2584
78
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40
0x2580
1040
OSTRZEŻENIE!
Rejestratory "nachodzą na siebie" w przestrzeni adresowej Modbus. (patrz: akapit powyżej)
Struktura pojedynczego wpisu została przedstawiona poniżej. Data oznacza moment wyzwolenia. Jeśli wpis wypełniony jest wartościami 0xFFFF oznacza to, że jest pusty i nie należy go uwzględniać.
Pierwszy rejestr
Ostatni rejestr
Liczba rejestrów
Opis
Starszy bajt
Młodszy bajt
+0
+0
1
końcówka roku
miesiąc
+1
+1
1
dzień
godzina
+2
+2
1
minuta
sekunda
+3
+3
1
milisekunda
+4
+4
1
powód wyzwolenia
+5
+5
1
procent czasu rejestratora mająca miejsce przed wyzwoleniem (wartość z odpowiedniej nastawy)
+6
+7
2
zarezerwowane
+8
+15
8
pobudzenia zabezpieczeń, jakie miały miejsce w czasie trwania przebiegu (4 liczby 32-bitowe)
+16
+23
8
zadziałania zabezpieczeń, jakie miały miejsce w czasie trwania przebiegu (4 liczby 32-bitowe)
+24
+24
1
numer rejestratora
+25
+25
1
crc (nieistotne)
str. 53
8.3 Wybór bloku do odczytu (funkcja 16, offset 0x2570)
Liczba rejestrów: 2
Numer przebiegu odczytany z listy należy zapisać pod wskazany adres, aby urządzenie udostępniło dane rejestratora do odczytu. Poszczególne bloki w ramach przebiegu numerowane są od zera.
Pierwszy rejestr
Ostatni rejestr
Liczba rejestrów
Opis
+0
+0
1
numer przebiegu do odczytu
+1
+1
1
numer bloku do odczytu
8.4 Odczyt bloku
Liczba rejestrów: przesyłana w parametrach rejestratora
Rozmiar bloku zależy od tego, jakie kanały są aktywne. Aby ułatwić zadanie i zwiększyć niezawodność systemu, urządzenie oblicza rozmiar bloku i udostępnia tę daną wśród parametrów rejestratora (patrz: 1. Parametry rejestratora, rozmiar bloku). Poniżej przedstawiono zawartość pojedynczego bloku. Rozmiar bloku wynosi: 36 + liczba-aktywnych-kanałów-pomiarowych ∙ 2 + liczba-aktywnych-kanałów-próbkowanych ∙ (16 lub 32).
Pierwszy rejestr
Ostatni rejestr
Liczba rejestrów
Opis
+0
+0
1
numer przebiegu (powtórzone spod adresu 0x2570, funkcji 16)
+1
+1
1
numer bloku (powtórzone spod adresu 0x2571, funkcji 16)
+2
+9
8
pobudzenia zabezpieczeń, jakie miały miejsce w czasie trwania bloku (4 liczby 32-bitowe)
+10
+17
8
zadziałania zabezpieczeń, jakie miały miejsce w czasie trwania bloku (4 liczby 32-bitowe)
+18
+19
2
sygnały z logiki
+20
+34
15
stany wejść/wyjść (15 liczb 16-bitowych)
+35
+35
1
crc (nieistotne)
+36
+rozmiar bloku - 1
rozmiar bloku - 36
dane
Pole dane ma następującą strukturę:
 Dla każdego aktywnego kanału pomiarowego jedna liczba typu float (32 bity). Najpierw starszy bajt, potem młodszy. Transmitowana wartość po stronie wtórnej.
 Dla każdego aktywnego kanału próbkowanego 16 lub 32 próbki (jedna próbka - liczba 16 bitowa ze znakiem). Liczba miejsc po przecinku zależy od pomiaru:
o I1: 2
o I2: 2
o I3: 2
o U1: 2
o U2: 2
o U3: 2
o U0: 2
o I0: 3
str. 54
o IR1: 2
o IR2: 2
o IR3: 2
o U12: 2
o U23: 2
o U31: 2
o U0_obl: 2
o I0_obl: 3
W polu stany wejść wyjść każdy rejestr przechowuje stany jednej karty. Kolejno są to karty ze slotów: A, B, C, D, E, F, G, H, I, J, K, L, M, N, W. Bit 0 odpowiada wejściu/wyjściu 1, bit 1 wejściu/wyjściu 2 itd. Gdy mamy do czynienia z jednostką centralną o liczbie slotów mniejszej niż 14 lub gdy któryś slot nie zawiera karty wejść/wyjść, rejestr odpowiadający slotowi zwraca same zera.
8.5 Problemy w trakcie odczytu
W trakcie odczytu rejestratora mogą się zdarzyć trzy różne sytuacje, które spowodują, że odczytywany przebieg zniknie z urządzenia:
 zmiana nastaw rejestratora
 skasowanie rejestratora
 przepełnienie listy przebiegów
Próba odczytu bloku nieistniejącego przebiegu skutkuje zwróceniem przez urządzenie błędu Modbus. Zaleca się w takiej sytuacji rozpoczęcie procedury od punktu 1.
9 Odczyt rejestratora kryterialnego
OSTRZEŻENIE!
Poniższy dokument opisuje protokół pobierania rejestratorów obowiązujący dla wszystkich nowych sterowników e²TANGO. Niektóre starsze urządzenia mogą nie być kompatybilne. Oprogramowanie e²TANGO-Studio oraz firmware panelu zachowują zgodność z wszystkimi sterownikami. W wypadku oprogramowania firm trzecich zaleca się aktualizację urządzenia.
Rejestrator kryterialny zapisuje określone parametry co 10 ms. Długość pojedynczej rejestracji zależy od skonfigurowanej liczby zapamiętywanych rejestracji oraz ilości zapamiętywanych pomiarów. Przebiegi numerowane są kolejnymi liczbami naturalnymi. Numery resetowane są do zera gdy lista jest czyszczona poleceniem kasowania lub wskutek zmiany nastaw. Numery rosną do wartości 0xFFFF po czym numeracja zaczyna się od początku. Numer danego przebiegu nigdy się nie zmienia. Numery nie powtarzają się wśród aktualnie pamiętanych rejestracji.
Kanały pomiarowe zapamiętują wartość skuteczną rejestrowanej wartości fizycznej. Wartość ta zapamiętywana jest co 10ms. Każdy blok zawiera jedną liczbę typu float dla każdego kanału pomiarowego. Liczba ta bezpośrednio przekłada się na wartość pomiaru.
Konfiguracja rejestratora odbywa się w sekcji "Konfiguracja → Nastawy ogólne → Rejestrator kryterialny". W sekcji tej możemy wyłączyć rejestrację wartości pomiarowych w niektórych kanałach co pozwala zaoszczędzić miejsce i wydłużyć czas rejestracji. W transmisji Modbus pojawiają się tylko
str. 55
aktywne kanały w tej samej kolejności, w jakiej figurują w opcjach. Rejestrowane kanały pomiarowe to:
 I1
 I2
 I3
 U1
 U2
 U3
 I0
 U0
 φ0
 I1R
 I2R
 I3R
OSTRZEŻENIE!
Dokładna ilość danych pobieranych z urządzenia zależy od konfiguracji rejestratora. Przed odczytem upewnij się, że twój system zna wszystkie odpowiednie parametry. Zmiana parametrów w urządzeniu spowoduje skasowanie dotychczas zarejestrowanych przebiegów.
Adresy rejestratora kryterialnego:
 0x0860 (funkcja 4) - aktualnie odczytywany blok
 0x25D0 (funkcja 16) - numer odczytywanego bloku oraz rejestratora
 0x2620 (funkcja 3) - parametry rejestratora
 0x25E0 (funkcja 3) - lista rejestracji
Aby odczytać rejestrator kryterialny postępuj według następującej procedury:
1. Odczytaj parametry rejestratora (0x2620 f. 3)
2. Odczytaj listę rejestracji (0x25E0 f. 3)
3. Wybierz blok do odczytu (0x25D0 f. 16)
4. Odczytaj blok (0x0860 f. 4)
5. Powtarzaj punkty 3. oraz 4. aż odczytasz wszystkie interesujące przebiegi
9.1 Parametry rejestratora (funkcja 3, offset 0x2620)
Liczba rejestrów: 4 + 4*n, gdzie n - liczba rejestrowanych kanałów pomiarowych
Pierwszy rejestr
Ostatni rejestr
Liczba rejestrów
Opis
+0
+0
1
suma CRC bloku (nieistotne)
+1
+1
1
wartość zarezerwowana
+2
+2
1
liczba bloków 10ms w każdej rejestracji
+3
+3
1
rozmiar bloku 10ms (w rejestrach)
+4
+4+4∙n-1
4∙n
parametry przekładników dla kanałów pomiarowych
(po dwie liczby stałoprzecinkowe uint32 –
str. 56
strona pierwotna i strona wtórna)
9.2 Lista rejestracji (funkcja 3, offset 0x25E0)
Liczba rejestrów: 26 * 40
Każdy zarejestrowany przebieg opisany jest przez jeden rekord o rozmiarze 26 słów. Lista rejestracji może zwierać do 40 wpisów. Należy odczytywać całe rekordy lub ich wielokrotności.
Kolejne rekordy w tabeli ułożone są w przestrzeni adresowej Modbus co 1 rejestr. Przykłady tego, jak odczytywać kolejne wpisy, przedstawiono w tabeli poniżej. Ze względu na specyfikę protokołu Modbus RTU, oraz górne ograniczenie rozmiaru ramki w protokole Ethernet nie zaleca się czytania więcej niż 10 wpisów jednym zapytaniem. Przykład:
rejestry do odczytania
adres
liczba rejestrów
0
0x25E0
26
1
0x25E1
26
2
0x25E2
26
4,5,6
0x25E4
78
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39
0x25E0
1040
Struktura pojedynczego wpisu została przedstawiona poniżej. Data oznacza moment wyzwolenia. Jeśli wpis wypełniony jest wartościami 0xFFFF oznacza to, że jest pusty i nie należy go uwzględniać.
Pierwszy rejestr
Ostatni rejestr
Liczba rejestrów
Opis
Starszy bajt
Młodszy bajt
+0
+0
1
końcówka roku
miesiąc
+1
+1
1
dzień
godzina
+2
+2
1
minuta
sekunda
+3
+3
1
milisekunda
+4
+4
1
powód wyzwolenia
+5
+5
1
procent czasu rejestratora przed wyzwoleniem (wartość z odpowiedniej nastawy – Nastawy Ogólne)
+6
+7
2
zarezerwowane
+8
+15
8
pobudzenia zabezpieczeń, jakie miały miejsce w czasie trwania przebiegu (4 liczby 32-bitowe)
+16
+23
8
zadziałania zabezpieczeń, jakie miały miejsce w czasie trwania przebiegu (4 liczby 32-bitowe)
+24
+24
1
numer rejestratora
+25
+25
1
crc (nieistotne)
9.3 Wybór bloku do odczytu (funkcja 16, offset 0x25D0)
Liczba rejestrów: 2
Numer przebiegu odczytany z listy należy zapisać pod wskazany adres, aby urządzenie udostępniło dane rejestratora do odczytu. Poszczególne bloki w ramach przebiegu numerowane są od zera.
Pierwszy rejestr
Ostatni rejestr
Liczba rejestrów
Opis
str. 57
+0
+0
1
numer przebiegu do odczytu
+1
+1
1
numer bloku 10ms do odczytu
9.4 Odczyt bloku
Liczba rejestrów: przesyłana w parametrach rejestratora
Rozmiar bloku zależy od tego, jakie kanały są aktywne. Aby ułatwić zadanie i zwiększyć niezawodność systemu, urządzenie oblicza rozmiar bloku i udostępnia tę daną wśród parametrów rejestratora (patrz: 1. Parametry rejestratora, rozmiar bloku). Poniżej przedstawiono zawartość pojedynczego bloku. Rozmiar bloku wynosi: 36 + liczba-aktywnych-kanałów-pomiarowych ∙ 2.
Pierwszy rejestr
Ostatni rejestr
Liczba rejestrów
Opis
+0
+0
1
numer przebiegu (powtórzone spod adresu 0x25D0, funkcji 16)
+1
+1
1
numer bloku (powtórzone spod adresu 0x25D1, funkcji 16)
+2
+9
8
pobudzenia zabezpieczeń, jakie miały miejsce w czasie trwania bloku (4 liczby 32-bitowe)
+10
+17
8
zadziałania zabezpieczeń, jakie miały miejsce w czasie trwania bloku (4 liczby 32-bitowe)
+18
+19
2
sygnały z logiki
+20
+34
15
stany wejść/wyjść (15 liczb 16-bitowych)
+35
+35
1
crc (nieistotne)
+36
+rozmiar bloku - 1
rozmiar bloku - 36
dane
Pole dane może mieć zmienną długość i zależy od ilości rejestrowanych pomiarów. Dla każdego aktywnego kanału pomiarowego jedna liczba typu float (32 bity). Najpierw starszy bajt, potem młodszy. Transmitowana wartość po stronie wtórnej. Rejestrowane wartości pomiarów: I1, I2, I3, U1, U2, U3, I0, U0, Φ0, IR1, IR2, IR3
W polu stany wejść wyjść każdy rejestr przechowuje stany jednej karty. Kolejno są to karty ze slotów: A, B, C, D, E, F, G, H, I, J, K, L, M, N, W. Bit 0 odpowiada wejściu/wyjściu 1, bit 1 wejściu/wyjściu 2 itd. Gdy mamy do czynienia z jednostką centralną o liczbie slotów mniejszej niż 14 lub gdy któryś slot nie zawiera karty wejść/wyjść, rejestr odpowiadający slotowi zwraca same zera.
9.5 Problemy w trakcie odczytu
W trakcie odczytu rejestratora mogą się zdarzyć trzy różne sytuacje, które spowodują, że odczytywany przebieg zniknie z urządzenia:
 zmiana nastaw rejestratora
 skasowanie rejestratora
 przepełnienie listy przebiegów
Próba odczytu bloku nieistniejącego przebiegu skutkuje zwróceniem przez urządzenie błędu Modbus. Zaleca się w takiej sytuacji rozpoczęcie procedury od punktu 1.
str. 58
10 Komunikacja ETHERNET
Ethernet w e²TANGO może obsłużyć jednocześnie dwa łącza w protokole Modbus/TCP lub Modbus/RTU. W zależności od portu połączenia:
502 - łącze 1 protokół Modbus/TCP
10502 - łącze 2 protokół Modbus/TCP
10503 - łącze 1 protokół Modbus/RTU
10504 - łącze 2 protokół Modbus/RTU