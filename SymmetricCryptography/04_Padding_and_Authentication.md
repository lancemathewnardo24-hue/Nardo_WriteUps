# Padding and Authentication in Symmetric Cryptography

## Introduction

When using block ciphers, two critical issues arise:
1. **Plaintext length** may not be multiple of block size (padding)
2. **No integrity verification** in basic encryption (authentication)

This writeup covers both problems and their solutions.

---

## Part 1: Padding

### Why Padding is Needed

Block ciphers operate on fixed-size blocks (typically 128 bits for AES). Most messages aren't exact multiples of block size.

#### Example
```
Block size: 16 bytes
Message: "Hello World!" (12 bytes)
Missing: 4 bytes

Need to pad with 4 bytes to make it 16 bytes total
```

### Padding Schemes

#### 1. PKCS#7 (Most Common) ✅

**Rule**: Add n bytes, each with value n, where n is the number of bytes needed

#### Example
```
Plaintext: "Hello World!" (12 bytes, block size 16)
Needs: 4 bytes of padding
Each padding byte value: 0x04

Padded: "Hello World!" + [0x04][0x04][0x04][0x04]

In hex:
48 65 6C 6C 6F 20 57 6F 72 6C 64 21 04 04 04 04
```

#### Edge Case: Full Block Padding
```
Plaintext: "Hello World!1234" (16 bytes, exactly one block)
Needs: full block of padding (16 bytes)
Each padding byte value: 0x10

Padded with entire extra block: [0x10][0x10][0x10][0x10]... (16 times)
```

**Why?** If no padding when exact multiple, we can't distinguish between padding and data.

#### Implementation
```python
def pkcs7_pad(data, block_size):
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length] * padding_length)
    return data + padding

def pkcs7_unpad(data, block_size):
    padding_length = data[-1]
    return data[:-padding_length]

# Usage
message = b"Hello World!"
padded = pkcs7_pad(message, 16)
unpadded = pkcs7_unpad(padded, 16)
```

#### 2. Zero Padding ⚠️ (Not Recommended)

**Rule**: Add zero bytes until block size reached

```
Plaintext: "Hello World!" (12 bytes)
Needs: 4 bytes
Padded: "Hello World!" + [0x00][0x00][0x00][0x00]
```

**Problems:**
- Can't distinguish padding from data ending in zeros
- Ambiguous during decryption
- Not standard for TLS/cryptographic applications

#### 3. ANSI X9.23 ⚠️

**Rule**: Fill with 0x00 bytes except last byte = padding length

```
Plaintext: "Hello World!" (12 bytes, need 4)
Padded: "Hello World!" + [0x00][0x00][0x00][0x04]
```

#### 4. Bit Padding

**Rule**: Add one 1 bit, then zero bits until block filled

Less common, used in some standards.

---

### Padding Oracle Attacks

#### The Problem
If server reveals whether padding is valid, attacker can decrypt message!

#### How it Works
1. Attacker sends modified ciphertext
2. Server tries to decrypt and check padding
3. Server responds differently if padding valid
4. Attacker uses response to deduce plaintext byte-by-byte

#### Protection
- **Don't reveal padding errors**: Same response for any decryption error
- **Use authenticated encryption**: GCM prevents this entirely
- **Encrypt-then-MAC**: Check MAC before decryption

#### Example
```
Vulnerable:
- Padding error: "Invalid padding" (attacker learns decryption succeeded)
- MAC error: "Invalid MAC"

Secure:
- Any error: "Decryption failed" (same message for both)
```

---

## Part 2: Authentication

### Why Authentication Matters

Encryption alone provides **confidentiality** (secrecy) but not **authenticity** (integrity).

#### Example Attack
```
Encrypted message: A7 F3 2B C1 D8 45 09 2F...

Attacker doesn't know plaintext, but can flip bits:
Modified: A7 F3 2B C0 D8 45 09 2F...  (changed one bit)

Recipient decrypts successfully but gets corrupted message
Attacker can perform bit-flipping attacks!
```

### Authentication Methods

