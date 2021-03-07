import fire

import yaml
from src.Util import Util
from src.containers.SubprocessContainer import SubprocessContainer
from dependency_injector import containers, providers

class Workflow(object):
  """Workflow class"""

  def run(self,name):
      with open(Util.app_dir()+'.workflows/workflows.yml', 'r') as file:
          data = yaml.load(file, Loader=yaml.Loader)
          if name in data:
              # TODO: parse workflow here
              pass
  def test(self):
      obj = subprocess_container.test_factory()
      print(obj)

      obj2 = subprocess_container.test2_factory()
      print(obj2)

if __name__ == '__main__':

    SubprocessContainer.test_factory = providers.Object(10)
    setattr(SubprocessContainer, 'test2_factory', providers.Object(20))
    subprocess_container = SubprocessContainer.get_object()
    fire.Fire(Workflow)
