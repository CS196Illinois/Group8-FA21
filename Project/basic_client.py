import base58
import ipfshttpclient
from hashlib import sha256

def hash(d):
    h = sha256()
    h.update(d)
    return h.hexdigest()

def hash_file(fname):
    with open(fname, 'rb') as f:
        h = sha256()
        for chunk in iter(lambda: f.read(4096),b''):
            h.update(chunk)
    return h.hexdigest()

if __name__ == '__main__':
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

    with open('test_file', 'w') as f:
        f.write('CS 196 group 8\n')

    hs = client.add('test_file')['hash']
    assert hs == hash_file('test_file')
