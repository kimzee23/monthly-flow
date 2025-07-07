from datetime import datetime, timedelta


class UserAccount:
    def __init__(self, name, age, cycle_length, period_length, last_period_date):
        self.name = name
        self.age = age
        self.cycle_length = cycle_length
        self.period_length = period_length
        self._last_period_date = datetime.strptime(last_period_date, "%Y-%m-%d")


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, names):
        if not names.strip() :
            raise ValueError("Name cannot be empty")
        if not names.isalpha():
            raise ValueError("Name must contain only letters")
        self._name = names


    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if 10 <= age <= 55:
            self._age = age
        else:
            raise ValueError("Age must be between 11 and 55")
    @property
    def cycle_length(self):
        return self._cycle_length

    @cycle_length.setter
    def cycle_length(self, cycle_length):
        if 20 <= cycle_length <= 31:
            self._cycle_length = cycle_length
        else:
            raise ValueError("Cycle length must be between 20 and 31")

    @property
    def period_length(self):
        return self._period_length

    @period_length.setter
    def period_length(self, period_length):
        if 3<= period_length <= 5:
            self._period_length = period_length
        else:
            raise ValueError("Period length must be between (3 to 5 Day)if yours is not please kindly see a Doctor")
    @property
    def last_period_date(self):
        return self._last_period_date

    @last_period_date.setter
    def last_period_date(self, last_period_date):
        try:
            currentDate = datetime.strptime(last_period_date, "%Y-%m-%d")
            if currentDate.year > 2025:
                raise ValueError("Invalid date :year can't above the current year")
            self._last_period_date = currentDate
        except ValueError:
            raise ValueError("Invalid date :year can't be greater than current year")



    def get_next_period_day(self):
        return self.last_period_date + timedelta(days=self.cycle_length)

    def get_safe_and_unsafe_days(self):
        ovulation_day = self.last_period_date + timedelta(days=self.cycle_length - 14)
        start_unsafe_day = ovulation_day + timedelta(days=5)
        end_unsafe_day = ovulation_day + timedelta(days=1)
        return{
            "start unsafe day": start_unsafe_day.strftime("%Y-%m-%d"),
            "ovulation day": ovulation_day.strftime("%Y-%m-%d"),
            "end unsafe day": end_unsafe_day.strftime("%Y-%m-%d"),
        }
    def show_pregnancy_symptoms(self):
        print("""\n pregnancy symptoms:
            1.Missed period for a A day or Two
            2.Morning Sickness
            3.Fatigue
            4.Tender breast
            5.Frequent urination 
        """)
    def show_Mensturation_symptoms(self):
        print(""" \n Mensturation symptoms:
            1. cramps
            2. Mood swings
            3. Headaches
            4. Lower back pain
            5. Iwa wayre 
        """)

    def show_safe_sex_tools(self):
        print("""\n🛡 Safe Sex Tools & Tips:
        1. Condoms (male & female) : prevent pregnancy & STIs
        2. Birth control pills : daily pills to prevent ovulation
        3. Emergency contraception : "morning-after" pills
        4. IUD : long-term birth control (Family control) inserted by a doctor 
        5. Fertility awareness : avoid sex during fertile days
        6. Communication : talk openly with your partner
        7. Regular checkups : visit a health professional
        8. Avoid sex: (Safu epo abi Obo)
        """)



