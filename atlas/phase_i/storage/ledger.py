from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Tuple

from atlas.phase_i.core.types import ExperimentRecord


class AppendOnlyLedger:
    """I-02.01: Append-only хранилище.
    Сознательно не имеет delete/update API.
    """

    def __init__(self, storage_dir: Path):
        self.storage_dir = storage_dir
        self.storage_dir.mkdir(parents=True, exist_ok=True)

    def append(self, record: ExperimentRecord) -> Tuple[str, Path]:
        payload = json.dumps(record.to_dict(), ensure_ascii=False, sort_keys=True, indent=2)
        digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        path = self.storage_dir / f"{digest}.json"
        if not path.exists():
            path.write_text(payload, encoding="utf-8")
        return digest, path
