import os
import yaml


# Constants for trading settings
SHIFT_STOCHASTIC_VAL = 200
SHIFT_RSI_VAL = 100

PROJECT_DIR = os.getcwd()
PROJECT_DIR = '/Users/tongcc/dev/projects/trading'

with open(os.path.join(PROJECT_DIR, 'config', 'indicators_config.yaml'), 'r', encoding='utf-8') as f:
    indicator_config = yaml.safe_load(f)