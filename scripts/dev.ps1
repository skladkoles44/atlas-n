param(
  [ValidateSet("test","lint","show")]
  [string]$Task = "test"
)

$ErrorActionPreference = "Stop"

# Ensure venv exists
if (!(Test-Path ".\.venv\Scripts\python.exe")) {
  python -m venv .venv
}

# Use venv python explicitly (без "activate", чтобы не зависеть от политики ExecutionPolicy)
$PY = ".\.venv\Scripts\python.exe"

# Bootstrap tooling
& $PY -m pip install -U pip | Out-Host
& $PY -m pip install -r requirements-dev.txt | Out-Host

switch ($Task) {
  "show" {
    & $PY -c "import sys; print(sys.executable)" | Out-Host
    & $PY -c "import site; print(site.getsitepackages())" | Out-Host
  }
  "lint" {
    Write-Host "TODO: lint (добавим позже)"
  }
  default {
    & $PY -m pytest -q | Out-Host
  }
}
