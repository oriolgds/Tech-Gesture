from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from datetime import datetime, timedelta

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Create a certificate signing request (CSR)
subject = x509.Name([
    x509.NameAttribute(x509.NameOID.COUNTRY_NAME, u"ES"),
    x509.NameAttribute(x509.NameOID.STATE_OR_PROVINCE_NAME, u"Catalonia"),
    x509.NameAttribute(x509.NameOID.LOCALITY_NAME, u"Viladecans"),
    x509.NameAttribute(x509.NameOID.ORGANIZATION_NAME, u"Tech Gesture"),
    x509.NameAttribute(x509.NameOID.COMMON_NAME, u"localhost"),
])

csr = x509.CertificateSigningRequestBuilder().subject_name(
    subject
).sign(
    private_key, hashes.SHA256(), default_backend()
)

# Set expiration date
validity_period = timedelta(days=365)
now = datetime.utcnow()
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(subject)
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(now)
    .not_valid_after(now + validity_period)
    .sign(private_key, hashes.SHA256(), default_backend())
)

# Save private key
with open("private_key.pem", "wb") as private_key_file:
    private_key_file.write(private_key.private_bytes(
        Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()
    ))

# Save self-signed certificate
with open("certificate.pem", "wb") as certificate_file:
    certificate_file.write(cert.public_bytes(Encoding.PEM))
