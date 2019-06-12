import socket
import struct
import json
import subprocess
import os

class MYTCPServer:
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allo_reuse_address = False
    