#### 1. CBC-MAC (Cipher Block Chaining Message Authentication Code)

**How it works:**
1. Encrypt message in CBC mode
2. Use last ciphertext block as MAC
3. Transmit message + MAC
4. Receiver decrypts and verifies last block matches

**Properties:**
- Simple
- ❌ **Not secure for encryption** - use with separate key

#### 2. HMAC (Hash-based Message Authentication Code) ✅ Most Common

**How it works:**
1. Compute hash of (key + message)
2. Compute hash of (key + result)
3. Send message + HMAC

**Formula:**
```
HMAC(key, message) = Hash((key XOR outer_padding) + Hash((key XOR inner_padding) + message))
```

**Implementation:**
```python
import hmac
import hashlib

key = b"secret_key"
message = b"Hello World!"

# Create HMAC
mac = hmac.new(key, message, hashlib.sha256).digest()

# Verify
is_valid = hmac.compare_digest(
    hmac.new(key, message, hashlib.sha256).digest(),
    mac
)
```

**Advantages:**
- ✅ Secure with any hash function
- ✅ Well-analyzed
- ✅ Can use shared secret
- ✅ Fast

**Use Pattern: Encrypt-then-MAC**
```
1. Encrypt: plaintext → ciphertext (with key1)
2. Authenticate: MAC(ciphertext) (with key2)
3. Send: ciphertext + MAC
4. Receive: verify MAC first, then decrypt
```

#### 3. GCM (Galois/Counter Mode) ✅ Modern Standard

**How it works:**
- Combines encryption with Galois Field multiplication
- Produces authentication tag automatically
- Single operation for both

**Advantages:**
- ✅ Built-in authentication
- ✅ Parallelizable
- ✅ No padding needed
- ✅ NIST standard
- ✅ More efficient than encrypt-then-MAC

**Implementation:**
```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = os.urandom(32)
nonce = os.urandom(12)

cipher = AESGCM(key)
ciphertext = cipher.encrypt(nonce, plaintext, ad=None)
plaintext = cipher.decrypt(nonce, ciphertext, ad=None)
# Verification automatic - raises exception if tag invalid
```

---

## Best Practices

### For New Applications
```python
# Use AES-GCM (best practice)
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

key = os.urandom(32)
nonce = os.urandom(12)
cipher = AESGCM(key)
ciphertext = cipher.encrypt(nonce, plaintext)
```

### For Legacy Systems (if necessary)
```python
# Encrypt-then-MAC pattern
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import hmac
import hashlib
import os

key_enc = os.urandom(32)
key_mac = os.urandom(32)
iv = os.urandom(16)

# Encrypt
cipher = Cipher(algorithms.AES(key_enc), modes.CBC(iv))
encryptor = cipher.encryptor()
plaintext_padded = pkcs7_pad(plaintext, 16)
ciphertext = encryptor.update(plaintext_padded) + encryptor.finalize()

# Authenticate
tag = hmac.new(key_mac, iv + ciphertext, hashlib.sha256).digest()

# Send: iv + ciphertext + tag
```

### Never Do This
```python
❌ ciphertext = encrypt(plaintext)
   # Send without authentication
   # Attacker can modify ciphertext!

❌ Decrypt first, verify after
   # Padding oracle attacks possible

❌ Reuse same key for encryption and MAC
   # Theoretical vulnerabilities
```

---

## Security Checklist

- [ ] Use PKCS#7 or compatible padding
- [ ] Prefer AES-GCM for new code
- [ ] If not GCM: use Encrypt-then-MAC
- [ ] Use unique nonce/IV for each message
- [ ] Use cryptographically secure randomness
- [ ] Compare MACs safely (`hmac.compare_digest`)
- [ ] Never leak padding errors
- [ ] Use established libraries, not custom crypto

---

## Summary

1. **Padding**: PKCS#7 is standard, needed for block ciphers
2. **Authentication**: Essential for security, not optional
3. **Modes**: GCM provides both in one efficient operation
4. **Patterns**: Encrypt-then-MAC if not using GCM
5. **Libraries**: Use `cryptography` or similar, never roll your own
