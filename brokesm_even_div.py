decompositionArr = []
nestedArray = []
start = 2

##kazde cislo, rozlozim do sucinu prvocisel
def decompositionToPrimeNumbers(start,maxLimit): 
    for number in range(start,maxLimit + 1): ##start zacina na cisle 2, inak by dochádzalo k ukončení cyklu bez vrátenia hodnoty, ktoré python vyrieši vrátením None
      if maxLimit % number == 0:
        maxLimit = maxLimit / number
        start = 2 
        decompositionArr.insert(-1,number) ##rozklady jednotlivych cisel od 2 do 30 su ulozene v array
        decompositionToPrimeNumbers(start,int(maxLimit))
        return decompositionArr
      
for intervalElement in range(2,31):
    nestedArray.insert(-1,decompositionToPrimeNumbers(start,intervalElement)) ##rozklady cisel sa ulozia do nested array
    decompositionArr = []


occurrenceArray = []
summ = 1
for number in range(1,31):
    for array in nestedArray: ##loop cez vsetky arraye a pocitanie vyskytu jednotlivych cisel od 1 do 30
       countNumber = array.count(number)
       occurrenceArray.insert(-1,countNumber) ##vlozenie vyskytu konkretneho cisla napriec vsetkymi arrays
    if max(occurrenceArray) != 0:
        summ = summ * number**(max(occurrenceArray)) ##hladanie najmenšieho spolocneho nasobku
    occurrenceArray = []

print(summ)
      
      



