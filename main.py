from totp_handler import SeedGenerator, TOTPHandler


def main():
    # Create an instance of TOTPHandler
    totp_handler = TOTPHandler()

    # Generate a random seed
    seed = SeedGenerator().generate()
    print(f"Generated Seed: {seed}")

    # Generate a QR code image containing the provisioning URI
    name = "John Doe"
    issuer_name = "My App"
    file_name = "qr_code"
    qr_code_file_path = totp_handler.qr_code_generator.generate(seed, name, issuer_name, file_name)
    print(f"QR Code Image Generated: {qr_code_file_path}")
    num_attempts = 5
    for _ in range(num_attempts):
        generated_otp = totp_handler.otp_generator.generate(seed)
        print(f"Generated OTP: {generated_otp}")

        entered_otp = input("Enter OTP code: ")

        if totp_handler.otp_verifier.verify(entered_otp, seed):
            print("OTP Verified: Access Granted")
        else:
            print("OTP Verification Failed: Access Denied")


if __name__ == "__main__":
    main()
