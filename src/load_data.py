from pathlib import Path
from urllib.error import HTTPError
import pandas as pd

# Official UCI URLs
UCI_MAT_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student-mat.csv"
UCI_POR_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student-por.csv"

# Backup mirror (GitHub)
GITHUB_MAT_URL = "https://raw.githubusercontent.com/KunjalJethwani/StudentPerformance/master/student-mat.csv"
GITHUB_POR_URL = "https://raw.githubusercontent.com/KunjalJethwani/StudentPerformance/master/student-por.csv"


def _download_with_fallback(primary, backup, sep=";"):
    """Try primary URL, fall back to backup if 404."""
    try:
        return pd.read_csv(primary, sep=sep)
    except HTTPError:
        return pd.read_csv(backup, sep=sep)


def download_student_data(data_dir="data"):
    """Download Math + Portuguese datasets if not already local."""
    data_path = Path(data_dir)
    data_path.mkdir(parents=True, exist_ok=True)

    mat_path = data_path / "student-mat.csv"
    por_path = data_path / "student-por.csv"

    if not mat_path.exists():
        df = _download_with_fallback(UCI_MAT_URL, GITHUB_MAT_URL)
        df.to_csv(mat_path, index=False)

    if not por_path.exists():
        df = _download_with_fallback(UCI_POR_URL, GITHUB_POR_URL)
        df.to_csv(por_path, index=False)

    return mat_path, por_path


def load_student_data(data_dir="data"):
    """Return merged Math + Portuguese datasets."""
    mat_path, por_path = download_student_data(data_dir)
    df_mat = pd.read_csv(mat_path)
    df_por = pd.read_csv(por_path)
    return pd.concat([df_mat, df_por], ignore_index=True)


