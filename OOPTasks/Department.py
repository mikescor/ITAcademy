class Employee(object):

    def __init__(self, first_name, second_name, salary, experiance, manager):
        self.f_name = first_name
        self.s_name = second_name
        self.salary = salary
        self.experiance = experiance
        self.manager = manager

    def __repr__(self):
        return "%s %s, manager: %s, experiance: %i year(s)" % (self.f_name, self.s_name, self.manager, self.experiance)

    def getSalary(self):
        if self.experiance in range(2, 6):
            self.salary += 200
        elif self.experiance > 5:
            self.salary = self.salary * 1.2 + 500

        return self.salary


class Designer(Employee):
    def __init__(self, effCoeff, *args):
        super(Designer, self).__init__(*args)
        self.effCoeff = effCoeff

    def getSalary(self):
        return self.salary * self.effCoeff


class Developer(Employee):
    pass


class Manager(Employee):
    def __init__(self, team, *args):
        super(Manager, self).__init__(*args)
        self.team = team

    @classmethod
    def checkMembers(cls, team):
        counter = 0
        for member in team:
            if isinstance(member, Developer):
                counter += 1
        return counter > len(team) // 2

    def getSalary(self):
        if Manager.checkMembers(self.team):
            self.salary *= 1.1

        if len(self.team) in range(5, 11):
            self.salary += 200
        elif len(self.team) > 10:
            self.salary += 300

        return self.salary


class Department(object):
    def __init__(self, listManagers):
        self.listManagers = listManagers

    def getTeam(self):
        return [member.team for member in self.listManagers]

    def listSalary(self):
        for manager in self.listManagers:
            print("Team of ", manager.s_name)
            for emp in manager.team:
                print("%s %s got salary: %0.1f" % (emp.f_name, emp.s_name, emp.getSalary()))
