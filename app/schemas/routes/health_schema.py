from flask_restplus import fields
from app.restplus import api

from app.schemas.routes import response_serializer


class HealthSchema:
    def __init__(self):
        self._name = "Health"

    @property
    def health(self):
        """
        Serializer do HealthCheck
        """
        return api.model(self._name, self._obj_health)

    @property
    def response_health(self):
        """
        Serializer de resposta do produto
        """
        return response_serializer(data=self.health, name_model=f"{self._name}Response")

    @property
    def _obj_health(self):
        return {
            "environment": fields.String(readonly=True),
            "datetime": fields.String(readonly=True),
        }
