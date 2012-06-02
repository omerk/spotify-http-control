import commands
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "yo."

@app.route("/playpause")
def playpause():
	return sendkey("space")

@app.route("/next")
def next():
	return sendkey("Ctrl+Right")

@app.route("/prev")
def prev():
	return sendkey("Ctrl+Left")

@app.route("/vol_up")
def vol_up():
	return sendkey("Ctrl+Up")

@app.route("/vol_down")
def vol_down():
	return sendkey("Ctrl+Down")

# this key combo doesn't seem to work?
@app.route("/mute")
def mute():
	return sendkey("Ctrl+Shift+Down")

def sendkey(key):
	windows = commands.getstatusoutput("xdotool search --class Spotify")
	for window in windows[1].split("\n"):
		res = commands.getstatusoutput("xdotool key --clearmodifiers --window " + window + " " + key)

	#FIXME: add error handling
	return "ok"

if __name__ == "__main__":
	app.debug = True
	app.run()

