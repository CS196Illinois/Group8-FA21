import sys
import os
import requests
import argparse
import ipfshttpclient

def save_file(client, list_id, server):
    r = requests.get(server + f'/list/{list_id}').json()

    os.system(f'rm -r {list_id}') 
    os.mkdir(list_id)
    for ipfs_hash, name in r:
        with open(list_id + '/' + name, 'wb') as f:
            f.write(client.cat(ipfs_hash))

def upload_file(client, list_id, file_name, server):
    meta = client.add(file_name)
    requests.get(server + f'/upload?list_id={list_id}&ipfs_hash={meta["Hash"]}&name={file_name}')

if __name__ == '__main__':
    server = 'http://127.0.0.1:5000'
    parser = argparse.ArgumentParser()
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
    
    subparser = parser.add_subparsers()
    uploader = subparser.add_parser('upload')
    uploader.add_argument('--file', help='file name', required=True)
    uploader.add_argument('--list', help='list id', required=True)

    downloader = subparser.add_parser('download')
    downloader.add_argument('--list', help='list id', required=True)


    if len(sys.argv) < 2:
        parser.print_help()
    else:
        args = parser.parse_args()
        if sys.argv[1] == 'upload':
            upload_file(client, args.list, args.file, server)
        elif sys.argv[1] == 'download':
            save_file(client, args.list, server)