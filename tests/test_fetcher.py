from get_papers import fetcher

def test_pubmed_id_fetch():
    ids = fetcher.fetch_pubmed_ids("covid-19 vaccine")  # Removed 5
    assert isinstance(ids, list)
    assert all(isinstance(i, str) for i in ids)
