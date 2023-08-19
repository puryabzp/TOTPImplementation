import os
import pyotp
import qrcode
import qrcode.image.svg


class SeedGenerator:
    """
    This class is responsible for generating a random seed using the Base32 encoding.
    """

    @staticmethod
    def generate():
        """
        Generate and return a random seed using the Base32 encoding.

        Returns:
            str: A random seed (Base32 encoded).
        """
        return pyotp.random_base32()


class OTPGenerator:
    """
    This class is responsible for generating OTP codes based on a given seed.
    """

    def __init__(self):
        self.interval_as_sec = 30

    def generate(self, seed):
        """
        Generate an OTP code based on a given seed.

        Args:
            seed (str): The seed associated with the user.

        Returns:
            str: The generated OTP code.
        """
        totp = pyotp.TOTP(seed, interval=self.interval_as_sec)
        otp = totp.now()
        return otp


class OTPVerifier:
    """
    This class is responsible for verifying OTP codes based on the provided seed and interval.
    """

    def __init__(self, interval_as_sec=30):
        self.interval_as_sec = interval_as_sec

    def verify(self, otp, seed):
        """
        Verify an OTP code based on the provided seed and interval.

        Args:
            otp (str): The OTP code to verify.
            seed (str): The seed associated with the user.

        Returns:
            bool: True if the OTP is valid, False otherwise.
        """
        totp = pyotp.TOTP(seed, interval=self.interval_as_sec)
        return totp.verify(otp)


class QRCodeGenerator:
    """
    This class is responsible for generating QR code images containing provisioning URIs for OTP.
    """

    def __init__(self):
        self.interval_as_sec = 30

    @staticmethod
    def generate_temp_file(filename=None):
        """
        Generate a temporary file path in a specific directory.

        Args:
            filename (str, optional): The filename to append to the path.

        Returns:
            str: The temporary file path.
        """
        directory = 'temp_qrcodes'  # Change to your desired directory name
        os.makedirs(directory, exist_ok=True)  # Create directory if it doesn't exist
        if filename is not None:
            return os.path.join(os.path.join(os.getcwd(), directory), filename)
        return os.path.join(os.getcwd(), directory)

    def generate(self, seed, name, issuer_name, file_name):
        """
        Generate a QR code image containing the provisioning URI for OTP.

        Args:
            seed (str): The seed associated with the user.
            name (str): The user's name.
            issuer_name (str): The name of the issuer (e.g., the service or application name).
            file_name (str): The filename to save the QR code image (without extension).

        Returns:
            str: The file path of the generated QR code image.
        """
        totp = pyotp.TOTP(seed, interval=self.interval_as_sec)
        url = totp.provisioning_uri(name=name, issuer_name=issuer_name)
        img = qrcode.make(url, image_factory=qrcode.image.svg.SvgImage)
        file_path = self.generate_temp_file(f'{file_name}.svg')
        with open(file_path, 'wb') as qr:
            img.save(qr)
        return file_path


class Authenticator:
    """
    This class provides methods for offline verification of OTP codes.
    """

    @staticmethod
    def verify_google_authenticator(seed, otp):
        """
        Verify a Google Authenticator OTP code based on the provided seed.

        Args:
            seed (str): The seed associated with the user.
            otp (str): The OTP code to verify.

        Returns:
            bool: True if the OTP is valid, False otherwise.
        """
        return pyotp.TOTP(seed).verify(otp)


class TOTPHandler:
    """
    This class coordinates the various components for TOTP operations and provides a high-level interface.
    """

    def __init__(self):
        self.otp_generator = OTPGenerator()
        self.otp_verifier = OTPVerifier()
        self.qr_code_generator = QRCodeGenerator()
        self.authenticator = Authenticator()


# Create an instance of TOTPHandler
totp_handler = TOTPHandler()
