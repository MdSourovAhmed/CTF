## Just Crack It writeup (WWFCTF 2025)

Name: Just crack it
Difficulty: Medium to Hard
Author: spipm

## Story

We have his password history. I managed to extract the hashes during his daily run. They say he re-uses passwords. Can you crack them?

$2b$12$FK1REp/mHOnT/hOrNpwuVO4t6pOczl7Gf3eIri0e6f/KoKxdkjLUq
$2b$12$Aw5bPSmAhDOCdinnxhImKOkSPdUTcaTFVnOv52QVdlkrDinXAmG92
$2b$12$ITnjgStFDNtEWvPzdq71u.g4/3S4VXutsogFGoeiC0FJZulP.aaB.

The flag is wwf{final_password}.

## Internal information

The challenge tests three cracking skills:
- Cracking using a simple, short password list  (online_brute)
- Crack using a mask of known patterns          (like 202?d?a)
- Crack using rules on a custom wordlist        (like running brands)

Bcrypt is used to prevent teams with large cracking rigs from getting an advantage.

The passwords are:

P@ssw0rd
P@ssw0rd2025_
P@ssw0rd2025_Ad1d@5

pwds=[b'P@ssw0rd', b'P@ssw0rd2025_', b'P@ssw0rd2025_Ad1d@5']
for pwd in pwds:
  print(bcrypt.hashpw(pwd, bcrypt.gensalt(rounds=12)).decode())

