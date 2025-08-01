Challenge: Domain of Doom Revenge
Files: A simple Flask app that takes your “subject” (a domain), runs it through a regex filter, and then does dig +short -t A {domain}. Your job: bypass the regex, inject a shell command, and grab the flag.


---

1. Recon & First Steps

I cloned the challenge, opened the Flask code, and saw this in contact():

is_safe = re.search(
  r'^([a-z]+.)?[a-z\d\- ]+(\.(com|org|net|sa)){1,2}',
  domain
)

In plain English: “Allow an optional subdomain, some letters/digits/dashes/spaces, and one or two TLDs.” Looks harmless. right ! 
2. Head to Regex101

I copied the regex into Regex101 to visualise it. That lonely . wasn’t escaped, so it meant “match any single character.” My brain went:

> “Aha! That means I can sneak in a semicolon (;), right?”




---

3. Proof-of-Concept Injection

Back in the web form, I typed:

a; id .com

Hit submit—and voilà, my UID/GID printed on the page! The server did:

dig +short -t A a; id .com

shell-splitting on ; to run both dig a and then id .com.


---

4. Snatching the Flag

With injection confirmed, I needed the flag. Flags often hide in environment variables, so I tried:

x; env -u hello.com

Boom—entire environment dumped, right in my browser:

FLAG=ctf{d0m41n_0f_d00m_l1v35_0n}


---


And that’s how I tamed the Domain of Doom with a single rogue character and a cup of chai. 😉

