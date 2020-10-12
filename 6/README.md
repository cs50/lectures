# Lecture 6

6/filter/*.py
6/speller/dictionary.py

## Week 1

1/hello0.c
1/hello0.py

1/hello1.c
1/hello1.py
1/hello2.py
1/hello3.py

1/addition0.c
1/addition*.py

1/division.py

1/conditions.c
1/conditions.py

1/agree.c
1/agree0.py
1/agree1.py

1/meow0.c
1/meow0.py
1/meow1.c
1/meow1.py
1/meow2.c
1/meow2.py
1/meow3.c
1/meow3.py

1/positive.c
1/positive.py

1/mario*.py

1/int.py

## Week 2

2/scores*.py

2/uppercase*.py

2/argv*.py

2/exit.py

## Week 3

3/numbers.py
3/names.py
3/phonebook.py

## Week 4

4/compare.py
4/copy.py
4/swap.py
4/phonebook*.py

## Week 6

6/hogwarts/hogwarts.py
1/agree2.py

6/speech/*
6/faces/detect.py
6/faces/recognize.py
6/qr/qr.py
6/listen/*.py

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
