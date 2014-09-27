Installation der gnublin-api
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die Installation ist `hier (unter "With Raspberry Pi") <http://en.gnublin.org/index.php/API_Python>`_ 
 relativ gut beschrieben und klappte ohne Probleme. 

Für die Installation der Python API muss der Pfad zu den Gnublin-Modulen noch
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

