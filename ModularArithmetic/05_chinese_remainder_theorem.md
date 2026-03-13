# Challenge: Chinese Remainder Theorem (CRT)

**Category:** Mathematics > Modular Arithmetic  
**Difficulty:** Medium  
**URL:** https://cryptohack.org/courses/modular/crt/

---

## 📖 Theory

### Chinese Remainder Theorem (CRT)

Given a system of congruences with **pairwise coprime** moduli:
```
x ≡ a₁ (mod n₁)
x ≡ a₂ (mod n₂)
...
x ≡ aₖ (mod nₖ)
```

There exists a **unique** solution modulo `N = n₁ * n₂ * ... * nₖ`.

### Construction

```
N  = n₁ * n₂ * ... * nₖ
Nᵢ = N / nᵢ
yᵢ = Nᵢ^(-1) mod nᵢ   (modular inverse)
x  = Σ (aᵢ * Nᵢ * yᵢ) mod N
```

---

## 🧩 Challenge

Given a set of congruences, find the unique `x` satisfying all of them simultaneously.

Example:
```
x ≡ 2 (mod 5)
x ≡ 3 (mod 11)
x ≡ 10 (mod 17)
```

---

## 💡 Hints

- Verify moduli are pairwise coprime (`gcd(nᵢ, nⱼ) = 1` for all `i ≠ j`)
- `sympy.ntheory.modular.crt()` solves this directly
- Manual: compute `N`, then `Nᵢ = N // nᵢ`, then `yᵢ = pow(Nᵢ, -1, nᵢ)`

---

## ✅ Solution

```python
# Manual CRT
def crt(remainders, moduli):
    N = 1
    for n in moduli:
        N *= n
    
    x = 0
    for a, n in zip(remainders, moduli):
        Ni = N // n
        yi = pow(Ni, -1, n)  # modular inverse
        x += a * Ni * yi
    
    return x % N

# Example
remainders = [2, 3, 10]
moduli     = [5, 11, 17]

x = crt(remainders, moduli)
print(x)

# Verify
for a, n in zip(remainders, moduli):
    assert x % n == a, f"Failed: {x} % {n} != {a}"
print("Verified!")

# Using sympy
from sympy.ntheory.modular import crt as sympy_crt
M, x_sym = sympy_crt(moduli, remainders)
print(x_sym)
```

---

## 🔑 Key Takeaway

CRT is **critical** in cryptography:
- **RSA-CRT**: speeds up RSA decryption by ~4x (compute mod `p` and mod `q` separately)
- **Hastad's Broadcast Attack**: if same message sent to 3+ recipients with same small `e`, CRT reconstructs `m^e` then takes `e`-th root
- **Garner's algorithm**: efficient CRT for multi-prime RSA
- **Fault attacks**: flip a bit during RSA-CRT to factor `n`
