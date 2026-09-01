import csv
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

# ============================================================
# ICICI PRUDENTIAL - SOURCE DATA GENERATOR
#
# 4 CSV FILES
# 2 JSON FILES
#
# ============================================================

random.seed(42)

# ------------------------------------------------------------
# ROW COUNTS
# ------------------------------------------------------------

NUM_CUSTOMERS = 10_000
NUM_POLICIES = 20_000
NUM_PREMIUM_PAYMENTS = 100_000
NUM_CLAIMS = 30_000
NUM_AGENTS = 2_000
NUM_INVESTMENTS = 100_000

OUTPUT_DIR = Path("icici_prudential_source_data")


# ============================================================
# FILE PATHS
# ============================================================

CUSTOMER_FILE = (
    OUTPUT_DIR /
    "customer_crm" /
    "customers_2026_09_01.csv"
)

POLICY_FILE = (
    OUTPUT_DIR /
    "policy_admin" /
    "policies_2026_09_01.csv"
)

PREMIUM_FILE = (
    OUTPUT_DIR /
    "premium_billing" /
    "premium_payments_2026_09_01.csv"
)

CLAIM_FILE = (
    OUTPUT_DIR /
    "claims" /
    "claims_2026_09_01.csv"
)

AGENT_FILE = (
    OUTPUT_DIR /
    "agent_branch" /
    "agents_2026_09_01.json"
)

INVESTMENT_FILE = (
    OUTPUT_DIR /
    "investment_ulip" /
    "investment_transactions_2026_09_01.json"
)


# ============================================================
# MASTER DATA
# ============================================================

FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Rohan",
    "Rahul", "Vikram", "Karan", "Amit", "Suresh",
    "Rajesh", "Manish", "Nikhil", "Akash", "Ankit",
    "Varun", "Rohit", "Kunal", "Mohit", "Abhishek",
    "Priya", "Ananya", "Aditi", "Sneha", "Neha",
    "Pooja", "Kavya", "Isha", "Meera", "Riya",
    "Shreya", "Divya", "Nandini", "Swati", "Simran",
    "Tanvi", "Sakshi", "Anushka", "Radhika", "Preeti"
]

LAST_NAMES = [
    "Sharma", "Verma", "Patel", "Reddy", "Gupta",
    "Mehta", "Shah", "Iyer", "Nair", "Rao",
    "Singh", "Kumar", "Joshi", "Agarwal", "Bansal",
    "Desai", "Kulkarni", "Mishra", "Chatterjee", "Das",
    "Malhotra", "Kapoor", "Menon", "Pillai", "Saxena",
    "Tiwari", "Pandey", "Banerjee", "Ghosh", "Yadav"
]

LOCATIONS = [
    ("Mumbai", "Maharashtra", "400001"),
    ("Pune", "Maharashtra", "411001"),
    ("Bengaluru", "Karnataka", "560001"),
    ("Chennai", "Tamil Nadu", "600001"),
    ("Hyderabad", "Telangana", "500001"),
    ("Delhi", "Delhi", "110001"),
    ("Gurugram", "Haryana", "122001"),
    ("Noida", "Uttar Pradesh", "201301"),
    ("Kolkata", "West Bengal", "700001"),
    ("Ahmedabad", "Gujarat", "380001"),
    ("Jaipur", "Rajasthan", "302001"),
    ("Lucknow", "Uttar Pradesh", "226001"),
    ("Kochi", "Kerala", "682001"),
    ("Indore", "Madhya Pradesh", "452001"),
    ("Bhopal", "Madhya Pradesh", "462001"),
    ("Chandigarh", "Chandigarh", "160001"),
    ("Nagpur", "Maharashtra", "440001"),
    ("Surat", "Gujarat", "395001"),
    ("Coimbatore", "Tamil Nadu", "641001"),
    ("Visakhapatnam", "Andhra Pradesh", "530001")
]

