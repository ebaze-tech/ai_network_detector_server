from auth.database import engine, Base
from auth import models

Base.metadata.create_all(bind=engine)
print("✅ Database created")
