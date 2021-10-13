# Installation

```
# https://github.com/numpy/numpy/issues/15947#issuecomment-686159427
brew install cmake dlib openblas
OPENBLAS="$(brew --prefix openblas)" pip3 install numpy
pip3 install face_recognition
```

```
pip3 install pyttsx3
```

```
brew install portaudio
pip3 install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
pip3 install SpeechRecognition
```

```
pip3 install "qrcode[pil]"
```
