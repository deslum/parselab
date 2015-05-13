# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class MtsItem(Item):
	name 			= Field()
	price 			= Field()
	properties 		= Field()
	isSmart 		= Field()
	os 				= Field()
	processor 		= Field()
	freq 			= Field()
	isSensor 		= Field()
	displayColor 	= Field()
	display 		= Field()
	resolution 		= Field()
	autoRotate 		= Field()
	photo 			= Field()
	pixels 			= Field()
	isFrontend 		= Field()
	isHD 			= Field()
	maxResolution 	= Field()
	fotoLight 		= Field()
	isTwoSim 		= Field()
	is3g 			= Field()
	sms 			= Field()
	operationMemory = Field()
	memoryValue 	= Field()
	isSlot 			= Field()
	memoryCardType 	= Field()
	maxCardMemory 	= Field()
	isWiFi 			= Field()
	isBluetooth 	= Field()
	isUSB 			= Field()
	isHeadfone 		= Field()
	isMultimedia 	= Field()
	isorientation 	= Field()
	isGPS 			= Field()
	phoneType 		= Field()
	width 			= Field()
	length 			= Field()
	height 			= Field()
	ves 			= Field()
	simType 		= Field()
	accumValue 		= Field()
	offTime 		= Field()
	callTime 		= Field()


