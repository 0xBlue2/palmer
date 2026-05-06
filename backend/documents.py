"""
MGA Title IX document stubs with official URLs for Cohere RAG.

Each document is passed to the Cohere API as a Document object. The 'data' dict
must contain at least 'text' (the content the model reads) plus any metadata
fields you want available in citation sources (title, url).
"""

from cohere.types import Document
from backend.helpers import *
from backend.CONSTANTS import *
# import os

documents: list[Document]= []

""""
LOCAL_DOCS = { # todo: better implementation
    "NEW_Title_IX_Policy_effective_2020-08-11.pdf":
        {
            "url": "https://www.mga.edu/title-ix/docs/NEW_Title_IX_Policy_effective_2020-08-11.pdf",
            "title": "Middle Georgia State University Title IX Policy, effective August 2020"
        },
    "USG-BOR-06-07 Sexual Misconduct Policy.pdf":
        { 
            "url": "https://usg.policystat.com/policy/19466143/latest",
            "title": "University System of Georgia Sexual Misconduct Policy"
        }
}

REMOTE_DOCS = {
    "https://www.mga.edu/police/docs/Annual_Security_Report.pdf": {
        "title": "MGA 2025 Annual Security and Fire Safety Report"
    }
}

for filename in os.listdir(RAG_DOCUMENTS_DIR):
    file = Path(RAG_DOCUMENTS_DIR) / filename
    url = LOCAL_DOCS[filename]["url"]
    title = LOCAL_DOCS[filename]["title"]
    documents.extend(chunk_markdown_from_file(path=str(file.absolute()), web_url=url, title=title))


for url in REMOTE_DOCS:
    title = REMOTE_DOCS[url]["title"]
    documents.extend(chunk_markdown_from_url(url=url, title=title))
"""

# manual addition for local file with special url
# could also just move the file to RAG_DOCUMENTS_DIR and add to LOCAL_DOCS
documents.extend(
    chunk_markdown_from_file(
        path="backend/templates/pages/resources.md",
        web_url="/resources",
        title="Website Resources Page"
        )
)

