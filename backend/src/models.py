from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import INET, MACADDR, UUID, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from .database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(INET, nullable=False)
    mac_address = Column(MACADDR, nullable=False, index=True)
    manufacturer = Column(String(255))
    device_type = Column(String(100))
    first_seen = Column(TIMESTAMP, server_default=func.now())
    last_seen = Column(TIMESTAMP, server_default=func.now(), index=True)
    is_flagged = Column(Boolean, default=False)
    is_marked_safe = Column(Boolean, default=False)
    scan_id = Column(UUID(as_uuid=True))

class ThreatMac(Base):
    __tablename__ = "threat_macs"

    id = Column(Integer, primary_key=True, index=True)
    mac_address = Column(MACADDR, unique=True, nullable=False, index=True)
    threat_type = Column(String(100), nullable=False)
    description = Column(Text)
    severity = Column(String(20))
    added_date = Column(TIMESTAMP, server_default=func.now())
    source = Column(String(255))

class PhishingUrl(Base):
    __tablename__ = "phishing_urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(Text, unique=True, nullable=False)
    domain = Column(String(255), nullable=False, index=True)
    description = Column(Text)
    category = Column(String(100))
    added_date = Column(TIMESTAMP, server_default=func.now())
    last_verified = Column(TIMESTAMP)
    is_active = Column(Boolean, default=True)

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    alert_type = Column(String(50), nullable=False)
    severity = Column(String(20))
    title = Column(String(255), nullable=False)
    description = Column(Text)
    details = Column(JSONB)
    status = Column(String(20), default='active', index=True)
    justification = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now(), index=True)
    resolved_at = Column(TIMESTAMP)
    resolved_by = Column(String(100))

class ScanHistory(Base):
    __tablename__ = "scan_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    scan_date = Column(TIMESTAMP, server_default=func.now(), index=True)
    devices_found = Column(Integer, default=0)
    new_devices = Column(Integer, default=0)
    threats_detected = Column(Integer, default=0)
    scan_duration_seconds = Column(Integer)
    network_range = Column(String(50))
    status = Column(String(20))

class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    key_name = Column(String(100), unique=True, nullable=False)
    key_hash = Column(String(255), nullable=False)
    component = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.now())
    last_used = Column(TIMESTAMP)
    is_active = Column(Boolean, default=True)
