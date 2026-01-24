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
import unittest

import tgcrypto


class TestCTR256NIST(unittest.TestCase):
    # https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Standards-and-Guidelines/documents/examples/AES_CTR.pdf

    def test_ctr256_encrypt(self):
        key = bytes.fromhex("""
        603DEB10 15CA71BE 2B73AEF0 857D7781
        1F352C07 3B6108D7 2D9810A3 0914DFF4
        """.replace(" ", "").replace("\n", ""))

        iv = bytes.fromhex("""
        F0F1F2F3 F4F5F6F7 F8F9FAFB FCFDFEFF
        """.replace(" ", "").replace("\n", ""))

        plaintext = bytes.fromhex("""
        6BC1BEE2 2E409F96 E93D7E11 7393172A
        AE2D8A57 1E03AC9C 9EB76FAC 45AF8E51
        30C81C46 A35CE411 E5FBC119 1A0A52EF
        F69F2445 DF4F9B17 AD2B417B E66C3710
        """.replace(" ", "").replace("\n", ""))

        ciphertext = bytes.fromhex("""
        601EC313 775789A5 B7A7F504 BBF3D228
        F443E3CA 4D62B59A CA84E990 CACAF5C5
        2B0930DA A23DE94C E87017BA 2D84988D
        DFC9C58D B67AADA6 13C2DD08 457941A6
        """.replace(" ", "").replace("\n", ""))

        self.assertEqual(tgcrypto.ctr256_encrypt(plaintext, key, iv, bytes(1)), ciphertext)

    def test_ctr256_decrypt(self):
        key = bytes.fromhex("""
        603DEB10 15CA71BE 2B73AEF0 857D7781
        1F352C07 3B6108D7 2D9810A3 0914DFF4
        """.replace(" ", "").replace("\n", ""))

        iv = bytes.fromhex("""
        F0F1F2F3 F4F5F6F7 F8F9FAFB FCFDFEFF
        """.replace(" ", "").replace("\n", ""))

        ciphertext = bytes.fromhex("""
        601EC313 775789A5 B7A7F504 BBF3D228
        F443E3CA 4D62B59A CA84E990 CACAF5C5
        2B0930DA A23DE94C E87017BA 2D84988D
        DFC9C58D B67AADA6 13C2DD08 457941A6
        """.replace(" ", "").replace("\n", ""))

        plaintext = bytes.fromhex("""
        6BC1BEE2 2E409F96 E93D7E11 7393172A
        AE2D8A57 1E03AC9C 9EB76FAC 45AF8E51
        30C81C46 A35CE411 E5FBC119 1A0A52EF
        F69F2445 DF4F9B17 AD2B417B E66C3710
        """.replace(" ", "").replace("\n", ""))

        self.assertEqual(tgcrypto.ctr256_decrypt(ciphertext, key, iv, bytes(1)), plaintext)


class TestCTR256Cryptography(unittest.TestCase):
    # https://github.com/pyca/cryptography/blob/cd4de3ce6dc2a0dd4171b869e187857e4125853b/vectors/cryptography_vectors/ciphers/AES/CTR/aes-256-ctr.txt

    def test_ctr256_encrypt_extra1(self):
        key = bytes.fromhex("776BEFF2851DB06F4C8A0542C8696F6C6A81AF1EEC96B4D37FC1D689E6C1C104")
        iv = bytes.fromhex("00000060DB5672C97AA8F0B200000001")
        plaintext = bytes.fromhex("53696E676C6520626C6F636B206D7367")
        ciphertext = bytes.fromhex("145AD01DBF824EC7560863DC71E3E0C0")

        self.assertEqual(tgcrypto.ctr256_encrypt(plaintext, key, iv, bytes(1)), ciphertext)

    def test_ctr256_encrypt_extra2(self):
        key = bytes.fromhex("F6D66D6BD52D59BB0796365879EFF886C66DD51A5B6A99744B50590C87A23884")
        iv = bytes.fromhex("00FAAC24C1585EF15A43D87500000001")
        plaintext = bytes.fromhex("000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F")
        ciphertext = bytes.fromhex("F05E231B3894612C49EE000B804EB2A9B8306B508F839D6A5530831D9344AF1C")

        self.assertEqual(tgcrypto.ctr256_encrypt(plaintext, key, iv, bytes(1)), ciphertext)

    def test_ctr256_encrypt_extra3(self):
        key = bytes.fromhex("FF7A617CE69148E4F1726E2F43581DE2AA62D9F805532EDFF1EED687FB54153D")
        iv = bytes.fromhex("001CC5B751A51D70A1C1114800000001")
        plaintext = bytes.fromhex("000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F20212223")
        ciphertext = bytes.fromhex("EB6C52821D0BBBF7CE7594462ACA4FAAB407DF866569FD07F48CC0B583D6071F1EC0E6B8")

        self.assertEqual(tgcrypto.ctr256_encrypt(plaintext, key, iv, bytes(1)), ciphertext)


