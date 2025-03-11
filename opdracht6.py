import re

def controleer_hoofdletters(tekst):
    patroon = r'^[A-Z]' 
    
   
    if re.match(patroon, tekst):
        return True  
    return False 

def main():
   
    tekst1 = "Dit is een correcte tekst."  
    tekst2 = "Het gehaalde cijfer is NVT"  
    tekst3 = "de winter is koud" 
    tekst4 = "python is een leuke codeertaal"  

   
    teksten = [tekst1, tekst2, tekst3, tekst4]
    
   
    for tekst in teksten:
        resultaat = "goedgekeurd" if controleer_hoofdletters(tekst) else "afgekeurd"
        print(f"Tekst: {tekst}")
        print(f"Resultaat: {resultaat}")
        print("-" * 50)

if __name__ == "__main__":
    main()

