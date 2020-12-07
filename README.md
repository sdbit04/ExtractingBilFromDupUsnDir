
**Problem statement:**
Input folder has multiple tar.gz files:
     Each tar.gz file has a report.tar.gz, and multiple USN folders.
     Each USN folder, has a .zip folder of same name.
     So direct extraction may override the extracted folder-name of one by another 
     This program will be helpful to extract all the files from each .zip folder having same name.
     
     
     
Assumed dir-structure of each tar.gz file:
33610_CHR USN V2_20201204142706.tar.gz
└───20201204142706_report.tar.gz
├───20201204142706
	├───vUSN_NE=194709_IP_10_160_0_2
	│   └───usn
	│       └───chr
	|             └───20201204130000_20201204145959_chr.zip(Same-name)
	|					└───file1.bil
	|						file2.bil
	|						
	└───vUSN_NE=194714_IP_10_160_14_2
		└───usn
			└───chr
				└───20201204130000_20201204145959_chr.zip(Same-name)
					└───file3.bil
						file4.bil 
						
**Usage**: 
C:> extract_bil_from_targz_has_dup_usn.exe "Path for Input folder having tar.gz files"

**Functionality**:
This program will extract all the .bill files, and keep under Input/20201204142706/chr_nic
Delete input tar.gz and the report.tar.gz artifact, all the .zip folders having same name after extracting .bil from them.
