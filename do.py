import os
import logging 

from absl import app
from absl import flags

from utils import parse_helper

LOGGER = logging.getLogger("dummy-gen")

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'project_yml_path', None,
    'the path of the project.yml, normally it is stored on the top of the project.'
)

flags.DEFINE_string(
    'table_suffix', None,
    'suffix appended to the model tables (not overwrite, create views with this suffix)'
)

flags.DEFINE_bool('refresh', False, 'whether to refresh this version of data, not recommended, better to change "data_id".')

class Core:
  PROJ_CONF = parse_helper.parse_project_yml(FLAGS.project_yml_path)
  PROJ_ROOT_PATH = os.path.join(os.getcwd, os.path.dirname(__file__))
  MODEL_PATH = os.path.join(PROJ_ROOT_PATH, PROJ_CONF['models'])
  SEED_PATH = os.path.join(PROJ_ROOT_PATH, PROJ_CONF['seed'])
  STATIC_PATH = os.path.join(PROJ_ROOT_PATH, PROJ_CONF['static'])

  def is_version_data_existed(self):
    """Check if there are already existed data in BQ
    
    Method: iterate all models and 
    """
    # if exists, skip
    # return 

    return True

def main():
# generate data
  # parse project yaml (DONE)
  core = Core()
  # check if this version of data has existed
  # TODO: not using BQ locally
  if core.is_version_data_existed() or FLAGS.refresh:
    LOGGER.info('Data existed. Avoid duplicate generation...')
  else:
  # build graph
    # parse models yaml

    # return graph

  # generate data in order
    # create empty table & seed

    # independent columns

    # static columns

    # ref columns

# post process
  # import data into tables (version), e.g. customers_ken_golden

  # create views without version name (but with suffix if 'table_suffix' provided)
