# Some Exercises Day 15


"""
Comprehensive exercise: Employee management system for a cybersecurity
company (CyberShield Inc.)
========================================================================
Each TODO covers one concept from the video. Complete them in order,
then run this file (python security_agency_exercise.py) to check your 
solutions against the expected output.
"""


class Department:
    """Simple class that gets embedded inside Employee -> this is "Combining Objects" """

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def __str__(self):
        return f"{self.name} (Budget: ${self.budget:,})"


class Employee:
    # TODO 1 (Static attribute): shared value across ALL employees, not per-instance
    company_name = "Aliens Inc."  # set to "CyberShield Inc."

    # TODO 2 (Static attribute): running total of employees created
    employee_count = 0

    def __init__(self, name, department: Department, salary, ssn):
        self.name = name                       # public attribute
        self.department = department           # combining objects
        self._years_of_service = 0             # TODO 3: make this protected (single underscore)
        self.__salary = None                    # TODO 4: private attribute (filled via the setter below)
        self.salary = salary                    # this will call the setter you write in TODO 7
        self.__ssn = self.__encrypt_ssn(ssn)    # private attribute + calling a private method

        # TODO 5: increment Employee.employee_count by 1
        Employee.employee_count += 1

    # ---------------- Property: salary getter/setter ----------------
    @property
    def salary(self):
        # TODO 6: return the private __salary value
        return self.__salary

    @salary.setter
    def salary(self, value):
        # TODO 7: if value <= 0, raise ValueError("Salary must be positive")
        # otherwise, store it in __salary
        if value <= 0:
            raise ValueError("Salary must be positive")
        else:
            self.__salary = value

    # ---------------- Protected method ----------------
    def _calculate_bonus(self):
        """
        Protected method: an implicit agreement that this is for internal use /
        meant to be overridden by subclasses (see SecurityAnalyst below).
        Default behavior: 5% of salary.
        """
        # TODO 8
        return self.__salary * 0.05

    # ---------------- Private method ----------------
    def __encrypt_ssn(self, ssn):
        """
        Private method (name-mangled): masks the national ID number.
        Example: replace every digit except the last 4 with '*'
        "29001011234567" -> "**********4567"
        """
        # TODO 9
        return  "*" * (len(ssn) - 4) + ssn[len(ssn) - 4:]

    # ---------------- Static method ----------------
    @staticmethod
    def is_valid_department_budget(budget):
        """Doesn't need self or cls -- just checks the number is positive"""
        # TODO 10
        return budget > 0

    def give_raise(self, percentage):
        # TODO 11: increase salary by a percentage -- use self.salary = ... (i.e. the setter)
        # do NOT touch __salary directly
        self.salary += self.salary * (percentage / 100)

    def __str__(self):
        return (f"{self.name} | {self.department.name} | "
                f"${self.salary:,.2f} | Bonus: ${self._calculate_bonus():,.2f}")


class SecurityAnalyst(Employee):
    """
    TODO 12 (Inheritance + Overriding a protected method):
    A security analyst gets a 10% bonus instead of 5% if they hold
    a certification (is_certified=True).
    """

    def __init__(self, name, department, salary, ssn, is_certified=False):
        super().__init__(name, department, salary, ssn)
        self.is_certified = is_certified

    def _calculate_bonus(self):
        # TODO 13: if is_certified, return 10% of salary
        # otherwise, fall back to the parent's behavior (you can call super()._calculate_bonus())
        if self.is_certified: 
            return self.salary * 0.1
        else:
            return super()._calculate_bonus()


# ========================= Tests =========================
if __name__ == "__main__":
    soc_dept = Department("Security Operations", 500_000)

    emp1 = Employee("Ahmed Hassan", soc_dept, 15000, "29001011234567")
    analyst1 = SecurityAnalyst("Sara Youssef", soc_dept, 22000, "29505051234567", is_certified=False)

    print(emp1)
    print(analyst1)

    print(f"Employee count (static attribute): {Employee.employee_count}")
    print(f"Company name (static attribute): {Employee.company_name}")

    try:
        emp1.salary = -500
    except ValueError as e:
        print(f"Negative salary correctly rejected: {e}")

    print(f"Is 10000 a valid budget? {Employee.is_valid_department_budget(10000)}")
    print(f"Is -500 a valid budget? {Employee.is_valid_department_budget(-500)}")

    emp1.give_raise(10)
    print(f"After raise: {emp1}")

    # Try accessing private/protected attributes from outside the class
    # (this is Python's "Consenting Adults" philosophy in action)
    print(emp1._years_of_service)     # works fine (but shouldn't be done in real code)
    # print(emp1.__salary)            # raises AttributeError (name mangling)
    print(emp1._Employee__salary)     # this works -- now you see the mangling in action