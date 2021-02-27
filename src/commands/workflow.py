import fire

import yaml
from src.Util import Util
from src.containers.SubprocessContainer import SubprocessContainer

class Workflow(object):
  """Workflow class"""

  def run(self,name):
      with open(Util.app_dir()+'.workflows/workflows.yml', 'r') as file:
          data = yaml.load(file, Loader=yaml.Loader)
          if name in data:
              # TODO: parse workflow here
              pass

if __name__ == '__main__':
    subprocess_container = SubprocessContainer.get_object()
    fire.Fire(Workflow)
