# InfluxTempMonitor <br>
<img align="center" src="https://www.svgrepo.com/show/237418/turkey.svg"  height="30" width="40" />Tr:
<img align="center" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"  height="30" width="40" /></a>
<img align="center" src="https://github.com/betulbodurrr/InfluxTempMonitor/blob/main/img/influxdb-svgrepo-com.svg"  height="30" width="40" /></a><br>

[InfluxDB Dokümantasyonuna Erişmek için Tıklayınız.](https://docs.influxdata.com/flux/v0/get-started/data-model/) <br> <br>
Grafana için :http://localhost:3000<br>
Influxdb için:http://localhost:8086<br>
WeB Arayüzü için:http://localhost:8000<br>  <br>
InfluxDB'yi önce kurmamız gerekiyor.<br>

# InfluxDB Kurulum:<br>
[Bu linkten](https://www.influxdata.com/downloads/) bilgisayarımıza uygun olan influxDB'yi buluyoruz.Ben Windows için kuracağım.<br> 
1-PowerShell'i "Yönetici" olarak çalıştırıyoruz.<br> <br> <br>
<img align="center" src="https://github.com/betulbodurrr/InfluxTempMonitor/blob/main/img/influxdbkurulum.png"  height="150" width="250" /></a><br> <br>
2-Sırasıyla aşağıdaki komutları PowerShell'e Copy-Paste yapın.<br>
2.1- wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.7.6-windows.zip -UseBasicParsing -OutFile influxdb2-2.7.6-windows.zip<br>
2.2- Expand-Archive .\influxdb2-2.7.6-windows.zip -DestinationPath 'C:\Program Files\InfluxData\influxdb\'<br>
Kurulum gerçekleşmiş oldu.Şimdi projeye bağladığımız InfluxDB'yi çalıştırmalıyız.<br>

# InfluxDB çalıştırma:<br>
1-win+R ile çıkan search'e "cmd" yazıyoruz.<br>
2-Açılan komut isteminde InfluxDB'nin bulunduğu klasöre gidiyoruz.Yukarıdaki gibi kurduysanız aşağıdaki komutları yazmanız yeterli olacaktır.<br> <br>
<img align="center" src="https://github.com/betulbodurrr/InfluxTempMonitor/blob/main/img/influxexe.png"  height="150" width="500" /></a><br> <br>
2.1- cd C:\Program Files\InfluxData\influxdb<br>
2.2- influxd.exe<br> <br>
<img align="center" src="https://github.com/betulbodurrr/InfluxTempMonitor/blob/main/img/influxexecalistirma.png"  height="200" width="500" /></a><br> <br>
Artık InfluxDB çalışır durumda.http://localhost:8086 ile InfluxDB arayüzüne erişebilirsiniz.<br>

Projemizi terminal üzerinden çalıştırdığımızda random bir şekilde oluşturulan sıcaklık değerleri önce InfluxDB'ye sonra görselleştirmek için Grafana'ya iletilir ve Grafana'dan da kendi web sitemizde görüntüleriz.<br> <br>
<img align="center" src="https://www.svgrepo.com/show/365950/usa.svg"  height="20" width="30" />En:
<img align="center" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"  height="30" width="40" /></a>
<img align="center" src="https://github.com/betulbodurrr/InfluxTempMonitor/blob/main/img/influxdb-svgrepo-com.svg"  height="30" width="40" /></a><br>

[Click here to access InfluxDB Documentation.](https://docs.influxdata.com/flux/v0/get-started/data-model/) <br> <br>
For Grafana:http://localhost:3000<br>
For InfluxDB:http://localhost:8086<br>
For Web Interface:http://localhost:8000<br>  <br>
First, we need to install InfluxDB.<br>

# InfluxDB Installation:<br>
Find the appropriate InfluxDB version for your computer from [this link](https://www.influxdata.com/downloads/). I will install it for Windows.<br> 
1-Run PowerShell as "Administrator".<br> <br> <br>
<img align="center" src="https://github.com/betulbodurrr/InfluxTempMonitor/blob/main/img/influxdbkurulum.png"  height="150" width="250" /></a><br> <br>
2-Copy and paste the following commands into PowerShell in sequence:<br>
2.1- wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.7.6-windows.zip -UseBasicParsing -OutFile influxdb2-2.7.6-windows.zip<br>
2.2- Expand-Archive .\influxdb2-2.7.6-windows.zip -DestinationPath 'C:\Program Files\InfluxData\influxdb\'<br>
The installation is now complete. Next, we need to run the InfluxDB we have linked to the project<br>

# Running InfluxDB:<br>
1-Press Win+R and type "cmd" in the search bar.<br>
2-In the opened command prompt, navigate to the folder where InfluxDB is located. If you installed it as described above, you can use the following commands:<br> <br>
<img align="center" src="https://github.com/betulbodurrr/InfluxTempMonitor/blob/main/img/influxexe.png"  height="150" width="500" /></a> <br> <br>
2.1- cd C:\Program Files\InfluxData\influxdb<br>
2.2- influxd.exe<br> <br>
<img align="center" src="https://github.com/betulbodurrr/InfluxTempMonitor/blob/main/img/influxexecalistirma.png"  height="200" width="500" /></a><br> <br>
Now, InfluxDB is running. You can access the InfluxDB interface at http://localhost:8086.<br>

When we run our project from the terminal, randomly generated temperature values will first be sent to InfluxDB and then visualized in Grafana, which we will display on our website.<br>

# Proje/Project:<br>
<img align="center" src="https://github.com/betulbodurrr/InfluxTempMonitor/blob/main/img/influxdbarayuz.png"  height="600" width="1000" /></a><br> <br>
<img align="center" src="https://github.com/betulbodurrr/InfluxTempMonitor/blob/main/img/grafanarayuz.png"  height="600" width="1000" /></a><br> <br>
<img align="center" src="https://github.com/betulbodurrr/InfluxTempMonitor/blob/main/img/projearayuz.png"  height="600" width="1000" /></a><br> <br>
