from django.contrib.auth.models import User
from main.services import check_admin, get_user_id_by_username
from main.authentication_backend import authentication
from typing import Union
import logging


class PasswordValidator:
	"""Main password validator"""


	def __init__(self, password: str, user: str):
		"""Inits all the variables"""

		self.password = password
		self.user = user


	def check_password_history(self) -> bool:
		"""Checks whether user has passed not old password"""

		if User.objects.filter(
			username=self.user, 
			password=self.password
		):
			return False
		return True


	def check_password_length(self) -> bool:
		"""Checks whether pass_length is not less than 8"""

		if len(self.password) < 8:
			return False
		return True


	def check_password_capital_letter(self) -> bool:
		"""Checks whether pass starts with capital letter"""

		if not self.password[0].isupper():
			return False
		return True
		

	def validate(self) -> bool:
		"""Validates password"""

		if self.check_password_history():
			if self.check_password_length():
				if self.check_password_capital_letter():
					return (True, "Ok")
				return (False, "Пароль должен начинаться с большой букви")
			return (False, "Пароль должен состоять не менее чем из 8 символов")
		return (False, "Пароль не может быть анологичным установленому")


class LoginUserValidator:
	"""Checks user to login"""


	def __init__(self, username):
		"""Inits username for the futher actions"""

		self.username = username


	def is_admin(self) -> bool:
		"""Checks whether user is admin not to go to other steps of validation"""

		if check_admin(self.username):
			return True
		return False


	def check_user_id(self) -> Union[bool, int]:
		"""Checks whether user's id is valid"""

		if user_id := get_user_id_by_username(self.username):
			return user_id
		return False

		
	def validate_user__check_on(self, request: object) -> object:
		"""Starts validation for permanent login"""

		if not self.is_admin():
			return authentication(username=self.username, password=request.POST["password"])
		return authentication(username=self.username, admin=True)


	def validate_user__check_off(self) -> Union[bool, int, object]:
		"""Starts validation for temperate login"""

		if not self.is_admin():
			if user_id := self.check_user_id():
				return user_id
			return False
		return authentication(username=self.username, admin=True)
