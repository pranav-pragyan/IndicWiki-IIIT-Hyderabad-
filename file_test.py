import os

path = r"C:\Users\Pranav Pragyan\Desktop\New\full_length_articles"
os.chdir(path)

xml_file = open('final_xml.xml', 'a', encoding="utf-8")

i = 1
for file in os.listdir():
    if file.endswith(".txt"):
        full_path = f"{path}\{file}"
        print("{}. {}".format(i, full_path))
        i += 1
        f = open(full_path, "r", encoding="utf-8", errors='ignore')
        content = f.read()
        xml_file.write(content)
        xml_file.write("\n\n")
        # print(content)

xml_file.close()
