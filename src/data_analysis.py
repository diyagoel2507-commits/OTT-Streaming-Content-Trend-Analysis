
from pathlib import Path
import pandas as pd

# Locate the project dataset
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "netflix_titles.csv"


def load_data():
    """Load the Netflix titles dataset."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_PATH}. "
            "Please place netflix_titles.csv inside the data folder."
        )

    return pd.read_csv(DATA_PATH)


def show_data_overview(df):
    """Display basic dataset information."""
    print("=" * 50)
    print("OTT STREAMING CONTENT ANALYSIS")
    print("=" * 50)

    print(f"\nTotal records: {len(df)}")
    print(f"Total columns: {len(df.columns)}")

    print("\nMissing values by column:")
    print(df.isnull().sum())

    print("\nDuplicate rows:", df.duplicated().sum())


def analyze_content_types(df):
    """Count movies and TV shows."""
    print("\nCONTENT TYPE DISTRIBUTION")
    print(df["type"].value_counts())


def analyze_release_years(df):
    """Show the most common release years."""
    print("\nTOP 10 RELEASE YEARS")
    print(
        df["release_year"]
        .value_counts()
        .head(10)
        .sort_index()
    )


def analyze_countries(df):
    """Count titles by individual country."""
    countries = (
        df["country"]
        .dropna()
        .str.split(", ")
        .explode()
        .str.strip()
    )

    print("\nTOP 10 COUNTRIES")
    print(countries.value_counts().head(10))


def analyze_genres(df):
    """Count titles by individual listed genre."""
    genres = (
        df["listed_in"]
        .dropna()
        .str.split(", ")
        .explode()
        .str.strip()
    )

    print("\nTOP 10 GENRES")
    print(genres.value_counts().head(10))


def main():
    df = load_data()

    show_data_overview(df)
    analyze_content_types(df)
    analyze_release_years(df)
    analyze_countries(df)
    analyze_genres(df)


if __name__ == "__main__":
    main()
