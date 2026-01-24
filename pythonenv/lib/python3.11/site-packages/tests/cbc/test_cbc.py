#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import os
import random
import re
import unittest

import tgcrypto


class TestCBC256NIST(unittest.TestCase):
    # https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Standards-and-Guidelines/documents/examples/AES_CBC.pdf

    def test_cbc256_encrypt(self):
        key = bytes.fromhex("""
        603DEB10 15CA71BE 2B73AEF0 857D7781
        1F352C07 3B6108D7 2D9810A3 0914DFF4
        """.replace(" ", "").replace("\n", ""))

        iv = bytes.fromhex("""
        00010203 04050607 08090A0B 0C0D0E0F
        """.replace(" ", "").replace("\n", ""))

        plaintext = bytes.fromhex("""
        6BC1BEE2 2E409F96 E93D7E11 7393172A
        AE2D8A57 1E03AC9C 9EB76FAC 45AF8E51
        30C81C46 A35CE411 E5FBC119 1A0A52EF
        F69F2445 DF4F9B17 AD2B417B E66C3710
        """.replace(" ", "").replace("\n", ""))

        ciphertext = bytes.fromhex("""
        F58C4C04 D6E5F1BA 779EABFB 5F7BFBD6
        9CFC4E96 7EDB808D 679F777B C6702C7D
        39F23369 A9D9BACF A530E263 04231461
        B2EB05E2 C39BE9FC DA6C1907 8C6A9D1B
        """.replace(" ", "").replace("\n", ""))

        self.assertEqual(tgcrypto.cbc256_encrypt(plaintext, key, iv), ciphertext)

    def test_cbc256_decrypt(self):
        key = bytes.fromhex("""
        603DEB10 15CA71BE 2B73AEF0 857D7781
        1F352C07 3B6108D7 2D9810A3 0914DFF4
        """.replace(" ", "").replace("\n", ""))

        iv = bytes.fromhex("""
        00010203 04050607 08090A0B 0C0D0E0F
        """.replace(" ", "").replace("\n", ""))

        ciphertext = bytes.fromhex("""
        F58C4C04 D6E5F1BA 779EABFB 5F7BFBD6
        9CFC4E96 7EDB808D 679F777B C6702C7D
        39F23369 A9D9BACF A530E263 04231461
        B2EB05E2 C39BE9FC DA6C1907 8C6A9D1B
        """.replace(" ", "").replace("\n", ""))

        plaintext = bytes.fromhex("""
        6BC1BEE2 2E409F96 E93D7E11 7393172A
        AE2D8A57 1E03AC9C 9EB76FAC 45AF8E51
        30C81C46 A35CE411 E5FBC119 1A0A52EF
        F69F2445 DF4F9B17 AD2B417B E66C3710
        """.replace(" ", "").replace("\n", ""))

        self.assertEqual(tgcrypto.cbc256_decrypt(ciphertext, key, iv), plaintext)


class TestCBC256Cryptography(unittest.TestCase):
    # https://github.com/pyca/cryptography/blob/cd4de3ce6dc2a0dd4171b869e187857e4125853b/vectors/cryptography_vectors/ciphers/AES/CBC

    TEMPLATE = """
    def test_cbc256_{mode}_{name}_{count}(self):
        key = bytes.fromhex("{key}")
        iv = bytes.fromhex("{iv}")
        plaintext = bytes.fromhex("{plaintext}")
        ciphertext = bytes.fromhex("{ciphertext}")
    
        self.assertEqual(tgcrypto.cbc256_{mode}({input}, key, iv), {output})
    """.replace("\n    ", "\n")

    PATTERN = r"COUNT = (\d+)\nKEY = (\w+)\nIV = (\w+)\n(PLAINTEXT|CIPHERTEXT) = (\w+)\n(PLAINTEXT|CIPHERTEXT) = (\w+)"

    BASE_PATH = os.path.dirname(__file__) + "/vectors"

    for path in os.listdir(BASE_PATH):
        path = BASE_PATH + "/" + path

        with open(path, "r", encoding="utf-8") as f:
            for match in re.finditer(PATTERN, f.read()):
                count, key, iv, plain_or_cipher, bytes1, _, bytes2 = match.groups()

                if plain_or_cipher == "PLAINTEXT":
                    mode = "encrypt"
                    plaintext = bytes1
                    ciphertext = bytes2
                    input = "plaintext"
                    output = "ciphertext"
                else:
                    mode = "decrypt"
                    plaintext = bytes2
                    ciphertext = bytes1
                    input = "ciphertext"
                    output = "plaintext"

                exec(
                    TEMPLATE.format(
                        mode=mode,
                        name=os.path.split(path)[-1].split(".")[0],
                        count=count,
                        key=key,
                        iv=iv,
                        plaintext=plaintext,
                        ciphertext=ciphertext,
                        input=input,
                        output=output
                    )
                )


