from django_crud.helper import SYSTEM_CONSTANT


class CRUDHelper:

    def __init__(self, model, data=None):
        self.model = model
        self.request = data
        pk = None
        if self.request is not None:
            if self.request.get("id") is not None:
                pk = self.request.get("id")
            elif self.request.get("pk") is not None:
                pk = self.request.get("pk")
        if pk is None:
            self.modelObject = model()
        else:
            self.modelObject = self.get_by_id(pk)

        self.error_message = "Unknown Error."
        self.total = 0

    def is_valid(self):
        for key in self.model.get_all_fields():
            value = self.model.get_all_fields()[key]
            form_field = self.request.get(key)
            if bool(value):
                if "required" in value:
                    if form_field is None or form_field == "":
                        if "message" in value:
                            self.error_message = value["message"]
                        else:
                            self.error_message = key + " Required Field"
                        return False
            if form_field is not None and form_field != "":
                if "belongsTo" in value and value["belongsTo"]:
                    self.resolve_belongs_to(key, form_field)
                else:
                    setattr(self.modelObject, key, form_field)
        return True

    def resolve_belongs_to(self, key, form_field):
        model_name = key.title()
        pv_crud_helper = CRUDHelper(eval(model_name))
        belongs_to_data = pv_crud_helper.get_by_id(form_field)
        setattr(self.modelObject, key, belongs_to_data)

    def save(self):
        self.modelObject.save()

    def get_error_message(self):
        return self.error_message

    def get_model(self):
        return self.modelObject

    def get_by(self, dictionary):
        return self.model.objects.filter(**dictionary).get()

    def get_by_id(self, pk):
        return self.get_by({"id__exact": pk})

    def delete_by_id(self, pk):
        data = self.get_by({"id__exact": pk})
        if data is None:
            self.error_message = "Invalid Record"
            return False
        data.delete()
        return True

    def get_list(self):
        query = self.model.objects
        self.total = query.count()
        col_name = self.request.get('colName')
        if col_name is not None and self.request.get('colValue') is not None:
            if col_name != "" and col_name != "#":
                criteria = self.request.get('colName') + '__contains'
                query = query.filter(**{criteria: self.request.get('colValue')})

        if self.request.get('sort') is None:
            query = query.order_by("-id")
        else:
            query = query.order_by(self.request.get('sort'))

        offset = 0
        if self.request.get('offset') is not None:
            offset = int(self.request.get('offset'))

        limit = SYSTEM_CONSTANT.ITEMS_PER_PAGE
        if self.request.get('limit') is not None:
            limit = int(self.request.get('limit'))

        limit = limit + offset
        query = query.all()[offset:limit]

        return query

    def get_total(self):
        return self.total