class TestCTR256Input(unittest.TestCase):
    TYPE_ERROR_PATTERN = r"'\w+' does not (support|have) the buffer interface|a bytes-like object is required, not '\w+'"

    def test_ctr256_encrypt_invalid_args_count(self):
        with self.assertRaisesRegex(TypeError, r"function takes exactly \d arguments \(\d given\)"):
            tgcrypto.ctr256_encrypt(os.urandom(8), os.urandom(32), os.urandom(16))

    def test_ctr256_encrypt_invalid_args_type(self):
        with self.assertRaisesRegex(TypeError, self.TYPE_ERROR_PATTERN):
            tgcrypto.ctr256_encrypt(1, 2, 3, 4)

    def test_ctr256_encrypt_empty_data(self):
        with self.assertRaisesRegex(ValueError, r"Data must not be empty"):
            tgcrypto.ctr256_encrypt(b"", os.urandom(32), os.urandom(16), bytes(1))

    def test_ctr256_encrypt_invalid_key_size(self):
        with self.assertRaisesRegex(ValueError, r"Key size must be exactly 32 bytes"):
            tgcrypto.ctr256_encrypt(os.urandom(8), os.urandom(31), os.urandom(16), bytes(1))

    def test_ctr256_encrypt_invalid_iv_size(self):
        with self.assertRaisesRegex(ValueError, r"IV size must be exactly 16 bytes"):
            tgcrypto.ctr256_encrypt(os.urandom(8), os.urandom(32), os.urandom(15), bytes(1))

    def test_ctr256_encrypt_invalid_state_size(self):
        with self.assertRaisesRegex(ValueError, r"State size must be exactly 1 byte"):
            tgcrypto.ctr256_encrypt(os.urandom(8), os.urandom(32), os.urandom(16), bytes([1, 2, 3]))

    def test_ctr256_encrypt_invalid_state_value(self):
        with self.assertRaisesRegex(ValueError, r"State value must be in the range \[0, 15\]"):
            tgcrypto.ctr256_encrypt(os.urandom(8), os.urandom(32), os.urandom(16), bytes([16]))

    def test_ctr256_decrypt_invalid_args_count(self):
        with self.assertRaisesRegex(TypeError, r"function takes exactly \d arguments \(\d given\)"):
            tgcrypto.ctr256_decrypt(os.urandom(8), os.urandom(32), os.urandom(16))

    def test_ctr256_decrypt_invalid_args_type(self):
        with self.assertRaisesRegex(TypeError, self.TYPE_ERROR_PATTERN):
            tgcrypto.ctr256_decrypt(1, 2, 3, 4)

    def test_ctr256_decrypt_empty_data(self):
        with self.assertRaisesRegex(ValueError, r"Data must not be empty"):
            tgcrypto.ctr256_decrypt(b"", os.urandom(32), os.urandom(16), bytes(1))

    def test_ctr256_decrypt_invalid_key_size(self):
        with self.assertRaisesRegex(ValueError, r"Key size must be exactly 32 bytes"):
            tgcrypto.ctr256_decrypt(os.urandom(8), os.urandom(31), os.urandom(16), bytes(1))

    def test_ctr256_decrypt_invalid_iv_size(self):
        with self.assertRaisesRegex(ValueError, r"IV size must be exactly 16 bytes"):
            tgcrypto.ctr256_decrypt(os.urandom(8), os.urandom(32), os.urandom(15), bytes(1))

    def test_ctr256_decrypt_invalid_state_size(self):
        with self.assertRaisesRegex(ValueError, r"State size must be exactly 1 byte"):
            tgcrypto.ctr256_decrypt(os.urandom(8), os.urandom(32), os.urandom(16), bytes([1, 2, 3]))

    def test_ctr256_decrypt_invalid_state_value(self):
        with self.assertRaisesRegex(ValueError, r"State value must be in the range \[0, 15\]"):
            tgcrypto.ctr256_decrypt(os.urandom(8), os.urandom(32), os.urandom(16), bytes([16]))


class TestCTR256Random(unittest.TestCase):
    DATA_MAX_SIZE = 1024
    KEY_SIZE = 32
    IV_SIZE = 16

    TESTS_AMOUNT = 500

    TEMPLATE = """
    def test_ctr256_random_{mode1}_{count}(self):
        data = {data}
        key = {key}
        iv = {iv}
        iv_copy = iv.copy()
        state = {state}
        state_copy = state.copy()

        a = tgcrypto.ctr256_{mode1}(data, key, iv, state)
        b = tgcrypto.ctr256_{mode2}(a, key, iv_copy, state_copy)

        self.assertEqual(data, b)
    """.replace("\n    ", "\n")

    for count in range(TESTS_AMOUNT):
        exec(
            TEMPLATE.format(
                mode1="encrypt",
                mode2="decrypt",
                count=count,
                data=os.urandom(random.randint(1, DATA_MAX_SIZE)),
                key=os.urandom(KEY_SIZE),
                iv=bytearray(os.urandom(IV_SIZE)),
                state=bytearray([random.randint(0, 15)])
            )
        )

    for count in range(TESTS_AMOUNT):
        exec(
            TEMPLATE.format(
                mode1="decrypt",
                mode2="encrypt",
                count=count,
                data=os.urandom(random.randint(1, DATA_MAX_SIZE)),
                key=os.urandom(KEY_SIZE),
                iv=bytearray(os.urandom(IV_SIZE)),
                state=bytearray([random.randint(0, 15)])
            )
        )


if __name__ == "__main__":
    unittest.main()
