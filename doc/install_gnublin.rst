Installation der gnublin-api
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die Installation ist `hier <http://en.gnublin.org/index.php/API>`_, bzw. hinter
den dort aufgeführten Links der verschiedenen Boards (Gnublin, Raspberry Pi und
BeagleBone Black) relativ gut beschrieben und klappte fast ohne Probleme. Im
`Tutorial API BeagleBoneBlack
<http://en.gnublin.org/index.php/Tutorial_API_BeagleBoneBlack>`_ fehlt die
Anweisung 

.. code:: bash

  cd gnublin-api

vor dem ersten "make". Später kann dieser Schritt dann wegfallen.

Hat man die C++ API installierert stehen zusätzlich einige Komandozeilen
Befehle zu Verfügung um die Gnublin-Module anzusteuern.

Für die Installation der Python API muss der Pfad zu den Gnublin-Modulen nach
an den Python Interpreter mitgeteielt werden. 

.. code:: bash

  export PYTHONPATH=$PYTHONPATH:/pfad/zu/den/Python/Modulen

auf dem Raspberry Pi z.B.:

.. code:: bash

  export PYTHONPATH=$PYTHONPATH:/home/pi/gnublin2/gnublin-api


Damit die Prgramme nicht immer als root ausgeführt werden müssen, kann der
Bentzer, unter dem die Programme laufen sollen den Gruppen für i2c und gpio
zuzufügen:

.. code:: bash

  sudo usermod -aG i2c <Benutzer>
  sudo usermod -aG gpio <Benutzer>

auf dem Raspberry Pi z.B.:

.. code:: bash

  sudo usermod -aG i2c pi
  sudo usermod -aG gpio pi

