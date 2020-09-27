from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from main.models import Record, ModificatedUser, Review, Service, DoctorInfo, VisitImage, SocialLoginSettings
from typing import Union,Dict
from django.utils.translation import gettext_lazy as _

import random
import datetime
import pytz


def get_username_by_email(email) -> Union[str,None]:
	"""Returns user's username got by email"""

	try:
		return User.objects.get(email=email).username
	except ObjectDoesNotExist:
		return None

def create_user_id() -> int:
	"""Returns a random special user_id to check whether user is authentificated"""

	number = ["1", "2", "3", "4", "5", "6", "7", "8"]
	random.shuffle(number)
	user_id = "".join(number)
	all_user_ids = [elem.number_of_user for elem in ModificatedUser.objects.all()]

	return int(user_id) if user_id not in all_user_ids else create_user_id()

def check_admin(username: str) -> bool:
	"""Check whether user is admin"""

	user = User.objects.get(username=username)
	return True if user.is_staff else False

def get_users_records(request) -> object:
	"""Returns user's records"""

	try:
		user = ModificatedUser.objects.select_related("user").get(number_of_user=request.COOKIES["*1%"]).user
	except (ObjectDoesNotExist, KeyError):
		user = User.objects.get(username=request.user.username)
	return Record.objects.filter(author=user.first_name)


def get_user_id_by_username(username: str) -> Union[object, None]:
	"""Returns a user_id to save it to cookies"""

	try:
		user_instanse = User.objects.get(username=username)
		query = ModificatedUser.objects.select_related("user").get(user=user_instanse)
		return query.number_of_user
	except ObjectDoesNotExist:
		return None

def get_email(request: object) -> str:
	"""Returns user's email"""

	try:
		return ModificatedUser.objects.select_related("user").get(number_of_user=request.COOKIES["*1%"]).user.email
	except KeyError:
		return request.user.email

def get_last_name(request: object) -> str:
	"""Returns user's last_name"""

	try:
		return ModificatedUser.objects.select_related("user").get(number_of_user=request.COOKIES["*1%"]).user.last_name
	except KeyError:
		return None

def get_user(request) -> str:
	"""Returns user's username"""

	try:
		return ModificatedUser.objects.select_related("user").get(number_of_user=request.COOKIES["*1%"]).user.username
	except KeyError:
		return request.user.username


def get_first_name(request: object) -> str:
	"""Retuns user's first_name"""

	try:
		return ModificatedUser.objects.select_related("user").get(number_of_user=request.COOKIES["*1%"]).user.first_name
	except KeyError:
		return None

def encode_phone_number(number: Union[int, str, None]) -> str:
	"""Returns already encoded user's number"""

	if number:
		encoded_number = [digit if len(number) - index <= 4 else "*" for index,digit in enumerate(str(number))]
		return "".join(encoded_number)
	return None

def get_user_phone_number(request) -> str or None:
	"""Returns response from the 'encoded_phone_number' func"""

	try:
		user = User.objects.get(username=get_user(request))
	except (ObjectDoesNotExist, KeyError):
		try:
			user = User.objects.get(username=request.user.username)
		except ObjectDoesNotExist:
			return None
	try:
		phone_number = ModificatedUser.objects.get(user=user).number
		return encode_phone_number(phone_number)
	except ObjectDoesNotExist:
		return None


def made_records(request) -> Union[bool,None]:
	"""Checks whether user has already made any records"""


	try:
		return ModificatedUser.objects.get(number_of_user=request.COOKIES["*1%"]).made_records
	except KeyError:
		user = User.objects.get(username=request.user.username)
		try:
			return ModificatedUser.objects.get(user=user).made_records
		except ObjectDoesNotExist:
			return None


def get_work_date() -> int:
	"""Checks whether now time is in a gap of work time"""

	now = datetime.datetime.today()
	work_time = {
		"9:00":datetime.datetime(
			datetime.datetime.today().year,
			datetime.datetime.today().month,
			datetime.datetime.today().day,
			9,0,0,0
		),
		"12:00":datetime.datetime(
			datetime.datetime.today().year,
			datetime.datetime.today().month,
			datetime.datetime.today().day,
			12,0,0,0
		),
		"13:15":datetime.datetime(
			datetime.datetime.today().year,
			datetime.datetime.today().month,
			datetime.datetime.today().day,
			13,15,0,0
		),
		"16:15":datetime.datetime(
			datetime.datetime.today().year,
			datetime.datetime.today().month,
			datetime.datetime.today().day,
			16,15,0,0
		)}
	if now < work_time["12:00"] and now > work_time["9:00"]:
		return (True, work_time["12:00"].strftime("%H:%M"))
	elif now < work_time["16:15"] and now > work_time["13:15"]:
		return (True, work_time["16:15"].strftime("%H:%M"))
	time_stamps = [(work_time[key] - now,key) for key in work_time.keys()]
	min_elem = min(time_stamps)
	return (False,work_time[min_elem[1]].strftime("%H:%M"))


def get_first_service() -> object:
	"""Returns the first service"""

	return Service.objects.first()


