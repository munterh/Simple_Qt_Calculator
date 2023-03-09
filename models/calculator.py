class Calculator:

    entry_dict = {"0": "digit", "1": "digit", "2": "digit", "3": "digit", "4": "digit", "5": "digit",
                  "6": "digit", "7": "digit", "8": "digit", "9": "digit", ".": "digit", "+": "plus",
                  "-": "minus", "*": "star", "/": "slash", "=": "equal", "C": "clear", "none": "none"
    }

    __slots__ = ("main_field_str","plus_minus_field","star_slash_field",
                "current_connective","last_connective","current_entry_full","last_entry_cat",
                "outer_connective")
    def __init__(self):
        self.main_field_str = ""
        self.plus_minus_field = 0
        self.star_slash_field = 0

        self.current_connective = "none" 
        self.last_connective = "none" 
        self.current_entry_full = "none"
        self.last_entry_cat = "none"
        self.outer_connective = "none"

    def display_current_state(self):
        return self.main_field_str

    def entry(self,entry):
        self.last_entry_cat = Calculator.entry_dict[self.current_entry_full]
        self.current_entry_full = entry

        match Calculator.entry_dict[entry]:
            case "plus": self.plus()
            case "minus": self.minus()
            case "star": self.star()
            case "slash": self.slash()
            case "clear": self.clear()
            case "equal": self.equal()
            case "digit": self.digit()

        # print()
        # print("Main Field:", self.main_field_str)    
        # print("Star_Slash_Field: ", self.star_slash_field)
        # print("Plus_Minus_Field: ", self.plus_minus_field)
        # print("Current connective: ",self.current_connective)
        # print("Last connective: ",self.last_connective)
        # print("Outer connective:",self.outer_connective)
        # print()
        
    def plus_minus_equal(self):
        result = eval(self.main_field_str)

        match self.last_connective:
            case "plus": result += self.plus_minus_field
            case "minus": result -= self.plus_minus_field 
            case "star": result *= self.star_slash_field
            case "slash": result /= self.star_slash_field

        match self.outer_connective:
            case "plus": result += self.plus_minus_field
            case "minus": result -= self.plus_minus_field

            case "clear": self.clear()
            case "equal": self.equal()
            case "digit": self.digit()

        if  self.current_connective in ("plus","minus","equal"):
            self.main_field_str = str(result)

        self.last_connective = "none"
        self.outer_connective = "none"
        
    def plus(self):
        self.last_connective = self.current_connective
        self.current_connective = "plus"
        self.plus_minus_equal()

    def minus(self):
        self.last_connective = self.current_connective
        self.current_connective = "minus"
        self.plus_minus_equal()

    def equal(self):
        self.last_connective = self.current_connective
        self.current_connective = "equal"
        self.plus_minus_equal()

    def star_slash(self):
        if self.last_connective in {"plus","minus"}:
            self.outer_connective = self.last_connective
            self.last_connective = "none"

        match self.last_connective:
            case "star": self.main_field_str = str(self.star_slash_field * eval(self.main_field_str))
            case "slash": self.main_field_str = str(self.star_slash_field / eval(self.main_field_str))

    def star(self):
        self.last_connective = self.current_connective
        self.current_connective = "star"
        self.star_slash()
        
    def slash(self):
        self.last_connective = self.current_connective
        self.current_connective = "slash"
        self.star_slash()

    def digit(self):
        if self.last_entry_cat in {"plus","minus","equal"}:
            self.plus_minus_field = eval(self.main_field_str)
            self.main_field_str = ""
            
        if self.last_entry_cat in {"star","slash"}:
            self.star_slash_field = eval(self.main_field_str)
            self.main_field_str = ""
        
        self.main_field_str += self.current_entry_full

    def clear(self):
        self.main_field_str = ""
        self.plus_minus_field = 0
        self.star_slash_field = 0

        self.current_connective = "none" 
        self.last_connective = "none" 
        self.current_entry_full = "none"
        self.last_entry_cat = "none"
        self.outer_connective = "none" 

