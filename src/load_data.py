from pathlib import Path
import pandas as pd

# UCI dataset URLs
UCI_MAT_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student-mat.csv"
UCI_POR_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student-por.csv"


def download_student_data(data_dir: str = "data"):
    """
    Download the UCI student performance datasets (Math + Portuguese)
    if they are not already present locally.
    """
    data_path = Path(data_dir)
    data_path.mkdir(parents=True, exist_ok=True)

    mat_path = data_path / "student-mat.csv"
    por_path = data_path / "student-por.csv"

    if not mat_path.exists():
        df_mat = pd.read_csv(UCI_MAT_URL, sep=";")
        df_mat.to_csv(mat_path, index=False)

    if not por_path.exists():
        df_por = pd.read_csv(UCI_POR_URL, sep=";")
        df_por.to_csv(por_path, index=False)

    return mat_path, por_path


def load_student_data(data_dir: str = "data") -> pd.DataFrame:
    """
    Ensure the UCI datasets are downloaded, then load and merge them.
    """
    mat_path, por_path = download_student_data(data_dir)
    df_mat = pd.read_csv(mat_path)
    df_por = pd.read_csv(por_path)
    df = pd.concat([df_mat, df_por], ignore_index=True)
    return df

