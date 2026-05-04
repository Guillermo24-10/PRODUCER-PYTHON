from azure.storage.blob import BlobServiceClient


CONN = "AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;"
CONTENEDOR = "entrada"


def subir_json(nombre, contenido):
    client = BlobServiceClient.from_connection_string(CONN, api_version="2019-12-12")
    container = client.get_container_client(CONTENEDOR)

    try:
        container.create_container()
    except:
        pass

    container.upload_blob(name=nombre, data=contenido, overwrite=True)
    print(f"JSON SUBIDO: {nombre}")
