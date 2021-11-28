from src.convert_length import convert_length as convert_length_impl
from src.convert_time import convert_time as convert_time_impl
from src.convert_weight import convert_weight as convert_weight_impl
from src.si_prefix import si_prefix as si_prefix_impl
from swagger_server.models.conversion_result import ConversionResult  # noqa: E501
from swagger_server.models.server_status import ServerStatus  # noqa: E501
from swagger_server.models.si_prefix import SiPrefix  # noqa: E501


def convert_length(value, from_unit, to_unit):  # noqa: E501
    """Converts a length value between systems or units

    Convert a length value from one system or unit to another. # noqa: E501

    :param value: Value to convert.
    :type value: float
    :param from_unit: The unit in which the value is represented.
    :type from_unit: str
    :param to_unit: The unit to convert to.
    :type to_unit: str

    :rtype: ConversionResult
    """
    return convert_length_impl(value, from_unit, to_unit)


def convert_time(value, from_unit, to_unit):  # noqa: E501
    """Converts a time value between systems or units

    Convert a time value from one system or unit to another. # noqa: E501

    :param value: Value to convert.
    :type value: float
    :param from_unit: The unit in which value is represented.
    :type from_unit: str
    :param to_unit: The unit to convert to.
    :type to_unit: str

    :rtype: ConversionResult
    """
    return convert_time_impl(value, from_unit, to_unit)


def convert_weight(value, from_unit, to_unit):  # noqa: E501
    """Converts a weight value between systems or units

    Convert a weight value from one system or unit to another. # noqa: E501

    :param value: Value to convert.
    :type value: float
    :param from_unit: The unit in which value is represented.
    :type from_unit: str
    :param to_unit: The unit to convert to.
    :type to_unit: str

    :rtype: ConversionResult
    """
    return convert_weight_impl(value, from_unit, to_unit)


def si_prefix(value, unit=None):  # noqa: E501
    """Find the most matching SI prefix for a quantity

    Find a prefix with which the value can be presented in the range 1-999 with at most 3 decimal places, if possible. For example, 12345678 X is presented as 12.346 MX. # noqa: E501

    :param value: Value to convert.
    :type value: float
    :param unit: Optional unit to append to string representations of the converted value.
    :type unit: str

    :rtype: SiPrefix
    """
    return si_prefix_impl(value, unit)


def status():  # noqa: E501
    """Gets server status

    Check if server is up and healthy. # noqa: E501


    :rtype: ServerStatus
    """
    return status()
