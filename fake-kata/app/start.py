import os
# import socket

import uvicorn
# from helper.ssl_gen import generate_selfsigned_cert


if __name__ == "__main__":
    # hsn = socket.gethostname()
    # ip = socket.gethostbyname(hsn)
    #
    # generate_selfsigned_cert(
    #     hostname=os.getenv('COMMON_NAME', 'localhost'),
    #     ip_addresses=[ip, '127.0.0.1', '0.0.0.0'],
    #     KEY_FILE=os.getenv('KEY', "private.key"),
    #     CERT_FILE=os.getenv("CERT", "selfsigned.crt"),
    # )
    uvicorn.run(
        "main:app",
        host=os.getenv('HOST', '0.0.0.0'),
        port=int(os.getenv('PORT', 443)),
        # ssl_keyfile=os.getenv('KEY', "private.key"),
        # ssl_certfile=os.getenv("CERT", "selfsigned.crt"),
        workers=int(os.getenv("WORKERS", 5)),
        reload=bool(os.getenv("RELOAD", False)),
        http="httptools",
        log_level='debug'
    )
