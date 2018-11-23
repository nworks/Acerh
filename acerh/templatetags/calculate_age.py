from django.shortcuts import render
from django.utils.dateparse import parse_date
import datetime
from django.utils.timezone import now


from django import template
# Create your views here.



register = template.Library()


@register.simple_tag
def calculate_age(born):
	s = datetime.datetime.strptime(born, "%d-%m-%Y").date()
	today = datetime.date.today()
	try: 
		birthday = s.replace(year=today.year)
	except ValueError: # raised when birth date is February 29 and the current year is not a leap year
		birthday = s.replace(year=today.year, day=s.day-1)
	if birthday > today:
		return today.year - s.year - 1
	else:
		return today.year - s.year


register.filter('age', calculate_age)