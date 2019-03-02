# ID3-Split-Calculator
A decision tree learning calculator for the Iterative Dichotomiser 3 (ID3) algorithm.

By utilizing the [ID3 Algorithm](https://en.wikipedia.org/wiki/ID3_algorithm), the best feature to split on is decided. This program requires to additional libraries outside of the default libraries included with Python (math, csv). Therefore this needs to extra set-up configuration. 
Tested and working on Python 3.7. 

An example of using this calculator is included in exampleUsage.py. 

## Usage:

1. Clone this repo by following the generic instructions found [here](https://help.github.com/en/articles/cloning-a-repository).

2. Import the Library, for example: 
```python 
import ID3Split as ID3
```

3. Use the loadDataSet function to load the data from the csv file:
```python
dataSet = ID3.loadDataSet('data.csv')
```

4. Utilize the built in functions to find Entropy & Information gains

---

Example of using this calculator with data from 'data.csv':

```python
import ID3Split as ID3

dataSet = ID3.loadDataSet('data.csv')
print("numFeatures = " + str(len(dataSet[0][0: -1])))
entropy = ID3.calEntropy(dataSet)
maxvalue = ID3.computeInfoGains(dataSet)
input("Press any key to continue . . . \n")
quit()
```

If run correctly, the following should be the output: 

```
numFeatures = 3
#Tuples = 20
{'C1': 10, 'C0': 10}
p1 = 10/20 = 0.5, log2(p1) = -1.0, p1 x log2(p1) = -0.5
p2 = 10/20 = 0.5, log2(p2) = -1.0, p2 x log2(p2) = -0.5
Info(D) = 1.0

===== Splitting on Gender =====
|D1| / |D| = 10/20 = 0.5
#Tuples = 10
{'C1': 6, 'C0': 4}
p1 = 6/10 = 0.6, log2(p1) = -0.7369655941662062, p1 x log2(p1) = -0.44217935649972373
p2 = 4/10 = 0.4, log2(p2) = -1.3219280948873622, p2 x log2(p2) = -0.5287712379549449
Info(D) = 0.9709505944546686

Info[Gender] (D) = 0.4854752972273343

|D2| / |D| = 10/20 = 0.5
#Tuples = 10
{'C1': 4, 'C0': 6}
p1 = 4/10 = 0.4, log2(p1) = -1.3219280948873622, p1 x log2(p1) = -0.5287712379549449
p2 = 6/10 = 0.6, log2(p2) = -0.7369655941662062, p2 x log2(p2) = -0.44217935649972373
Info(D) = 0.9709505944546686

Info[Gender] (D) = 0.9709505944546686

Gain(Gender) = 1.0 - 0.9709505944546686 = 0.02904940554533142
===== Splitting on Car Type =====
|D1| / |D| = 8/20 = 0.4
#Tuples = 8
{'C0': 8}
p1 = 8/8 = 1.0, log2(p1) = 0.0, p1 x log2(p1) = 0.0
Info(D) = -0.0

Info[Car Type] (D) = 0.0

|D2| / |D| = 8/20 = 0.4
#Tuples = 8
{'C1': 7, 'C0': 1}
p1 = 7/8 = 0.875, log2(p1) = -0.1926450779423959, p1 x log2(p1) = -0.16856444319959643
p2 = 1/8 = 0.125, log2(p2) = -3.0, p2 x log2(p2) = -0.375
Info(D) = 0.5435644431995964

Info[Car Type] (D) = 0.21742577727983858

|D3| / |D| = 4/20 = 0.2
#Tuples = 4
{'C1': 3, 'C0': 1}
p1 = 3/4 = 0.75, log2(p1) = -0.4150374992788438, p1 x log2(p1) = -0.31127812445913283
p2 = 1/4 = 0.25, log2(p2) = -2.0, p2 x log2(p2) = -0.5
Info(D) = 0.8112781244591328

Info[Car Type] (D) = 0.3796814021716651

Gain(Car Type) = 1.0 - 0.3796814021716651 = 0.6203185978283349
===== Splitting on Guitar =====
|D1| / |D| = 2/20 = 0.1
#Tuples = 2
{'C1': 2}
p1 = 2/2 = 1.0, log2(p1) = 0.0, p1 x log2(p1) = 0.0
Info(D) = -0.0

Info[Guitar] (D) = 0.0

|D2| / |D| = 4/20 = 0.2
#Tuples = 4
{'C1': 2, 'C0': 2}
p1 = 2/4 = 0.5, log2(p1) = -1.0, p1 x log2(p1) = -0.5
p2 = 2/4 = 0.5, log2(p2) = -1.0, p2 x log2(p2) = -0.5
Info(D) = 1.0

Info[Guitar] (D) = 0.2

|D3| / |D| = 9/20 = 0.45
#Tuples = 9
{'C1': 5, 'C0': 4}
p1 = 5/9 = 0.5555555555555556, log2(p1) = -0.84799690655495, p1 x log2(p1) = -0.4711093925305278
p2 = 4/9 = 0.4444444444444444, log2(p2) = -1.1699250014423124, p2 x log2(p2) = -0.5199666673076944
Info(D) = 0.9910760598382222

Info[Guitar] (D) = 0.6459842269272

|D4| / |D| = 5/20 = 0.25
#Tuples = 5
{'C1': 1, 'C0': 4}
p1 = 1/5 = 0.2, log2(p1) = -2.321928094887362, p1 x log2(p1) = -0.46438561897747244
p2 = 4/5 = 0.8, log2(p2) = -0.3219280948873623, p2 x log2(p2) = -0.2575424759098898
Info(D) = 0.7219280948873623

Info[Guitar] (D) = 0.8264662506490406

Gain(Guitar) = 1.0 - 0.8264662506490406 = 0.17353374935095944
bestInfoGain = Gain(Car Type) = 0.6203185978283349
bestFeat index = 1
bestFeat name = Car Type
Attribute Car Type is selected as splitting attribute.
Press any key to continue . . . 
```
