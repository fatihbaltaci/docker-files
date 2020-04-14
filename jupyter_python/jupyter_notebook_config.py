import os
from IPython.lib import passwd

c = get_config()

c.NotebookApp.open_browser = False

c.NotebookApp.ip = "0.0.0.0"
c.NotebookApp.port = 8888

c.NotebookApp.notebook_dir = '/workspace'

c.NotebookApp.allow_root = True

if 'PASSWORD' in os.environ:
    c.NotebookApp.password = passwd(os.environ['PASSWORD'])
    del os.environ['PASSWORD']
