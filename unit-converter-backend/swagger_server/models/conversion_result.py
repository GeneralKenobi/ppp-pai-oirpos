# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ConversionResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, value: float=None):  # noqa: E501
        """ConversionResult - a model defined in Swagger

        :param value: The value of this ConversionResult.  # noqa: E501
        :type value: float
        """
        self.swagger_types = {
            'value': float
        }

        self.attribute_map = {
            'value': 'value'
        }
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'ConversionResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ConversionResult of this ConversionResult.  # noqa: E501
        :rtype: ConversionResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> float:
        """Gets the value of this ConversionResult.

        Converted value.  # noqa: E501

        :return: The value of this ConversionResult.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value: float):
        """Sets the value of this ConversionResult.

        Converted value.  # noqa: E501

        :param value: The value of this ConversionResult.
        :type value: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value
