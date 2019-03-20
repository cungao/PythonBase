#!D:\Èí¼þ¹¤¾ß\Python_Package\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pycgi==0.1a3','console_scripts','pycgi'
__requires__ = 'pycgi==0.1a3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pycgi==0.1a3', 'console_scripts', 'pycgi')()
    )
