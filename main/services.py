from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from main.models import Record, ModificatedUser, Review

from typing import Union,Dict
import random
import datetime


def get_username_by_email(**credentials: Dict[str,object]) -> Union[str,None]:
    """Returns user's username got by email"""
    
    try:
        user = User.objects.get(email=credentials["email"])    
        return user.username
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

def get_users_records(**kwargs: dict) -> object:
    """Returns user's records"""
    
    try:
        user = User.objects.get(username=kwargs["request"].user.username)
        return Record.objects.filter(author=user.first_name)
    except KeyError:
        user = ModificatedUser.objects.select_related("user").get(number_of_user=kwargs["cookies"]).user
        return Record.objects.filter(author=user.first_name)


def get_user_id_by_username(username: str) -> Union[object, None]:
    """Returns a user_id to save it to cookies"""

    try:
        user_instanse = User.objects.get(username=username)
        query = ModificatedUser.objects.select_related("user").get(user=user_instanse)
        return query.number_of_user
    except ObjectDoesNotExist:
        return None
    
def get_email(cookie: int) -> str:
    """Returns user's email"""

    user_id = ModificatedUser.objects.get(number_of_user=cookie)
    return user_id.user.email

def get_last_name(cookie: int) -> str:
    """Returns user's last_name"""

    user_id = ModificatedUser.objects.get(number_of_user=cookie)
    return user_id.user.last_name

def get_user(**kwargs) -> str:
    """Returns user's username"""

    if kwargs.get("cookie"):
        return ModificatedUser.objects.get(number_of_user=kwargs["cookie"]).user.username
    elif kwargs.get("request"):
        if kwargs["request"].COOKIES.get("*1%"):
            return ModificatedUser.objects.get(number_of_user=kwargs["request"].COOKIES["*1%"]).user.username
        else:
            if username := kwargs["request"].user.username:
                return username
            return None

def get_first_name(cookie: int) -> str:
    """Retuns user's first_name"""

    user_id = ModificatedUser.objects.get(number_of_user=cookie)
    return user_id.user.first_name


def encode_phone_number(number: Union[int, str]) -> str:
    """Returns already encoded user's number"""

    encoded_number = [digit if len(number) - index <= 4 else "*" for index,digit in enumerate(str(number))]
    return "".join(encoded_number)

def get_user_phone_number(**kwargs: Dict[object,int]) -> str or None:
    """Returns response from the 'encoded_phone_number' func"""

    if kwargs.get("request"):
        user = User.objects.get(username=kwargs["request"].user.username)
        try:
            if phone_number := ModificatedUser.objects.get(user=user).number:
                return encode_phone_number(phone_number)
            return None
        except ObjectDoesNotExist:
            return None
    username = get_user(cookie=kwargs["cookie"])
    try:
        user = User.objects.get(username=username)
        if phone_number := ModificatedUser.objects.get(user=user).number:
            return encode_phone_number(phone_number)
        return None
    except ObjectDoesNotExist:
        return None

def made_records(**kwargs) -> Union[bool,None]:
    """Checks whether user has already made any records"""

    if kwargs.get("request"):
        user = User.objects.get(username=kwargs["request"].user.username)
        try:
            return ModificatedUser.objects.get(user=user).made_records
        except ObjectDoesNotExist:
            return None
    elif kwargs.get("cookies"):
        try:
            return ModificatedUser.objects.get(number_of_user=kwargs["cookies"]).made_records
        except ObjectDoesNotExist:
            return None
    else:
        assert False, "You passed not right data"

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
        
    
def get_all_reviews() -> list:

    return Review.mro()
    



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


def get_all_made_orders() -> int:
    """Return the number of all existing records"""

    return Record.objects.filter(status=True).count()
    
