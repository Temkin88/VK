import peewee as pw

from database.base import BaseModel, db
from database.product_functionality import ProductFunctionality
from database.user import User


class TestResult(BaseModel):
    testresult_id = pw.IntegerField(unique=True)
    product_functionality = pw.ManyToManyField(
        ProductFunctionality, backref="testresults"
    )
    user = pw.ForeignKeyField(User, backref="testresults", null=True)
    reason = pw.TextField(null=True, default="unknown reason")


TestResult.create_table()
TestResultProductFunctionality = TestResult.product_functionality.get_through_model()

db.create_tables([TestResultProductFunctionality])
