import os
import yaml


# Constants for trading settings
SHIFT_STOCHASTIC_VAL = 200
SHIFT_RSI_VAL = 100

with open(os.path.join(os.getcwd(), 'config', 'indicators_config.yaml'), 'r', encoding='utf-8') as f:
    indicator_config = yaml.safe_load(f)