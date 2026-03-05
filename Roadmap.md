# CryptoHack 3-Week Roadmap 

This roadmap follows the **exact CryptoHack structure** and is designed for ~2–3 hours per day.

Tracks Covered:
- Introduction
- Modular Arithmetic (10 Lessons)
- Symmetric Cryptography (11 Lessons)
- Public-Key Cryptography (14 Lessons)
- Elliptic Curves (18 Lessons)

---

# 🗓️ Week 1 — Foundations

## 📘 Introduction Track (Day 1)

Complete:
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
