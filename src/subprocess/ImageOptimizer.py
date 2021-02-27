import subprocess

class ImageOptimizer:
    def __init__(self, path):
        self.path = path
    def execute(self):
        subprocess.run('optimize-images ' + self.path)
