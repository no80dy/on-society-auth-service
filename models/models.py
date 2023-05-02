from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship


metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=True),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("profile_image", Text),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)

oauth_account = Table(
    "oauth_account",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("oauth_name", String(length=100), index=True, nullable=False),
    Column("access_token", String(length=1024), nullable=False),
    Column("expires_at", Integer, nullable=True),
    Column("refresh_token", String(length=1024), nullable=True),
    Column("account_id", String(length=320), index=True, nullable=False),
    Column("account_email", String(length=320), nullable=False),
    Column("user_id", Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False)
)

users_oauth_accounts = relationship(
    "oauth_accounts",
    lazy="joined",
    foreign_keys=[oauth_account.c.user_id],
    uselist=True,
)
