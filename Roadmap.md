# CyberSecurity Cryptography Writeups - Monthly Roadmap

Complete roadmap for cryptography learning organized by month with weekly breakdowns.

---

# 📅 FEBRUARY: Introduction To Cryptohack

## Week 1: Foundations & Core Challenges

### Daily Breakdown
- **Day 1**: Introduction to Cryptography (encoding, XOR, bytes, big integers)
- **Day 2-3**: Challenges 1-6 (basic to intermediate concepts)
- **Day 4-5**: Challenges 7-10 (advanced applications) + Review

### ✅ Completed Topics (Week 1)
- Introduction to Cryptography
- Encoding & Decoding
- XOR operations and reversibility
- Bytes & Big Integers
- Basic Python scripting for crypto

---

## Week 2: Practice & Mastery

### Daily Breakdown
- **Day 1**: Challenge Re-Practice (solve without hints)
- **Day 2**: Implement From Scratch (custom crypto functions)
- **Day 3**: Advanced Scenarios & Edge Cases
- **Day 4**: Code Optimization & Refactoring
- **Day 5**: Comprehensive Writeup & Summary Project

### ✅ Completed Topics (Week 2)
- Challenge mastery without external help
- Implementation of crypto functions from scratch
- Edge case handling and error management
- Code optimization techniques
- Comprehensive documentation

### 🎯 Goal Achieved
Deep foundational understanding of basic cryptography and Python scripting for crypto tasks with practical mastery of all introduction challenges.

[View February Details](IntroductionToCryptoHack/ROADMAP.md)

---

# 📅 MARCH: Symmetric Cryptography & Modular Arithmetic

## Week 1: Modular Arithmetic Foundations

### Daily Breakdown
- **Day 1**: Modular Arithmetic 1 & 2 (basics and operations)
- **Day 2**: Modular Inverting (finding multiplicative inverse)
- **Day 3**: Quadratic Residues (properties and testing)
- **Day 4-5**: Review & Practice Exercises

### ✅ Completed Topics
- Modulo operations
- GCD & Extended Euclidean Algorithm
- Modular inverse calculations
- Quadratic residues

---

## Week 2: Advanced Number Theory & Symmetric Encryption

### Daily Breakdown
- **Day 1**: Chinese Remainder Theorem (CRT applications)
- **Day 2**: Primitive Roots (generators in cyclic groups)
- **Day 3**: Discrete Logarithm (one-way functions)
- **Day 4**: Symmetric Encryption Overview (concepts and algorithms)
- **Day 5**: AES & Cipher Modes (deep dive into modern encryption)
- **Day 6**: Padding & Authentication (security essentials)

### ✅ Completed Topics
- All 7 modular arithmetic lessons
- Symmetric encryption fundamentals
- AES algorithm mechanics
- Block cipher modes (ECB, CBC, CTR, GCM)
- PKCS#7 padding & authentication (HMAC, GCM)

### 🎯 Goals Achieved
- Strong mathematical foundations for cryptography
- Practical understanding of modern symmetric encryption
- Security best practices for encryption

[View March Details](SymmetricCryptography/ROADMAP.md)

---

# 📅 APRIL: Gandalf | Lakera Prompt Injection

## Week 1: Prompt Injection Challenges

### Daily Breakdown
- **Day 1**: Challenge 1 - Basic Prompt Injection
- **Day 2**: Challenge 2 - Constraint Bypass Techniques
- **Day 3**: Challenge 3 - Context & Data Extraction
- **Day 4**: Challenge 4 - Multi-turn Attack Strategies
- **Day 5**: Challenge 5 - Advanced Exploitation

### 📋 Learning Objectives
- Understand LLM vulnerabilities
- Learn prompt injection attack vectors
- Develop defensive mindset
- Practice responsible security research

[View April Details](April/ROADMAP.md)

---

# 📊 Overall Progress Summary

