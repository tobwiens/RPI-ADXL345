import time

import adxl345 as adxl345

import datetime

import RPi.GPIO as GPIO

from kafka import KafkaProducer

from measurement import AccelerometerMeasurement
from measurementBurst import AccelerometerMeasurementBurst

kafka_producer = KafkaProducer(bootstrap_servers=['ec2-54-93-107-90.eu-central-1.compute.amazonaws.com:9092'])

WATERMARK_INTERRUPT_PIN = 4

WATERMARK = 25

def setup_raspberry_interrupts():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(WATERMARK_INTERRUPT_PIN, GPIO.IN)


setup_raspberry_interrupts()

accelerometer = adxl345.ADXL345(i2c_port=1, address=0x53)
accelerometer.measure_stop()
accelerometer.enable_watermark_interrupt()
accelerometer.set_data_rate(data_rate=adxl345.DataRate.R_100)

accelerometer.set_range(g_range=adxl345.Range.G_2, full_res=True)

accelerometer.set_fifo_mode(fifo_mode=adxl345.FIFO.STREAM)
accelerometer.set_trigger_amount(trigger_sample_amount=WATERMARK)
accelerometer.measure_start()

outputFile = open("output.log", "w+")

count = 0
start_time = start_time = time.time()

while True:
    accelerometer_interrupt = i = GPIO.input(WATERMARK_INTERRUPT_PIN)

    if accelerometer_interrupt:
        measurementBurst = AccelerometerMeasurementBurst(datetime.datetime.now().isoformat(), 100)

        for i in range(0, WATERMARK):
            x, y, z = accelerometer.get_3_axis_adjusted()
            measurement = AccelerometerMeasurement(x, y, z)
            measurementBurst.add_measurement(measurement)
            count = count + 1

        data_string = measurementBurst.toJSON()
        outputFile.write(data_string)
        kafka_producer.send('TOB01.sensors.accel', bytearray(data_string, 'ascii'))

    if count == 100:
        print("Measured 100 times")
        print("Within time: "+str(time.time() - start_time))
        start_time = time.time()
        count = 0



