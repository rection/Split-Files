import unittest
import Split

LINK="www.google.com"
bolum=42

FIRST=Split.install()
class birinci_secenek:

    if __name__ == '__main__':
        unittest.main()

    def check_test(self):
        answer=FIRST.check(LINK)
        self.assertEqual(answer,'Found the web page')

    def wget_test(self):
        answer_wget=FIRST.wget()
        self.assertEqual(answer_wget,'I have installed wget')

    def download_test(self,LINK,bolum):
        answer_download=FIRST.download(LINK,bolum)
        self.assertEqual(answer_download,'I have downloaded file')
