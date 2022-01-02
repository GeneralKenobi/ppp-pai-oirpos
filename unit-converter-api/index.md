Unit Converter
==============

This is a sample unit converter web server.

More information: [https://github.com/GeneralKenobi](https://github.com/GeneralKenobi)

Contact Info: [szymzog050@student.polsl.pl](szymzog050@student.polsl.pl)

Version: 1.0.0

Apache 2.0

http://www.apache.org/licenses/LICENSE-2.0.html

Access
------

Methods
-------

\[ Jump to [Models](#__Models) \]

### Table of Contents

#### [Default](#Default)

*   [`get /convert/length`](#convertLength)
*   [`get /convert/time`](#convertTime)
*   [`get /convert/weight`](#convertWeight)
*   [`get /si/prefix`](#siPrefix)
*   [`get /status`](#status)

Default
=======

[Up](#__Methods)

    get /convert/length

Converts a length value between systems or units (convertLength)

Convert a length value from one system or unit to another.

### Query parameters

value (required)

Query Parameter — Value to convert.

fromUnit (required)

Query Parameter — The unit in which the value is represented.

toUnit (required)

Query Parameter — The unit to convert to.

### Return type

[ConversionResult](#ConversionResult)

### Example data

Content-Type: application/json

    {
      "value" : 12.346
    }

### Produces

This API call produces the following media types according to the Accept request header; the media type will be conveyed by the Content-Type response header.

*   `application/json`

### Responses

#### 200

Conversion successful. [ConversionResult](#ConversionResult)

#### 400

If any parameter is missing or invalid.[](#)

* * *

[Up](#__Methods)

    get /convert/time

Converts a time value between systems or units (convertTime)

Convert a time value from one system or unit to another.

### Query parameters

value (required)

Query Parameter — Value to convert.

fromUnit (required)

Query Parameter — The unit in which value is represented.

toUnit (required)

Query Parameter — The unit to convert to.

### Return type

[ConversionResult](#ConversionResult)

### Example data

Content-Type: application/json

    {
      "value" : 12.346
    }

### Produces

This API call produces the following media types according to the Accept request header; the media type will be conveyed by the Content-Type response header.

*   `application/json`

### Responses

#### 200

Conversion successful. [ConversionResult](#ConversionResult)

#### 400

If any parameter is missing or invalid.[](#)

* * *

[Up](#__Methods)

    get /convert/weight

Converts a weight value between systems or units (convertWeight)

Convert a weight value from one system or unit to another.

### Query parameters

value (required)

Query Parameter — Value to convert.

fromUnit (required)

Query Parameter — The unit in which value is represented.

toUnit (required)

Query Parameter — The unit to convert to.

### Return type

[ConversionResult](#ConversionResult)

### Example data

Content-Type: application/json

    {
      "value" : 12.346
    }

### Produces

This API call produces the following media types according to the Accept request header; the media type will be conveyed by the Content-Type response header.

*   `application/json`

### Responses

#### 200

Conversion successful. [ConversionResult](#ConversionResult)

#### 400

If any parameter is missing or invalid.[](#)

* * *

[Up](#__Methods)

    get /si/prefix

Find the most matching SI prefix for a quantity (siPrefix)

Find a prefix with which the value can be presented in the range 1-999 with at most 3 decimal places, if possible. For example, 12345678 X is presented as 12.346 MX.

### Query parameters

value (required)

Query Parameter — Value to convert.

unit (optional)

Query Parameter — Optional unit to append to string representations of the converted value.

### Return type

[SiPrefix](#SiPrefix)

### Example data

Content-Type: application/json

    {
      "formatted" : "12.346 Gt",
      "prefix" : {
        "symbol" : "G",
        "name" : "giga",
        "power" : 9.0,
        "word" : "billion"
      },
      "value" : 12.346
    }

### Produces

This API call produces the following media types according to the Accept request header; the media type will be conveyed by the Content-Type response header.

*   `application/json`

### Responses

#### 200

Value adjusted to the selected prefix. [SiPrefix](#SiPrefix)

* * *

[Up](#__Methods)

    get /status

Gets server status (status)

Check if server is up and healthy.

### Return type

[ServerStatus](#ServerStatus)

### Example data

Content-Type: application/json

    {
      "message" : "OK"
    }

### Produces

This API call produces the following media types according to the Accept request header; the media type will be conveyed by the Content-Type response header.

*   `application/json`

### Responses

#### 200

Server is up and running. [ServerStatus](#ServerStatus)

#### 500

Server is up but it's not running.[](#)

* * *

Models
------

\[ Jump to [Methods](#__Methods) \]

### Table of Contents

1.  [`ConversionResult`](#ConversionResult)
2.  [`ServerStatus`](#ServerStatus)
3.  [`SiPrefix`](#SiPrefix)
4.  [`SiPrefix_prefix`](#SiPrefix_prefix)

### `ConversionResult` [Up](#__Models)

value

[BigDecimal](#BigDecimal) Converted value.

example: 12.346

### `ServerStatus` [Up](#__Models)

message

[String](#string) A few words describing the current status of the server

example: OK

### `SiPrefix` [Up](#__Models)

value

[BigDecimal](#BigDecimal) Value converted for representation with an SI prefix.

example: 12.346

formatted

[String](#string) Value formatted with the prefix and optional unit.

example: 12.346 Gt

prefix

[SiPrefix\_prefix](#SiPrefix_prefix)

### `SiPrefix_prefix` [Up](#__Models)

The used SI prefix.

name (optional)

[String](#string) The name of the prefix.

example: giga

symbol (optional)

[String](#string) Symbol representing the prefix.

example: G

power

[BigDecimal](#BigDecimal) The power of 10 which is represented by the prefix.

example: 9.0

word (optional)

[String](#string) English word for the prefix.

example: billion
