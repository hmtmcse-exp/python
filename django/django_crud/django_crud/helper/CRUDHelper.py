
class CRUDHelper:

    def __init__(self, model, data):
        self.model = model
        self.modelObject = model()
        self.data = data
        self.error_message = "Unknown Error."

    def is_valid(self):
        for key in self.model.get_all_fields():
            value = self.model.get_all_fields()[key]
            form_field = self.data.get(key)
            if bool(value):
                if "required" in value:
                    if form_field is None or form_field == "":
                        if "message" in value:
                            self.error_message = value["message"]
                        else:
                            self.error_message = key + " Required Field"
                        return False
            if form_field is not None and form_field != "":
                setattr(self.modelObject, key, form_field)
        return True

    def save(self):
        self.modelObject.save()

    def get_error_message(self):
        return self.error_message

    def get_model(self):
        return self.modelObject

    def get_list(self):
        pass

    def get_total(self):
        pass
