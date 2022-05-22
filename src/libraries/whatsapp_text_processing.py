import os
import datetime
import pandas as pd



def create_df_from_wp_txt(config):

    """
    """

    # Settng up required variables from config...
    OWN_NAME = config["own_name"]
    EXPORT_FORMAT = config["export_format"]
    EXPORT_DIR_PATH = config["export_dir_path"]


    # Change dir to chatistics for analysing chat and exporting csv
    os.chdir(config["chat_dir_path"])


    os.system(f'python parse.py whatsapp --own-name {OWN_NAME} && \
            python export.py -f {EXPORT_FORMAT}')
        # TODO: Implement subprocess to get exxported file name from the terminal output

    onlyfiles = [f for f in os.listdir(EXPORT_DIR_PATH) if os.path.isfile(os.path.join(EXPORT_DIR_PATH, f))]
    parsed_file_path = os.path.join(EXPORT_DIR_PATH,onlyfiles[1])
    print("######", parsed_file_path)

    df = pd.read_csv(parsed_file_path)

    return df


def convert_to_df():
    pass
