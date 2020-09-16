#!/usr/bin/python3
from gtts import gTTS
import subprocess
import speech_recognition as sr

def gtts_speak(text):
	tts = gTTS(text=text,lang='en')
	filename = "voice.wav"
	tts.save(filename)
	play(filename)

def play(audio_file_path):
    subprocess.call(["ffplay", "-nodisp", "-autoexit", audio_file_path])

def audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		text = ""

		try:
			text = r.recognize_google(audio)
			print(text)
		except Exception as e:
			print("Exception" + str(e))

	return text.lower()




if __name__ == '__main__':
	sentence = audio()
	gtts_speak(sentence)