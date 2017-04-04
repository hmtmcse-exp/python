from university.models import Department


class DepartmentService:

    @classmethod
    def get_all(cls, offset=0, limit=-1):
        data = Department.objects.filter(
            enable=True
        )
        total = data.count()
        print(data.query)
        data = data.order_by("-id").all()[1:10]
        print(data.query)
        print("total: " + str(total))
        return data

    @classmethod
    def save_form(cls, data):
        department = Department()
