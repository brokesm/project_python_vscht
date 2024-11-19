start = 1
maxLimit = 70616204741131

##kazde cislo, ktore nie je prvocislo dokazem rozlozit do sucinu prvocisel
def decompositionToPrimeNumbers(start,maxLimit): 
  ##maxLimit je na začiatku zadané číslo a postupne sa bude zmenšovať, keď dojde k úspešnému deleniu. Preto rekurzia
    for number in range(start,maxLimit+1): ##pričítanie 1 je preto, aby cyklus bežal od jednotky po hornú hranicu vrátane
      if maxLimit % number == 0 and number != 1:
        maxLimit = maxLimit / number
        start = 1 ##rovnako aj spodná hranica rangeu sa musí reštartovať po každom úspešnom delení
        print(number) ##vyprintí postupne všetky prvočíselné delitele, posledné číslo je žiadaný výsledok
        decompositionToPrimeNumbers(start,int(maxLimit))
        break

decompositionToPrimeNumbers(start,maxLimit)
