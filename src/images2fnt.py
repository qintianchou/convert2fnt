# -*- coding: utf-8 -*-
import os
from PIL import Image

# import utility
import utility


output_path_name="output"


def joint_image(out_image_name,image_dict):
	outW=0
	outH=0
	for key in image_dict.keys():
		size=utility.image_size_at_path(key)
		outW+=size[0]
		outH=max(size[1],outH)

	print "out image size %dx%d" %(outW,outH)

	toImage = Image.new('RGBA', (outW, outH))

	x=0
	for key in image_dict.keys():
		fromImage=Image.open(key)
		toImage.paste(fromImage,( x, 0))
		print "\t %s offset %d" %(key,x)
		x+=fromImage.size[0]

	toImage.save(out_image_name)



def make_fnt_file(pre_str,image_dict):
	# print "make_fnt_file:","\n".join(image_dict)

	fnt_name=output_path_name+"/"+pre_str+".fnt"
	image_name=pre_str+".png"
	fnt_define=dict()
	index=0
	xOffset=0
	max_height=0
	max_width=0
	fnt_define_item=list()
	for key in image_dict.keys():
		print "\t+",key+"\t","Key:",chr(int(image_dict[key]))

		image_size=utility.image_size_at_path(key)
		fnt_define_item_data=dict()
		fnt_define_item_data["id"]=image_dict[key]
		fnt_define_item_data["x"]=str(xOffset)
		fnt_define_item_data["y"]=str(0)
		fnt_define_item_data["width"]=str(image_size[0])
		fnt_define_item_data["height"]=str(image_size[1])
		fnt_define_item_data["xoffset"]=str(0)
		fnt_define_item_data["yoffset"]=str(0)
		fnt_define_item_data["xadvance"]=str(image_size[0])
		fnt_define_item_data["page"]=str(0)
		fnt_define_item_data["chnl"]=str(0)
		fnt_define_item_data["letter"]=chr(int(image_dict[key]))

		fnt_define_item.append(fnt_define_item_data)

		index+=1
		xOffset+=image_size[0]
		max_width=max(max_width,image_size[0])
		max_height=max(max_height,image_size[1])

	fnt_define["data"]=fnt_define_item
	fnt_define["size"]=str(max_width)
	fnt_define["lineHeight"]=str(max_height)
	fnt_define["base"]=str(max_width)
	fnt_define["scaleW"]=str(xOffset)
	fnt_define["scaleH"]=str(max_height)
	fnt_define["file"]=image_name
	fnt_define["count"]=len(image_dict)

	image_name=output_path_name+"/"+image_name

	utility.create_fnt_file(fnt_name, fnt_define)
	print "make:",fnt_name,"done!"
	joint_image(image_name,image_dict)
	print "make:",image_name,"done!"
	print"*************************************************************"


def check_and_make(str_pre,convert_list):
	if len(convert_list)>=4 :
		print"*************************************************************"
		print str_pre+":"
		make_fnt_file(str_pre,convert_list)


def main():
	file_list=os.listdir(os.getcwd())

	if not os.path.exists(output_path_name):
		os.makedirs(output_path_name)


	convert_list=dict()
	str_pre=""
	for file_name in file_list:
		if not os.path.isfile(file_name) or file_name.find(".png") == -1:
			continue
		
		underline_pos=file_name.rfind('_')
		if underline_pos == -1:
			continue
		character = file_name[underline_pos+1:file_name.rfind(".")]
		if len(character) > 1 :
			continue
		ascii_code = ord(character)

		temp_str_pre=file_name[0:underline_pos]
		if str_pre != "" and str_pre != temp_str_pre:
			check_and_make(str_pre,convert_list)
			convert_list=dict()

		str_pre=temp_str_pre
		convert_list[file_name]=ascii_code

	
	check_and_make(str_pre,convert_list)



if __name__ == '__main__':
	main()




