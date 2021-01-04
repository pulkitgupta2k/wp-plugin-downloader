from helper_download import *
from helper_upload import *
from get_cookie import cookie_driver

if __name__ == "__main__":
    # Login to GPL
    cookie_driver()

    ####################################

    # GET DOWNLOAD LINKS SECTION
    # - Plugins
    # make_plugins_json()  # uncomment this to update products
    # make_downlinks_json()  # uncomment this to update products
    # - Themes
    # make_themes_json  # uncomment this to update products
    # make_downlinks_json_themes()  # uncomment this to update products

    ####################################

    # DOWNLOAD PLUGINS AND THEMES
    # - Plugins
    download_driver()  # downloads the files
    # - Themes
    download_driver_themes()  # downloads the files

    ####################################

    # UPLOAD TO PLESK
    # - Plugins
    upload_driver()  # upload the files
    # - Themes
    upload_driver_themes()  # downloads the files
