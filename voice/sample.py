from gtts import gTTS
import vlc
text = "Hello Ashi"
tts = gTTS(text, lang='en')
tts.save("s.mp3")
p = vlc.MediaPlayer("s.mp3")
p.play()
