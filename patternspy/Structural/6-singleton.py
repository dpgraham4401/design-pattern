# Singleton pattern
# used to ensure that class has only one instance and provide a global point of access to it.
# This is useful when
# 1. We need to control access to a shared resource.
# 2. Prevents state held by the global instance from being overwritten.
# Generally, the singleton pattern should be used sparingly. it inherently introduced coupling, can make testing
# difficult. It also technically violates the Single Responsibility Principle (SRP).

class PrinterDriver:
    """
    A singleton printer driver. For purposes of this example, only one printer driver can be used at any time
    A singleton class should make the constructor private, and expose a static method to get (or create if necessary)
    the singleton instance.
    """
    _instance = None
    jobs = []

    @classmethod
    def get_driver(cls) -> "PrinterDriver":
        return cls.__new__(cls)

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add_job(self, job):
        self.jobs.append(job)

    def display_jobs(self):
        print(self.jobs)


def main():
    driver1 = PrinterDriver.get_driver()
    driver2 = PrinterDriver.get_driver()
    # in pythonic fashion, we've overridden the __new__ method. We instantiate the class like normal.
    # which is not strictly in line with the singleton pattern, but arguably more pythonic and easier to understand.
    driver3 = PrinterDriver()
    # we can see that all three references point to the same instance in memory
    print(f"driver1 {repr(driver1)}\ndriver2 {repr(driver2)}\ndriver3 {repr(driver3)}")
    if (driver1 is driver2) and (driver2 is driver3):
        print("All reference the same instance")

    # Here, the client code doesn't need to know that it's using the same instance of the PrinterDriver
    driver1.add_job("print job 1")
    driver2.add_job("print job 2")
    driver3.add_job("print job 3")

    # But, driver1 will display all jobs, including those added by driver2 and driver3
    driver1.display_jobs()


if __name__ == "__main__":
    main()