class TestCBC256Input(unittest.TestCase):
    TYPE_ERROR_PATTERN = r"'\w+' does not (support|have) the buffer interface|a bytes-like object is required, not '\w+'"

    def test_cbc256_encrypt_invalid_args_count(self):
        with self.assertRaisesRegex(TypeError, r"function takes exactly \d arguments \(\d given\)"):
            tgcrypto.cbc256_encrypt(os.urandom(16), os.urandom(32))

    def test_cbc256_encrypt_invalid_args_type(self):
        with self.assertRaisesRegex(TypeError, self.TYPE_ERROR_PATTERN):
            tgcrypto.cbc256_encrypt(1, 2, 3)

    def test_cbc256_encrypt_empty_data(self):
        with self.assertRaisesRegex(ValueError, r"Data must not be empty"):
            tgcrypto.cbc256_encrypt(b"", os.urandom(32), os.urandom(16))

    def test_cbc256_encrypt_invalid_key_size(self):
        with self.assertRaisesRegex(ValueError, r"Key size must be exactly 32 bytes"):
            tgcrypto.cbc256_encrypt(os.urandom(16), os.urandom(31), os.urandom(16))

    def test_cbc256_encrypt_invalid_iv_size(self):
        with self.assertRaisesRegex(ValueError, r"IV size must be exactly 16 bytes"):
            tgcrypto.cbc256_encrypt(os.urandom(16), os.urandom(32), os.urandom(15))

    def test_cbc256_decrypt_invalid_args_count(self):
        with self.assertRaisesRegex(TypeError, r"function takes exactly \d arguments \(\d given\)"):
            tgcrypto.cbc256_decrypt(os.urandom(16), os.urandom(32))

    def test_cbc256_decrypt_invalid_args_type(self):
        with self.assertRaisesRegex(TypeError, self.TYPE_ERROR_PATTERN):
            tgcrypto.cbc256_decrypt(1, 2, 3)

    def test_cbc256_decrypt_empty_data(self):
        with self.assertRaisesRegex(ValueError, r"Data must not be empty"):
            tgcrypto.cbc256_decrypt(b"", os.urandom(32), os.urandom(16))

    def test_cbc256_decrypt_invalid_key_size(self):
        with self.assertRaisesRegex(ValueError, r"Key size must be exactly 32 bytes"):
            tgcrypto.cbc256_decrypt(os.urandom(16), os.urandom(31), os.urandom(16))

    def test_cbc256_decrypt_invalid_iv_size(self):
        with self.assertRaisesRegex(ValueError, r"IV size must be exactly 16 bytes"):
            tgcrypto.cbc256_decrypt(os.urandom(16), os.urandom(32), os.urandom(15))


class TestCBC256Random(unittest.TestCase):
    DATA_CHUNK_MAX_SIZE = 64
    KEY_SIZE = 32
    IV_SIZE = 16

    TESTS_AMOUNT = 500

    TEMPLATE = """
    def test_cbc256_random_{mode1}_{count}(self):
        data = {data}
        key = {key}
        iv = {iv}
        iv_copy = iv.copy()

        a = tgcrypto.cbc256_{mode1}(data, key, iv)
        b = tgcrypto.cbc256_{mode2}(a, key, iv_copy)

        self.assertEqual(data, b)
    """.replace("\n    ", "\n")

    for count in range(TESTS_AMOUNT):
        exec(
            TEMPLATE.format(
                mode1="encrypt",
                mode2="decrypt",
                count=count,
                data=os.urandom(random.randint(1, DATA_CHUNK_MAX_SIZE) * 16),
                key=os.urandom(KEY_SIZE),
                iv=bytearray(os.urandom(IV_SIZE)),
            )
        )

    for count in range(TESTS_AMOUNT):
        exec(
            TEMPLATE.format(
                mode1="decrypt",
                mode2="encrypt",
                count=count,
                data=os.urandom(random.randint(1, DATA_CHUNK_MAX_SIZE) * 16),
                key=os.urandom(KEY_SIZE),
                iv=bytearray(os.urandom(IV_SIZE)),
            )
        )


if __name__ == "__main__":
    unittest.main()
