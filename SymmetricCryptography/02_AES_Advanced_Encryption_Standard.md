# AES (Advanced Encryption Standard)

## Overview

AES is the most widely used symmetric encryption algorithm in the world. It was selected by the US government to protect classified information and is now standard worldwide.

## History

- **1997**: NIST calls for AES cipher proposals
- **2000**: Rijndael cipher selected as AES winner
- **2001**: FIPS 197 standard published
- **Present**: Default choice for symmetric encryption

## Key Features

### Security Parameters
- **Block Size**: 128 bits (16 bytes)
- **Key Sizes**: 128, 192, or 256 bits
- **Rounds**: 10 (128-bit key), 12 (192-bit key), 14 (256-bit key)
- **State**: 4×4 matrix of bytes

### Why AES is Strong
- No known practical attacks against full AES
- Resistant to all known attacks including differential and linear cryptanalysis
- 256-bit key provides quantum resistance for foreseeable future

## How AES Works

### High-Level Process
1. **Key Expansion**: Generate round keys from original key
2. **Initial Round**: AddRoundKey operation
3. **Main Rounds**: Repeat for (rounds - 1) iterations:
   - SubBytes: Substitute each byte using S-box
   - ShiftRows: Rearrange bytes
   - MixColumns: Mix columns (except final round)
   - AddRoundKey: XOR with round key
4. **Final Round**: Same but no MixColumns

### Key Operations

#### SubBytes
- Substitution using S-box (Substitution box)
- Non-linear transformation
- Provides confusion

#### ShiftRows
- Rotate bytes in each row
- Row 0: no shift
- Row 1: shift left by 1
- Row 2: shift left by 2
- Row 3: shift left by 3

#### MixColumns
- Multiply each column by polynomial matrix
- Over Galois Field (GF(2^8))
- Provides diffusion

#### AddRoundKey
- XOR with derived round key
- Linear operation

## AES Variants

### AES-128
- 128-bit key
- 10 rounds
- Fast, good balance
- Suitable for most applications

### AES-192
- 192-bit key
- 12 rounds
- Medium speed, stronger

### AES-256
- 256-bit key
- 14 rounds
- Slower, maximum security
- Future-proof for long-term confidentiality

## Modes of Operation

### Recommended Modes
- **GCM (Galois/Counter Mode)**: Authenticated encryption
- **CBC (Cipher Block Chaining)**: Traditional, requires authentication
- **CTR (Counter Mode)**: Streaming, parallelizable

### Modes to Avoid
- **ECB (Electronic Codebook)**: Reveals patterns

## Implementation in Python

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate key and IV
key = os.urandom(32)  # AES-256
iv = os.urandom(16)

# Create cipher in CBC mode
cipher = Cipher(
    algorithms.AES(key),
    modes.CBC(iv),
    backend=default_backend()
)

# Encrypt
encryptor = cipher.encryptor()
plaintext = b"Secret message"
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Decrypt
decryptor = cipher.decryptor()
decrypted = decryptor.update(ciphertext) + decryptor.finalize()
```

## Security Considerations

### Key Length
- **AES-128**: Sufficient for most applications
- **AES-192**: Recommended for sensitive data
- **AES-256**: Maximum security, government use

### IV/Nonce
- Use random IV for each message
- Never reuse IV with same key
- IV doesn't need to be secret

### Authentication
- AES alone only provides confidentiality
- Use HMAC or authenticated modes (GCM) for integrity
- Prefer AES-GCM for combined security

## Performance

### Speed Comparison (typical)
- AES-128: ~10 Gbps (on modern CPU)
- AES-192: ~8 Gbps
- AES-256: ~6 Gbps

### Hardware Acceleration
- AES-NI instructions on modern CPUs
- Significant speedup (3-5x)
- Automatic in libraries using hardware support

## Best Practices

1. **Use AES-256 for high security**
2. **Use AES-GCM for authenticated encryption**
3. **Generate cryptographically secure random keys**
4. **Use unique IV for each encryption**
5. **Never implement AES yourself** - use established libraries
6. **Rotate keys periodically**
7. **Protect key material** - use secure key storage

## Conclusion

AES is the gold standard for symmetric encryption. It's fast, secure, and thoroughly analyzed. For modern applications requiring confidentiality, AES-GCM is the recommended choice providing both encryption and authentication in one operation.
