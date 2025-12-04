# app/utils/tmp_setup.py
import os
import tempfile
from pathlib import Path

def ensure_writable_tmp():
    """
    Try to create and use a writable temp folder.
    Prefer /tmp (Linux serverless), else fallback to tempfile.gettempdir().
    Returns the chosen tmp dir path as string.
    """
    candidates = ["/tmp", tempfile.gettempdir()]
    for base in candidates:
        try:
            p = Path(base) / "x2p_tmp"
            p.mkdir(parents=True, exist_ok=True)
            if os.access(str(p), os.W_OK):
                os.environ["TMPDIR"] = str(p)
                os.environ["TMP"] = str(p)
                os.environ["TEMP"] = str(p)
                tempfile.tempdir = str(p)
                return str(p)
        except Exception:
            continue
    # fallback to system tempdir (do not raise)
    return tempfile.gettempdir()
