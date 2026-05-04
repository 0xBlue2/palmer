"""
MGA Title IX document stubs with official URLs for Cohere RAG.

Each document is passed to the Cohere API as a Document object. The 'data' dict
must contain at least 'text' (the content the model reads) plus any metadata
fields you want available in citation sources (title, url).
"""

from cohere.types import Document

# ---------------------------------------------------------------------------
# Document 1 – MGA Title IX Policy Overview
# ---------------------------------------------------------------------------
TITLE_IX_POLICY = Document(
    id="mga-title-ix-policy",
    data={
        "title": "MGA Title IX Policy",
        "url": "https://www.mga.edu/title-ix/",
        "text": (
            "Middle Georgia State University (MGA) is committed to providing an environment free from "
            "discrimination based on sex, in accordance with Title IX of the Education Amendments of 1972. "
            "Title IX prohibits discrimination on the basis of sex in any education program or activity "
            "receiving federal financial assistance. MGA's Title IX policy covers sexual harassment, sexual "
            "assault, dating violence, domestic violence, and stalking. "
            "\n\n"
            "Title IX Coordinator: MGA's designated Title IX Coordinator is responsible for overseeing "
            "compliance with Title IX requirements, including investigating complaints of sex discrimination, "
            "sexual harassment, and related misconduct. The Title IX Coordinator can be reached at the "
            "Office of Title IX Compliance, Middle Georgia State University. Contact information and current "
            "coordinator details are available at https://www.mga.edu/title-ix/. "
            "\n\n"
            "Covered Conduct: MGA's policy prohibits quid pro quo sexual harassment (where an employee "
            "conditions an educational benefit on participation in unwelcome sexual conduct), hostile "
            "environment sexual harassment (unwelcome conduct based on sex that is so severe, pervasive, "
            "and objectively offensive that it effectively denies a person equal access to education), "
            "sexual assault (rape, fondling, incest, or statutory rape as defined under the Clery Act), "
            "dating violence, domestic violence, and stalking. "
            "\n\n"
            "Reporting: Any person may report sex discrimination, sexual harassment, or related misconduct "
            "to MGA's Title IX Coordinator regardless of whether the person reporting is the alleged victim. "
            "Reports may be made in person, by mail, by telephone, or by email. MGA also offers confidential "
            "reporting options through its counseling center and health services. Anonymous reporting is "
            "available through the EthicsPoint hotline. "
            "\n\n"
            "Grievance Process: Upon receiving a formal complaint, MGA will conduct a prompt, fair, and "
            "impartial investigation. Both the complainant and respondent are entitled to an advisor of "
            "their choice (including an attorney) throughout the process. The standard of evidence used "
            "is preponderance of the evidence (more likely than not). Both parties may appeal the outcome. "
            "\n\n"
            "Supportive Measures: MGA will offer supportive measures to the complainant and respondent "
            "as appropriate, including counseling, extensions of deadlines, changes in housing or class "
            "schedules, campus no-contact orders, and increased security. "
            "\n\n"
            "Non-Retaliation: MGA strictly prohibits retaliation against any person who reports sex "
            "discrimination, participates in a Title IX investigation, or opposes a practice made unlawful "
            "under Title IX. Retaliation is itself a violation of MGA policy and Title IX. "
            "\n\n"
            "MGA follows the University System of Georgia Board of Regents Policy on Sexual Misconduct "
            "(Policy 6.7) and all applicable federal regulations, including the 2020 and 2022 Title IX "
            "regulations issued by the U.S. Department of Education. "
        ),
    },
)
# ---------------------------------------------------------------------------
# Document 2 – MGA Annual Security and Fire Safety Report (Clery Report)
# ---------------------------------------------------------------------------
ANNUAL_SECURITY_REPORT = Document(
    id="mga-annual-security-fire-safety-report",
    data={
        "title": "MGA Annual Security and Fire Safety Report (Clery Report)",
        "url": "https://www.mga.edu/police/docs/Annual_Security_Report.pdf",
        "text": (
            "Middle Georgia State University (MGA) publishes an Annual Security and Fire Safety Report "
            "(also called the Clery Report) each year in compliance with the Jeanne Clery Disclosure of "
            "Campus Security Policy and Campus Crime Statistics Act. The report is available online at "
            "https://www.mga.edu/police/annual-report.php and in print from the MGA Department of "
            "Public Safety. "
            "\n\n"
            "Campus Safety Policies: MGA's Department of Public Safety (DPS) provides law enforcement "
            "and security services on all MGA campuses. DPS officers are certified peace officers in "
            "Georgia with full law enforcement authority on campus. The department operates 24 hours a "
            "day, 7 days a week. "
            "\n\n"
            "Crime Reporting: The Clery Act requires MGA to disclose statistics for specific crimes "
            "that occur on campus, in campus residential facilities, on public property adjacent to "
            "campus, and in non-campus buildings. Covered crimes include criminal homicide, sexual "
            "offenses (rape, fondling, incest, statutory rape), robbery, aggravated assault, burglary, "
            "motor vehicle theft, arson, hate crimes, dating violence, domestic violence, and stalking. "
            "\n\n"
            "Sexual Assault Prevention: MGA provides comprehensive primary prevention and awareness "
            "programs for all incoming students and new employees, including programming on: the "
            "definition of sexual harassment and sexual violence; MGA's prohibition of sex "
            "discrimination; safe and positive bystander intervention; recognition of warning signs "
            "of abusive behavior; and available resources. Ongoing awareness and prevention campaigns "
            "are conducted throughout the year. "
            "\n\n"
            "Reporting Mechanisms: Campus Sexual Assault Victims' Bill of Rights – MGA informs "
            "victims of sexual assault of their right to: notify law enforcement and campus security; "
            "seek campus disciplinary action; seek a protective order; receive information about "
            "counseling and support; request changes to academic and living situations. "
            "\n\n"
            "Confidential Reporting: Victims who wish to maintain confidentiality may speak with "
            "campus counselors and health service providers. Professional counselors are not required "
            "to report crimes to law enforcement without the victim's consent. "
            "\n\n"
            "Campus Security Authorities (CSAs): MGA has designated Campus Security Authorities "
            "who are required to report Clery Act crimes to the Department of Public Safety for "
            "statistical reporting purposes. CSAs include deans, directors, department heads, "
            "faculty advisors, coaches, and others with significant responsibility for student "
            "and campus activities. "
            "\n\n"
            "Timely Warnings: MGA will issue a timely warning to the campus community whenever "
            "a Clery Act crime is reported that poses a serious or continuing threat to students "
            "and employees. Timely warnings are distributed via the MGA Alert emergency notification "
            "system, which includes email, text message, and campus siren systems. "
            "\n\n"
            "Fire Safety: The annual report also contains fire safety statistics and policies for "
            "on-campus student housing. MGA student housing facilities are equipped with smoke "
            "detectors, fire suppression systems, and fire extinguishers. Fire drills are conducted "
            "each semester in residential facilities. "
        ),
    },
)

