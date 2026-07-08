import peewee as pw

from project.db.models.base_model import BaseModel


class Defect(BaseModel):
    id = pw.AutoField()
    project_id = pw.IntegerField()
    name = pw.TextField()
    issue = pw.TextField(null=True, default=None)
    launch_count = pw.IntegerField()
    test_result_count = pw.IntegerField()
    test_case_count = pw.IntegerField()

    def __repr__(self):
        return f"<Defect(id={self.id}, issue={self.issue})>"

    def __str__(self):
        return self.__repr__()


Defect.create_table()
