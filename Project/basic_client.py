import os
import ipfshttpclient

if __name__ == '__main__':
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

    with open('test_file', 'w') as f:
        f.write('CS 196 group 8\n')

    hs = client.add('test_file')['Hash']
    os.system('rm test_file')

    print(client.cat(hs))