import pytest

import parsl
from parsl.app.app import App
from parsl.data_provider.files import File
from parsl.tests.configs.local_threads_globus import config

parsl.local(config)


@App('python')
def sort_strings(inputs=[], outputs=[]):
    with open(inputs[0].filepath, 'r') as u:
        strs = u.readlines()
        strs.sort()
        with open(outputs[0].filepath, 'w') as s:
            for e in strs:
                s.write(e)


@pytest.mark.local
def test_implicit_staging_ftp():
    """Test implicit staging for an ftp file

    Create a remote input file (ftp) that points to file_test_cpt.txt.
    """

    unsorted_file = File('ftp://ftp.uconn.edu/48_hour/file_test_cpt.txt')

    # Create a local file for output data
    sorted_file = File('sorted.txt')

    f = sort_strings(inputs=[unsorted_file], outputs=[sorted_file])
    f.result()


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action='store_true',
                        help="Count of apps to launch")
    args = parser.parse_args()

    if args.debug:
        parsl.set_stream_logger()

    test_implicit_staging_ftp()
