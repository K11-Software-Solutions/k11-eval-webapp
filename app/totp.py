import pyotp
def generate_secret(): return pyotp.random_base32()
def verify_totp(secret, token): return pyotp.TOTP(secret).verify(token)
