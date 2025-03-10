import io, sys, unittest
import contextlib
from decimal import Decimal
from datetime import date

from foalorm.orm import *
from foalorm.orm.tests.testutils import *
from foalorm.orm.tests import setup_database, teardown_database

db = Database()


class Student(db.Entity):
    name = Required(str)
    scholarship = Optional(int)
    gpa = Optional(Decimal, 3, 1)
    dob = Optional(date)
    group = Required('Group')
    courses = Set('Course')
    biography = Optional(LongUnicode)

class Group(db.Entity):
    number = PrimaryKey(int)
    students = Set(Student)

class Course(db.Entity):
    name = Required(str, unique=True)
    students = Set(Student)


normal_stdout = sys.stdout


class TestShow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        setup_database(db)

        with db_session:
            g1 = Group(number=1)
            g2 = Group(number=2)
            c1 = Course(name='Math')
            c2 = Course(name='Physics')
            c3 = Course(name='Computer Science')
            Student(id=1, name='S1', group=g1, gpa=3.1, courses=[c1, c2], biography='some text')
            Student(id=2, name='S2', group=g1, gpa=3.2, scholarship=100, dob=date(2000, 1, 1))
            Student(id=3, name='S3', group=g1, gpa=3.3, scholarship=200, dob=date(2001, 1, 2), courses=[c2, c3])

    @classmethod
    def tearDownClass(cls):
        teardown_database(db)

    def setUp(self):
        rollback()
        db_session.__enter__()

    def tearDown(self):
        rollback()
        db_session.__exit__()

    def test_1(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            Student.select().show()
        self.assertEqual('\n' + f.getvalue().replace(' ', '~'), '''
id|name|scholarship|gpa|dob~~~~~~~|group~~~
--+----+-----------+---+----------+--------
1~|S1~~|None~~~~~~~|3.1|None~~~~~~|Group[1]
2~|S2~~|100~~~~~~~~|3.2|2000-01-01|Group[1]
3~|S3~~|200~~~~~~~~|3.3|2001-01-02|Group[1]
''')

    def test_2(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            Group.select().show()
        self.assertEqual('\n' + f.getvalue().replace(' ', '~'), '''
number
------
1~~~~~
2~~~~~
''')


if __name__ == '__main__':
    unittest.main()
