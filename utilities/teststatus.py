from utilities.custom_logger import custom_logger
import logging


class TestStatus:
    log = custom_logger(logging.INFO)
    result_list = []

    def set_result(self, result, message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + message)
            else:
                self.result_list.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + message)
        except:
            self.result_list.append("FAIL")
            self.log.error("### EXCEPTION Occurred")

    def mark(self, result, message):
        self.set_result(result, message)

    def mark_final(self, result, message):
        self.set_result(result, message)

        if "FAIL" in self.result_list:
            self.log.error("### TEST FAILED")
            self.result_list.clear()
            assert True == False
        else:
            self.log.info("### TEST SUCCESSFUL")
            self.result_list.clear()
            assert True == True