# ---------------------------------------------------------------------------
# Document 3 – USG Board of Regents Sexual Misconduct Policy (Policy 6.7)
# ---------------------------------------------------------------------------
USG_SEXUAL_MISCONDUCT_POLICY = Document(
    id="usg-bor-sexual-misconduct-policy",
    data={
        "title": "University System of Georgia Board of Regents Sexual Misconduct Policy (Policy 6.7)",
        "url": "https://www.usg.edu/policymanual/section6/C2655",
        "text": (
            "The University System of Georgia (USG) Board of Regents Policy 6.7 – Sexual Misconduct "
            "establishes system-wide standards for preventing and addressing sexual misconduct at all "
            "USG institutions, including Middle Georgia State University. "
            "\n\n"
            "Prohibited Conduct: The policy prohibits sexual harassment (including quid pro quo harassment "
            "and hostile environment harassment), sexual assault, dating violence, domestic violence, "
            "stalking, and retaliation. These prohibitions apply to all members of the university "
            "community: students, faculty, staff, and third parties. "
            "\n\n"
            "Jurisdiction: USG institutions have jurisdiction over conduct that occurs: (1) on campus "
            "or other property owned or controlled by the institution; (2) in the context of an "
            "institution-sponsored program or activity; or (3) off campus where the conduct creates "
            "a hostile environment on campus or has continuing effects on campus. "
            "\n\n"
            "Mandatory Reporting: All USG employees (with limited exceptions for confidential "
            "employees) are mandatory reporters who must promptly notify the Title IX Coordinator "
            "when they have knowledge of sexual misconduct. "
            "\n\n"
            "Standard of Evidence: USG institutions use the preponderance of evidence standard "
            "(more likely than not) in determining responsibility. "
            "\n\n"
            "Institutional Obligations: Each USG institution must: designate a Title IX Coordinator; "
            "publish a non-discrimination notice; maintain grievance procedures; provide training to "
            "all relevant personnel; and conduct annual assessments of its sexual misconduct program. "
        ),
    },
)

resources = open("backend/templates/pages/resources.md", "r").read()
# chunk resources into sections for better retrieval and citation
resources_sections = resources.split("\n## ")
resources_sections = [section.strip() for section in resources_sections if section.strip()]
WEBSITE_RESOURCES_PAGE = Document(
    id="website-resources-page",
    data={
        "title": "Website Resources Page",
        "url": "/resources",
        "text": (
            resources_sections
        ),
    },
)

# All documents to pass to the Cohere API
ALL_DOCUMENTS = [
    TITLE_IX_POLICY,
    ANNUAL_SECURITY_REPORT,
    USG_SEXUAL_MISCONDUCT_POLICY,
    WEBSITE_RESOURCES_PAGE,
]
