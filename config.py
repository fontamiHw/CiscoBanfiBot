class Config(object):
    
    def __init__(self):
        self.token = "M2IwNDU0OWItYTg1ZC00YjQyLTkwMDMtODQyZDMyYzA1M2U2NmQ1MjdlOTktNWFi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
        self.name = "MikExperiment"
        self.uniqueId = "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OLzI5ODFhMjhjLTQ0MTUtNDcwMy1iOWRjLTViNmJlNzlkNjg0MQ"
        self.proxies=None


    def get_token(self):
        return self.token

    def get_name(self):
        return self.name

    def get_uniqueId(self):
        return self.uniqueId  

    def get_proxies(self):
        return self.proxies