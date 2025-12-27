from auth.database import engine, Base


from auth import models as auth_models
from scan import models as scan_models

Base.metadata.create_all(bind=engine)

print("Database and tables created successfully")