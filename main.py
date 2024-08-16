import shutil

import uvicorn
from multiprocessing import freeze_support
from reflex import constants
from reflex.utils.prerequisites import get_web_dir
import os

if __name__ == "__main__":
    freeze_support()
    web_dir = get_web_dir()
    # Create a .nocompile file to skip compile for backend.
    if not web_dir.exists():
        os.makedirs(web_dir)
    if web_dir.exists():
        (web_dir / constants.NOCOMPILE_FILE).touch()
        shutil.copy('reflex.json', web_dir)
    uvicorn.run('reflex.app_module_for_backend:app.api',
                reload=True,
                timeout_keep_alive=10,
                # reload_dirs="reflex_test",
                reload_excludes=[str(web_dir)],
                workers=2,
                host="0.0.0.0",
                port=8000,
                log_level="info")