def get_newest_services() -> list:
	"""Returns all the services except the first one"""

	today = datetime.datetime.now()
	try:
		range_date = datetime.datetime(today.year, today.month, today.day-7, 0, 0, 0, tzinfo=pytz.UTC)
	except ValueError:
		days_in_month = {
			1:31,
			2:28 if today.year % 4 != 0 else 29,
			3:31,
			4:30,
			5:31,
			6:30,
			7:31,
			8:31,
			9:30,
			10:31,
			11:30,
			12:31
		}
		range_date = datetime.datetime(today.year, today.month-1, days_in_month[today.month-1]-7, 0, 0, 0, tzinfo=pytz.UTC)
	return Service.objects.filter(made_time__gte=range_date, pk__gt=Service.objects.first().pk)


def get_service_info(pk) -> object:
	"""Returns the exact service gotten by pk"""

	return Service.objects.get(pk=pk)


def get_info_about_doctor(request: object) -> object:
	"""Returns the info about doctor in german or in russian"""

	if request.LANGUAGE_CODE == "ru":
		try:
			return DoctorInfo.objects.first().about_text
		except (ObjectDoesNotExist, AttributeError):
			try:
				return DoctorInfo.objects.first().about_text_de
			except (ObjectDoesNotExist, AttributeError):
				return "Информация не добавлена"
	else:	
		try:
			return DoctorInfo.objects.first().about_text_de
		except (ObjectDoesNotExist, AttributeError):
			try:
				return DoctorInfo.objects.first().about_text
			except (ObjectDoesNotExist, AttributeError):
				return "Информация не добавлена"


def get_all_reviews() -> object:
	"""Returns all the reviews"""

	return Review.objects.all()

def get_all_records() -> object:
	"""Returns all the records"""

	return Record.objects.all()


def get_first_visit_image() -> object:
	"""Returns the first visit image"""

	return VisitImage.objects.first()
	

def get_all_visit_images() -> object:
	"""Returns all the visit images except the first one"""

	try:
		return VisitImage.objects.filter(pk__gt=VisitImage.objects.first().pk)
	except AttributeError:
		return None
	

def do_logout__cookie(request: object) -> None:
	"""Processes logout process"""

	try:
		user = ModificatedUser.objects.get(number_of_user=request.COOKIES["*1%"])
	except KeyError:
		return False
	return True
	

def get_user_data(request):
	"""Returns all the data about regestrated user"""

	try:
		data_list = [
			("Email", get_email(request.COOKIES["*1%"])),
			(_("Логин"), get_user(request.COOKIES["*1%"])),
			(_("Имя"), get_first_name(request.COOKIES["*1%"])),
			(_("Фамилия"), get_last_name(request.COOKIES["*1%"])),
			(_("Номер телефона"), get_user_phone_number(request=request))
		]
	except KeyError:
		data_list = [
			("Email", request.user.email),
			(_("Логин"), request.user.username),
			(_("Имя"), request.user.first_name if request.user.first_name != "" else None),
			(_("Фамилия"), request.user.last_name if request.user.last_name != "" else None),
			(_("Номер телефона"), get_user_phone_number(request=request))
		]
	
	return data_list


def get_all_made_orders() -> int:
	"""Return the number of all existing records"""

	return Record.objects.filter(status=True).count()


def get_all_auth_service_status() -> list:
	"""Returns a list with all the auth-services"""

	return SocialLoginSettings.objects.all()


class SplitedQuerySet:

	def _create_separated_query_set(self, model: object) -> None:
		"""
		Separates query_set on two parts
		(consists of len of the query_set)
		"""

		self.query_set = model.objects.all()
		self.first_part = int(len(self.query_set) / 2)
		self.second_part = len(self.query_set) - self.first_part

	def _create_first_list(self) -> object:
		"""Returns parts of the first query_set"""

		if self.first_part == self.second_part:
			for article in range(0, self.first_part):
				yield self.query_set[article]
		else:
			for article in range(0, self.first_part + 1):
				yield self.query_set[article]

	def _create_second_list(self) -> object:
		"""Returns parts of the second query_set"""

		for article in range(self.second_part, len(self.query_set)):
			yield self.query_set[article]

	def _get_first_list(self) -> None:
		"""Creates the first separated list"""

		self.first = self._create_first_list()

	def _get_second_list(self) -> None:
		"""Creates the second separated list"""

		self.second = self._create_second_list()

	def _first_gen(self) -> Union[object,None]:
		"""Returns the parts of the first generator"""

		try:
			return next(self.first)
		except StopIteration:
			pass

	def _second_gen(self) -> Union[object,None]:
		"""Returns the parts of the second generator"""

		try:
			return next(self.second)
		except StopIteration:
			pass

	def _get_finall_list(self) -> list:
		"""Returns the finall list of separated query_set"""

		return [
				(self._first_gen(), self._second_gen())
				for _ in range(0, self.second_part)
			]


	def get_list(self, model) -> object:
		"""Does all the methods to return the finall list"""

		self._create_separated_query_set(model)
		self._create_first_list()
		self._create_second_list()
		self._get_first_list()
		self._get_second_list()
		return self._get_finall_list()
