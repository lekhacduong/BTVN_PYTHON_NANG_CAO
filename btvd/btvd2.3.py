from xml.dom import minidom

doc = minidom.parse("sample.xml")

# lay ten cty
company = doc.getElementsByTagName("name")[0].firstChild.data
print(f"Ten cong ty: {company}")

# lay dsach nv
staff = doc.getElementsByTagName("staff")

# duyet nv
for i in staff:
    # lay id
    staff_id = i.getAttribute("id")
    
    # lay ten va luong
    name  = i.getElementsByTagName("name")[0].firstChild.data
    salary = i.getElementsByTagName("salary")[0].firstChild.data
    
    print(f"ID: {staff_id}")
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    