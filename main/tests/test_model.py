from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from main.models import (Record,
						ModificatedUser,
						Review,
						Service)


class ReviewModelTest(TestCase):
	"""Test to check all the functionality of ReviewModel"""    

	@classmethod
	def setUpTestData(cls) -> None:

		"""Creates all important data to run all the other tests
		-> Creates new User entry with such credentials as 'Test' and 'test1234'
		-> Creates new Review entry with the author related with previously made user instanse
		
		"""

		new_user = User.objects.create_user(username="Test",password="test1234").save()
		cls.user = User.objects.get(username="Test")

		record = Review.objects.create(
			author=cls.user,
			review="It is a test",
			mark=5,
		).save()

		cls.record = Review.objects.get(author=cls.user)


	def test_author_field(self) -> None:
		"""Checks whether the author of previously made review is equal to previously made user object"""

		self.assertEqual(self.record.author.username,self.user.username)
		

	def test_review_field(self):
		"""Checks whether the max length of review field is 400 and its verbose name is 'Отзыв'"""

		self.assertEqual(self.record._meta.get_field("review").max_length,400)
		self.assertEqual(self.record._meta.get_field("review").verbose_name,"Отзыв")


	def test_mark_field(self):
		"""Checks whether the verbose name of mark field is 'Оценка'"""

		self.assertEqual(self.record._meta.get_field("mark").verbose_name,"Оценка")


	def test_db_table(self):
		"""Checks whether the db_table name is 'reviews'"""

		self.assertEqual(self.record._meta.db_table,"reviews")


	def test_verbose_name_and_verbose_name(self):
		"""Checks whether the verbose name is 'Отзыв' and the verbose_name_plural is 'Отзывы'"""

		self.assertEqual(self.record._meta.verbose_name,"Отзыв")
		self.assertEqual(self.record._meta.verbose_name_plural,"Отзывы")


class RecordModelTest(TestCase):
	"""This test checks all the functionality of RecordModel"""

	@classmethod
	def setUpTestData(cls):
		"""Prepares all the important data for the futher testing
		-> Creates new User object with such credentials as 'Test' and 'test1234'
		-> Creates new ModificatedUser objects with the additional info about user
		-> Creates new Record object 

		"""

		User.objects.create_user(username="Test",password="test1234").save()
		cls.user = User.objects.get(username="Test")
		ModificatedUser.objects.create(user=cls.user,number=1234567890,number_of_user=12345678).save()
		cls.phone = ModificatedUser.objects.get(user=cls.user)
		new_record = Record.objects.create(
				author = User.objects.get(username="Test"),
				name = "Test",
				description = "It is a test",
				phone = ModificatedUser.objects.get(user=cls.user),    
		).save()
		cls.record = Record.objects.get(author=User.objects.get(username="Test"))
		
		
	def test_author_field(self):
		"""Checks whether the author of the record is equal to the User objects"""

		self.assertEqual(self.record.author.username,self.user.username)


	def test_phone_field(self):
		"""Checks whethe the user's phone number is equal to the ModificatedUser object"""

		self.assertEqual(self.record.phone,self.phone)


	def test_name_field(self):
		"""Checks whether max_length of the name field is 30"""

		self.assertEqual(self.record._meta.get_field("name").max_length,30)
		

	def test_description_field(self):
		"""Checks whether max_length of the description field is 200"""

		self.assertEqual(self.record._meta.get_field("description").max_length,200)


	def test_status_field(self):
		"""Checks whether the default statement of the status field is False"""

		self.assertFalse(self.record._meta.get_field("status").default)


	def test_seen_field(self):
		"""Checks whether the default statement of the seen field is False"""

		self.assertFalse(self.record._meta.get_field("seen").default)


	def test_str_and_repr(self):
		"""Checks whether the __str__ and __repr__ statements are equal to the name field"""

		self.assertEqual(self.record.name,self.record.__str__())
		self.assertEqual(self.record.name,self.record.__repr__())


	def test_db_tablename(self):
		"""Checks whether the db_table name is 'records'"""

		self.assertEqual(self.record._meta.db_table,"records")


	def test_verbose_name_and_verbose_name_plural(self):
		"""Checks whether the verbose name is 'Запись' and verbose_name_plural is 'Записи'"""

		self.assertEqual(self.record._meta.verbose_name,"Запись")
		self.assertEqual(self.record._meta.verbose_name_plural,"Записи")


