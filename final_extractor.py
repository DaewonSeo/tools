#coding:utf-8
import xlsxwriter

def main(text):
	workbook = xlsxwriter.Workbook('professor_list.xlsx')
	worksheet = workbook.add_worksheet()

	text1 = text.split(';')
	row = 0
	col = 0

	checking_list = []

	for b in text1:
		if "[" in b:
			idx_1 = b.split('[')[1].replace(',','')
			checking_list.append(idx_1)
					
			
		elif "]" in b:
			idx_2 = b.split(']')[0].replace(',','')
			checking_list.append(idx_2)
			idx_3 = b.split(']')[1].split(',')[0]
			checking_list.append(idx_3)
			checking_list.reverse()
			
			for item in checking_list:
				if item is checking_list[-1]:
					worksheet.write(row,col,item)
					col += 1
					row += 1
				else:
					worksheet.write(row,col,item)
					col += 1
			checking_list = []
			col = 0


			
		else:
			idx_4 = b.replace(',','')
			checking_list.append(idx_4)
			
			

	workbook.close()


if __name__ == "__main__":
	text = '[Huh, Hee Jae; Kwon, Min-Jung; Ki, Chang-Seok] Sungkyunkwan Univ, Sch Med, Samsung Med Ctr, Dept Lab Med & Genet, Seoul 135710, South Korea; [Cho, Kyoo-ho; Lee, Ji Eun; Lee, Phil Hyu] Yonsei Univ, Coll Med, Dept Neurol, Seoul, South Korea'
	main(text)

