from sqlalchemy import Column, Integer, String, Boolean, MetaData, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

metadata = MetaData()
Base = declarative_base(metadata=metadata)


hospital_patient = Table(
    'hospital_patient',
    Base.metadata,
    Column('hospital_id', Integer, ForeignKey('hospitals.id'), primary_key=True),
    Column('patient_id', Integer, ForeignKey('patients.id'), primary_key=True),
    extend_existing=True,
)   

class Hospital(Base): 
    __tablename__ = 'hospitals'       
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact = Column(Integer, nullable=False) 
    location = Column(String, nullable=False)
    address = Column(String, nullable=False)
    bed_capacity = Column(Integer())
    patient = relationship("Patient",secondary=hospital_patient, back_populates="hospital")
    
    
    
    
    
    def __init__(self, name, contact, location, address, bed_capacity):
        self.name= name
        self.contact = contact
        self.location = location
        self.address = address
        self.bed_capacity = bed_capacity
        
    def __repr__(self) -> str:
        
        return f"{self.name}"   

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact = Column(Integer, nullable=False) 
    location = Column(String, nullable=False)
    address = Column(String, nullable=False)
    admit = Column(Boolean)
    hospital= relationship('Hospital',secondary=hospital_patient, back_populates='patient')
    
    def __init__(self, name, contact, location, address, admit):
        self.name= name
        self.contact = contact
        self.location = location
        self.address = address
        self.admit = admit
        
    def __repr__(self) -> str:
        
        return f"{self.name}"   
 
    
    
class Transport(Base):
    __tablename__ = 'transports'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    contact = Column(Integer, nullable=False) 
    location = Column(String, nullable=False)
    address = Column(String, nullable=False)
    hospital_id= Column(Integer, ForeignKey('hospitals.id'), nullable=False)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    
    
    def __init__(self, title, contact, location, address,hospital_id, patient_id ):
        self.title= title
        self.contact = contact
        self.location = location
        self.address = address
        self.hospital_id = hospital_id
        self.patient_id= patient_id
        
        
    def __repr__(self):
        
        return f"{self.title}" 


       
    
    
  