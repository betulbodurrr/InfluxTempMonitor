from django.apps import AppConfig
import threading
import random
import time
from datetime import datetime
from django.conf import settings
from influxdb_client import InfluxDBClient, Point, WritePrecision, WriteOptions

class MyAppConfig(AppConfig):
    name = 'app'

    def ready(self):
        temperature_thread = threading.Thread(target=self.generate_temperature)
        temperature_thread.start()

    def veriKayit(self, temperature):
        url = settings.INFLUXDB_CONFIG['url']
        token = settings.INFLUXDB_CONFIG['token']
        org = settings.INFLUXDB_CONFIG['org']
        bucket = settings.INFLUXDB_CONFIG['bucket']

        client = InfluxDBClient(url=url, token=token)
        write_api = client.write_api(write_options=WriteOptions(batch_size=500, flush_interval=10_000))

        point = Point("temperature") \
            .tag("location", "random") \
            .field("value", temperature) \
            .time(datetime.utcnow(), WritePrecision.NS)

        write_api.write(bucket=bucket, org=org, record=point)
        client.close()

    def generate_temperature(self):
        while getattr(threading.current_thread(), "do_run", True):
            temperature = random.randint(10, 40)
            print("Sıcaklık değeri:", temperature)
            self.veriKayit(temperature)
            time.sleep(10)
            
    def stop_thread(self):
            if getattr(self, 'temperature_thread', None):
                self.temperature_thread.do_run = False

    def ready(self):
        self.temperature_thread = threading.Thread(target=self.generate_temperature)
        self.temperature_thread.start()

    def shutdown(self):
         self.stop_thread()     