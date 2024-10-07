# EncryptIt

## Introduction
EncryptIt is a command line tool for encrypting and decrypting files using AES.
You need Python 3.1X+ version and run in command line:

## Installation

```
git clone https://github.com/Qurclinc/EncryptIt.git
cd EncryptIt
```
And then install dependences
### _For Windows:_
```
pip install -r requirements.txt
```
### _For UNIX systems:_
```
sudo pip3 install -r requirements.txt
```

## Help

You can get info about flags using -h --help flag

### Example for encrypting:
```
python EncryptIt -a encrypt -i test.txt -o test.bin --key $up3r$3cr37K3y
```

### Example for decrypting:
```
python EncryptIt -a decrypt -i test.bin -o decoded.txt --key $up3r$3cr37K3y
```

### Generating keys
You can also use _keygen.py_ for generating 16 bytes size key and do not use flag `--key`. The byte-string from file `key` will be used instead. To do this, all you need is to run next command:
```
python keygen.py
```
