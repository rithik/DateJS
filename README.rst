DateJS |Build Status|
=====================

Convert Date from a JavaScript Date object to a Python DateTime object
----------------------------------------------------------------------

Usage
-----

To use this library, you must first install the library (pip install
DateJS)

In your code, you must import DateJS package by including
``from DateJS import DateJS``.

To convert JavaScript Date, initialize a DateJS object by doing
``DateJS(JAVASCRIPT_DATE_STRING, convert)``, where the
``JAVASCRIPT_DATE_STRING`` can be determined by running
``new Date().toString()`` in JavaScript and ``convert`` is whether you
would like to convert the time to the server timezone.

Get Values
----------

You can access a wide array of values by calling one of the following
methods:

Year -> ``getYear()``
^^^^^^^^^^^^^^^^^^^^^

Month -> ``getMonth()``
^^^^^^^^^^^^^^^^^^^^^^^

Date -> ``getDate()``
^^^^^^^^^^^^^^^^^^^^^

Hours -> ``getHours()``
^^^^^^^^^^^^^^^^^^^^^^^

Minutes -> ``getMinutes()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Seconds -> ``getSeconds()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Milliseconds -> ``getMilliseconds()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Common Timezone (From pytz.common_timezones) -> ``getTimezone()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Time (as a DateTime object) -> ``getTime()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Common Errors
-------------

If you get a JavaScript Runtime Error, you can fix this by running
``sudo apt-get install nodejs``. This will configure the JavaScript
Runtime Environment.

Examples
--------

Format: ``DateJS(JAVASCRIPT_STRING, convert)``.

.. code:: python

   from DateJS import DateJS

   dJS = DateJS("Thu Oct 19 2017 21:50:06 GMT-0400 (Eastern Daylight Time)", True)

   dJS.getTime() # Get datetime object of time with timezone data

   dJS.getTimezone() # Returns a timezone object from pytz

If you use the example above, JavaScript will automatically convert the
Date into the timezone of the python server. In order to maintain the
existing timezone, you can set the convert field to ``False``.

.. code:: python


   dJS = DateJS("Thu Oct 19 2017 21:50:06 GMT-0400 (Eastern Daylight Time)", False)

   dJS.getTime() # Get datetime object of time with timezone data

   dJS.getTimezone() # Returns a timezone object from pytz

Unnoticed Errors
----------------

If you would like to report any errors, please open an issue. If you
know how to fix the issue, please submit appropriate changes.

.. |Build Status| image:: https://travis-ci.org/rithik/DateJS.svg?branch=master

