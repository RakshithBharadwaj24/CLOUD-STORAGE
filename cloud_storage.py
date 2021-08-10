import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A1xWkm4gA63kH4HtrV621S64-DnQBiI5mEsH5eQopNSVXO1-3fq8NRwP3mmEvyK2brjYN0luvyFWdYL64fj2m9_S97L89Xjb4YuueYe5gKIJwZBB-zTc2d_HkRajNT8T1uSnV9c'
    transferData = TransferData(access_token)

    file_from = "c:/users/dinesh/desktop/file1.txt"
    file_to ="/upload_cloud/test.txt"

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
