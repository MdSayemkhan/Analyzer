import pandas as pd
from data_analyzer import DataAnalyzer 

def test_summary_statistics():
    data = pd.DataFrame({
        'col1': [1, 2, 3, 4, 5],
        'col2': [5, 4, 3, 2, 1]
    })
    analyzer = DataAnalyzer(data)
    summary = analyzer.summary_statistics()
    assert summary['col1']['mean'] == 3

def test_handle_missing():
    data = pd.DataFrame({
        'col1': [1, 2, None, 4, 5],
        'col2': [5, None, 3, None, 1]
    })
    analyzer = DataAnalyzer(data)
    analyzer.handle_missing(strategy='fill', fill_value=0)
    assert analyzer.data.isnull().sum().sum() == 0
