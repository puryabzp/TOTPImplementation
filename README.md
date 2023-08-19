# Two-Factor Authentication (TOTP) Implementation

This project implements a Two-Factor Authentication (TOTP) system in Python. TOTP is a time-based variant of OTP (One-Time Password) that enhances the security of user authentication by generating temporary codes based on the current time.

## What is TOTP?

TOTP stands for Time-Based One-Time Password. It is a widely used method for implementing two-factor authentication (2FA). TOTP codes are typically valid for a short period of time and are generated based on a shared secret key and the current time. This makes TOTP a secure and effective method for protecting user accounts.

## Why Use TOTP?

Using TOTP adds an extra layer of security to user authentication. It requires users to provide both something they know (password) and something they have (OTP code). This makes it more difficult for unauthorized individuals to gain access to user accounts even if they have the password.

## Google Authenticator

Google Authenticator is a popular TOTP application that generates OTP codes on mobile devices. It's commonly used to enable 2FA for various online accounts.

## Using Google Authenticator with this Code

1. Run the provided code to generate a random seed.
2. Generate a QR code containing the provisioning URI using QRCodeGenerator.generate().
3. Scan the QR code using the Google Authenticator app to add the account.
4. The app will display OTP codes that change every 30 seconds.

## How to Use this Code


### Using the Provided `main.py` Script

The `main.py` script demonstrates the usage of the TOTP implementation provided in this project. It showcases how to generate a random seed, create a QR code containing the provisioning URI, and verify OTP codes.

### Prerequisites

Make sure you have Python installed on your system.

### Running the Script

1. Open a terminal and navigate to the project directory.
2. Run the following command to execute the script:

   ```bash
   python main.py
   ```
3. Scan generated QrCode With Google Authenticator
4. Enter OTP from Google Authenticator   
Remember that the system time should be accurate for correct OTP generation and verification.



