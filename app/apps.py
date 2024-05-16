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

        # InfluxDB istemcisini oluşturun
        client = InfluxDBClient(url=url, token=token)
        write_api = client.write_api(write_options=WriteOptions(batch_size=500, flush_interval=10_000))

        # Sıcaklık verisini yazılacak veri noktasına dönüştürün
        point = Point("temperature") \
            .tag("location", "random") \
            .field("value", temperature) \
            .time(datetime.utcnow(), WritePrecision.NS)

        # Veriyi InfluxDB'ye yazın
        write_api.write(bucket=bucket, org=org, record=point)
        client.close()

    def generate_temperature(self):
        while True:
            temperature = random.randint(10, 40)
            print("Sıcaklık değeri:", temperature)
            self.veriKayit(temperature)
            time.sleep(10)