class ServiceModelTest(TestCase):
	"""Test for the checking all the functionality of Service model"""

	@classmethod
	def setUpTestData(cls):
		"""Does all the preparing actions
		-> Creates new Service objects
		"""

		new_service = Service.objects.create(
				name = "Test",
				description = "It is a test",
				price = 10000,
				currency = "EUR",
		)
		new_service.save()
		cls.service = Service.objects.get(name="Test")


	def test_name_field(self):
		"""Tests the functionality of name field
		-> Field type
		-> max_length
		-> verbose_name
		"""

		self.assertEqual(self.service._meta.get_field("name").get_internal_type(),"CharField")
		self.assertEqual(self.service._meta.get_field("name").max_length,200)
		self.assertEqual(self.service._meta.get_field("name").verbose_name,"Название услуги")
		

	
	def test_description_field(self):
		"""Tests the functionality of description field
		-> Field type
		-> max_length
		-> verbose_name
		-> default value
		"""

		self.assertEqual(self.service._meta.get_field("description").get_internal_type(),"CharField")
		self.assertEqual(self.service._meta.get_field("description").max_length,400)
		self.assertEqual(self.service._meta.get_field("description").verbose_name,"Описание")
		self.assertEqual(self.service._meta.get_field("description").default,"-")

	def test_price_field(self):
		"""Tests the functionality of price field
		-> Field type
		-> verbose_name
		"""

		self.assertEqual(self.service._meta.get_field("price").get_internal_type(),"IntegerField")
		self.assertEqual(self.service._meta.get_field("price").verbose_name,"Стоимость услуги")
	
	def test_currency_field(self):
		"""Tests the functionality of currency field
		-> Field type
		-> max_length
		-> verbose_name
		"""

		self.assertEqual(self.service._meta.get_field("currency").get_internal_type(),"CharField")
		self.assertEqual(self.service._meta.get_field("currency").max_length,10)
		self.assertEqual(self.service._meta.get_field("currency").verbose_name,"Валюта")


	def test_str_repr_methods(self):
		"""Tests __str__ and __repr__ methods"""

		self.assertEqual(self.service.__str__(),self.service.name)
		self.assertEqual(self.service.__repr__(),self.service.__str__())

	def test_absolute_url(self):
		"""Tests the functionality of get_absolute_url method"""

		self.assertEqual(self.service.get_absolute_url(),reverse("ServiceInfo",kwargs={"pk":self.service.pk}))


	def test_db_table(self):
		"""Checks the value of db_table attribute"""

		self.assertEqual(self.service._meta.db_table,"services")
		
	def test_verbose_name_and_verbose_plural_name(self):
		"""Checks the values of verbose_name and verbose_name_plural attributes"""

		self.assertEqual(self.service._meta.verbose_name, "Услуга")
		self.assertEqual(self.service._meta.verbose_name_plural, "Услуги")


class ModificatedUserTest(TestCase):
	"""Tests for the checking of the functionality of ModificatedUser model"""

	@classmethod
	def setUpTestData(cls):
		"""Does all the preparing actions for the futher tests
		-> Creates new User object with such credentials as 'Test' and 'test1234'
		-> Creates new ModificatedUser object with OneToOne field related to previously made User object

		"""

		new_user = User.objects.create_user(
			username="Test",password="test1234"
			)
		new_user.save()
		moduser = ModificatedUser.objects.create(
			user=User.objects.get(username="Test"),
			number=1234567890,
			number_of_user=12345678
			)
		moduser.save()
		cls.user = ModificatedUser.objects.get(number=1234567890)

	
	def test_user_field(self):
		"""Tests whether the type of user field is OneToOne"""

		self.assertTrue(self.user._meta.get_field("user").one_to_one)
		
	
	def test_number_field(self):
		"""Tests such functionality as:
		-> The type of the field
		-> blank value
		-> unique value
		-> verbose_name value
		"""

		self.assertEqual(self.user._meta.get_field("number").get_internal_type(),"CharField")
		self.assertTrue(self.user._meta.get_field("number").blank)
		self.assertTrue(self.user._meta.get_field("number").unique)
		self.assertEqual(self.user._meta.get_field("number").verbose_name,"Номер телефона")

	
	def test_number_of_user_field(self):
		"""Tests such functionality as:
		-> The type of the field
		-> default value
		-> unique value
		-> verbose_name value
 		"""

		self.assertEqual(self.user._meta.get_field("number_of_user").get_internal_type(),"IntegerField")
		self.assertFalse(self.user._meta.get_field("number_of_user").default)
		self.assertEqual(self.user._meta.get_field("number_of_user").verbose_name,"Номер пользователя")

	
	def test_made_records_field(self):
		"""Tests such functionality as:
		-> The type of the field
		-> default value
		-> verbose_name value
 		"""

		self.assertEqual(self.user._meta.get_field("made_records").get_internal_type(),"BooleanField")
		self.assertFalse(self.user._meta.get_field("made_records").default)
		self.assertEqual(self.user._meta.get_field("made_records").verbose_name,"Делал ли записи")


	def test_str_repr(self):
		"""Tests __str__ and __repr__ methods"""

		self.assertEqual(self.user.__str__(),"12345678")
		self.assertEqual(self.user.__repr__(),self.user.__str__())

	
	def test_db_table_name(self):
		"""Tests the value of db_table attribute"""

		self.assertEqual(self.user._meta.db_table,"moduser")


	def test_verbose_name_and_verbose_plural_name(self):
		"""Tests the value of verbose_name and verbose_name_plural attributes"""

		self.assertEqual(self.user._meta.verbose_name,"Дополнительная информация")
		self.assertEqual(self.user._meta.verbose_name_plural,self.user._meta.verbose_name)
