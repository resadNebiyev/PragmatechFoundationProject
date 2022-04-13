with open("students-data.txt") as t:
     with open("success_students.txt","w") as s:
          with open("fail_students.txt","w") as f:
# setirler uzerinde islemek ucun loop
               for line in t.readlines()[1:]:
# 2-ci loop bitdikden sonra novbeti setiri analiz ederken indeksleri 0-layiriq
                    bosluq_index = []
                    index = 0
# setirdeki bosluqlari ayirmaq ucun 2-ci loop yaradiriq
                    for letter in line:                   
                         if letter == " ":                        
                              bosluq_index.append(index)
# her herf deyiserken indeks artir
                         index+=1
# ad ve soyadlari ayirmaq
                    # name_surname = line[:bosluq_index[0]]
                    name_surname = line.split(' ')[0]
                    _surname = name_surname.split('-')[-1]
                    _name = name_surname[:name_surname.index(_surname)-1].replace('-',' ')
                    
                    
# imtahan neticelerini ayirmaq
                    exam_results = line.split(" ")[-1]
                    first_exam = int(exam_results.split("/")[0])
                    second_exam = int(exam_results.split("/")[1])
                    final_exam = int(exam_results.split("/")[2])
                    _average = int((first_exam * 0.5 + second_exam * 0.5)/10 * final_exam/10)
                    # print(_average)
# imtahanda kecirilecek fennler
                    exam_subjects = line[bosluq_index[0]+1:bosluq_index[-1]] 
# imtahandan kecen telebeleri hesablamaq
                    if _average > 50 and final_exam>90:
                         s.write(_name)
                         s.write(" "* (25-len(_name)))
                         s.write(_surname)
                         s.write(" "* (25-len(_surname)))
                         s.write(exam_subjects)
                         s.write(" "* (25-len(exam_subjects)))
                         s.write(str(_average))
                         s.write("\n")
# imtahandan kesilen telebeleri hesablamaq   
                    else:
                         f.write(_name)
                         f.write(" "* (25-len(_name)))
                         f.write(_surname)
                         f.write(" "* (25-len(_surname)))
                         f.write(exam_subjects)
                         f.write(" "* (25-len(exam_subjects)))
                         f.write(str(_average))
                         f.write("\n")
                         
                    