# WayToLife
2. Workflow of WayToLife:
1) A web-based health-care system is required to gather voluntary blood donors and connect them with the needy people who have high requirements for a particular blood type. We have implemented this using Django.
2) Doctor Appointment- We have built a doctor appointment ecosystem via video calls and e-prescriptions.
3) Smart Blood Banks
4) Ambulance Tracking System
5) Heart disease prediction
6) Kidney disease prediction


3. Working of WaytoLife:
1) A web-based health-care system is required to gather voluntary blood donors and connect them with the needy people who have high requirements for a particular blood type. 
2) A system that predicts the disease at the earliest is very important to avoid any unwanted sufferings. This system predicts general and more commonly occurring diseases that when remained unchecked can turn into life-threatening ones. Here user has to give input some day to day observable symptoms he/she is suffering from and our app predicts the ailment he/she is suffering from and redirects them to the appropriate doctor.
3) WaytoLyf solves the primary objective of lack of awareness about blood availability as we can easily get information about blood in our nearest location.
4) Many times we suffer from various diseases which may be unknown to us because of lack of availability of proper clinics and doctors in our area. Then those people can benefit from our website as they have to just input the symptoms they are suffering from and they will get the possible disease they are suffering from as output.
5) For predicting the actual disease from the symptoms (given by the patient as user input), we are using random forest classifier and using criterion as entropy.
If the patient selects a symptom, then it’s value is marked as 1 else 0. And that value has been stored in a datafile Data1.csv which acts as our testing set.
We have a training set of around 40k entries which we have used to train our ML model giving a moderately high accuracy score.

Smart Blood Banks:
6) There will be 3 parties involved in this; the patient, the donor & the admin. The patient can log in and look for the required amount of blood they will be requiring. Similarly the donor can log in to donate the amount of blood that he/she wants to donate. The admin has the authority of acting as a linkage between the patients and the donors. 

Ambulance Tracking System using Restful API
7) Using our website, patients or families of patients can efficiently look for for the ambulance vehicles readily available for service. If it is not available at some hospitals then we would automatically recommend those hospitals where the ambulances are readily available. 

Heart Disease Prediction Model
8) Model is used for predicting the presence of heart disease of a person.

The model accuracy is 88.5% using SVG Classifier.

Model is trained using a kaggle dataset for heart disease prediction

Further modifications to improve the model accuracy will be made

Kidney Disease Prediction Model
9) Model is used for predicting the presence of chronic kidney disease of a person.

The model accuracy is 99.5% as of now using Random forest Classifier.

Model is trained using a Kaggle dataset for kidney disease prediction

Further modifications to improve the model performance will be made and also overfitting will be checked



4. Tech Stacks Used
PHP
CSS
JAVASCRIPT
MACHINE LEARNING
PYTHON
BOOTSTRAP
SCIKIT-LEARN’s DECISION TREE CLASSIFIER
MY SQL
Streamlite
SKLEARN
NUMPY PANDAS
RANDOM FOREST
SVM
MEDIA PIPE
OPEN CV
DJANGO

6. Future Additions 🤞:
We will be implementing a system where the patient can predict any diseases he/she is suffering from by giving inputs of day to day symptoms.

7. Contributors ㊗️:
Devaditya Roy (ML & Deep Learning)
Devaditya Roy (Full Stack)
Anjana Banerjee (Ppt, Business & Finances)
Ankit Purakayastha (Bootstrap)# WayToLife
# WayToLife
