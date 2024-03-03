# multicarriage
![PyPI - Version](https://img.shields.io/pypi/v/multicarriage)
![Pepy Total Downlods](https://img.shields.io/pepy/dt/multicarriage)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/multicarriage)
![GitHub repo size](https://img.shields.io/github/repo-size/xyzpw/multicarriage)


A Python module designed for writing and updating text on multiple lines using the the carriage return.<br><br>
![multicarriage-preview](https://github.com/xyzpw/multicarriage/assets/76017734/fea181cd-3bbe-4ad5-beec-de6518033a2d)

## Usage
### Previewing Package
```bash
$ python3 -m multicarriage.demo
```
### Importing Package
```python
import multicarriage
```
### Creating Newlines
Creating newlines prevents text from being overwritten.
```python
multicarriage.MultiCarriage.create_newline(2)
```
### Writing to Screen
```python
multicarriage.MultiCarriage.write("first text", 2, clearline=True)
multicarriage.MultiCarriage.write("second text", 1, clearline=True)
```
Setting the `clearline` parameter to true will erase the current line of which the cursor is on, assuring there will be no overwritten text.
### Example of Real Script Usage
Example script that will write and update 3 lines at once.
```python
# example of auto updating epoch and datetime
import multicarriage
import time
import datetime

# creating newlines to avoid overwriting current text
multicarriage.MultiCarriage.create_newline(3)
while True:
    try:
        timestamp = time.time()
        date = datetime.datetime.fromtimestamp(timestamp)
        multicarriage.MultiCarriage.write(f"epoch: {timestamp}", 3, clearline=True, flushtxt=True)
        multicarriage.MultiCarriage.write(f"epoch (s): {timestamp//1}", 2, clearline=True, flushtxt=True)
        multicarriage.MultiCarriage.write(f"datetime string: {date}", 1, clearline=True, flushtxt=True)
        time.sleep(1/10)
    except KeyboardInterrupt:
        raise SystemExit(0)
```