OCCUPATIONS = [
    "Software Engineer",
    "Business Owner",
    "Doctor",
    "Teacher",
    "Banker",
    "Accountant",
    "Consultant",
    "Government Employee",
    "Lawyer",
    "Marketing Manager",
    "Sales Manager",
    "Data Analyst",
    "Civil Engineer",
    "Architect",
    "Self Employed",
    "Professor",
    "HR Manager",
    "Financial Analyst",
    "Pharmacist",
    "Entrepreneur"
]

POLICY_TYPES = [
    "Term Insurance",
    "ULIP",
    "Endowment",
    "Child Plan",
    "Pension Plan",
    "Savings Plan",
    "Whole Life"
]

POLICY_STATUSES = [
    "Active",
    "Lapsed",
    "Matured",
    "Cancelled"
]

PAYMENT_FREQUENCIES = [
    "Monthly",
    "Quarterly",
    "Half-Yearly",
    "Annual"
]

PAYMENT_METHODS = [
    "UPI",
    "Net Banking",
    "Debit Card",
    "Credit Card",
    "NACH",
    "Cheque"
]

CLAIM_TYPES = [
    "Death Claim",
    "Maturity Claim",
    "Health Claim",
    "Accidental Death",
    "Critical Illness"
]

CLAIM_STATUSES = [
    "Registered",
    "Under Review",
    "Approved",
    "Rejected",
    "Settled"
]

CLAIM_REASONS = [
    "Natural Death",
    "Accident",
    "Critical Illness",
    "Hospitalization",
    "Policy Maturity"
]

FUND_NAMES = [
    "Equity Fund",
    "Balanced Fund",
    "Debt Fund",
    "Bluechip Fund",
    "Growth Fund",
    "Dynamic Fund",
    "Infrastructure Fund"
]

TRANSACTION_TYPES = [
    "Premium Allocation",
    "Fund Switch",
    "Partial Withdrawal",
    "Fund Transfer",
    "Top Up"
]

AGENT_DESIGNATIONS = [
    "Insurance Advisor",
    "Senior Insurance Advisor",
    "Financial Consultant",
    "Relationship Manager",
    "Senior Relationship Manager"
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def random_date(start_date, end_date):

    delta = end_date - start_date

    random_days = random.randint(
        0,
        delta.days
    )

    return start_date + timedelta(
        days=random_days
    )


def random_phone():

    return (
        random.choice(
            ["6", "7", "8", "9"]
        )
        +
        "".join(
            random.choices(
                "0123456789",
                k=9
            )
        )
    )


def write_csv(file_path, data):

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=data[0].keys()
        )

        writer.writeheader()

        writer.writerows(data)

    print(
        f"Created CSV: {file_path} "
        f"| Rows: {len(data):,}"
    )


def write_json(file_path, data):

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=2
        )

    print(
        f"Created JSON: {file_path} "
        f"| Rows: {len(data):,}"
    )


# ============================================================
# 1. AGENTS + BRANCH INFORMATION
# JSON SOURCE
# ============================================================

print("\nGenerating AGENT / BRANCH source...")

agents = []

for i in range(
    1,
    NUM_AGENTS + 1
):

    first_name = random.choice(
        FIRST_NAMES
    )

    last_name = random.choice(
        LAST_NAMES
    )

    city, state, pincode = random.choice(
        LOCATIONS
    )

    agent = {

        "agent_id":
            f"AGT{i:05d}",

        "agent_code":
            f"ICICI-AG-{i:05d}",

        "first_name":
            first_name,

        "last_name":
            last_name,

        "full_name":
            f"{first_name} {last_name}",

        "gender":
            random.choice([
                "Male",
                "Female"
            ]),

        "date_of_joining":
            random_date(
                datetime(2015, 1, 1),
                datetime(2026, 8, 31)
            ).strftime("%Y-%m-%d"),

        "designation":
            random.choice(
                AGENT_DESIGNATIONS
            ),

        "phone_number":
            random_phone(),

        "email":
            f"agent{i}@example.com",

        "branch_id":
            f"BR{random.randint(1, 200):04d}",

        "branch_name":
            f"{city} Insurance Branch",

        "branch_city":
            city,

        "branch_state":
            state,

        "branch_pincode":
            pincode,

        "agent_status":
            random.choice([
                "Active",
                "Inactive",
                "Suspended"
            ]),

        "source_system":
            "AGENT_BRANCH",

        "created_at":
            "2026-09-01T08:00:00",

        "updated_at":
            "2026-09-01T08:00:00"
    }

    agents.append(agent)


