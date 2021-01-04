from helper_download import *
from helper_upload import *
from get_cookie import cookie_driver

if __name__ == "__main__":
    # Login to GPL
    cookie_driver()

    # Plugins section:

    # make_plugins_json()  # uncomment this to update products
    # make_downlinks_json()  # uncomment this to update products
    download_driver()  # downloads the files
    # upload_driver() # upload the files

    ###########################################

    # Themes Section

    # make_themes_json  # uncomment this to update products
    # make_downlinks_json_themes()  # uncomment this to update products
    download_driver_themes()  # downloads the files
    # upload_driver_themes() # downloads the files
