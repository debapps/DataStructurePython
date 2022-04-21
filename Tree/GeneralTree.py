#
# This program creates general tree data structure for a Organization Hierarchy.
#

class Employee:
    # Initialization Method.
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.manageTeam = []
        self.parent = None
    
    # Add Employee Method: add a employee name and designation as child node.
    def addChildEmp(self, employee):
        employee.parent = self
        self.manageTeam.append(employee)

    # Get the level of the hierarchy.
    def getLevel(self):
        self.level = 0
        
        self.parentEmp = self.parent
        while self.parentEmp:
            self.parentEmp = self.parentEmp.parent
            self.level += 1
        
        return self.level 
    
    # Get the proper spacing and tree format for printing hierarchy.
    def getPrefix(self):
        self.spacing = ' ' * self.getLevel() * 3
        
        if self.parent:
            self.prefix = self.spacing + '|_ _' 
        else:
            self.prefix = ''
        
        return self.prefix
        

    # Print the Name of the employee.
    def showName(self):
        self.prefix = self.getPrefix()
        print(self.prefix + self.name)

    # Print the designation of the employee.
    def showDesig(self):
        self.prefix = self.getPrefix()
        print(self.prefix + self.designation)

    # Print the Name and designation of the employee.
    def showBoth(self):
        self.prefix = self.getPrefix()
        print(self.prefix + f'{self.name} ({self.designation})')
    
    # Print the employee hierarchy.
    def showHier(self, type):
        if type == 'name':
            self.showName()
        elif type == 'designation':
            self.showDesig()
        elif type == 'both':
            self.showBoth()
        else:
            print('Please mention the type of Hierarchy')
            return
        
        if self.manageTeam:
            for self.emp in self.manageTeam:
                self.emp.showHier(type)

# This Method builds the hierarchy.

def biuld_hier():
    # level 0
    ceo = Employee('Nilupul', 'CEO')
    
    # level 1
    cto = Employee('Chinmay', 'CTO')
    hr = Employee('Gels', 'HR Head')
    
    # level 2
    infra_head = Employee('Viswa', 'Infrastructure Head')
    app_head = Employee('Aamir', 'Application Head')
    req_mngr = Employee('Peter', 'Recruitment Manager')
    pol_mngr = Employee('Waqas', 'Policy Manager')

    # level 3
    cld_mngr = Employee('Dhaval', 'Cloud Manager')
    app_mngr = Employee('Abhijit', 'App Manager')

    # Adding childs.
    infra_head.addChildEmp(cld_mngr)
    infra_head.addChildEmp(app_mngr)

    cto.addChildEmp(infra_head)
    cto.addChildEmp(app_head)
    hr.addChildEmp(req_mngr)
    hr.addChildEmp(pol_mngr)

    ceo.addChildEmp(cto)
    ceo.addChildEmp(hr)

    return ceo
    
if __name__ == '__main__':
    ceo = biuld_hier()
    ceo.showHier('name')
    print('=' * 50)
    ceo.showHier('designation')
    print('=' * 50)
    ceo.showHier('both')
    print('=' * 50)