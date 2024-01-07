import yaml
from pathlib import Path
from log_utils import appname

# Define the configuration
default_config = {
    'host': '127.0.0.1',
    'osc_port': 9000
}


def get_config_path():
    # Construct the path to the configuration file
    config_dir = Path.home().joinpath('.config', appname)
    config_dir.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
    return config_dir.joinpath('config.yaml')

def store_config(config):
    config_path = get_config_path()
    with open(config_path, 'w') as file:
        yaml.dump(config, file)
    print(f"Configuration stored at {config_path}")

def retrieve_config():
    config_path = get_config_path()
    if not config_path.exists():
        print("Config file does not exist. Creating a default one.")
        store_config(default_config)
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)


# Example usage
def main():
    # Retrieve the configuration
    retrieved_config = retrieve_config()
    print(f"Retrieved configuration: {retrieved_config}")


if __name__ == "__main__":
    main()
