# Block Cipher Modes of Operation

## Introduction

Block ciphers like AES encrypt fixed-size blocks of data. Modes of operation define how to handle arbitrary-length messages by combining multiple block cipher operations securely.

## Why Modes Matter

### Problems with Simple Block Encryption
- Same plaintext block always produces same ciphertext (reveals patterns)
- Difficult to handle messages longer than block size
- No built-in authentication
- Vulnerable to various attacks

### Solution: Modes of Operation
- Combine multiple block operations
- Provide security properties (confidentiality, authenticity)
- Handle arbitrary message lengths
- Defend against specific attacks

## Common Modes

### 1. ECB (Electronic Codebook) ❌ **DO NOT USE**

#### How it works
- Divide plaintext into blocks
- Encrypt each block independently with same key
- Concatenate ciphertext blocks

#### Visual Example
```
Plaintext:  [Block1] [Block2] [Block1]
Cipher:     [Cipher1][Cipher2][Cipher1]  ← Same ciphertext for same plaintext!
```

#### Problems
- **Pattern visibility**: Identical plaintext blocks → identical ciphertext blocks
- **Reveals message structure**: Patterns visible in encrypted images
- **No randomness**: Deterministic encryption
- **Insecure**: Not recommended for any application

#### Example Vulnerability
```
Encrypting an image with ECB reveals structure:
Plain image → recognizable patterns remain visible → Encrypted image
```

---

### 2. CBC (Cipher Block Chaining) ✅ **Common**

#### How it works
1. XOR plaintext block with IV or previous ciphertext block
2. Encrypt result with block cipher
3. Use resulting ciphertext as input for next block

#### Diagram
```
IV ──┐
     ├→ [XOR] → [Encrypt] → Ciphertext1 ──┐
     │                                      │
Plaintext1                         Ciphertext1
                                       │
                                       ├→ [XOR] → [Encrypt] → Ciphertext2
                                       │
                              Plaintext2
```

#### Properties
- ✅ Deterministic but appears random (IV provides randomness)
- ✅ Patterns hidden
- ✅ Standard for TLS/SSL
- ❌ Requires random IV for each message
- ❌ No built-in authentication
- ❌ Sequential (cannot parallelize)

#### Implementation
```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

key = os.urandom(32)
iv = os.urandom(16)

cipher = Cipher(
    algorithms.AES(key),
    modes.CBC(iv)
)

encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()
```

#### Important Notes
- IV must be random and unique for each message
- IV can be transmitted in plaintext
- Padding required (PKCS7 standard)
- Must authenticate separately (use HMAC)

---

### 3. CTR (Counter Mode) ✅ **Recommended**

#### How it works
1. Initialize counter with IV
2. Encrypt counter with block cipher
3. XOR plaintext with encrypted counter
4. Increment counter for each block

#### Diagram
```
Counter → [Encrypt] → [XOR] ← Plaintext
                        │
                    Ciphertext
                        │
                    Counter++
```

#### Properties
- ✅ Converts block cipher to stream cipher
- ✅ Parallelizable (counters independent)
- ✅ No padding needed
- ✅ Fast on multi-core processors
- ✅ Nonce can be public
- ❌ Same as CBC: no authentication

#### Implementation
```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = os.urandom(32)
nonce = os.urandom(16)

cipher = Cipher(
    algorithms.AES(key),
    modes.CTR(nonce)
)

encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()
```

#### Use Cases
- Real-time streaming
- Large file encryption
- Parallel processing environments

---

### 4. GCM (Galois/Counter Mode) ✅ **BEST FOR NEW APPLICATIONS**

#### How it works
1. Uses CTR mode for encryption
2. Computes authentication tag using Galois Field multiplication
3. Combines confidentiality and authenticity

#### Diagram
```
Plaintext → [CTR Mode] → Ciphertext ─┐
                                      ├→ [GF Multiply] → Authentication Tag
Key ───────────────────────────────┐
AD (Additional Data) ──────────────┘
```

#### Properties
- ✅ Authenticated encryption
- ✅ Provides confidentiality AND authenticity
- ✅ Parallelizable
- ✅ NIST recommended standard
- ✅ No padding needed
- ✅ Can protect additional data (AD) without encrypting it

#### Implementation
```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = os.urandom(32)  # 256-bit key
nonce = os.urandom(12)  # 96-bit nonce

cipher = AESGCM(key)

# Encrypt and authenticate
ciphertext = cipher.encrypt(nonce, plaintext, additional_data=None)

# Decrypt and verify
plaintext = cipher.decrypt(nonce, ciphertext, additional_data=None)
```

#### Important Notes
- **Nonce**: Use unique nonce for each message (random or counter)
- **Tag**: Authentication tag appended to ciphertext
- **AD (Associated Data)**: Can authenticate without encrypting
- **Reusing nonce with same key = compromise**

#### Use Cases
- TLS 1.3 (recommended cipher suite)
- HTTPS
- Encrypted messaging
- Secure file storage

---

### 5. OFB (Output Feedback) ⚠️ **Legacy**

#### How it works
- Similar to CFB but uses encrypted output directly as feedback
- Block cipher output feeds back into itself

#### Properties
- Stream cipher behavior
- Can work with arbitrary plaintext lengths
- Parallelizable with pre-computed feedback
- **Vulnerable to known plaintext attacks**
- Not recommended for new applications

---

### 6. CFB (Cipher Feedback) ⚠️ **Legacy**

#### How it works
- Encrypts IV/previous ciphertext
- Uses output to XOR plaintext
- Result becomes next feedback value

#### Properties
- Works with less than block size data
- Self-synchronizing (recovers from errors)
- Sequential processing
- Older mode, not recommended

---

## Comparison Table

| Mode | Confidentiality | Authentication | Parallelizable | Streaming | Padding | Use Case |
|------|-----------------|-----------------|----------------|-----------|---------|----------|
| **ECB** | ❌ | ❌ | ✅ | ❌ | ✅ | **DO NOT USE** |
| **CBC** | ✅ | ❌ | ❌ | ❌ | ✅ | Legacy, TLS 1.2 |
| **CTR** | ✅ | ❌ | ✅ | ✅ | ❌ | Streaming, parallel |
| **GCM** | ✅ | ✅ | ✅ | ✅ | ❌ | **Modern standard** |
| **OFB** | ✅ | ❌ | ⚠️ | ✅ | ❌ | Legacy |
| **CFB** | ✅ | ❌ | ❌ | ✅ | ❌ | Legacy |

## Recommendations

### For New Applications
**Use AES-GCM** - Best of both worlds:
- Authenticated encryption
- Fast and efficient
- NIST approved
- Industry standard

### For Legacy Systems
- CBC mode with HMAC authentication
- Ensure unique random IV for each message

### For High-Performance Streaming
- CTR mode + separate HMAC
- Parallelizable
- No padding overhead

### Never Use
- ❌ ECB mode
- ❌ Modes without authentication

## Key Takeaways

1. **Mode selection matters** - wrong mode = security compromise
2. **ECB is insecure** - never use it
3. **GCM is preferred** - modern, authenticated, efficient
4. **IV/Nonce management critical** - reuse = compromise
5. **Always authenticate** - GCM does it, otherwise use HMAC
6. **Use established libraries** - don't implement yourself

## Summary

Block cipher modes extend basic block encryption to handle real-world requirements. While many modes exist for historical or specialized reasons, modern applications should default to **AES-GCM** for its combination of security, performance, and standardization.
