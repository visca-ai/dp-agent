from os import getenv

from state_formatters.dp_formatters import *

DB_NAME = getenv('DB_NAME', 'test')
DB_HOST = getenv('DB_HOST', '127.0.0.1')
DB_PORT = getenv('DB_PORT', 27017)
DB_PATH = getenv('DB_PATH', '/data/db')

# TODO: move response timeout to transport settings
# TODO: change naming to transport settings
HIGHLOAD_SETTINGS = {
    'agent_namespace': 'deeppavlov_agent',
    'agent': {
        'name': 'dp_agent',
        'response_timeout_sec': 120
    },
    'channels': {},
    'transport': {
        'type': 'AMQP',
        'AMQP': {
            'host': '127.0.0.1',
            'port': 5672,
            'login': 'guest',
            'password': 'guest',
            'virtualhost': '/'
        }
    }
}

MAX_WORKERS = 4

AGENT_ENV_FILE = "agent.env"

# TODO: may be we should move default values setting for service config params from code to special config section
# Implicit service default params:
# batch_size = 1
# infer_url = http://127.0.0.1:5000/model

SKILLS = [
    {
        "name": "odqa",
        "batch_size": 1,
        "protocol": "http",
        "host": "127.0.0.1",
        "port": 2080,
        "endpoint": "model",
        "path": "odqa/ru_odqa_infer_wiki",
        "env": {
            "CUDA_VISIBLE_DEVICES": ""
        },
        "dockerfile": "dockerfile_skill_cpu",
        "formatter": odqa_formatter
    },
    {
        "name": "chitchat",
        "batch_size": 1,
        "protocol": "http",
        "host": "127.0.0.1",
        "port": 2081,
        "endpoint": "model",
        "path": "faq/tfidf_autofaq",
        "env": {
            "CUDA_VISIBLE_DEVICES": ""
        },
        "profile_handler": True,
        "dockerfile": "dockerfile_skill_cpu",
        "formatter": chitchat_formatter
    }
]

ANNOTATORS_1 = [
    {
        "name": "ner",
        "batch_size": 1,
        "protocol": "http",
        "host": "127.0.0.1",
        "port": 2083,
        "endpoint": "model",
        "path": "ner/ner_rus",
        "env": {
            "CUDA_VISIBLE_DEVICES": ""
        },
        "dockerfile": "dockerfile_skill_cpu",
        "formatter": ner_formatter
    }
]

ANNOTATORS_2 = [
    {
        "name": "sentiment",
        "batch_size": 1,
        "protocol": "http",
        "host": "127.0.0.1",
        "port": 2084,
        "endpoint": "model",
        "path": "classifiers/rusentiment_cnn",
        "env": {
            "CUDA_VISIBLE_DEVICES": ""
        },
        "dockerfile": "dockerfile_skill_cpu",
        "formatter": sentiment_formatter
    }
]

ANNOTATORS_3 = []

SKILL_SELECTORS = [
    {
        "name": "chitchat_odqa",
        "batch_size": 1,
        "protocol": "http",
        "host": "127.0.0.1",
        "port": 2082,
        "endpoint": "model",
        "path": "classifiers/rusentiment_bigru_superconv",
        "env": {
            "CUDA_VISIBLE_DEVICES": ""
        },
        "dockerfile": "dockerfile_skill_cpu",
        "formatter": chitchat_odqa_formatter
    }
]

RESPONSE_SELECTORS = []

POSTPROCESSORS = []

DEBUG = True
