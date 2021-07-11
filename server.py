import uvicorn
import ssl

if __name__ == '__main__':
    uvicorn.run("src.main:app",
                host="0.0.0.0",
                port=8001,
                reload=True,
                # ssl_version=ssl.PROTOCOL_SSLv23,
                # cert_reqs=ssl.CERT_OPTIONAL,
                # ssl_keyfile="./key.pem",  # Note that the generated certificates
                # ssl_certfile="./cert.pem",
                ssl_keyfile="src/localhost+2-key.pem",
                ssl_certfile="src/localhost+2.pem"
                )