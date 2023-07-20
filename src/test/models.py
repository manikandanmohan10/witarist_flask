import uuid
from src.config.db import db
from sqlalchemy.dialects.postgresql import UUID

class TestTable(db.Model):
    __tablename__ = 'tabTest'

    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
