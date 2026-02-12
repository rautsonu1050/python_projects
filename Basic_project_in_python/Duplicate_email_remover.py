# Email list with duplicates
emails = [
    "abc@email.com",
    "xyz@email.com",
    "abc@email.com",
    "jkl@email.com",
    "xyz@email.com"
]

# Remove duplicates using set
unique_emails = set(emails)
print(f"Total emails: {len(emails)}")
print(f"Unique emails: {len(unique_emails)}")
print("\nUnique email list:")
for email in sorted(unique_emails):
    print(email)

# Find common subscribers in two lists
list1 = {"abc@email.com", "xyz@email.com", "jkl@email.com"}
list2 = {"xyz@email.com", "david@email.com", "jkl@email.com"}

common = list1 & list2
print(f"\nCommon subscribers: {common}")