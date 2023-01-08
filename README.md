# BasicPlots

Quick Python plots with Matplotlib.

## Install

On the command line:
```
python -m build
pip install dist/BasicPlots-0.0.1-py3-none-any.whl
```

## Use

Pick a backend for Matplotlib
`export MPLBACKEND=TkAgg`

Use the plotting functions
```python
import matplotlib.pyplot as plt
import BasicPlots

fig, ax = BasicPlots.barchart(['a', 'b'], [1,2])
fig.show()
```

## Author, Licence

Copyright :copyright: 2023 Alan Tseng

GNU General Public License v3
