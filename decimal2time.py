#! /usr/bin/env python
#-*- coding: utf-8 -*-
# Jonathan Liuti for Vox Teneo
# Copyright (C) 2011 Jonathan Liuti
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import datetime

class DecimalToTime(object):
	"""This class handles decimal number to time conversion"""
	def __init__(self):
		print("Welcome to decimal to time script.")	
	
	def convert_decimal_to_time(self, decimal):
		hour = int(decimal)
		minute = int((decimal-hour) * 60)
		return datetime.time(hour,minute)

	def ask_for_value(self):
		"""Helper to display input the decimal value"""
		while True:
			try:				
				choice = raw_input("Please enter a decimal value or 'Q' to exit: ")
				if (choice.upper() == "Q"):
					break
				choice = float(choice)
				print self.convert_decimal_to_time(choice)
				
			except:
				print('Error: This is not a valid decimal value.')
obj= DecimalToTime()
obj.ask_for_value()

