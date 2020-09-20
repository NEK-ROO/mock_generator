import yaml

from absl import flags

FLAGS = flags.FLAGS

def parse_project_yml(fname: str) -> dict:
    """Parse project yaml to get project level configs
  
  Args:
    fname: the path of the project.yml

  Output:
    a json from the yaml
  """
    proj_yml = yaml.load(open(fname), Loader=yaml.SafeLoader)
    return proj_yml

def 