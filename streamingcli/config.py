from pathlib import Path

PROJECT_LOCAL_CONFIG_FILE_NAME = ".streaming_config.yml"
PROJECT_K8S_CONFIGMAP_KEY = "project_configmap.json"
PLATFORM_K8S_CONFIGMAP_NAME = "streaming-platform-config"
PLATFORM_K8S_CONFIGMAP_KEY = "platform_config.json"
PLATFORM_K8S_SECRET_NAME = "streaming-platform-secret"
PLATFORM_DEFAULT_DEPLOYMENT_TARGET_NAME = "default"
PROFILE_ENV_VARIABLE_NAME = "SCLI_PROFILE"
SCLI_CONFIG_DIR_NAME = ".scli"
DEFAULT_PROFILE_DIR = f"{str(Path.home())}/{SCLI_CONFIG_DIR_NAME}"
DEFAULT_PROFILE_PATH = f"{DEFAULT_PROFILE_DIR}/profiles.yml"
PYTHON_TEMPLATE_PROJECT = "PYTHON_TEMPLATE_PROJECT"
JUPYTER_TEMPLATE_PROJECT = "JUPYTER_TEMPLATE_PROJECT"
DEFAULT_FLINK_APP_NAME = "flink_app.py"
DEFAULT_NOTEBOOK_NAME = "notebook.ipynb"
ADDITIONAL_DEPENDENCIES_DIR = "/app/lib"