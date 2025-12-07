from pathlib import Path
from urllib.error import HTTPError
import pandas as pd

# Primary (official) UCI URLs
UCI_MAT_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student-mat.csv"
UCI_POR_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student-por.csv"

# Fallback GitHub mirror URLs (same data)
GITHUB_MAT_URL = "https://raw.githubusercontent.com/KunjalJethwani/StudentPerformance/master/student-mat.csv"
GITHUB_POR_URL = "https://raw.githubusercontent.com/KunjalJethwani/StudentPerformance/master/student-por.csv"


def _download_with_fallback(url_primary: str, url_backup: str, sep: str = ";") -> pd.DataFrame:
    """
    Try to download from the primary URL first.
    If that fails with HTTPError (e.g. 404), use the backup URL.
    """
    try:
        return pd.read_csv(url_primary, sep=sep)
    except HTTPError:
        # Fallback to backup mirror if UCI is unavailable or URL changed
        return pd.read_csv(url_backup, sep=sep)


def download_student_data(data_dir: str = "data"):
    """
    Download the student performance datasets (Math + Portuguese)
    if they are not already present locally.

    Returns
    -------
    (Path, Path): paths to local math and portuguese CSV files
    """
    data_path = Path(data_dir)
    data_path.mkdir(parents=True, exist_ok=True)

    mat_path = data_path / "student-mat.csv"
    por_path = data_path / "student-por.csv"

    if not mat_path.exists():
        df_mat = _download_with_fallback(UCI_MAT_URL, GITHUB_MAT_URL, sep=";")
        df_mat.to_csv(mat_path, index=False)

    if not por_path.exists():
        df_por = _download_with_fallback(UCI_POR_URL, GITHUB_POR_URL, sep=";")
        df_por.to_csv(por_path, index=False)

    return mat_path, por_path


def load_student_data(data_dir: str = "data") -> pd.DataFrame:
    """
    Ensure datasets are downloaded, then load and merge them.
    """
    mat_path, por_path = download_student_data(data_dir)
    df_mat = pd.read_csv(mat_path)
    df_por = pd.read_csv(por_path)
    df = pd.concat([df_mat, df_por], ignore_index=True)
    return df

