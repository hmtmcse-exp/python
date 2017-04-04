class TmpMemory:

    TMP_DATA_HOLDER = None

    @staticmethod
    def set_redirect_tmp(data):
        TmpMemory.TMP_DATA_HOLDER = data

    @staticmethod
    def get_redirect_tmp():
        data = TmpMemory.TMP_DATA_HOLDER
        TmpMemory.TMP_DATA_HOLDER = None
        return data
