"""
Compress module tests
"""

import os
import tarfile
import tempfile
import unittest

from zipfile import ZipFile, ZIP_DEFLATED

from txtai.compress import Compress, CompressFactory

# pylint: disable = C0411
from utils import Utils


class TestCompress(unittest.TestCase):
    """
    Compress tests.
    """

    def testInvalidTar(self):
        """
        Test invalid tar file
        """

        path = os.path.join(tempfile.gettempdir(), "badtar")
        with tarfile.open(path, "w") as tar:
            tar.add(Utils.PATH, arcname="..")

        compress = CompressFactory.create("tar")

        # Validate error is thrown for file
        with self.assertRaises(IOError):
            compress.unpack(path, path)

    def testInvalidZip(self):
        """
        Test invalid zip file
        """

        path = os.path.join(tempfile.gettempdir(), "badzip")
        with ZipFile(path, "w", ZIP_DEFLATED) as zfile:
            zfile.write(Utils.PATH + "/article.pdf", arcname="../article.pdf")

        compress = CompressFactory.create("zip")

        # Validate error is thrown for file
        with self.assertRaises(IOError):
            compress.unpack(path, path)

    def testNotImplemented(self):
        """
        Test exceptions for non-implemented methods
        """

        compress = Compress()

        self.assertRaises(NotImplementedError, compress.pack, None, None)
        self.assertRaises(NotImplementedError, compress.unpack, None, None)
