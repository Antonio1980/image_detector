import configparser
import os
from src import src_dir


def get_parser(config):
    parser = configparser.ConfigParser()
    with open(config, mode='r', buffering=-1, closefd=True):
        parser.read(config)
        return parser


class BaseConfig:

    config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.cfg')
    parser = get_parser(config_file)

    IMAGE_OUTPUT = src_dir + parser.get('PATH', 'output_image')
    IMAGE_INPUT = src_dir + parser.get('PATH', 'input_image')
    LOGS = src_dir + parser.get('PATH', 'logs')
