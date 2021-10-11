from jinja2.environment import Environment
from streamingcli.project.local_project_config import LocalProjectConfigIO
from streamingcli.project.template_loader import TemplateLoader
from dataclasses import dataclass
import click


@dataclass
class ProviderConfig:
    templateName: str
    outputFileName: str


class CICDInitializer:
    @staticmethod
    def setup_cicd(provider: str):
        provider_config = CICDInitializer.get_providers_config(provider)
        local_project_config = LocalProjectConfigIO.load_project_config()
        project_name = local_project_config.project_name
        cicd_yaml = CICDInitializer.generate_from_template(provider_config.templateName, project_name)
        CICDInitializer.save_yaml_file(cicd_yaml, provider_config.outputFileName)
        click.echo(
            f"Initialized {provider} CICD configuration file for project: {project_name}"
        )

    @staticmethod
    def generate_from_template(template_name: str, project_name: str) -> str:
        template = TemplateLoader.load_project_template(template_name)
        return Environment().from_string(template).render(project_name = project_name)

    @staticmethod
    def save_yaml_file(yaml: str, otput_file_name: str):
        with open(f"./{otput_file_name}", "w") as cicd_file:
            cicd_file.write(yaml)

    @staticmethod
    def get_providers_config(provider: str) -> ProviderConfig:
        providers_dict = {
            "gitlab": ProviderConfig("gitlab-ci.yml", ".gitlab-ci.yml")
        }
        return providers_dict[provider]