def decorate(func):
    def wrapper(text):
        return "### " + func(text) + " ###"
    return wrapper


class Report:

    def __init__(self, title):
        self.title = title
        self.sections = []

    @classmethod
    def create_report(cls):
        return cls("My Report")

    def add_section(self, section):
        self.sections.append(section)

    def __str__(self):
        result = self.title + "\n"

        for section in self.sections:
            result = result + section + "\n"

        return result

    def __len__(self):
        return len(self.sections)


@decorate
def format_text(text):
    return text.upper()


report = Report.create_report()

report.add_section("Introduction")
report.add_section("Python Programming")
report.add_section("Conclusion")

print(report)

print("Number of sections:", len(report))

print(format_text("final report"))