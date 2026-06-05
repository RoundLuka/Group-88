from pprint import pprint
import sqlite3
import pandas as pd


conn = sqlite3.connect('Bank.db')
cursor = conn.cursor()

##Left Join
## sqlite-ს არ აქვს CONCAT ფუნქციის მხარდაჭერა, გამოიყენება || სიმბოლო

# query = """
#         SELECT
#             officer.NAME AS Officer_Name,
#             officer.LNAME AS Officer_LName,
#             officer.MAIL AS Officer_Mail,
#             office.CITY || '. ' || office.STREET AS Office_Address
#         FROM
#             officer
#         LEFT JOIN
#             office
#         ON
#             officer.OFFICE_ID = office.ID;
#       """
#
# results = cursor.execute(query).fetchall()
# pprint(results)


##Inner Join
#
# query = """
#             SELECT
#                 officer.NAME, officer.LNAME, loan.VOLUME, loan.PERCENT, loan.PERIOD
#             FROM
#                 officer
#             JOIN
#                 loan ON officer.ID = loan.OFFICER_ID
#             WHERE
#                 CURRENCY="GEL" and VOLUME > 500000
#             ORDER BY
#                 officer.LNAME, officer.NAME, loan.VOLUME DESC
#         """
#
# results = cursor.execute(query).fetchall()
# pprint(results)


### მხოლოდ ის ოფიცრები, რომლებსაც მხოლოდ ლარში აქვთ სესხი და არცერთ სხვა ვალუტაში
### GROUP BY - საერთო ინფორმაციის მიხედვით ჩანაწერების დაჯგუფება
## HAVING - პირობა უზრუნველყოფს, ოფიცერს მხოლოდ ლარში ქონდეს სესხი. მუშაობს GROUP BY-სთან ერთად.
### HAVING პირობა გამოიყენება აგრეგაციის ფუნქციების საჭიროების დროს (WHERE-ს ეს არ შეუძლია). 
### ასევე, HAVING რადგანაც ვიყენებთ, ვალუტის შემოწმებისას გვჭირდება აგრეგაცია, ამ შემთხვევაში MAX (MIN-იც იგივეს გააკეთებს).

#
# query = """
#             SELECT
#                 officer.NAME AS Officer_Name,
#                 officer.LNAME AS Officer_LName,
#                 loan.VOLUME AS Loan_VOLUME,
#                 loan.PERCENT AS Loan_Percent
#             FROM
#                 officer
#             JOIN
#                 loan ON officer.ID = loan.OFFICER_ID
#             WHERE
#                 officer.ID IN (
#                                 SELECT
#                                     loan.OFFICER_ID
#                                 FROM
#                                     loan
#                                 GROUP BY
#                                     loan.OFFICER_ID
#                                 HAVING
#                                     COUNT(DISTINCT loan.CURRENCY) = 1 AND
#                                     MAX(loan.CURRENCY) = 'GEL'
#                 )
#             ORDER BY
#                 officer.LNAME, officer.NAME, loan.VOLUME DESC;
# """
#
# results = cursor.execute(query).fetchall()
# pprint(results)


### მხოლოდ ის ოფიცრები, რომლებსაც მხოლოდ ევროში აქვთ სესხი და არცერთ სხვა ვალუტაში, მომხმარებლებთან ერთად
#
# query = """
#             SELECT
#                 officer.NAME AS Officer_Name,
#                 officer.LNAME AS Officer_LName,
#                 loan.VOLUME AS Loan_Volume,
#                 loan.PERCENT AS Loan_Percent,
#                 loan.PERIOD AS Loan_Period,
#                 customer.NAME AS Customer_Name,
#                 customer.LNAME AS Customer_LName
#             FROM
#                 officer
#             JOIN
#                 loan ON officer.ID = loan.OFFICER_ID
#             JOIN
#                 customer ON loan.CUSTOMER_ID = customer.ID
#             WHERE
#                 officer.ID IN (
#                                 SELECT
#                                     loan.OFFICER_ID
#                                 FROM
#                                     loan
#                                 GROUP BY
#                                     loan.OFFICER_ID
#                                 HAVING
#                                     COUNT(DISTINCT loan.CURRENCY) = 1 AND
#                                     MAX(loan.CURRENCY) = 'EUR'
#                 )
#             ORDER BY
#                 officer.LNAME, officer.NAME, loan.VOLUME DESC;
#         """
#
# results = cursor.execute(query).fetchall()
# pprint(results)


