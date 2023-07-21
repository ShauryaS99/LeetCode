class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if len(queryIP.split(".")) == 4:
            isValid = self.validIPv4(queryIP)
            if isValid:
                return "IPv4"
            else:
                return "Neither"
        elif len(queryIP.split(":")) == 8:
            isValid = self.validIPv6(queryIP)
            if isValid:
                return "IPv6"
            else:
                return "Neither"
        else:
            return "Neither"
    
    def validIPv4(self, queryIP):
        elements = queryIP.split(".")
        for i in elements:
            try:
                int(i)
            except ValueError:
                return False
            if int(i) < 0 or int(i) > 255:
                return False
            if i != '0' and len(i) != len(i.lstrip('0')):
                return False
        return True
    
    def validIPv6(self, queryIP):
        elements = queryIP.split(":")
        for i in elements:
            try:
                int(i, 16)
            except ValueError:
                return False
            if len(i) < 1 or len(i) > 4:
                return False
        return True
    