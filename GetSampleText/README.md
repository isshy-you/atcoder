# Get Sample from AtCoder

# Features

* download sample input/output text from AtCoder and store text file
* check my code by sample input text
# Requirement (tested enviroment)

* Python 3.10.5
# Installation

```PowerShell
pip install requests
pip install bs4
```

# Usage

py GetSampleText.py [abc|arc] (number) ([a|b|c|d|e|f|g]) (sample_number) (code.py)

example : ABC283 C all input/output 
```PowerShell
py .\GetSxampleText\GetSxampleText.py abc 283 c
py .\GetSxampleText\GetSxampleText.py abc 283 c
```
```PowerShell
py .\GetSxampleText\GetSxampleText.py abc 283 c 0
py .\GetSxampleText\GetSxampleText.py abc 283 c 0
```

example : ABC283 C only No.2
```PowerShell
py .\GetSxampleText\GetSxampleText.py abc 283 c 2
py .\GetSxampleText\GetSxampleText.py abc 283 c 2
```

example : ABC283 C all input/output & check my code
```PowerShell
py .\GetSxampleText\GetSxampleText.py abc 283 c 0 ABC283C.py
py .\GetSxampleText\GetSxampleText.py abc 283 c 0 ABC283C.py
```

example : ABC283 C only No.2 & check my code
```PowerShell
py .\GetSxampleText\GetSxampleText.py abc 283 c 2 ABC283C.py
py .\GetSxampleText\GetSxampleText.py abc 283 c 2 ABC283C.py
```

# Note


# Author

https://github.com/isshy-you
# License

[MIT license](https://en.wikipedia.org/wiki/MIT_License)