write_json(
    AGENT_FILE,
    agents
)


# ============================================================
# 2. CUSTOMER / CRM
# CSV SOURCE
# ============================================================

print("\nGenerating CUSTOMER source...")

customers = []

for i in range(
    1,
    NUM_CUSTOMERS + 1
):

    first_name = random.choice(
        FIRST_NAMES
    )

    last_name = random.choice(
        LAST_NAMES
    )

    city, state, pincode = random.choice(
        LOCATIONS
    )

    customer = {

        "customer_id":
            f"CUST{i:07d}",

        "first_name":
            first_name,

        "last_name":
            last_name,

        "full_name":
            f"{first_name} {last_name}",

        "gender":
            random.choice([
                "Male",
                "Female"
            ]),

        "date_of_birth":
            random_date(
                datetime(1960, 1, 1),
                datetime(2004, 12, 31)
            ).strftime("%Y-%m-%d"),

        "phone_number":
            random_phone(),

        "email":
            f"{first_name.lower()}."
            f"{last_name.lower()}"
            f"{i}@example.com",

        "city":
            city,

        "state":
            state,

        "pincode":
            pincode,

        "occupation":
            random.choice(
                OCCUPATIONS
            ),

        "annual_income":
            random.randint(
                300000,
                5000000
            ),

        "customer_status":
            random.choice([
                "Active",
                "Inactive"
            ]),

        "customer_since":
            random_date(
                datetime(2015, 1, 1),
                datetime(2026, 8, 31)
            ).strftime("%Y-%m-%d"),

        "source_system":
            "CRM",

        "created_at":
            "2026-09-01T08:00:00",

        "updated_at":
            "2026-09-01T08:00:00"
    }

    customers.append(
        customer
    )


write_csv(
    CUSTOMER_FILE,
    customers
)


# ============================================================
# 3. POLICY ADMINISTRATION
# CSV SOURCE
# ============================================================

print("\nGenerating POLICY source...")

policies = []

for i in range(
    1,
    NUM_POLICIES + 1
):

    customer = random.choice(
        customers
    )

    agent = random.choice(
        agents
    )

    policy_type = random.choice(
        POLICY_TYPES
    )

    policy_start = random_date(
        datetime(2018, 1, 1),
        datetime(2026, 8, 31)
    )

    policy_term = random.choice([
        5,
        10,
        15,
        20,
        25,
        30
    ])

    policy_end = (
        policy_start
        +
        timedelta(
            days=365 * policy_term
        )
    )

    sum_assured = random.choice([
        500000,
        1000000,
        1500000,
        2000000,
        2500000,
        5000000,
        10000000
    ])

    annual_premium = round(
        sum_assured *
        random.uniform(
            0.015,
            0.08
        ),
        2
    )

    frequency = random.choice(
        PAYMENT_FREQUENCIES
    )

    if frequency == "Monthly":

        premium_amount = round(
            annual_premium / 12,
            2
        )

    elif frequency == "Quarterly":

        premium_amount = round(
            annual_premium / 4,
            2
        )

    elif frequency == "Half-Yearly":

        premium_amount = round(
            annual_premium / 2,
            2
        )

    else:

        premium_amount = annual_premium

    policy = {

        "policy_id":
            f"POL{i:08d}",

        "policy_number":
            f"ICICI-{10000000 + i}",

        "customer_id":
            customer["customer_id"],

        "agent_id":
            agent["agent_id"],

        "branch_id":
            agent["branch_id"],

        "policy_type":
            policy_type,

        "policy_start_date":
            policy_start.strftime(
                "%Y-%m-%d"
            ),

        "policy_end_date":
            policy_end.strftime(
                "%Y-%m-%d"
            ),

        "policy_term_years":
            policy_term,

        "sum_assured":
            sum_assured,

        "annual_premium":
            annual_premium,

        "premium_frequency":
            frequency,

        "premium_amount":
            premium_amount,

        "payment_method":
            random.choice(
                PAYMENT_METHODS
            ),

        "policy_status":
            random.choice(
                POLICY_STATUSES
            ),

        "source_system":
            "POLICY_ADMIN",

        "created_at":
            "2026-09-01T08:00:00",

        "updated_at":
            "2026-09-01T08:00:00"
    }

    policies.append(
        policy
    )


