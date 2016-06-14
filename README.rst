RPI-ADXL345
====================
Python library to interface ADXL345 Accelerometer 
(already test with Raspberry Pi2)


Dependencies
====================
smbus


Usage
====================
Example code for 

- Calibration for offset and sensitivity (cross axis calibration), please follow instruction in Terminal
- Reading g and pitch:

.. code-block:: bash

	import adxl345
	import time

	accelerometer = adxl345.ADXL345(i2c_port=1, address=0x53)
	accelerometer.load_calib_value()
	accelerometer.set_data_rate(data_rate=adxl345.DataRate.R_100)
	accelerometer.set_range(g_range=adxl345.Range.G_16, full_res=True)
	accelerometer.measure_start()

	#accelerometer.calibrate()	# Calibrate only one time


	while(True):
		x, y, z = accelerometer.get_3_axis_adjusted()
		print('x: ', x, 'y: ', y, 'z: ', z)
		print('pitch: ', accelerometer.get_pitch())
		time.sleep(1)
		
		
