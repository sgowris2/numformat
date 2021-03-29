# numformat

Numformat is a library that helps you easily format number-like objects __(int, float, decimal.Decimal, str)__ in a way that is consistent with scientific and engineering practices.

It has options to convert number-like objects to strings with different notations while allowing control over [Significant Figures](https://en.wikipedia.org/wiki/Significant_figures), [Precision](https://simple.wikipedia.org/wiki/Precision_(numbers)), and output string length.

#### Usage examples:

```python:
import numformat as nf

# Convert to scientific notation
nf.sciformat(103000000)
>> '1.03e+08'

# Convert to engineering notation
nf.enggformat("103000000")
>> '103E+6'

# Auto-format with default options
nf.autoformat(103000000.0)
>> '103000000.0'

# Auto-format and use a maximum of 5 significant figures
nf.autoformat(103000.000, max_sig_figs=5)
>> '103000'

# Auto-format and use a maximum of 2 significant figures
nf.autoformat("10300.00", max_sig_figs=2)
>> '10000'

# Auto-format to a string that has a maximum length of 6 characters
nf.autoformat(103000000, max_length=6)
>> '1e+08'

# Auto-format to a string that has a maximum length of 8 characters
nf.autoformat(103100000, max_length=8, preserve_sig_figs=False)
>> '1.03e+08'

# Auto-format to a string that has a maximum length of 8 characters but also preserve all significant figures.
nf.autoformat(103100000, max_length=8, preserve_sig_figs=True)
>> '103.1E+6'

# Auto-format to a string with a maximum length of 6 characters but don't allow scientific notation
nf.autoformat(103000000, max_length=6, allow_scientific_notation=False)
>> '103E+6'

# Auto-format to a string with a maximum length of 6 characters but don't allow scientific or engineering notation. 
# Conditions cannot be met, therefore, it returns the number in standard notation.
nf.autoformat(103000000, max_length=6, allow_scientific_notation=False, allow_engineering_notation=False)
>> '103000000'

# Auto-format to a string with a maximum length of 6 characters but don't allow scientific or engineering notation. 
# Conditions cannot be met, and strict = True, therefore, returns an error.
nf.autoformat(103000000, max_length=6, allow_scientific_notation=False, allow_engineering_notation=False, strict=True)
>> ValueError: Could not represent the input within 6 characters.

