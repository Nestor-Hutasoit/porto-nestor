from influxdb import InfluxDBClient
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, count, round
import os
import sys

# 1. ATUR VARIABEL LINGKUNGAN PYTHON UNTUK SPARK
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

print("Memulai proses Apache Spark...")

# 2. Hubungkan ke Spark Master
spark = SparkSession.builder \
    .appName("AnalisisSmartHotel") \
    .master("spark://127.0.0.1:7077") \
    .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
    .config("spark.executor.memory", "1g") \
    .config("spark.cores.max", "2") \
    .getOrCreate()

# 3. Matikan log WARN/INFO yang nyepam di terminal
spark.sparkContext.setLogLevel("ERROR")

# 4. Tarik Data dari InfluxDB Server Luis
print("Menarik data dari InfluxDB...")
db_client = InfluxDBClient(host="100.127.227.8", port=31086, database="smarthotel")

try:
    hasil = db_client.query("SELECT * FROM sensor_kamar")
    poin_data = list(hasil.get_points())
except Exception as e:
    print(f"❌ Gagal menarik data dari InfluxDB: {e}")
    exit()

if not poin_data:
    print("❌ Data tidak ditemukan di database. Pastikan ESP32 sudah mengirim data.")
    exit()

# 5. Konversi Data ke Spark DataFrame 
df_pandas = pd.DataFrame(poin_data)
# Pastikan kolom time dihapus agar tidak bentrok format tanggal
if 'time' in df_pandas.columns:
    df_pandas = df_pandas.drop(columns=['time']) 

df_spark = spark.createDataFrame(df_pandas)

print("\n✅ Data Berhasil Masuk ke Spark! Berikut 5 baris pertama:")
df_spark.show(5)

# ==========================================
# 6. MULAI ANALISIS DATA DENGAN SPARK
# ==========================================

print("📊 ANALISIS 1: Rata-rata Suhu & Kelembapan Berdasarkan Status Kamar")
analisis_1 = df_spark.groupBy("status").agg(
    count("*").alias("Total_Data"),
    round(avg("suhu"), 2).alias("Rata_Suhu"),
    round(avg("kelembapan"), 2).alias("Rata_Kelembapan")
)
analisis_1.show()


print("📊 ANALISIS 2: Statistik Ekstrem (Suhu Tertinggi & Terendah)")
analisis_2 = df_spark.select(
    max("suhu").alias("Suhu_Maksimal"),
    min("suhu").alias("Suhu_Minimal"),
    max("kelembapan").alias("Kelembapan_Maksimal"),
    min("kelembapan").alias("Kelembapan_Minimal")
)
analisis_2.show()


print("📊 ANALISIS 3: Deteksi Aktivitas Pintu")
analisis_3 = df_spark.groupBy("pintu").agg(
    count("*").alias("Frekuensi_Kejadian")
)
analisis_3.show()

# Selesai
spark.stop()
print("Selesai menganalisis data!")