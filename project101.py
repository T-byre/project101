import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filenames in files:
                local_path = os.path.join(root, filenames)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)
                with open(file_from, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path,mode=WriteMode('overwrite'))


        

def main():
    access_token = 'sl.BHrVdPMruxsFoQpt9wrkiooDCRrSo8DAHjWmC7ZuhJwhCSKJjZyojOX2__cAeEBSLWoXUyIJ9pNPXAo3iIp-DSdgulxJT7vXKdqrQ2d5lNxx39o3qm8B_qmVVM7sWX7rRU4iAJkmFcbW'
    transferData = TransferData(access_token)

    file_from = 'C:/Users/18472/Downloads/c100/demo'
    file_to = '/test_dropbox1'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()