import tarfile
import os
import re
import zipfile
import argparse
import shutil


def extract_tar_n_get_out_dir(path_of_tar_gz):
    input_dir_name = os.path.dirname(path_of_tar_gz)
    input_file_name = os.path.basename(path_of_tar_gz)
    matches = re.finditer("2020\d{10,12}.tar.gz", input_file_name)
    date_time_of_input_file = None
    for match in matches:
        date_time_of_input_file = match.group().rstrip(".tar.gz")

    with tarfile.open(path_of_tar_gz, 'r:gz') as tf:
        tf.extractall(input_dir_name)

    report_file_to_delete = os.path.join(input_dir_name, date_time_of_input_file + "_report.tar.gz")
    print("delete " + report_file_to_delete)
    os.remove(report_file_to_delete)
    print("delete " + path_of_tar_gz)
    os.remove(path_of_tar_gz)
    # The above extract will extract the required output files at a folder named as date_time_of_input_file
    # Thereby we get extracted_folder_path using below statement
    extracted_folder_path = os.path.join(input_dir_name, date_time_of_input_file)
    print(extracted_folder_path)
    return extracted_folder_path


def read_a_tar_gz_having_dup_usn_n_extract_bil(path_of_tar_gz,input_base_directory):
    out_dir = os.path.join(input_base_directory, "Bil_Out_dir")
    location_zipped_bil_files_folders = extract_tar_n_get_out_dir(path_of_tar_gz)

    delete_location_zipped_bil_files_folders = True
    for c_path, dirs, files in os.walk(location_zipped_bil_files_folders):
        for file in files:
            if re.search(".*.zip", file):
                zipped_bil_file_path = os.path.join(c_path, file)
                try:
                    with zipfile.ZipFile(zipped_bil_file_path) as zip_file_ob:
                        zip_file_ob.extractall(out_dir)
                except (FileNotFoundError, EOFError, zipfile.BadZipFile):
                    print("Failed to extract {}".format(zipped_bil_file_path))
                    delete_location_zipped_bil_files_folders = False
                else:
                    os.remove(zipped_bil_file_path)

    else:
        if delete_location_zipped_bil_files_folders:
            shutil.rmtree(location_zipped_bil_files_folders)


def extract_bill_from_all_tar_gz(input_base_directory):
    file_list = os.listdir(input_base_directory)
    for file in file_list:
        if file.endswith(".tar.gz"):
            file_path = os.path.join(input_base_directory, file)
            read_a_tar_gz_having_dup_usn_n_extract_bil(file_path, input_base_directory)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Input_dir_having_tar_gz_file", help="Please provide the location where input *tar.gz files are located")
    args = parser.parse_args()
    Base_input_directory = args.Input_dir_having_tar_gz_file
    extract_bill_from_all_tar_gz(Base_input_directory)

