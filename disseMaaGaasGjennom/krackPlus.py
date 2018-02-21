#!/bin/python

#NOTES:
## Sultan is one way to run bash commands simply: https://github.com/aeroxis/sultan

# Development notes:
## all of this is experimental. Feel free to change everything 

### IMPORTS ###

# Kivy framework is used for GUI
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label 
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

# Subprocess is used to run bash commands
import subprocess

# Defines the instance of the widget.
class KrackWidget(Widget):
	pass # used to keep a class valid even though it doesn't contain anything

# 
def callback(instance):
	print('Processing...')
	subprocess.call("./prepareClientScan.sh")

# Setup: installs necessary software and sets up a test network 
class ClientScanSetup(Widget):	
	vulnCheckButton = Button(text='Check whether device is vulnerable')
	vulnCheckButton.bind(on_press=callback)	

class KrackPlusApp(App):
	def build(self):
		Window.size = (820, 580)	
		#TODO should be a nice gray or something
		Window.clearcolor = (.12,.12,.12,.12)
		#TODO btn1 should be removed eventually
		btn1 = Button(text='Click to check whether device is vulnerable')
		btn1.bind(on_press=callback)	
		return btn1

				


if __name__ == '__main__':
	KrackPlusApp().run()