def generate_document(document_type, name, details):
    templates = {
        "Leave Request": f"""LEAVE REQUEST

To, The Concerned Authority

Subject: Leave Request

Dear Sir/Madam,

I, {name}, am requesting leave based on the following details:

{details}

I kindly request that my leave be considered.

Sincerely,
{name}
""",
        "Rental Agreement Draft": f"""RENTAL AGREEMENT - DRAFT

Party/Applicant: {name}

Key details:
{details}

1. Property and tenancy details should be specified.
2. Rent, deposit, duration, and payment terms should be specified.
3. Maintenance and utility responsibilities should be specified.
4. Termination and notice conditions should be specified.

This draft should be reviewed by a qualified legal professional before use.
""",
        "Complaint Letter": f"""FORMAL COMPLAINT - DRAFT

Complainant: {name}

Details:
{details}

To the concerned authority,

I am submitting this complaint regarding the matter described above.
I request that the matter be reviewed and appropriate action be taken.

Sincerely,
{name}
""",
        "Affidavit Draft": f"""AFFIDAVIT - EDUCATIONAL DRAFT

Deponent: {name}

Statement:
{details}

Signature: __________________
Date: ______________________
Place: _____________________

A qualified legal professional should review this document before official use.
"""
    }
    return templates.get(document_type, f"""LEGAL DOCUMENT DRAFT

Name: {name}

Details:
{details}
""")
