import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
sys.path.append(ROOT_DIR)

from app.config.database import engine

import app.models.logs as logs

logs.Base.metadata.create_all(bind=engine)
print("Table log created successfully")
