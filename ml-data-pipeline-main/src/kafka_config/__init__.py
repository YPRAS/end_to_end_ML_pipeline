
import os


#Authentication 
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"

#Cloud Api details 
API_KEY = "D3GGCVRC5D5MZUJU"#os.getenv('API_KEY',None)
ENDPOINT_SCHEMA_URL  = "https://psrc-777rw.asia-south2.gcp.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)
API_SECRET_KEY = "3L3bplDcuDpDUS+qO7olwsPin36tjSYvVTf8wcc0nFx2/zUpsLwHk0SsJ1/y4AWz" #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = "pkc-xrnwx.asia-south2.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)
SCHEMA_REGISTRY_API_KEY = "2ZHZOG6IE426I3LS" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "msI8sJnOGUCso/jH/e1SMkYNA/+LJyY9LBwNUoSx0TBddMURBA4dq44xMbYvNgYB" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    #print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

