import datetime
import os
from wand.image import Image

PDF_SOURCE = '2018_code_calendar.pdf[{}]'
BACKGROUND_SOURCE = 'paper.jpg'


PAGE_OFFSET = 6
MARGIN_LEFT = 100
MARGIN_TOP = 10

current_week = datetime.datetime.now().isocalendar()[1]
OUTPUT = 'turing' + str(current_week) + '.jpg'
page = PAGE_OFFSET + current_week

with Image(filename=PDF_SOURCE.format(page), resolution=160) as calendar:
	with Image(filename=BACKGROUND_SOURCE) as background:
		background.composite_channel('default_channels', calendar, 'blend', MARGIN_LEFT, MARGIN_TOP)
		background.save(filename=OUTPUT)
		
address = os.getcwd() + "/" + OUTPUT 
os.system("osascript -e \"tell application \\\"Finder\\\" to set desktop picture to POSIX file \\\"" + address + "\\\"\"")
