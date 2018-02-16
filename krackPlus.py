#!/bin/python

#NOTES:
## Sultan is one way to run bash commands simply: https://github.com/aeroxis/sultan

# Development notes:
## all of this is experimental. Feel free to change everything 

# Kivy framework is used for GUI
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label 
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

## TEMPORARY
red = [1,0,0,1]
green = [0,1,0,1]


# Subprocess is used to run bash commands
import subprocess


# Defines the instance of the widget.
class KrackWidget(Widget):
	pass # used to keep a class valid even though it doesn't contain anything



class DisplayRows(GridLayout):
    def __init__(self, **kwargs):
        self.cols = 2
        self.row = 2

# 
def callback(instance):
    print('The button <%s> is being pressed' % instance.text)

# Setup: installs necessary software and sets up a test network 
class ClientScanSetup(Widget):	
	btn1 = Button(text='Check whether device is vulnerable')
	btn1.bind(on_press=callback)	
	#Should use subprocess to run a bash script

class KrackPlusApp(App):
	def build(self):
		Window.size = (820, 580)	
		#TODO should be a nice gray or something
		Window.clearcolor = (.12,.12,.12,.12)
		DisplayRows()
		ClientScanSetup()
				


if __name__ == '__main__':
	KrackPlusApp().run()