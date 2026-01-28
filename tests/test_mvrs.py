from datetime import datetime
from pathlib import Path
import tempfile

from atlas.phase_i.core.types import ContextSnapshot, ExperimentRecord, Outcome
from atlas.phase_i.storage.ledger import AppendOnlyLedger


def test_i_01_01_full_context():
    # I-01.01: полный контекст — обязательные поля должны существовать
    ctx = ContextSnapshot(
        timestamp=datetime.now(),
        timezone="UTC",
        methodology_ref="mvrs-test-v1",
        network_profile={"latency_ms": 42},
        client_stack={"python": "3.13"},
    )
    d = ctx.to_dict()
    assert d["timezone"] == "UTC"
    assert d["methodology_ref"] == "mvrs-test-v1"
    assert "latency_ms" in d["network_profile"]


def test_i_02_01_append_only():
    # I-02.01: ledger только append (архитектурно: нет delete/overwrite API)
    with tempfile.TemporaryDirectory() as tmp:
        ledger = AppendOnlyLedger(Path(tmp))

        ctx = ContextSnapshot(
            timestamp=datetime.now(),
            timezone="UTC",
            methodology_ref="mvrs-test-v1",
        )
        rec = ExperimentRecord(
            config_id="cfg_dummy",
            context=ctx,
            outcome=Outcome.SUCCESS,
            execution_hash="exec_dummy",
            chain_hash="chain_genesis",
        )

        h = ledger.append(rec)
        # файл должен появиться
        p = Path(tmp) / f"{h}.json"
        assert p.exists()

        # и важное: удаления API нет
        assert not hasattr(ledger, "delete")
        assert not hasattr(ledger, "remove")
