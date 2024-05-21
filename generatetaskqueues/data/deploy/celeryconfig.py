import os
import ssl
import json
# Refer to Celery's configuration documentation for details on these settings.
# https://docs.celeryproject.org/en/stable/userguide/configuration.html

def setBrokerSSL():
    if bool(os.getenv('BROKER_USE_SSL') in ('True', 'true')):
        return {'keyfile': os.environ.get('RABBITMQ_SSL_KEY_FILE'),
                'certfile': os.environ.get('RABBITMQ_SSL_CERT_FILE'),
                'ca_certs': os.environ.get('RABBITMQ_SSL_CA_FILE'),
                'cert_reqs': ssl.CERT_REQUIRED}
    else:
        return None

celery_secrets=json.loads(os.environ.get('HAPI_CELERY_CONFIG'))

# SETUP BROOKER URI
RABBITMQ_DEFAULT_USER = os.environ.get('RABBITMQ_DEFAULT_USER')
RABBITMQ_DEFAULT_PASS = celery_secrets['RABBITMQ_DEFAULT_PASS'] 
RABBITMQ_DEFAULT_VHOST = os.environ.get('RABBITMQ_DEFAULT_VHOST')
RABBITMQ_HOSTNAME= os.environ.get('RABBITMQ_HOST','cybercom-rabbitmq')
RABBITMQ_PORT= os.environ.get('RABBITMQ_PORT','5671')

# Broker Connection
broker_url = f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@{RABBITMQ_HOSTNAME}:{RABBITMQ_PORT}/{RABBITMQ_DEFAULT_VHOST}"
broker_use_ssl = setBrokerSSL()
broker_connection_retry_on_startup = True
worker_send_task_events = True
result_expires = None
accept_content = ['json']

# SETUP MONGO URI
SSL_PATH = os.environ.get('SSL_PATH')
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = celery_secrets['MONGO_PASSWORD']
MONGO_HOSTNAME = os.environ.get('MONGO_HOST','cybercom-mongo')
MONGO_PORT = os.environ.get('MONGO_PORT','27017')
result_backend = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOSTNAME}:{MONGO_PORT}/?ssl=true&tlsCAFile={SSL_PATH}/testca/cacert.pem&tlsCertificateKeyFile={SSL_PATH}/client/mongodb.pem" 

mongodb_backend_settings = {
    "database": os.environ.get('MONGO_DB', "cybercom"),
    "taskmeta_collection": os.environ.get('MONGO_TOMBSTONE_COLLECTION', "tombstone")
}

imports = tuple(os.environ.get('CELERY_IMPORTS').split(','))
