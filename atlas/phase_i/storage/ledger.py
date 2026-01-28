import hashlib
import json
from pathlib import Path

from ..core.types import ExperimentRecord


class AppendOnlyLedger:
    """
    I-02.01: Append-only хранилище.
    Контракт: append(record) -> content_hash (str)
    Файл: <content_hash>.json
    """

    def __init__(self, storage_path: Path):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)

    def append(self, record: ExperimentRecord) -> str:
        record_dict = record.to_dict()
        record_json = json.dumps(record_dict, sort_keys=True, ensure_ascii=False)
        content_hash = hashlib.sha256(record_json.encode("utf-8")).hexdigest()

        file_path = self.storage_path / f"{content_hash}.json"
        if file_path.exists():
            return content_hash  # идемпотентно

        file_path.write_text(record_json, encoding="utf-8")
        return content_hash
