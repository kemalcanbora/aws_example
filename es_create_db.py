from json import loads
from aws_base import Aws


class ES(Aws):
    def __init__(self):
        super(ES, self).__init__()
        self.es = self.connection_aws(service="es")

    def create_db(self):
        response = self.es.create_elasticsearch_domain(loads("./config/ES.json"))
        return response
