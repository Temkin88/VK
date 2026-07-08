import peewee as pw

from .base import BaseModel, db
from .product_functionality import ProductFunctionality
from .user import User


class TestResult(BaseModel):
    testresult_id = pw.IntegerField(unique=True)
    product_functionality = pw.ManyToManyField(
        ProductFunctionality, backref="testresults"
    )
    user = pw.ForeignKeyField(User, backref="testresults", null=True)
    reason = pw.TextField(null=True, default="unknown reason")

    def __str__(self):
        return f"TestResult(id={self.testresult_id})"

    def __repr__(self):
        return f"TestResult(id={self.testresult_id})"


TestResult.create_table()
TestResultProductFunctionality = TestResult.product_functionality.get_through_model()

db.create_tables([TestResultProductFunctionality])
