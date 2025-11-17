from app.config.database import engine

import app.models.logs as logs

logs.Base.metadata.create_all(bind=engine)
print("Table log created successfully")
