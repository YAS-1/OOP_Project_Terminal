class Hospital_system:
    def __init__(self):
        pass

    @property
    def add_to_system(self):
        pass
    @property
    def display_records(self):
        pass

    

# Class Patient---------------------------------------------------------------------------------
class Patient(Hospital_system):
    def __init__(self):
        super().__init__()
        self.records = {}

    @property
    def create_patient(self):
        self.__name = input('\nEnter the patient full name: ')
        self.__age = int(input("\nEnter patient age: "))
        self.__gender = input("\nEnter patient gender: ")
        self.__phone_number = input("\nEnter patient phone number: ")
        self.__PatientID = (input("\nEnter patient ID: "))
        self.__PatientMedical = input("\nEnter Patient Medical Issues: ")
    @property
    def add_to_system(self):
        if self.__PatientID in self.records:
            print("\nPatient already exists in the system\n")
        else:
            self.records[self.__PatientID] = [self.__name,self.__gender,self.__age,self.__phone_number,self.__PatientMedical]
            print('\nPatient added to System\n')
        print('------------------------------------------')

    @property
    def display_records(self):
        if len(self.records) == 0:
            print("\nNo patient records available\n")
            print('------------------------------------------')
        else:
            for key, patient in self.records.items():
                print(f'\nPatient ID: {key}')
                print(f'Patient name: {patient[0]}')
                print(f'Patient gender: {patient[1]}')
                print(f'Patient age: {patient[2]}')
                print(f"Patient Medical Issues: {patient[4]}")
                print(f'Patient Phone number: {patient[3]}')
                print('------------------------------------------')

#Class Doctor--------------------------------------------------------------------------
class Doctor(Hospital_system):
    def __init__(self):
        super().__init__()
        self.Doc_records = {}

    @property
    def create_Doc(self):
        self.__name = input("\nEnter the Doctor's full name: ")
        self.__gender = input("\nEnter Doctor's gender: ")
        self.__phone_number = input("\nEnter Doctor's phone number: ")
        self.__DocID = (input("\nEnter Doctor's ID: "))
        
    @property
    def add_to_system(self):
        if self.__DocID in self.Doc_records:
            print("\nDoctor already exists in the system\n")
        else:
            self.Doc_records[self.__DocID] = [self.__name,self.__gender,self.__phone_number]
            print('\nDoctor added to System\n')
        print('------------------------------------------')

    @property
    def display_records(self):
        if len(self.Doc_records) == 0:
            print("\nNo Doctor records available\n")
        else:
            for key, doctor in self.Doc_records.items():
                print(f'\nDoctor ID: {key}')
                print(f'Doctor name: {doctor[0]}')
                print(f'Doctor gender: {doctor[1]}')
                print(f'Doctor Phone number: {doctor[2]}')
        print('------------------------------------------')

#Class Appointment-------------------------------------------------------------
class Appointment(Hospital_system):
    def __init__(self):
        super().__init__()
        self.appointments = {}
    
    @property
    def appointment_scheduling(self):
        self.__date = input("\nEnter the date of the appointment: ")
        self.__time = input("\nEnter the time of the appointment: ")
        self.__docname = input("\nEnter the Doctor's full name: ")
        self.__DocID = input("\nEnter the Doctor's ID: ")
        self.__Patientname = input("\nEnter the Patients's full name: ")
        self.__PatientID = input("\nEnter the Patient's ID: ")

    @property
    def add_to_system(self):
        if self.__DocID in self.appointments and self.__PatientID in self.appointments:
            print("\nAppointment already set\n")
        else:
            self.appointments[self.__DocID] = [self.__date,self.__time,self.__PatientID]
            print('\nAppointment scheduled\n')
        print('------------------------------------------')

    @property
    def display_records(self):
        if len(self.appointments) == 0:
            print("\nNo appointments Scheduled\n")
        else:
            for key, appointment in self.appointments.items():
                print(f'\nDoctor ID: {key}')
                print(f'Patient ID: {appointment[2]}')
                print(f'Appointment date: {appointment[0]}')
                print(f'Appointment time: {appointment[1]}')
        print('------------------------------------------')

