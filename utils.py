import glob, requests, json


def make_data_request(url, data):
    """
    Post textual data and return json
    :param url: url to send to
    :param data: textual payload
    :return: json response
    """
    resp = requests.post(url, data=data).json()
    return resp


def get_tranql_queries(root_dir):
    """
    Returns set of files in root_dir
    :param root_dir: path to get files from
    :return: list of files
    """
    # Remove trailing path sep
    root_dir = root_dir.rstrip('/').rstrip('\\')
    files = glob.glob(f'{root_dir}/*')
    queries = []
    for f in files:
        with open(f) as stream:
            queries.append((f, stream.read()))
    return queries


def write_out_response(file_name, data):
    """
    Writes json to file
    :param file_name: output file name
    :param data: to write
    :return:
    """
    with open(file_name, 'w') as stream:
        json.dump(data, stream, indent=2)

