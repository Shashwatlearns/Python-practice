import numpy as np 
ages = np.array([[25, 30, 35, 40, 45, 11, 43, 65],
                [22, 28, 33, 38, 44, 12, 41, 60]])
teenagers =ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 60)]
seniors = ages[ages >= 60] 
evens = ages[ages%2==0]
odds = ages[ages%2!=0]
print(adults)
print(teenagers)
print(seniors)
print(evens)
people =np.where(ages>18,ages,"minor")
print(people)