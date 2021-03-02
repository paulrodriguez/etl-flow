ifrom dependency_injector import containers, providers
from ..sources.FileList import FileList

class SourceContainer(containers.DeclarativeContainer):
    filelist_factory = providers.Factory(FileList)

    @staticmethod
    def get_object():
        return SourceContainer()
