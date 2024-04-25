from TestCode import login
class Test_01_Header:
    header = 20
    def logo(self):
        self.obj = login.Test_01_login()
        self.obj.check()
        print("done")

test_header = Test_01_Header()
test_header.logo()