class Solution:
    def reformatDate(self, date: str) -> str:
        month_map = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }
        
        day, month, year = date.split(" ")
        day = day[:-2]
        if int(day) < 10:
            day = "0" + day
        month = month_map[month]
        result = f"{year}-{month}-{day}"
        return result
        