# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.si_prefix_prefix import SiPrefixPrefix  # noqa: F401,E501
from swagger_server import util


class SiPrefix(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, value: float=None, formatted: str=None, prefix: SiPrefixPrefix=None):  # noqa: E501
        """SiPrefix - a model defined in Swagger

        :param value: The value of this SiPrefix.  # noqa: E501
        :type value: float
        :param formatted: The formatted of this SiPrefix.  # noqa: E501
        :type formatted: str
        :param prefix: The prefix of this SiPrefix.  # noqa: E501
        :type prefix: SiPrefixPrefix
        """
        self.swagger_types = {
            'value': float,
            'formatted': str,
            'prefix': SiPrefixPrefix
        }

        self.attribute_map = {
            'value': 'value',
            'formatted': 'formatted',
            'prefix': 'prefix'
        }
        self._value = value
        self._formatted = formatted
        self._prefix = prefix

    @classmethod
    def from_dict(cls, dikt) -> 'SiPrefix':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SiPrefix of this SiPrefix.  # noqa: E501
        :rtype: SiPrefix
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> float:
        """Gets the value of this SiPrefix.

        Value converted for representation with an SI prefix.  # noqa: E501

        :return: The value of this SiPrefix.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value: float):
        """Sets the value of this SiPrefix.

        Value converted for representation with an SI prefix.  # noqa: E501

        :param value: The value of this SiPrefix.
        :type value: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def formatted(self) -> str:
        """Gets the formatted of this SiPrefix.

        Value formatted with the prefix and optional unit.  # noqa: E501

        :return: The formatted of this SiPrefix.
        :rtype: str
        """
        return self._formatted

    @formatted.setter
    def formatted(self, formatted: str):
        """Sets the formatted of this SiPrefix.

        Value formatted with the prefix and optional unit.  # noqa: E501

        :param formatted: The formatted of this SiPrefix.
        :type formatted: str
        """
        if formatted is None:
            raise ValueError("Invalid value for `formatted`, must not be `None`")  # noqa: E501

        self._formatted = formatted

    @property
    def prefix(self) -> SiPrefixPrefix:
        """Gets the prefix of this SiPrefix.


        :return: The prefix of this SiPrefix.
        :rtype: SiPrefixPrefix
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix: SiPrefixPrefix):
        """Sets the prefix of this SiPrefix.


        :param prefix: The prefix of this SiPrefix.
        :type prefix: SiPrefixPrefix
        """
        if prefix is None:
            raise ValueError("Invalid value for `prefix`, must not be `None`")  # noqa: E501

        self._prefix = prefix