# ---------------------------------------------------------------------------
# Document 1 – MGA Title IX Policy Overview
# ---------------------------------------------------------------------------
TITLE_IX_POLICY = Document(
    id="mga-title-ix-policy",
    data={
        "title": "MGA Title IX Policy",
        "url": "https://www.mga.edu/title-ix/docs/NEW_Title_IX_Policy_effective_2020-08-11.pdf",
        "text": [
            "Middle Georgia State University (MGA) is committed to providing an environment free from discrimination based on sex, in accordance with Title IX of the Education Amendments of 1972.",
            "Title IX prohibits discrimination on the basis of sex in any education program or activity receiving federal financial assistance.",
            "MGA's Title IX policy covers sexual harassment, sexual assault, dating violence, domestic violence, and stalking.",
            "Title IX Coordinator: MGA's designated Title IX Coordinator is responsible for overseeing compliance with Title IX requirements, including investigating complaints of sex discrimination, sexual harassment, and related misconduct.",
            "The Title IX Coordinator can be reached at the Office of Title IX Compliance, Middle Georgia State University.",
            "Contact information and current coordinator details are available at https://www.mga.edu/title-ix/.",
            "Covered Conduct: MGA's policy prohibits quid pro quo sexual harassment (where an employee conditions an educational benefit on participation in unwelcome sexual conduct), hostile environment sexual harassment (unwelcome conduct based on sex that is so severe, pervasive, and objectively offensive that it effectively denies a person equal access to education), sexual assault (rape, fondling, incest, or statutory rape as defined under the Clery Act), dating violence, domestic violence, and stalking.",
            "Reporting: Any person may report sex discrimination, sexual harassment, or related misconduct to MGA's Title IX Coordinator regardless of whether the person reporting is the alleged victim.",
            "Reports may be made in person, by mail, by telephone, or by email.",
            "MGA also offers confidential reporting options through its counseling center and health services.",
            "Anonymous reporting is available through the EthicsPoint hotline.",
            "Grievance Process: Upon receiving a formal complaint, MGA will conduct a prompt, fair, and impartial investigation.",
            "Both the complainant and respondent are entitled to an advisor of their choice (including an attorney) throughout the process.",
            "The standard of evidence used is preponderance of the evidence (more likely than not).",
            "Both parties may appeal the outcome.",
            "Supportive Measures: MGA will offer supportive measures to the complainant and respondent as appropriate, including counseling, extensions of deadlines, changes in housing or class schedules, campus no-contact orders, and increased security.",
            "Non-Retaliation: MGA strictly prohibits retaliation against any person who reports sex discrimination, participates in a Title IX investigation, or opposes a practice made unlawful under Title IX.",
            "Retaliation is itself a violation of MGA policy and Title IX.",
            "MGA follows the University System of Georgia Board of Regents Policy on Sexual Misconduct (Policy 6.7) and all applicable federal regulations, including the 2020 and 2022 Title IX regulations issued by the U.S. Department of Education."
        ],
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
        "text": [
            "Middle Georgia State University (MGA) publishes an Annual Security and Fire Safety Report (also called the Clery Report) each year in compliance with the Jeanne Clery Disclosure of Campus Security Policy and Campus Crime Statistics Act.",
            "The report is available online at https://www.mga.edu/police/annual-report.php and in print from the MGA Department of Public Safety.",
            "Campus Safety Policies: MGA's Department of Public Safety (DPS) provides law enforcement and security services on all MGA campuses.",
            "DPS officers are certified peace officers in Georgia with full law enforcement authority on campus.",
            "The department operates 24 hours a day, 7 days a week.",
            "Crime Reporting: The Clery Act requires MGA to disclose statistics for specific crimes that occur on campus, in campus residential facilities, on public property adjacent to campus, and in non-campus buildings.",
            "Covered crimes include criminal homicide, sexual offenses (rape, fondling, incest, statutory rape), robbery, aggravated assault, burglary, motor vehicle theft, arson, hate crimes, dating violence, domestic violence, and stalking.",
            "Sexual Assault Prevention: MGA provides comprehensive primary prevention and awareness programs for all incoming students and new employees, including programming on: the definition of sexual harassment and sexual violence; MGA's prohibition of sex discrimination; safe and positive bystander intervention; recognition of warning signs of abusive behavior; and available resources.",
            "Ongoing awareness and prevention campaigns are conducted throughout the year.",
            "Reporting Mechanisms: Campus Sexual Assault Victims' Bill of Rights – MGA informs victims of sexual assault of their right to: notify law enforcement and campus security; seek campus disciplinary action; seek a protective order; receive information about counseling and support; request changes to academic and living situations.",
            "Confidential Reporting: Victims who wish to maintain confidentiality may speak with campus counselors and health service providers.",
            "Professional counselors are not required to report crimes to law enforcement without the victim's consent.",
            "Campus Security Authorities (CSAs): MGA has designated Campus Security Authorities who are required to report Clery Act crimes to the Department of Public Safety for statistical reporting purposes.",
            "CSAs include deans, directors, department heads, faculty advisors, coaches, and others with significant responsibility for student and campus activities.",
            "Timely Warnings: MGA will issue a timely warning to the campus community whenever a Clery Act crime is reported that poses a serious or continuing threat to students and employees.",
            "Timely warnings are distributed via the MGA Alert emergency notification system, which includes email, text message, and campus siren systems.",
            "Fire Safety: The annual report also contains fire safety statistics and policies for on-campus student housing.",
            "MGA student housing facilities are equipped with smoke detectors, fire suppression systems, and fire extinguishers.",
            "Fire drills are conducted each semester in residential facilities."
        ],
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
        "text": [
            "The University System of Georgia (USG) Board of Regents Policy 6.7 – Sexual Misconduct establishes system-wide standards for preventing and addressing sexual misconduct at all USG institutions, including Middle Georgia State University.",
            "Prohibited Conduct: The policy prohibits sexual harassment (including quid pro quo harassment and hostile environment harassment), sexual assault, dating violence, domestic violence, stalking, and retaliation.",
            "These prohibitions apply to all members of the university community: students, faculty, staff, and third parties.",
            "Jurisdiction: USG institutions have jurisdiction over conduct that occurs: (1) on campus or other property owned or controlled by the institution; (2) in the context of an institution-sponsored program or activity; or (3) off campus where the conduct creates a hostile environment on campus or has continuing effects on campus.",
            "Mandatory Reporting: All USG employees (with limited exceptions for confidential employees) are mandatory reporters who must promptly notify the Title IX Coordinator when they have knowledge of sexual misconduct.",
            "Standard of Evidence: USG institutions use the preponderance of evidence standard (more likely than not) in determining responsibility.",
            "Institutional Obligations: Each USG institution must: designate a Title IX Coordinator; publish a non-discrimination notice; maintain grievance procedures; provide training to all relevant personnel; and conduct annual assessments of its sexual misconduct program."
        ],
    },
)

documents.extend([TITLE_IX_POLICY, ANNUAL_SECURITY_REPORT, USG_SEXUAL_MISCONDUCT_POLICY])