## ქალაქების მიხედვით გაცემული სესხები
#
# query = """
#             SELECT
#                 office.CITY AS City,
#                 office.STREET AS Street,
#                 loan.CURRENCY AS Currency,
#                 SUM(loan.VOLUME) AS Total_Loan_Volume,
#                 ROUND(AVG(loan.PERCENT),2) AS Average_Loan_Percent
#             FROM
#                 loan
#             JOIN
#                 officer ON loan.OFFICER_ID = officer.ID
#             JOIN
#                 office ON officer.OFFICE_ID = office.ID
#             GROUP BY
#                 office.CITY, office.STREET, loan.CURRENCY
#             ORDER BY
#                 office.CITY, office.STREET, loan.CURRENCY;
#         """
#
# results = cursor.execute(query).fetchall()
# pprint(results)

### ჯამურად, ლარში რაოდენობა
# query = """
#             SELECT
#                 office.CITY AS City,
#                 SUM(CASE
#                         WHEN loan.CURRENCY = 'USD' THEN loan.VOLUME * 2.82
#                         WHEN loan.CURRENCY = 'EUR' THEN loan.VOLUME * 2.9
#                         ELSE loan.VOLUME
#                     END) AS Total_Loan_Volume_Lari
#             FROM
#                 loan
#             JOIN
#                 officer ON loan.OFFICER_ID = officer.ID
#             JOIN
#                 office ON officer.OFFICE_ID = office.ID
#             GROUP BY
#                 office.CITY
#             ORDER BY
#                 office.CITY
# """
#
# results = cursor.execute(query).fetchall()
# pprint(results)


###პროცენტის და სხვაობის გამოთვლა
#
# query = """
#             SELECT
#                 officer.NAME AS Officer_Name,
#                 officer.LNAME AS Officer_LName,
#                 loan.CURRENCY AS Currency,
#                 SUM(loan.VOLUME) AS Loan_Volume,
#                 SUM(loan.VOLUME + (loan.VOLUME * loan.PERCENT / 100)) AS Total_Amount_To_Return,
#                 SUM((loan.VOLUME * loan.PERCENT / 100)) AS Profit
#             FROM
#                 loan
#             JOIN
#                 officer ON loan.OFFICER_ID = officer.ID
#             GROUP BY
#                 officer.ID, loan.CURRENCY
#             ORDER BY
#                 officer.LNAME, officer.NAME, loan.CURRENCY;
#
#
# """
#
# results = cursor.execute(query).fetchall()
# pprint(results)


### პროცენტების მიხედვით გადანაწილება
#
# query = """
#         SELECT
#             office.CITY AS City,
#             office.TYPE AS Bank_Type,
#             loan.CURRENCY AS Currency,
#             CASE
#                 WHEN loan.PERCENT <= 14 THEN 'Low Percent'
#                 WHEN loan.PERCENT BETWEEN 14 AND 17 THEN 'Medium Percent'
#                 WHEN loan.PERCENT > 17 THEN 'High Percent'
#                 ELSE 'Unknown'
#             END AS Interest_Category,
#             SUM(loan.VOLUME) AS Total_Loan_Volume,
#             ROUND(AVG(loan.PERCENT),2) AS Average_Interest_Percent
#         FROM
#             loan
#         JOIN
#             officer ON loan.OFFICER_ID = officer.ID
#         JOIN
#             office ON officer.OFFICE_ID = office.ID
#         GROUP BY
#             office.CITY, office.TYPE, loan.CURRENCY, Interest_Category
#         ORDER BY
#             office.CITY, office.TYPE, loan.CURRENCY, Interest_Category;
#
# """
#
# results = cursor.execute(query).fetchall()
# pprint(results)




