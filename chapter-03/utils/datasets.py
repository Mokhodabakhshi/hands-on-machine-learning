import requests
import tarfile


def download_and_extract_dataset(url, path):
    file_name = url.split("/")[-1]
    if not file_name:
        file_name = "dataset.tar"
    try:
        with requests.get(url) as r:
            r.raise_for_status()
            with open(file_name, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    except requests.exceptions.RequestException as e:
        print(f"error : {e}")
        return
    try:
        with tarfile.open(file_name, "r:*") as tar:
            tar.extractall(path, filter="data")
        print("successfuly extracted file")
    except tarfile.TarError as e:
        print(f"error to extracting tar file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        