write_csv(
    POLICY_FILE,
    policies
)


# ============================================================
# 4. PREMIUM / BILLING
# CSV SOURCE
# ============================================================

print("\nGenerating PREMIUM source...")

premium_payments = []

for i in range(
    1,
    NUM_PREMIUM_PAYMENTS + 1
):

    policy = random.choice(
        policies
    )

    payment_date = random_date(
        datetime(2023, 1, 1),
        datetime(2026, 8, 31)
    )

    premium_amount = policy[
        "premium_amount"
    ]

    actual_amount = round(
        premium_amount *
        random.uniform(
            0.98,
            1.02
        ),
        2
    )

    payment_status = random.choices(
        [
            "SUCCESS",
            "FAILED",
            "PENDING",
            "REFUNDED"
        ],
        weights=[
            88,
            5,
            5,
            2
        ]
    )[0]

    payment = {

        "payment_id":
            f"PREM{i:09d}",

        "policy_id":
            policy["policy_id"],

        "customer_id":
            policy["customer_id"],

        "payment_date":
            payment_date.strftime(
                "%Y-%m-%d"
            ),

        "due_date":
            (
                payment_date
                -
                timedelta(
                    days=random.randint(
                        0,
                        10
                    )
                )
            ).strftime(
                "%Y-%m-%d"
            ),

        "premium_amount":
            actual_amount,

        "payment_method":
            random.choice(
                PAYMENT_METHODS
            ),

        "payment_status":
            payment_status,

        "transaction_reference":
            f"TXN{100000000 + i}",

        "receipt_number":
            f"RCT{100000000 + i}",

        "source_system":
            "PREMIUM_BILLING",

        "created_at":
            "2026-09-01T08:00:00",

        "updated_at":
            "2026-09-01T08:00:00"
    }

    premium_payments.append(
        payment
    )


write_csv(
    PREMIUM_FILE,
    premium_payments
)


# ============================================================
# 5. CLAIMS
# CSV SOURCE
# ============================================================

print("\nGenerating CLAIM source...")

claims = []

for i in range(
    1,
    NUM_CLAIMS + 1
):

    policy = random.choice(
        policies
    )

    claim_date = random_date(
        datetime(2022, 1, 1),
        datetime(2026, 8, 31)
    )

    claim_type = random.choice(
        CLAIM_TYPES
    )

    claim_amount = random.choice([
        50000,
        100000,
        250000,
        500000,
        750000,
        1000000,
        2000000,
        5000000
    ])

    claim_status = random.choices(
        CLAIM_STATUSES,
        weights=[
            15,
            20,
            25,
            10,
            30
        ]
    )[0]

    approved_amount = (
        claim_amount
        if claim_status in [
            "Approved",
            "Settled"
        ]
        else 0
    )

    settlement_date = None

    if claim_status == "Settled":

        settlement_date = (
            claim_date
            +
            timedelta(
                days=random.randint(
                    5,
                    60
                )
            )
        ).strftime(
            "%Y-%m-%d"
        )

    claim = {

        "claim_id":
            f"CLM{i:08d}",

        "policy_id":
            policy["policy_id"],

        "customer_id":
            policy["customer_id"],

        "claim_number":
            f"ICLAIM-{10000000 + i}",

        "claim_date":
            claim_date.strftime(
                "%Y-%m-%d"
            ),

        "claim_type":
            claim_type,

        "claim_reason":
            random.choice(
                CLAIM_REASONS
            ),

        "claim_amount":
            claim_amount,

        "approved_amount":
            approved_amount,

        "claim_status":
            claim_status,

        "settlement_date":
            settlement_date,

        "source_system":
            "CLAIMS",

        "created_at":
            "2026-09-01T08:00:00",

        "updated_at":
            "2026-09-01T08:00:00"
    }

    claims.append(
        claim
    )


