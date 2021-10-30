# Gesture-Controlled-Website
A web app made with usage of Django and MediaPipe. Allows to dynamically change dimensions of displayed content with hand gestures.

<p align="center"><img src="https://user-images.githubusercontent.com/90696522/139433833-937e1161-f294-464d-aac1-89a3a5862abb.gif" alt="Website.gif"/>
<br>  
  
  
## Installation
### 1. Clone the project, install [Django](https://docs.djangoproject.com/en/3.2/topics/install/) and dependencies:
```
$ git clone https://github.com/Robxon/Gesture-Controlled-Website
$ cd Gesture_Controlled_Website
$ pip install -r requirements.txt
```
### 2. Run following command:
```  
python manage.py runserver
```
### 3. Open a browser to http://127.0.0.1:8000 (or localhost:8000) and wait for webcam stream to load.

## Usage
The dimensions of displayed webcam stream are dynamically changed based on hand gestures. Application tracks the distance between tips of your thumb and index finger, in vertical direction. Greater distance means bigger dimensions of the element.
  
