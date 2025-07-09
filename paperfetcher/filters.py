from typing import List, Tuple

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "college", "institute", "school", "department"]
    return not any(word in affiliation.lower() for word in academic_keywords)

def extract_company_authors(authors: List[dict]) -> Tuple[List[str], List[str], str]:
    non_academic_authors = []
    company_affiliations = []
    corresponding_email = ""
    for author in authors:
        if is_non_academic(author["affiliation"]):
            non_academic_authors.append(author["name"])
            company_affiliations.append(author["affiliation"])
            if author["email"] and not corresponding_email:
                corresponding_email = author["email"]
    return non_academic_authors, company_affiliations, corresponding_email
