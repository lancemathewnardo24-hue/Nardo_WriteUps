# Challenge: Modular Inverting

**Category:** Mathematics > Modular Arithmetic  
**Difficulty:** Easy  
**URL:** https://cryptohack.org/courses/modular/modinv/

---

## 📖 Theory

The **modular inverse** of `a` mod `n` is a number `b` such that:
```
a * b ≡ 1 (mod n)
```

Written as: `b = a^(-1) mod n`

### When Does It Exist?

The inverse exists **if and only if** `gcd(a, n) = 1` (i.e., `a` and `n` are coprime).

### Methods to Compute It

**Method 1: Extended Euclidean Algorithm (general)**
```
gcd(a, n) = a*x + n*y  →  x is the inverse
```

**Method 2: Fermat's Little Theorem (only when n is prime)**
```
a^(-1) ≡ a^(n-2) (mod n)
```

**Method 3: Python built-in (Python 3.8+)**
```python
pow(a, -1, n)
```

---

## 🧩 Challenge

Given `a` and a prime `p`, find `d` such that:
```
3 * d ≡ 1 (mod 13)
```
or more generally compute `a^(-1) mod p`.

---

## 💡 Hints

- Python 3.8+ supports `pow(a, -1, n)` directly
- If `n` is prime: `pow(a, n-2, n)`
- If `n` is not prime: use `gmpy2.invert(a, n)` or Extended GCD
- Always check `gcd(a, n) == 1` first

---

## ✅ Solution

```python
# Method 1: Python 3.8+ built-in (cleanest)
a = 3
p = 13
inverse = pow(a, -1, p)
print(inverse)  # → 9, because 3*9 = 27 ≡ 1 (mod 13)

# Verify
assert (a * inverse) % p == 1

# Method 2: Fermat (only for prime modulus)
inverse2 = pow(a, p - 2, p)
print(inverse2)

# Method 3: Extended GCD (works for any modulus)
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def modinv(a, n):
    g, x, _ = extended_gcd(a % n, n)
    if g != 1:
        raise ValueError("Inverse doesn't exist")
    return x % n

print(modinv(3, 13))

# Method 4: gmpy2 (fastest for large numbers)
import gmpy2
print(int(gmpy2.invert(a, p)))
```

---

## 🔑 Key Takeaway

Modular inverses appear everywhere in crypto:
- **RSA**: private key `d = e^(-1) mod φ(n)`
- **ECC**: point division and scalar operations
- **Shamir's Secret Sharing**: Lagrange interpolation
- Always verify: `(a * inv) % n == 1`
