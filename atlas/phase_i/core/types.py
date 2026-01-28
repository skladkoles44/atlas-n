from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict


class Outcome(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    ERROR = "ERROR"


@dataclass(frozen=True)
class ContextSnapshot:
    """I-01.01: Полный контекст эксперимента (минимальный каркас)."""

    timestamp: datetime
    timezone: str
    methodology_ref: str
    network_profile: Dict[str, Any] = field(default_factory=dict)
    client_stack: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp.isoformat(),
            "timezone": self.timezone,
            "methodology_ref": self.methodology_ref,
            "network_profile": self.network_profile,
            "client_stack": self.client_stack,
        }


@dataclass(frozen=True)
class ExperimentRecord:
    """I-02.01: Иммутабельная запись эксперимента (append-only слой хранит её как есть)."""

    config_id: str
    context: ContextSnapshot
    outcome: Outcome
    execution_hash: str
    chain_hash: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "config_id": self.config_id,
            "context": self.context.to_dict(),
            "outcome": self.outcome.value,
            "execution_hash": self.execution_hash,
            "chain_hash": self.chain_hash,
        }
