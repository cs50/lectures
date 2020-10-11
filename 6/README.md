# Lecture 6

6/filter/*.py
6/speller/dictionary.py

## Week 1

hello.c
hello.py

string.c
string*.py

int.c
int*.py

conditions.c
conditions.py

agree.c
agree0.py
agree1.py

cough*.py

positive.c
positive.py

mario*.py

overflow.py

## Week 2

scores2c.c
scores*.py

string2.c
string*.py

uppercase2.c
uppercase.py

argv1.c
argv*.py

exit.c
exit*.py

## Week 3

names.c
names.py

phonebook1.c
phonebook.py

## Week 4

compare4.c
compare.py

copy3.c
copy.py

swap.c
swap.py

phonebook.c
phonebook*.py

## Week 6

agree2.py

hogwarts
ai
faces
qr

### Installation

```
# https://github.com/python-pillow/Pillow/issues/3438#issuecomment-555019284
export CPATH=`xcrun --show-sdk-path`/usr/include
pip3 install Pillow
```

```
agree2.py
```

```
# https://github.com/numpy/numpy/issues/15947#issuecomment-686159427
brew install cmake dlib openblas
OPENBLAS="$(brew --prefix openblas)" pip3 install numpy
pip3 install face_recognition
```

```
brew install portaudio
pip3 install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
pip3 install SpeechRecognition
```

```
pip3 install "qrcode[pil]"
```
