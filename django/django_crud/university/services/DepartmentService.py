from university.models import Department


class DepartmentService:

    @classmethod
    def get_all(cls, offset=0, limit=-1):
        return Department.objects.all().filter(
            enable=True
        )