write_csv(
    CLAIM_FILE,
    claims
)


# ============================================================
# 6. INVESTMENT / ULIP
# JSON SOURCE
# ============================================================

print("\nGenerating INVESTMENT / ULIP source...")

investment_transactions = []

ulip_policies = [
    policy
    for policy in policies
    if policy["policy_type"] == "ULIP"
]


for i in range(
    1,
    NUM_INVESTMENTS + 1
):

    policy = random.choice(
        ulip_policies
    )

    transaction_date = random_date(
        datetime(2022, 1, 1),
        datetime(2026, 8, 31)
    )

    amount = round(
        random.uniform(
            1000,
            500000
        ),
        2
    )

    units = round(
        random.uniform(
            10,
            5000
        ),
        4
    )

    nav = round(
        random.uniform(
            10,
            150
        ),
        4
    )

    transaction = {

        "investment_transaction_id":
            f"INV{i:09d}",

        "policy_id":
            policy["policy_id"],

        "customer_id":
            policy["customer_id"],

        "transaction_date":
            transaction_date.strftime(
                "%Y-%m-%d"
            ),

        "transaction_type":
            random.choice(
                TRANSACTION_TYPES
            ),

        "fund_name":
            random.choice(
                FUND_NAMES
            ),

        "amount":
            amount,

        "units":
            units,

        "nav":
            nav,

        "transaction_status":
            random.choice([
                "SUCCESS",
                "PENDING",
                "FAILED"
            ]),

        "source_system":
            "INVESTMENT_ULIP",

        "created_at":
            "2026-09-01T08:00:00",

        "updated_at":
            "2026-09-01T08:00:00"
    }

    investment_transactions.append(
        transaction
    )


write_json(
    INVESTMENT_FILE,
    investment_transactions
)


# ============================================================
# FINAL SUMMARY
# ============================================================

total_rows = (
    NUM_CUSTOMERS
    + NUM_POLICIES
    + NUM_PREMIUM_PAYMENTS
    + NUM_CLAIMS
    + NUM_AGENTS
    + NUM_INVESTMENTS
)

print("\n")
print("=" * 70)
print("ICICI PRUDENTIAL - SOURCE DATA CREATED")
print("=" * 70)

print(
    f"Customers               : {NUM_CUSTOMERS:,} CSV"
)

print(
    f"Policies                : {NUM_POLICIES:,} CSV"
)

print(
    f"Premium Payments        : {NUM_PREMIUM_PAYMENTS:,} CSV"
)

print(
    f"Claims                  : {NUM_CLAIMS:,} CSV"
)

print(
    f"Agents + Branch         : {NUM_AGENTS:,} JSON"
)

print(
    f"Investment Transactions : {NUM_INVESTMENTS:,} JSON"
)

print("-" * 70)

print(
    f"TOTAL ROWS              : {total_rows:,}"
)

print("=" * 70)

print("""
FOLDER STRUCTURE:

icici_prudential_source_data/
│
├── customer_crm/
│   └── customers_2026_09_01.csv
│
├── policy_admin/
│   └── policies_2026_09_01.csv
│
├── premium_billing/
│   └── premium_payments_2026_09_01.csv
│
├── claims/
│   └── claims_2026_09_01.csv
│
├── agent_branch/
│   └── agents_2026_09_01.json
│
└── investment_ulip/
    └── investment_transactions_2026_09_01.json
""")

print("4 CSV + 2 JSON files generated successfully.")