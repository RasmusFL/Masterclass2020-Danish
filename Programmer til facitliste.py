# Opgave 1.13.2
def konvSum(N):     # funktionen tager N (et positivt heltal) som input og skriver summen ud
    sum = 0
    for n in range(1, N):  # bruger en for-løkke
        sum = sum + 1 / (n * (n + 1))  # udregningen udføres for alle n = 1, 2, 3, ... , N

    print("Summen er: ", sum)  # Skriver summen ud

# Opgave 1.13.3
print("\nOpgave 1.13.1")
konvSum(10)
konvSum(1000)
konvSum(100000)

# Opgave 2.5.3
def mellemSum1(n, m):       # første funktion bruger den fundne formel
    print("Summen er: ", (1/2)*(m*m + m - n*n + n))

def mellemSum2(n, m):       # udregner konkret
    sum = 0
    for k in range(n, m + 1):
        sum = sum + k
    print("Summen er: ", sum)

# Opgave 2.5.4
print("\nOpgave 2.5.4")
mellemSum1(467, 1220)
mellemSum2(467, 1220)
mellemSum1(250, 80000)
mellemSum2(250, 80000)