### WITH AS-ით შეგვიძლია შევქმნათ CTE (Common Table Expression) - დროებითი ცხრილი,
# რომელშიც შემდეგ შეგვიძლია გავაკეთოთ სხვადასხვა სელექტები
#
# query = """
#             WITH LoanCalc AS (
#                 SELECT
#                     officer.NAME AS Officer_Name,
#                     officer.LNAME AS Officer_LName,
#                     office.CITY AS City,
#                     office.TYPE AS Bank_Type,
#                     loan.CURRENCY AS Currency,
#                     CASE
#                         WHEN loan.PERCENT <= 14 THEN 'Low Percent'
#                         WHEN loan.PERCENT BETWEEN 14 AND 17 THEN 'Medium Percent'
#                         WHEN loan.PERCENT > 17 THEN 'High Percent'
#                         ELSE 'Unknown'
#                     END AS Interest_Category,
#                     loan.VOLUME AS Loan_Volume,
#                     loan.PERCENT AS Loan_Percent
#                 FROM
#                     loan
#                 JOIN
#                     officer ON loan.OFFICER_ID = officer.ID
#                 JOIN
#                     office ON officer.OFFICE_ID = office.ID
#                 WHERE
#                     loan.CURRENCY IN ('GEL', 'EUR', 'USD')
#             )
#
#             SELECT
#                 Officer_Name,
#                 Officer_LName,
#                 City,
#                 Bank_Type,
#                 Interest_Category,
#                 ROUND(SUM(CASE WHEN Currency = 'GEL' THEN Loan_Volume ELSE 0 END), 2) AS GEL_Loan_Volume,
#                 ROUND(SUM(CASE WHEN Currency = 'EUR' THEN Loan_Volume ELSE 0 END) * 2.9, 2) AS EUR_to_GEL_Loan_Volume,
#                 ROUND(SUM(CASE WHEN Currency = 'USD' THEN Loan_Volume ELSE 0 END) * 2.82, 2) AS USD_to_GEL_Loan_Volume,
#                 ROUND(SUM(CASE WHEN Currency = 'GEL' THEN Loan_Volume * Loan_Percent / 100 ELSE 0 END), 2) AS GEL_Loan_Interest,
#                 ROUND(SUM(CASE WHEN Currency = 'EUR' THEN Loan_Volume * Loan_Percent / 100 ELSE 0 END) * 2.9, 2) AS EUR_to_GEL_Loan_Interest,
#                 ROUND(SUM(CASE WHEN Currency = 'USD' THEN Loan_Volume * Loan_Percent / 100 ELSE 0 END) * 2.82, 2) AS USD_to_GEL_Loan_Interest
#             FROM
#                 LoanCalc
#             GROUP BY
#                 Officer_Name, Officer_LName, City, Bank_Type, Interest_Category
#             ORDER BY
#                 Officer_LName, Officer_Name, Interest_Category, City;
#
#
# """
#
#
# ### pandas მოდულის გამოყენებით შეგვიძლია CSV და Excel ფაილებში ჩავწეროთ მონაცემები
# # pandas პითონს არ მოყვება, ასევე, ჩასაწერი იქნება openpyxl მოდული, რომელიც გამოიყენება
# # ექსელის ფაილთან სამუშაოდ და რომელსაც იყენებს pandas-იც ენჯინად.
#
# df = pd.read_sql_query(query, conn)
#
# df.to_csv('loan_report.csv', index=False)
# df.to_excel('loan_report.xlsx', index=False, engine='openpyxl')


# results = cursor.execute(query).fetchall()
# pprint(results)



# cursor.close()
# conn.close()
