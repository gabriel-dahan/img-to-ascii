# ImgToAscii

### Install and Import the module :

Installing the module :
```bash
~ git clone https://github.com/gabriel-dahan/img-to-ascii/
~ cd img-to-ascii/

# Linux / MacOS
~ python3 -m pip install -U .

# Windows 
~ py -3 -m pip install -U .
```
_Consider using the `--user` parameter if you're not a root/admin user._

Importing the module :
```python
import imgtoascii
```
### Output ASCII to a text file
```python
img = imgtoascii.Img('example.png')
img.to_ascii(out_file = "example.ascii.txt")
```
### Print ASCII
```python
img = imgtoascii.Img('example.png')
text = img.to_ascii()
print(text)
```