| Month | Status | Duration | Topics |
|-------|--------|----------|--------|
| February | ✅ Completed | 2 weeks | Introduction (10 challenges + practice) |
| March | ✅ Completed | 2 weeks | Modular Arithmetic (7 lessons) + Symmetric Crypto (4 writeups) |
| April | 📋 Planned | 1 week | Prompt Injection (5 challenges) |

**Total Time Invested:** ~5 weeks

---

# 🎯 Next Steps

1. Continue to Week 2 deep practice in April (after completing current months)
2. Complete April Gandalf challenges
3. Add additional months as needed
4. Document findings and solutions for each challenge
5. Review and reinforce weak areas

---

# 📚 Additional Resources

- [February: Introduction Index](IntroductionToCryptoHack/INDEX.md)
- [March: Symmetric Crypto & Modular Arithmetic Index](SymmetricCryptography/INDEX.md)
- [April: Prompt Injection Index](April/INDEX.md)
- [Main README](README.md)
- Introduction to Cryptography
- Encoding
- XOR
- Bytes & Big Integers

### ✅ Goals
- Convert hex ↔ bytes
- Convert bytes ↔ string
- Convert integer ↔ hex
- Understand why XOR is reversible

---

## 🧮 Modular Arithmetic (Days 2–6)

Complete all 10 lessons.

### Topics Covered
- Modulo basics
- GCD
- Extended Euclidean Algorithm
- Modular inverse
- Fermat’s Little Theorem
- Euler’s Totient Function

### 💡 Must Understand
- Why modular inverse is important
- Why primes matter
- Why `pow(a, b, n)` is efficient
- Why large exponentiation works in crypto

---

## 🔁 Day 7 — Review

- Redo 3 hardest challenges
- Solve without hints
- Reimplement:
  - `gcd()`
  - `extended_euclid()`
  - `mod_inverse()`

🎯 End of Week 1:
You are comfortable with number theory fundamentals.

---

# 🗓️ Week 2 — Real Cryptography

## 🔐 Symmetric Cryptography (Days 8–10)

Complete 11 lessons.

### Topics Covered
- XOR encryption
- Block ciphers
- AES
- ECB mode
- CBC mode
- CTR mode
- PKCS7 Padding

### ⚠️ Critical Concepts
- Why ECB is insecure
- Why IVs matter
- Why nonce reuse breaks CTR
- Why XOR encryption is reversible

🎯 Goal:
Understand how AES actually protects data.

---

## 🔑 Public-Key Cryptography (Days 11–14)

Complete 14 lessons.

### Topics Covered
- RSA basics
- Prime factorization
- Euler’s Totient
- Modular exponentiation
- Low exponent attacks
- Weak RSA setups
- Diffie-Hellman

### 🔍 Core Formula (RSA)

Encryption:

c = m^e mod n


Private Key:

d ≡ e⁻¹ mod φ(n)


### 💡 Must Understand
- Why factoring `n` breaks RSA
- Why modular inverse is required
- Why Diffie-Hellman works without sharing the secret

🎯 End of Week 2:
You understand how modern encryption systems combine RSA + AES.

---

# 🗓️ Week 3 — Elliptic Curves (Hard)

## 📈 Elliptic Curve Math (Days 15–17)

Complete first half of 18 lessons.

### Topics Covered
- Curve equation:

y² = x³ + ax + b

- Point addition
- Point doubling
- Finite field curves
- Group properties

🎯 Understand:
Elliptic curves form a mathematical group.

---

## 🔄 Elliptic Curve Cryptography (Days 18–20)

### Topics Covered
- Scalar multiplication
- Discrete Log Problem
- ECDH (Elliptic Curve Diffie-Hellman)
- Small curve attacks

### 💡 Core Concept
Security comes from:
> Repeated point addition is easy  
> Reversing it (discrete log) is hard

---

## 🏁 Day 21 — Mastery Day

- Solve 5 random challenges from:
- Modular Arithmetic
- RSA
- ECC
- No hints allowed

🎯 Final Goal:
Confidently solve beginner → hard CryptoHack challenges.

---
