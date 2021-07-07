import os
from utils import get_tranql_queries, make_data_request, write_out_response
import nbformat as nbf


tranql_url = "https://heal.renci.org/tranql/tranql/query"


def main():
    queries = get_tranql_queries('./tranql_queries')
    q_responses = []
    for input_file_name, q in queries:
        response = make_data_request(tranql_url, q)
        q_responses.append(response)
        file_name = os.path.basename(input_file_name).split('.')[0]
        write_out_response(f"tranql_output/{file_name}.json", response)

def generate_notebook(notebook_file_name):
    """
    Generates ipython notebook to view results
    :param notebook_file_name:
    :return:
    """
    queries = get_tranql_queries('./tranql_queries')
    nb = nbf.v4.new_notebook()
    nb['cells'] = []
    import_code = """
from gamma_viewer import GammaViewer
from IPython.display import display
import json
    """
    nb['cells'].append(nbf.v4.new_code_cell(import_code))
    for file_name, query in queries:
        output_file = 'tranql_output/' + os.path.basename(file_name).split('.')[0] + '.json'
        text_cell =f"""
Query : 
{query}"""
        code_cell = f"""
with open("{output_file}") as stream:
    data = json.load(stream)
    viewer = GammaViewer(props={{"data": data}})
    display(viewer)
        """
        nb['cells'] += [nbf.v4.new_markdown_cell(text_cell), nbf.v4.new_code_cell(code_cell)]
        with open(notebook_file_name, 'w') as stream:
            nbf.write(nb, stream)


if __name__ == '__main__':
    main()
    generate_notebook("viewer.ipynb")
