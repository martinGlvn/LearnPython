import boto3
BUCKET_NAME = "martin-bucket-python"

# s3 -> realiza todas las operaciones del servicios "s3" mediante el client ->
s3 = boto3.client("s3")

# Lista de buckets s3 que tenemos en nuestra cuenta ->
buckets_resp = s3.list_buckets()
for bucket in buckets_resp("Buckets"):
    print(bucket)

# Lista de todos los objetos que tenemos dentro de un "bucket" ->
response = s3.list_object_v2(Bucket=BUCKET_NAME)
for obj in response("Contents"):
    print(obj)

# Cargar un archivo en un "bucket" de s3 ->
with open("./profile_martin.jpg", "rb")as f:
    # bucket en el cual se carga y nombre del objeto
    s3.upload_fileobj(f, BUCKET_NAME, "profile_martin.jdp")

# Descargar un archivo desde un "bucket" de s3 ->
s3.download_file(BUCKET_NAME, "descarga.jpg", "nombreDeMiArchivo,jpg")

# Descargar un archivo desde un "bucket" de s3 junto a su "data binary"
with open("download.jpg", "wb")as f:
    s3.download_file(BUCKET_NAME, "nombre.jpg", f)

# URL con tiempo de uso limitado ->
url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": BUCKET_NAME, "Key": "mi_imagen.jpg"},
    ExpiresIn=30  # 30segundos
)
print(url)

# Creacion de "bucket" S3 ->
bucket_location = s3.create_bucket(
    ACL="public-read", Bucket="new-martin-bucket"
)
print(bucket_location)

# Copiar objetos de un "bucket" s3 ->
s3.copy_object(
    ACL="public-read",
    Bucket="nuevo-destinto-bucket",
    CopySource=f"/{BUCKET_NAME}/profile.jpg",
    key="copia.jpg"
)

# Obtener detalles/datos de un objeto de un "bucket" s3 ->
respuestaDatos = s3.get_object(Bucket=BUCKET_NAME, Key="profile.jpg")
print(respuestaDatos)
