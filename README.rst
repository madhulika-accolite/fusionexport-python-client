FusionExport Python Client
==========================

Language SDK for FusionExport which enables exporting of charts and dashboards through Python.


Installation
------------

To install this Python package, use pip:

.. code-block:: shell

    pip install fusionexport
    
To start fusionexport-server use the command below

.. code-block:: shell

    start fusionexport.bat --config-file ./config.json

config.json example 

.. code-block:: json

    {
     "server": {
        "host": "0.0.0.0",
        "port": "1337",
        "logEnabled": true,
        "workerCount": "2",
        "timeout": "80000"
        }
    }
