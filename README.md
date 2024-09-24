<h1>Three Random Words</h1>
<br>
<img src='Design/images and backgrounds/Design layouts/App_Icon.jpg' width='300px' height='300px'>

<h2>Context</h2>

Three Random Words is an idea which spurred when I was at home during the summer holidays.

My family and I were collecting all the devices in the home, to see if we could either use, sell or recycle them. 
We were cleaning up out things from my room, when I was purging old devices my family and I had to donate, 
and we got to talking about how would be the best way to secure the device without it being too complicated, and that's where the idea was born.

Three Random Words is an emcompassing login system, which utilises 4 types of user authentication:

* [**Username and password**](#username-and-password)
* [**PIN**](#pin)
* [**Face detection and verification**](#face-detection-and-verification)
* [**Voice detection and verification**](#voice-detection-and-verification)

<h2>How does it work?</h2>
Depending on how the user wants to either register or login, there are 2 path to choose.

If the user is going to use the app for the first time, then Three Random Words will ask the user to register. Else, you can login the system by username and password, PIN, use the camera of your device and login or a say a phrase so it recognises you.

<h3>Registering</h3>
The app will provide a new username, password, PIN and store a picture and a voice recording of the user, but only for the first time, so it can be identified should the user logins again.

<h3>Ways to login</h3>

<h4>Username and password</h4>
Here the user enters their username and password, if they have already registered with the app.

<h4>PIN</h4>
A PIN is a form of authenticating that can be used when the user is want to access the device quickly and does not want to spend too much time logging in. 
The PIN is int this case 

<h4>Face detection and verification</h4>
I used [DeepFace](https://github.com/serengil/deepface) for the face recognition and [OpenCV](https://github.com/opencv/opencv)


<h4>Voice detection and verfication</h4>
I used [SpeechRecognition](https://github.com/Uberi/speech_recognition) for the voice detection and recognition.

It uses PYQT5 as GUI, mysql as database support 