#Class Room-----------------------------------------------------------------------------
class Room:
    def __init__(self):

        self.room_records = {}

    @property
    def create_room(self):
        self.__room_number = input("\nEnter the room number: ")
        self.__room_status = input("\nEnter the room status: ")
        self.__roomPatient = ""

    @property
    def store_room(self):
        if self.__room_number in self.room_records:
            print("\nThe room is already in the system\n")
        else:
            self.room_records[self.__room_number] = [self.__room_status,self.__roomPatient]
            print("\nRoom added to system\n")
        print('------------------------------------------')

    def assign_room(self,PatientID,Room):
        if Room in self.room_records:
            if self.room_records[Room][0] == "Vacant":
                self.room_records[Room] = ["Occupied",PatientID]  
                print(f"{Room} is occupied by {PatientID}")
                print('------------------------------------------')
            else:
                print("\nRoom is currently Occupied\n")
                print('------------------------------------------')
                self.assign_room(PatientID,Room)
        else:
            print("\nRoom number not in the system\n")
        print('------------------------------------------')
    
    @property
    def rooms(self):
        if len(self.room_records) == 0:
            print("\nNO ROOM RECORDS AVAILABLE\n")
            print('------------------------------------------')
        else:
            for key,room in self.room_records.items():
                print(f'\nRoom number: {key}')
                print(f'Room Status: {room[0]}')
                print(f'Occupant: {room[1]}')
        print('------------------------------------------')


#Class Bill------------------------------------------------------------------------------
class Bill:
    def __init__(self):
        self.bill_records = {}

    @property
    def create_bill(self):
        self.__PatientName = input("\nEnter the Patient's name")
        self.__PatientID = input("\nEnter the Patient's ID")
        self.__services = input("\nEnter the Services offered")
        self.__TotalCharges = input("\nEnter the Total Charges")
    
    @property
    def store_bill(self):
        if self.__PatientID in self.bill_records and self.__PatientName in self.bill_records:
            print("\nThe patient is already billed\n")
            print('------------------------------------------')
        else:
            self.bill_records[self.__PatientID] = [self.__PatientName, self.__services, self.__TotalCharges]
            print("\nBill added to system\n")
            print('------------------------------------------')

    @property
    def show_bills(self):
        if len(self.bill_records) == 0:
            print("\nNO BILLING RECORDS AVAILABLE\n")
            print('------------------------------------------')
        else:
            for key,bill in self.bill_records.items():
                print(f'\nPatient ID: {key}')
                print(f'Patient name: {appointment[0]}')
                print(f'Services offered: {appointment[1]}')
                print(f'Total Charges: {appointment[2]}')
        print('------------------------------------------')


start = '*'*20
print(f'\n{start}WELCOME TO THE HOSPITAL MANAGEMENT SYSTEM🏥{start}\n')

new_patient = Patient()
new_Doc = Doctor()
new_appointment = Appointment()
new_room = Room()
new_bill = Bill()

while True:
    option = input('\nPlease select an option from the following :\n a) Add a patient to the System\n b) View Patient records\n c) Add a Doctor to the System\n d) Schedule Appointment\n e) View scheduled appointments\n f) Add a room to the system\n g) Assign a Patient a room\n h) View Room records\n i) Bill a Patient\n j) View Bill records\n \nENTER YOUR OPTION: ')
    print('------------------------------------------')

    if option == 'a':
        new_patient.create_patient
        new_patient.add_to_system   

    if option == 'b':
        new_patient.display_records

    if option == 'c':
        new_Doc.create_Doc
        new_Doc.add_Doc

    if option == 'd':
        new_appointment.appointment_scheduling
        new_appointment.add_to_system

    if option == 'e':
        new_appointment.display_records

    if option == 'f':
        new_room.create_room
        new_room.store_room

    if option == 'g':
        Occupied_room = input("\nEnter room to assign to patient: ")
        Occupant = input("\nEnter patient to occupy room: ")
        new_room.assign_room(Occupant,Occupied_room)

    if option == "h":
        new_room.rooms

    if option == "i":
        new_bill.create_bill
        new_bill.store_bill
    
    if option == "j":
        new_bill.show_bills