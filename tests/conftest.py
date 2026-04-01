import pytest
import pandas as pd
import os
import spacy

@pytest.fixture(scope="session")
def load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        pytest.fail("SpaCy model 'en_core_web_sm' not found. Run 'python -m spacy download en_core_web_sm'")

@pytest.fixture
def dummy_ppl_df():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'dummy_people_table.csv')
    
    if not os.path.exists(csv_path):
        pytest.fail(f"Required test data missing at: {csv_path}")

    df = pd.read_csv(csv_path)
    df.set_index('Unnamed: 0', inplace=True)
    df.index.name = "PID"  
    return df