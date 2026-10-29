import unittest
from showcase.photo_upload import validate_upload, MAX_UPLOAD_BYTES


class PhotoUploadTests(unittest.TestCase):
    def test_accepts_supported_metadata(self):
        result = validate_upload(filename="room.webp", content_type="image/webp", size_bytes=1024)
        self.assertTrue(result.accepted)

    def test_rejects_unsupported_content_type(self):
        result = validate_upload(filename="payload.exe", content_type="application/octet-stream", size_bytes=1024)
        self.assertFalse(result.accepted)

    def test_rejects_too_large_file(self):
        result = validate_upload(filename="large.jpg", content_type="image/jpeg", size_bytes=MAX_UPLOAD_BYTES + 1)
        self.assertFalse(result.accepted)


if __name__ == "__main__":
    unittest.main()
