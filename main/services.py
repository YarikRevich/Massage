from django.contrib.auth.models import User
from main.models import Record
from main.models import ModificatedUser
import random


def get_username_by_email(**credentials) -> "username":
    """Returns user's username got by email"""

    username = User.objects.filter(email=credentials["email"])
    if username:
        return [x.username for x in username][0]
    return None


def create_user_id(username: str) -> "random numbers":
    """Returns a random special user_id to check whether user is authentificated"""

    number = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(number)
    code = "0"
    for num in number:
        code += str(num)
    for element in ModificatedUser.objects.all():
        if element.number_of_user == code:
            return create_user_id(username=username)
    return int(code)

def check_admin(username: str) -> "True or False":
    """Check whether user is admin"""

    user = User.objects.get(username=username)
    if user.is_staff:
        return True
    return False



def get_user_id_by_username(username: str) -> "User":
    """Returns a user_id to save it to cookies"""

    query = ModificatedUser.objects.select_related("user")
    user_id = [element.number_of_user for element in query if element.user.username == username]

    if user_id:
        return user_id[0]
    return None
    

def get_email(cookie) -> "email":
    """Returns user's email"""

    user_id = ModificatedUser.objects.get(number_of_user=cookie)
    return user_id.user.email


def get_last_name(cookie) -> "last_name":
    """Returns user's last_name"""

    user_id = ModificatedUser.objects.get(number_of_user=cookie)
    return user_id.user.last_name


def get_user(cookie) -> "username":
    """Returns user's username"""

    user_id = ModificatedUser.objects.get(number_of_user=cookie)
    return user_id.user.username


def get_first_name(cookie) -> "first_name":
    """Retuns user's first_name"""

    user_id = ModificatedUser.objects.get(number_of_user=cookie)
    return user_id.user.first_name


class SplitedQuerySet:

    def _create_separated_query_set(self, model):
        """
        Separates query_set on two parts 
        (consists of len of the query_set)
        """

        self.query_set = model.objects.all()
        self.first_part = int(len(self.query_set) / 2)
        self.second_part = len(self.query_set) - self.first_part

    def _create_first_list(self):
        """Returns parts of the first query_set"""

        if self.first_part == self.second_part:
            for article in range(0, self.first_part):
                yield self.query_set[article]
        else:
            for article in range(0, self.first_part + 1):
                yield self.query_set[article]

    def _create_second_list(self):
        """Returns parts of the second query_set"""

        for article in range(self.second_part, len(self.query_set)):
            yield self.query_set[article]

    def _get_first_list(self):
        """Creates the first separated list"""

        self.first = self._create_first_list()

    def _get_second_list(self):
        """Creates the second separated list"""

        self.second = self._create_second_list()

    def _first_gen(self):
        """Returns the parts of the first generator"""

        try:
            return next(self.first)
        except StopIteration:
            pass

    def _second_gen(self):
        """Returns the parts of the second generator"""

        try:
            return next(self.second)
        except StopIteration:
            pass

    def _get_finall_list(self):
        """Returns the finall list of separated query_set"""

        finall_list = []
        for _ in range(0, self.second_part):

            finall_list.append(
                (self._first_gen(), self._second_gen())
            )

        return finall_list

    def get_list(self, model):
        """Does all the methods to return the finall list"""

        self._create_separated_query_set(model)
        self._create_first_list()
        self._create_second_list()
        self._get_first_list()
        self._get_second_list()
        return self._get_finall_list()


def get_all_made_orders():

    all_records = Record.objects.filter(status=True)
    return len(all_records)
