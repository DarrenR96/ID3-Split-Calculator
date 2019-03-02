# ID3-Split-Calculator
A decision tree learning calculator for the Iterative Dichotomiser 3 (ID3) algorithm.

By utilizing the [ID3 Algorithm](https://en.wikipedia.org/wiki/ID3_algorithm), the best feature to split on is decided. This program requires to additional libraries outside of the default libraries included with Python. 
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

