from helper_download import *
from helper_upload import *

if __name__ == "__main__":
    # make_plugins_json() # uncomment this to update products
    # make_downlinks_json() # uncomment this to update products
    download_driver() # downloads the files
    upload_driver() # upload the files