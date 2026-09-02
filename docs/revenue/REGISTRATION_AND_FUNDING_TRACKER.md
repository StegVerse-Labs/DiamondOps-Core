# Registration and Funding Tracker

Last updated: 2026-09-02

## Entity and federal registrations

| Gate | Required evidence | Status | Blocking next step |
|---|---|---|---|
| Veteran business formation consultation / VVL pre-formation | TVC Veteran Verification Letter and consultant guidance | COMPLETE — VVL ISSUED 2026-08-20; private source evidence retained outside public repo | none |
| Texas veteran-owned formation-fee benefit | VVL; Comptroller Form 05-904; certificate of formation submitted together | COMPLETE FOR PRE-FILING PATH — TVC guidance confirms qualifying formation package is submitted through SOSUpload and VVL may be reused during its validity window | entity-specific formation packet |
| US for-profit entity | accepted Texas certificate of formation; governing/ownership document | READY FOR ENTITY-SPECIFIC PACKET — NOT FILED | exact legal name; registered agent/office; management/governing person; organizer; purpose; effective date; owner signature on 05-904; SOSUpload submission |
| EIN | IRS issuance confirmation | NOT RECORDED | accepted entity formation |
| SAM.gov | active entity record and UEI | NOT STARTED/NOT RECORDED | EIN and legal-name validation |
| SBA Company Registry | SBC Control ID | NOT STARTED/NOT RECORDED | SAM/eligibility prerequisites |
| DSIP | active account and organization access | NOT STARTED/NOT RECORDED | entity/SAM/SBA prerequisites |
| VetCert | application receipt and later decision | NOT STARTED/NOT RECORDED | accepted formation and federal registration prerequisites |

### Current formation checkpoint

- TVC Veteran Verification Letter issued: 2026-08-20.
- TVC guidance states the VVL may be used more than once and is valid for five years from issuance.
- Qualifying new veteran-owned entities must be Texas entities wholly owned by one or more qualifying individual veterans.
- Current strategy for entities seeking the veteran-owned benefit: preserve direct qualifying individual ownership at formation rather than place those entities under an LLC parent before qualification is established.
- Current Comptroller form: Form 05-904, Rev. 2-26/3.
- For an LLC, the filing packet is:
  1. Texas Certificate of Formation;
  2. Veteran Verification Letter for each qualifying veteran owner;
  3. Comptroller Form 05-904.
- TVC guidance directs online submission through SOSUpload.
- The public repository records only redacted status and workflow facts. Do not commit the VVL, unique identifier, home address, DD-214, signatures, tax identifiers, passwords, or other private ownership records.
- Entity-specific execution worksheet: `docs/revenue/TEXAS_VETERAN_OWNED_FORMATION_EXECUTION.md`.

### Remaining formation authority split

Machine-executable preparation:
- maintain the entity packet template and filing-order controls;
- keep public status synchronized in this tracker, inventory, claim registry, and mirror handoff;
- validate that no repository state falsely claims filing, acceptance, EIN, SAM, VetCert, or activation.

Human/external-authority execution:
- select and clear the exact legal entity name;
- supply/confirm registered agent and registered office;
- select member-managed or manager-managed structure and initial governing person;
- confirm organizer and business-purpose language;
- sign Form 05-904;
- submit the packet through SOSUpload;
- preserve the SOS receipt and accepted formation evidence privately, then record a redacted completion receipt here.

Do not commit sensitive identifiers, DD-214 contents, tax identifiers, passwords, signatures, private addresses, or private ownership records to a public repository. Commit only redacted receipts, status, dates, and secure-record pointers.

## Secure evidence convention
For every completed gate record:
- completion date;
- legal entity name used;
- non-sensitive identifier or redacted suffix where safe;
- receipt/reference location in secure storage;
- expiration/renewal date;
- next permitted action;
- responsible person.

## SBIR execution record

| Step | Evidence | Status |
|---|---|---|
| Official solicitation captured | solicitation/version/deadline record | PENDING VERIFICATION |
| One topic selected | topic ID and fit memo | PENDING |
| AaCT-E runnable baseline frozen | commit/tag, test command, expected assertions | REPOSITORY IDENTIFIED; WRITE AUTHORITY PREVIOUSLY BLOCKED |
| Phase I objectives defined | 3–5 measurable objectives | PENDING |
| Transition customer hypothesis | named agency/program class and need | PENDING |
| Technical volume | compliant draft | PENDING |
| Cost volume | basis and indirect-cost assumptions | PENDING |
| Submission receipt | DSIP confirmation | PENDING |

## Safety rule
Dates, award caps, eligibility rules, and certification requirements must be checked against the controlling official solicitation or agency portal before filing. Planning text is not filing authority.
