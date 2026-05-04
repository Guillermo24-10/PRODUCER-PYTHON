from azure.storage.queue import QueueClient


CONN = "AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;"
QUEUE = "cola-pdf"


def enviar_cola(nombre_archivo):
    queue = QueueClient.from_connection_string(CONN, QUEUE, api_version="2019-12-12")

    try:
        queue.create_queue()
    except Exception as e:
        pass

    queue.send_message(nombre_archivo)
    print(f"Mensaje enviado a cola: {nombre_archivo}")
