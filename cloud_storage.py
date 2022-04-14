import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BFfnZdpuYFSZF5QWey5AKKdw9emRaQidLfIrQH9P8K2GiKRmAr72jowQO2jVh42VNxg1dOTW1cLQC6Bf8XjREfld3HnyKmC1p4jNf-AqsH5295_zovCjvWGNOM27SVseZV7PRHQ'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