STUDENT_CODE_OF_CONDUCT = Document(
    id="mga-student-code-of-conduct",
    data= {
        "title": "MGA Student Code of Conduct, Section 9 - Sexual Misconduct Procedures",
        "url": "https://www.mga.edu/student-conduct/sexual-misconduct-procedures.php",
        "text": (

    "Community: Students, faculty, and staff, as well as contractors, vendors, visitors and guests.",
    "Complainant: An individual who is alleged to have experienced conduct that violates this Policy.",
    "Consent: Words or actions that show a knowing and voluntary willingness to engage in mutually agreed-upon sexual activity.",
    "Consent cannot be gained by force, intimidation or coercion; by ignoring or acting in spite of objections of another; or by taking advantage of the incapacitation of another where the respondent knows or reasonably should have known of such incapacitation.",
    "Minors under the age of 16 cannot legally consent under Georgia law.",
    "Consent is also absent when the activity in question exceeds the scope of consent previously given.",
    "Past consent does not imply present or future consent.",
    "Silence or an absence of resistance does not imply consent.",
    "Consent can be withdrawn at any time by a party by using clear words or actions.",

    "Dating Violence: Violence committed by a person who is or has been in a social relationship of a romantic or intimate nature with the alleged victim.",
    "The existence of such relationship shall be determined based on the totality of the circumstances including, without limitation to: (1) the length of the relationship; (2) the type of the relationship; and (3) the frequency of interaction between the persons involved in the relationship.",
    "Dating violence includes, but is not limited to, sexual or physical abuse or the threat of such abuse.",
    "Dating violence does not include acts covered under the definition of Domestic Violence.",

    "Domestic Violence: Violence committed by a current or former spouse or intimate partner of the alleged victim; by a person with whom the alleged victim shares a child in common; by a person who is cohabitating with, or has cohabitated with, the victim as a spouse or intimate partner, or by a person similarly situated to a spouse of the alleged victim.",

    "Incapacitation: The physical and/or mental inability to make informed, rational judgments.",
    "It can result from mental disability, sleep or any state of unconsciousness, involuntary physical restraint, status as a minor under the age of 16, or from intentional or unintentional taking of alcohol and/or other drugs.",
    "Whether someone is incapacitated is to be judged from the perspective of an objectively reasonable person.",

    "Nonconsensual Sexual Contact: Any physical contact with another person of a sexual nature without the person’s consent.",
    "It includes but is not limited to the touching of a person’s intimate parts (for example, genitalia, groin, breasts, or buttocks); touching a person with one’s own intimate parts; or forcing a person to touch his or her own or another person’s intimate parts.",
    "This provision also includes 'Fondling' as defined by the Clery Act.",

    "Nonconsensual Sexual Penetration: Any penetration of the vagina, anus, or mouth by a penis, object, tongue, finger, or other body part; or contact between the mouth of one person and the genitals or anus of another person.",
    "This provision also includes 'Rape, Incest, and Statutory Rape' as defined by the Clery Act.",

    "Confidential Employees: Institution employees who have been designated by the institution to talk with a Complainant or Respondent in confidence.",
    "Confidential Employees must only report that the incident occurred and provide date, time, location, and name of the Respondent (if known) without revealing any information that would personally identify the alleged victim.",
    "This minimal reporting must be submitted in compliance with Title IX and the Clery Act.",
    "Confidential Employees may be required to fully disclose details of an incident in order to ensure campus safety.",

    "Privileged Employees: Individuals employed by the institution to whom a complainant or alleged victim may talk in confidence, as provided by law.",
    "Disclosure to these employees will not automatically trigger an investigation against the complainant’s or alleged victim’s wishes.",
    "Privileged Employees include those providing counseling, advocacy, health, mental health, or sexual-assault related services (e.g., sexual assault resource centers, campus health centers, pastoral counselors, and campus mental health centers) or as otherwise provided by applicable law.",
    "Exceptions to confidentiality exist where the conduct involves suspected abuse of a minor (in Georgia, under the age of 18) or otherwise provided by law, such as imminent threat of serious harm.",

    "Reasonable Person: An individual who is objectively reasonable under similar circumstances and with similar identities to the person being evaluated by the institution.",
    "Reporter: An individual who reports an allegation of conduct that may violate this Policy but who is not a party to the complaint.",
    "Respondent: An individual who is alleged to have engaged in conduct that violates this Policy.",
    "Responsible Employees: Those employees who must promptly and fully report complaints of or information regarding sexual misconduct to the Coordinator.",
    "Responsible Employees include any administrator, supervisor, faculty member, or other person in a position of authority who is not a Confidential Employee or Privileged Employee.",
    "Student employees who serve in a supervisory, advisory, or managerial role are in a position of authority for purposes of this Policy (e.g., teaching assistants, residential assistants, student managers, orientation leaders).",

    "Sexual Exploitation: Taking non-consensual or abusive sexual advantage of another for one’s own advantage or benefit, or for the benefit or advantage of anyone other than the one being exploited.",
    "Examples of sexual exploitation may include, but are not limited to, the following: Invasion of sexual privacy; Prostituting another individual; Non-consensual photos, video, or audio of sexual activity; Non-consensual distribution of photo, video, or audio of sexual activity, even if the sexual activity or capturing of the activity was consensual; Intentional observation of nonconsenting individuals who are partially undressed, naked, or engaged in sexual acts; Knowingly transmitting an STD or HIV to another individual through sexual activity; Intentionally and inappropriately exposing one’s breasts, buttocks, groin, or genitals in non-consensual circumstances; and/or Sexually-based bullying.",

    "Sexual Harassment (Student on Student): Unwelcome verbal, nonverbal, or physical conduct based on sex (including gender stereotypes), determined by a Reasonable Person to be so severe, pervasive, and objectively offensive that it effectively denies a person equal access to participate in or to benefit from an institutional education program or activity.",
    "Sexual Harassment (Other Than Student on Student): Unwelcome verbal, nonverbal, or physical conduct, based on sex (including gender stereotypes), that may be any of the following: Implicitly or explicitly a term or condition of employment or status in a course, program, or activity; A basis for employment or educational decisions; or Is sufficiently severe, persistent, or pervasive to interfere with one’s work or educational performance creating an intimidating, hostile, or offensive work or learning environment, or interfering with or limiting one’s ability to participate in or to benefit from an institutional program or activity.",
    "The USG also prohibits unwelcome conduct determined by a Reasonable Person to be so severe, pervasive and objectively offensive that it effectively denies a person equal access to a USG education program or activity in violation of Title IX.",

    "Sexual Misconduct: Includes, but is not limited to, such unwanted behavior as dating violence, domestic violence, nonconsensual sexual contact, nonconsensual sexual penetration, sexual exploitation, sexual harassment and stalking.",

    "Stalking: Engaging in a course of conduct directed at a specific person that would cause a reasonable person to fear for their safety or the safety of others or suffer substantial emotional distress.",
    "For the purposes of this definition: Course of conduct means two or more acts, including, but not limited to, acts in which the stalker directly, indirectly, or through third parties, by any action, method, device, means, follows, monitors, observes, surveils, threatens, or communicates to or about a person, or interferes with person’s property.",
    "Substantial emotional distress means significant mental suffering or anguish that may but does not necessarily, require medical or other professional treatment or counseling.",

    "The Respondent and Complainant (where applicable), as parties to these proceedings, shall have the right to have an advisor (who may or may not be an attorney) of the party’s choosing, and at their own expense, for the express purpose of providing advice and counsel.",
    "The advisor may be present during meetings and proceedings during the investigatory and/or resolution process at which his or her advisee is present.",
    "The advisor may advise their advisee in any manner, including providing questions, suggestions, and guidance on responses to any questions posed to the advisee, but shall not participate directly during the investigation or hearing process.",

    "In no case shall a hearing to resolve charges of student misconduct take place before the investigative report has been finalized.",
    "Upon notice of the alleged Sexual Misconduct, the institution’s Title IX Coordinator ('Coordinator') will assess whether a formal investigation, informal resolution, or dismissal would be appropriate.",
    "In making this determination, the Coordinator will assess whether the allegation(s), if true, would rise to the level of prohibited conduct, whether a Formal Complaint must be filed, whether an investigation is appropriate in light of the circumstances, whether the parties prefer an informal resolution, and whether any safety concerns exist for the campus community.",
    "The need to issue a broader warning to the community in compliance with the Clery Act shall be assessed in compliance with federal law.",

    "Where a Complainant requests that their identity be withheld or the allegation(s) not be investigated, the Coordinator should consider whether or not such request(s) can be honored in a manner consistent with the institution’s obligations to promote a safe and nondiscriminatory environment.",
    "The institution should inform the Complainant that the institution cannot guarantee confidentiality.",
    "Honoring a Complainant’s request for confidentiality shall not prevent the institution from reporting information or statistical data as required by law, including the Clery Act.",

    "Anyone who has made a report or complaint, provided information, assisted, participated, or refused to participate in any manner in the Sexual Misconduct process, shall not be subjected to retaliation.",
    "Anyone who believes that they have been subjected to retaliation should immediately contact the Title IX Coordinator or their designee.",
    "Any person found to have engaged in retaliation shall be subject to disciplinary action.",

    "Individuals are prohibited from knowingly making false statements or knowingly submitting false information to a system or institution official.",
    "Any person found to have knowingly submitted false complaints, accusations, or statements including during a hearing, shall be subject to appropriate disciplinary action (up to and including suspension or expulsion) under the appropriate institutional process.",

    "Students should be encouraged to come forward and to report Sexual Misconduct notwithstanding their choice to consume alcohol or to use drugs.",
    "Information reported by a student during the Sexual Misconduct process concerning the consumption of drugs or alcohol will not be used against the particular student in a disciplinary proceeding or voluntarily reported to law enforcement; however, the student may be provided with resources on drug and alcohol counseling and/or education, as appropriate.",
    "Nevertheless, students may be required to meet with staff members regarding the incident and may be required to participate in appropriate educational program(s).",
    "The required participation in an education program under this amnesty procedure will not be considered a sanction.",
    "Nothing in this amnesty provision shall prevent an institution staff member who is otherwise obligated by law (the Clery Act) to report information or statistical data as required.",

    "Each institution shall take necessary and appropriate action to promote the safety and well-being of its community.",
    "Accordingly, Sexual Misconduct should be addressed when such acts occur on institution property, at institution-sponsored or affiliated events, or otherwise violates the institution’s student conduct policies, regardless to where such conduct occurs.",

    "FOR FORMAL TITLE IX COMPLAINTS: Both the Complainant and the Respondent, as parties to the matter, shall have the opportunity to use an advisor (who may or may not be an attorney) of the party’s choosing.",
    "The advisor may accompany the party to all meetings and may provide advice and counsel to the respective party through the Sexual Misconduct process, including providing questions, suggestions and guidance to the party, but may not actively participate in the process except to conduct cross-examination at the hearing as outlined in the Resolution/Hearing section below.",
    "If a party chooses not to use an advisor during the investigation, the institution will provide an advisor for the purpose of conducting cross-examination on behalf of the relevant party.",
    "All communication during the Sexual Misconduct process will be between the institution and the party and not the advisor.",
    "The institution will copy the party’s advisor prior to the finalization of the investigation report when the institution provides the parties with the right to inspect and review directly related information gathered during the investigation.",
    "With the party’s permission, the advisor may be copied on all communications.",

    "FOR NON-TITLE IX SEXUAL MISCONDUCT COMPLAINTS: Both the Complainant and the Respondent, as parties to the matter, shall have the opportunity to use an advisor (who may or may not be an attorney) of the party’s choosing at the party’s own expense.",
    "The advisor may accompany the party to all meetings and may provide advice and counsel to their respective parties throughout the Sexual Misconduct process but may not actively participate in the process.",
    "All communication during the Sexual Misconduct process will be between the institution and the party and not the advisor.",
    "With the party’s permission, the advisor may be copied on all communications.",

    "Interim measures may be implemented by the institution at any point after the institution becomes aware of the alleged student misconduct and should be designed to protect any student or other individual in the USG community.",
    "To the extent interim measures are imposed, they should minimize the burden on both the Complainant (where applicable) and the Respondent, where feasible.",
    "Interim measures may include, but are not limited to: Change of housing assignment; Issuance of a 'no contact' directive; Restrictions or bars to entering certain institution property; Changes to academic or employment arrangements, schedules, or supervision; Interim suspension; and Other measures designed to promote the safety and well-being of the parties and the institution’s community.",
    "An interim suspension should only occur where necessary to maintain safety and should be limited to those situations where the respondent poses a serious and immediate danger or threat to persons or property.",
    "In making such an assessment, the institution should consider the existence of a significant risk to the health or safety of the Complainant (where applicable) or the campus community; the nature, duration, and severity of the risk; the probability of potential injury; and whether less restrictive means can be used to significantly mitigate the risk.",
    "Before an interim suspension is issued, the institution must make all reasonable efforts to give the respondent the opportunity to be heard on whether his or her presence on campus poses a danger.",
    "If an interim suspension is issued, the terms of the suspension shall take effect immediately.",
    "The Respondent shall receive notice of the interim suspension and the opportunity to respond to the interim suspension.",
    "When requested by the respondent, a hearing to determine whether immediate suspension should continue will be held within three (3) University business days of the request.",
    "Where the potential sanctions for the alleged misconduct may involve a suspension or expulsion (even if such sanctions were be held 'in abeyance', such as probationary suspension or expulsion) the institution’s investigation and resolution procedures must provide these additional, minimum safeguards: The Respondent shall be provided with written notice of the complaint/allegations, pending investigation, possible charges, possible sanctions, and available support services.",
    "The notice shall also include the identity of any investigator involved.",
    "Notice shall be provided via University email.",
    "Where applicable, a copy shall also be provided to any and all complainants/alleged victims via the same means.",
    "Upon receipt of the written notice, the respondent shall have three (3) University business days to respond in writing.",
    "In that response, the respondent shall have the right to admit or deny the allegations, and to set force a defense of facts, witnesses, and documents – either written or electronic – in support.",
    "A non-response will be considered a general denial of the alleged misconduct.",

    "Throughout any investigation and resolution proceeding, a party shall receive written notice of the alleged Sexual Misconduct, shall be provided an opportunity to respond, and shall be allowed the right to remain silent or otherwise not participate in or during the investigation and resolution process without an adverse inference resulting.",
    "If a party chooses to remain silent or otherwise not participate in the investigation or resolution process, the investigation and resolution process may still proceed, and policy violations may result.",
    "Until a final determination of responsibility, the Respondent is presumed to have not violated the Sexual Misconduct Policy.",
    "Prior to the finalization of the investigation report, timely and equal access to information directly related to the allegations that have been gathered during the investigation and may be used at the hearing will be provided to the Complainant, the Respondent, and a party’s advisor (where applicable).",
    "Formal rules of evidence do not apply to the investigation process, additionally the standard of review throughout the Sexual Misconduct process is a preponderance of the evidence.",
    "The parties shall be provided with written notice of the report/allegations with sufficient details, pending investigation, possible charges, possible sanctions, available support services and interim measures, and other rights under applicable institutional policies.",
    "For the purposes of this provision sufficient details include the identities of the parties involved, if known, the conduct allegedly constituting Sexual Misconduct, and the date and location of the alleged incident, if known.",
    "This information will be supplemented as necessary with relevant evidence collected during the investigation.",
    "The notice should also include the identity of any investigator(s) involved.",
    "Notice should be provided via institution email to the party’s institution email.",
    "Upon receipt of the written notice, the parties shall have at least three (3) business days to respond in writing.",
    "In that response, the Respondent shall have the right to admit or deny the allegations, and to set forth a defense with facts, witnesses, and supporting materials.",
    "A Complainant shall have the right to respond to and supplement the notice.",
    "Throughout the Sexual Misconduct process the Complainant and the Respondent shall have the right to present witnesses and other inculpatory and exculpatory evidence.",
    "If the Respondent admits responsibility, the process may proceed to the sanctioning phase or may be informally resolved, if appropriate.",
    "An investigator shall conduct a thorough investigation and should retain written notes and/or obtain written or recorded statements from each interview.",
    "The investigator shall also keep a record of any party’s proffered witnesses not interviewed, along with a brief, written explanation of why the witnesses were not interviewed.",
    "An investigator shall not access, consider, disclose, or otherwise use a party’s records made or maintained by a physician, psychiatrist, psychologist, or other recognized professional made in connection with the party’s treatment unless the party has provided voluntary written consent.",
    "This also applies to information protected by recognized legal privilege.",
    "The initial investigation report shall be provided to the Complainant, the Respondent, and the party’s advisor (if applicable).",
    "This report should fairly summarize the relevant evidence gathered during the investigation and clearly indicate any resulting charges or alternatively, a determination of no charges.",
    "For purposes of this Policy, a charge is not a finding of responsibility.",
    "The Complainant and the Respondent shall have at least ten (10) calendar days to review and respond in writing to the initial investigation report and directly related information gathered during the investigation.",
    "The investigator will review the Complainant’s and the Respondent’s written responses, if any, to determine whether further investigation or changes to the investigation report are necessary.",
    "The final investigation report should be provided to the Complainant, the Respondent, and the party’s advisor, if applicable, at least ten (10) calendar days prior to the Hearing.",
    "The final investigation report should also be provided to all Hearing Panel members for consideration during the adjudication process.",

    "The Respondent and the Complainant, as parties to the matter, may have the option of selecting informal resolution as a possible resolution in certain cases where the parties agree, and it is deemed appropriate by the institution.",
    "Where a matter is not resolved through informal resolution a hearing shall be set.",
    "All Sexual Misconduct cases shall be heard by a panel of faculty and/or staff.",
    "All institutional participants in the Sexual Misconduct resolution process shall receive appropriate annual training as directed by the System Director or Coordinator and required by the Clery Act and Title IX.",
    "In no case shall a hearing to resolve a Sexual Misconduct allegation take place before the investigation report has been finalized.",
    "The investigator may testify as a witness regarding the investigation and findings but shall otherwise have no part in the hearing process and shall not attempt to otherwise influence the proceedings outside of providing testimony during the hearing.",
    "All directly related evidence shall be available at the hearing for the parties and their advisors to reference during the hearing.",
    "Relevant facts or evidence that were not known or knowable to the parties prior to the issuance of the final investigative report shall be admissible during the hearing.",
    "The institution will determine how the facts or evidence will be introduced.",
    "The admissibility of any facts or evidence known or knowable by the parties prior to the issuance of the final investigative report, and which were not submitted during the investigation, shall be determined by the institution in compliance with the obligation to provide both parties with an equal opportunity to present and respond to witnesses and other evidence.",
    "Notice of the date, time, and location of the hearing as well as the selected hearing panel members shall be provided to the Complainant and the Respondent at least ten (10) calendar days prior to the hearing.",
    "Notice shall be provided via institution email to the parties’ institution email.",
    "Parties may attend the hearing with their advisor.",
    "The hearing shall be conducted in-person or via video conferencing technology.",
    "Where the institution determines that a party or witness is unable to be present in person due to extenuating circumstances, the institution may establish special procedures to permit that individual to provide testimony from a separate location.",
    "In doing so, the institution must determine whether there is a valid basis for the individual’s unavailability, require that the individual properly sequester in a manner that ensures testimony has not been tainted, and decide that such arrangement will not unfairly disadvantage any party.",
    "Should it be reasonably believed that the individual presented tainted testimony, the hearing panel will disregard or discount the testimony.",
    "Parties may also request to provide testimony in a separate room from the opposing party, so long as no party is unfairly disadvantaged, and they have the opportunity to view the testimony remotely and submit follow-up questions.",
    "At all times participants in the hearing process, including parties, a party’s advisor, and institution officials, are expected to act in a manner that promotes dignity and decorum throughout the hearing.",
    "Participants are expected to be respectful to others and follow procedural formalities outlined by this Policy and the institution.",
    "The institution reserves the right to remove any participant from the hearing environment if the participant refuses to adhere to the institution’s established rules of decorum.",
    "Each institution shall maintain documentation of the investigation and resolution process, which may include written findings of fact, transcripts, audio recordings, and/or video recordings.",
    "Any documentation shall be maintained for seven years.",

    "Where a party or a witness is unavailable, unable, or otherwise unwilling to participate in the hearing, including being subject to cross-examination, the hearing panel shall not draw an adverse inference against the party or witness based solely on their absence from the hearing or refusal to subject to cross-examination.",
    "The parties shall have the right to present witnesses and evidence at the hearing.",
    "The parties shall have the right to confront any witness, including the other party, by having their advisor ask relevant questions directly to the witness.",
    "The Hearing Officer shall limit questions raised by the advisor when they are irrelevant to determining the veracity of the allegations against the Respondent(s).",
    "In any such event, the Hearing Officer shall err on the side of permitting all the questions raised and must document the reason for not permitting any particular questions to be raised.",
    "Questions and evidence about the Complainant’s sexual predisposition or prior sexual behavior, shall be deemed irrelevant, unless such questions and evidence are offered to prove that someone other than the Respondent committed the alleged conduct or consent between the parties during the alleged incident.",
    "The hearing panel shall not access, consider, disclose, or otherwise use a party’s records made or maintained by a physician, psychiatrist, psychologist, or other recognized medical professional made in connection with the party’s treatment unless the party has provided voluntary written consent.",
    "This also applies to information protected by recognized legal privilege.",
    "Formal rules of evidence do not apply to the resolution process and the standard of evidence shall be a preponderance of the evidence.",
    "Following a hearing, the parties shall be simultaneously provided with a written decision via institution email of the hearing outcome and any resulting sanctions or administrative actions.",
    "The decision must include the allegations, procedural steps taken through the investigation and resolution process, findings of facts supporting the determination(s), determination(s) regarding responsibility, and the evidence relied upon and rationale for any sanction or other administrative action.",
    "The institution shall also notify the parties of their right to appeal as outlined below.",

    "The parties shall have the right to present witnesses and evidence at the hearing.",
    "Witness testimony, if provided, shall pertain to knowledge and facts directly associated with the case being heard.",
    "The parties shall have the right to confront any witnesses, including the other party, by submitting written questions to the Hearing Officer for consideration.",
    "Advisors may actively assist in drafting questions.",
    "The Hearing Officer shall ask the questions as written and will limit questions only if they are irrelevant to determining the veracity of the allegations against the Respondent(s).",
    "In any such event, the Hearing Office shall err on the side of asking all submitted questions and must document the reason for not asking any particular questions.",
    "Questions and evidence about the Complainant’s sexual predisposition or prior sexual behavior, shall be deemed irrelevant, unless such questions and evidence are offered to prove that someone other than the Respondent committed the alleged conduct or consent between the parties during the alleged incident.",
    "The hearing panel shall not access, consider, disclose, or otherwise use a party’s records made or maintained by a physician, psychiatrist, psychologist, or other recognized medical professional made in connection with the party’s treatment unless the party has provided voluntary written consent.",
    "This also applies to information protected by recognized legal privilege.",
    "Formal rules of evidence do not apply to the resolution process and the standard of evidence shall be a preponderance of the evidence.",
    "Following a hearing, the parties shall be simultaneously provided with a written decision via institution email of the hearing outcome and any resulting sanctions or administrative actions.",
    "The decision must include the allegations, procedural steps taken through the investigation and resolution process, findings of facts supporting the determination(s), determination(s) regarding responsibility, and the evidence relied upon and rationale for any sanction or other administrative action.",
    "The institution shall also notify the parties of their right to appeal as outlined below.",

    "In determining the severity of sanctions or corrective actions the following should be considered: the frequency, severity, and/or nature of the offense; history of past conduct; an offender’s willingness to accept responsibility; previous institutional response to similar conduct; strength of the evidence; and the wellbeing of the university community.",
    "The institution will determine sanctions and issues notice of the same, as outlined above.",
    "The broad range of sanctions includes: expulsion, suspension for an identified time frame or until satisfaction of certain conditions, or both; temporary or permanent separation of the parties (e.g., change in classes, reassignment of residence, no contact orders, limiting geography of where parties can go on campus) with additional sanctions for violating no-contact orders; required participation in sensitivity training/awareness education programs; required participation in alcohol and other drug awareness and abuse prevention programs; counseling or mentoring; volunteering/community service; loss of institutional privileges; delays in obtaining administrative services and benefits from the institution (e.g., holding transcripts, delaying registration, graduation, diplomas); additional academic requirements relating to the scholarly work or research; financial restitution; or any other discretionary sanctions directly related to the violation of conduct.",
    "For suspension and expulsion, the institution must articulate, in its written decision, the substantial evidence relied upon in determining that suspension or expulsion is appropriate.",
    "For purposes of this Policy substantial evidence means evidence that a reasonable person might accept to support the conclusion.",

    "Appeals may be allowed in any case where sanctions are issued, even when such sanctions are held 'in abeyance,' such as probationary or expulsion.",
    "Where the sanction imposed includes a suspension or expulsion (even for one held in abeyance), the following appellate procedures must be provided.",
    "The Respondent (and in cases involving sexual misconduct or other forms of discrimination and/or harassment, the Complainant) shall have the right to appeal the outcome on any of the following grounds: To consider new information, sufficient to alter the decision, or other relevant facts not brought out in the original hearing (or appeal).",
    "To allege a procedural error within the hearing process that may have substantially impacted on the fairness of the hearing (or appeal), including but not limited to whether any hearing questions were improperly excluded or whether the decision was tainted by a conflict of interest or bias by the Title IX Coordinator, Conduct Officer, investigator(s), decision maker(s).",
    "To allege that the finding was inconsistent with the weight of the information.",
    "The appeal must be made in writing, must set forth one or more of the bases outlined above, and must be submitted within five (5) business days of the date of the final written decision.",
    "The appeal should be made to the institution’s President or their designee.",
    "The appeal shall be a review of the record only, and no new meeting with the Respondent or any Complainant is required.",
    "The President or their designee may: Affirm the original finding(s) and sanction(s); Affirm the original finding but issue a new sanction of greater or lesser severity; Remand the case back to any lower decision maker to correct a procedural or factual defect; Reverse or dismiss the case if there was a procedural or factual defect that cannot be remedied by remand.",
    "The President or their designee’s decision shall be simultaneously issued in writing to the parties within a reasonable time period.",
    "The President or their designee’s decision shall be the final decision of the institution.",
    "Should the respondent or the complainant wish to appeal the President’s decision, he or she may request an Application for Discretionary Review from the University System of Georgia and the Board of Regents.",
    "Applications for review shall be submitted in writing to the University System Office of Legal Affairs within 20 calendar days following the final institution decision.",
    "Information about this application can be found in the Board of Regents Policy 6.26.",
    "Appeals received after the designated deadlines above will not be considered unless the institution or Board of Regents has granted an extension prior to the deadline.",
    "If any appeal is not received by the deadline the last decision on the matter will become final.",

    "Any party may challenge the participation of any institutional official, employee, or student panel member in the process on the grounds of personal bias by submitting a written statement to the institution’s designee setting forth the basis for the challenge.",
    "The designee shall not be the same individual responsible for investigating or adjudicating the conduct allegation.",
    "The written challenge should be submitted within a reasonable time after the individual knows or reasonably should have known of the existence of the bias.",
    "The institution’s designee will determine whether to sustain or deny the challenge and, if sustained, the replacement to be appointed."
        )
    }
)

documents.append(STUDENT_CODE_OF_CONDUCT)