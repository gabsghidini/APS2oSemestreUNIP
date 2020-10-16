# APS 2º Semestre UNIP
Python project for School Semester Term Paper

Fictional Naval System for RMS Queen Mary (https://pt.wikipedia.org/wiki/RMS_Queen_Mary) made with Python, PyQt5 for GUI, SQLite3 for database and SHA256 for cryptography. 


1. Login Interface
  The program should check the user and password using SHA256 to encrypt the values and to check the already encrypted values on the SQLite3 database. After checking, if positive, the software should then head on to the Acess Interface. If not, the user must be showed an error to contact the administrator of the system.
 
2. Access Interface 
  The program will show information related to the ship, that including, the crew members, types of toxic substance that is carrying with its amount. Those information will be shown on the ListWidgets format.
  The program must allow the insertion of new information as well as altering the current information on the database regarding the crew members and the toxic substances.
  
3. Database
  As said previously, there should be 2 major databases, Crew Members and Toxic Substances.
  The Crew members database should contain the Basic Information about them: Full Name, ID, Date of Birth, Sex, Address, Phone Number, Height, Weight and Blood Type. Should be generated randomly to prevent any real data leak with the website: https://www.4devs.com.br/gerador_de_pessoas.
  The Toxic Substances data should contain the following substances: Ammonia, Methane and Methyloxirane alongside with their cubic volume (under safe volumes and conditions it is meant to be kept). As seen on the website: https://www.everycrsreport.com/reports/RL33048.html#TOC2_7, the description of the substances are: 
  
  Ammonia: Ammonia is an acutely toxic, potentially explosive, liquefied gas primarily used in the manufacture of fertilizers and as a fertilizer itself. It has many other uses as well; for example, as a chemical production component, as source of protein in livestock feeds, and in metal treatment operations. Ammonia can reach harmful concentrations in the air very quickly on loss of containment. It can causing severe skin irritation, and if inhaled, can cause respiratory irritation, eye corrosion, and fatal fluid buildup in the lungs.

  Methane: Methane (natural gas) is used as a heating fuel and industrial feedstock for a range of chemical processes. Methane is not inherently toxic, although high vapor concentrations may cause asphyxiation by displacing breathable air. Cryogenic methane (liquefied natural gas, or LNG) may freeze body parts with which it comes into contact. Methane is extremely flammable when mixed with air and may be explosive when such mixtures are in confined spaces.

  Methyloxirane: Methyloxirane is used to manufacture polyurethane foam (for furniture and cars), solvents (in paints, cleaners, and waxes), polyster resins, and other industrial products. Methyloxirane is a toxic liquid and a fire hazard. Human exposure may irritate the eyes, skin, and respiratory tract. Methyloxirane vapor is extremely flammable when mixed with air and reacts explosively with chlorine, ammonia, strong oxidants, and acids.
