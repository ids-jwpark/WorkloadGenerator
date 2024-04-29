import numpy as np
import pdb

class Dataset_generator:
    def __init__(self, mode, num_samples, epoch):
        self.mode = mode
        self.num = num_samples
        self.epoch = epoch
        # print(self.num)


    def dec_to_bin4(self, dec_num):
        self.dec_num = dec_num.copy()
        bin_result0, bin_mod0 = divmod(self.dec_num, 2)
        bin_result1, bin_mod1 = divmod(bin_result0, 2)
        bin_result2, bin_mod2 = divmod(bin_result1, 2)
        bin_result3, bin_mod3 = divmod(bin_result2, 2)

        bin_mod_values = [bin_mod3, bin_mod2, bin_mod1, bin_mod0]
        bin_binary = np.transpose(bin_mod_values)
        return bin_binary
    
    def dec_to_bin5(self, dec_num):
        self.dec_num = dec_num.copy()
        bin_result0, bin_mod0 = divmod(self.dec_num, 2)
        bin_result1, bin_mod1 = divmod(bin_result0, 2)
        bin_result2, bin_mod2 = divmod(bin_result1, 2)
        bin_result3, bin_mod3 = divmod(bin_result2, 2)
        bin_result4, bin_mod4 = divmod(bin_result3, 2)

        bin_mod_values = [bin_mod4, bin_mod3, bin_mod2, bin_mod1, bin_mod0]
        bin_binary = np.transpose(bin_mod_values)
        return bin_binary
    
    def dec_to_bin8(self, dec_num):
        self.dec_num = dec_num.copy()
        bin_result0, bin_mod0 = divmod(self.dec_num, 2)
        bin_result1, bin_mod1 = divmod(bin_result0, 2)
        bin_result2, bin_mod2 = divmod(bin_result1, 2)
        bin_result3, bin_mod3 = divmod(bin_result2, 2)
        bin_result4, bin_mod4 = divmod(bin_result3, 2)
        bin_result5, bin_mod5 = divmod(bin_result4, 2)
        bin_result6, bin_mod6 = divmod(bin_result5, 2)
        bin_result7, bin_mod7 = divmod(bin_result6, 2)

        bin_mod_values = [bin_mod7, bin_mod6, bin_mod5, bin_mod4, bin_mod3, bin_mod2, bin_mod1, bin_mod0]
        bin_binary = np.transpose(bin_mod_values)
        return bin_binary
    
    def dec_to_bin9(self, dec_num):
        self.dec_num = dec_num.copy()
        bin_result0, bin_mod0 = divmod(self.dec_num, 2)
        bin_result1, bin_mod1 = divmod(bin_result0, 2)
        bin_result2, bin_mod2 = divmod(bin_result1, 2)
        bin_result3, bin_mod3 = divmod(bin_result2, 2)
        bin_result4, bin_mod4 = divmod(bin_result3, 2)
        bin_result5, bin_mod5 = divmod(bin_result4, 2)
        bin_result6, bin_mod6 = divmod(bin_result5, 2)
        bin_result7, bin_mod7 = divmod(bin_result6, 2)
        bin_result8, bin_mod8 = divmod(bin_result7, 2)

        bin_mod_values = [bin_mod8, bin_mod7, bin_mod6, bin_mod5, bin_mod4, bin_mod3, bin_mod2, bin_mod1, bin_mod0]
        bin_binary = np.transpose(bin_mod_values)
        return bin_binary

    def dec_to_bin12(self, dec_num):
        self.dec_num = dec_num.copy()
        bin_result0, bin_mod0 = divmod(self.dec_num, 2)
        bin_result1, bin_mod1 = divmod(bin_result0, 2)
        bin_result2, bin_mod2 = divmod(bin_result1, 2)
        bin_result3, bin_mod3 = divmod(bin_result2, 2)
        bin_result4, bin_mod4 = divmod(bin_result3, 2)
        bin_result5, bin_mod5 = divmod(bin_result4, 2)
        bin_result6, bin_mod6 = divmod(bin_result5, 2)
        bin_result7, bin_mod7 = divmod(bin_result6, 2)
        bin_result8, bin_mod8 = divmod(bin_result7, 2)
        bin_result9, bin_mod9 = divmod(bin_result8, 2)
        bin_result10, bin_mod10 = divmod(bin_result9, 2)
        bin_result11, bin_mod11 = divmod(bin_result10, 2)

        bin_mod_values = [bin_mod11, bin_mod10, bin_mod9,bin_mod8, bin_mod7, bin_mod6, bin_mod5, bin_mod4, bin_mod3, bin_mod2, bin_mod1, bin_mod0]
        bin_binary = np.transpose(bin_mod_values)
        return bin_binary

    def dec_to_bin16(self, dec_num):
        self.dec_num = dec_num.copy()
        bin_result0, bin_mod0 = divmod(self.dec_num, 2)
        bin_result1, bin_mod1 = divmod(bin_result0, 2)
        bin_result2, bin_mod2 = divmod(bin_result1, 2)
        bin_result3, bin_mod3 = divmod(bin_result2, 2)
        bin_result4, bin_mod4 = divmod(bin_result3, 2)
        bin_result5, bin_mod5 = divmod(bin_result4, 2)
        bin_result6, bin_mod6 = divmod(bin_result5, 2)
        bin_result7, bin_mod7 = divmod(bin_result6, 2)
        bin_result8, bin_mod8 = divmod(bin_result7, 2)
        bin_result9, bin_mod9 = divmod(bin_result8, 2)
        bin_result10, bin_mod10 = divmod(bin_result9, 2)
        bin_result11, bin_mod11 = divmod(bin_result10, 2)
        bin_result12, bin_mod12 = divmod(bin_result11, 2)
        bin_result13, bin_mod13 = divmod(bin_result12, 2)
        bin_result14, bin_mod14 = divmod(bin_result13, 2)
        bin_result15, bin_mod15 = divmod(bin_result14, 2)

        bin_mod_values = [bin_mod15, bin_mod14, bin_mod13, bin_mod12, bin_mod11, bin_mod10, bin_mod9, bin_mod8, bin_mod7, bin_mod6, bin_mod5, bin_mod4, bin_mod3, bin_mod2, bin_mod1, bin_mod0]
        bin_binary = np.transpose(bin_mod_values)
        return bin_binary
    
    def dec_to_bin24(self, dec_num):
        self.dec_num = dec_num.copy()
        bin_result0, bin_mod0 = divmod(self.dec_num, 2)
        bin_result1, bin_mod1 = divmod(bin_result0, 2)
        bin_result2, bin_mod2 = divmod(bin_result1, 2)
        bin_result3, bin_mod3 = divmod(bin_result2, 2)
        bin_result4, bin_mod4 = divmod(bin_result3, 2)
        bin_result5, bin_mod5 = divmod(bin_result4, 2)
        bin_result6, bin_mod6 = divmod(bin_result5, 2)
        bin_result7, bin_mod7 = divmod(bin_result6, 2)
        bin_result8, bin_mod8 = divmod(bin_result7, 2)
        bin_result9, bin_mod9 = divmod(bin_result8, 2)
        bin_result10, bin_mod10 = divmod(bin_result9, 2)
        bin_result11, bin_mod11 = divmod(bin_result10, 2)
        bin_result12, bin_mod12 = divmod(bin_result11, 2)
        bin_result13, bin_mod13 = divmod(bin_result12, 2)
        bin_result14, bin_mod14 = divmod(bin_result13, 2)
        bin_result15, bin_mod15 = divmod(bin_result14, 2)
        bin_result16, bin_mod16 = divmod(bin_result15, 2)
        bin_result17, bin_mod17 = divmod(bin_result16, 2)
        bin_result18, bin_mod18 = divmod(bin_result17, 2)
        bin_result19, bin_mod19 = divmod(bin_result18, 2)
        bin_result20, bin_mod20 = divmod(bin_result19, 2)
        bin_result21, bin_mod21 = divmod(bin_result20, 2)
        bin_result22, bin_mod22 = divmod(bin_result21, 2)
        bin_result23, bin_mod23 = divmod(bin_result22, 2)
        

        bin_mod_values = [bin_mod23, bin_mod22, bin_mod21, bin_mod20, bin_mod19, bin_mod18, bin_mod17, bin_mod16, bin_mod15, bin_mod14, bin_mod13, bin_mod12, bin_mod11, bin_mod10, bin_mod9, bin_mod8, bin_mod7, bin_mod6, bin_mod5, bin_mod4, bin_mod3, bin_mod2, bin_mod1, bin_mod0]
        bin_binary = np.transpose(bin_mod_values)
        return bin_binary

    def dec_to_bin25(self, dec_num):
        self.dec_num = dec_num.copy()
        bin_result0, bin_mod0 = divmod(self.dec_num, 2)
        bin_result1, bin_mod1 = divmod(bin_result0, 2)
        bin_result2, bin_mod2 = divmod(bin_result1, 2)
        bin_result3, bin_mod3 = divmod(bin_result2, 2)
        bin_result4, bin_mod4 = divmod(bin_result3, 2)
        bin_result5, bin_mod5 = divmod(bin_result4, 2)
        bin_result6, bin_mod6 = divmod(bin_result5, 2)
        bin_result7, bin_mod7 = divmod(bin_result6, 2)
        bin_result8, bin_mod8 = divmod(bin_result7, 2)
        bin_result9, bin_mod9 = divmod(bin_result8, 2)
        bin_result10, bin_mod10 = divmod(bin_result9, 2)
        bin_result11, bin_mod11 = divmod(bin_result10, 2)
        bin_result12, bin_mod12 = divmod(bin_result11, 2)
        bin_result13, bin_mod13 = divmod(bin_result12, 2)
        bin_result14, bin_mod14 = divmod(bin_result13, 2)
        bin_result15, bin_mod15 = divmod(bin_result14, 2)
        bin_result16, bin_mod16 = divmod(bin_result15, 2)
        bin_result17, bin_mod17 = divmod(bin_result16, 2)
        bin_result18, bin_mod18 = divmod(bin_result17, 2)
        bin_result19, bin_mod19 = divmod(bin_result18, 2)
        bin_result20, bin_mod20 = divmod(bin_result19, 2)
        bin_result21, bin_mod21 = divmod(bin_result20, 2)
        bin_result22, bin_mod22 = divmod(bin_result21, 2)
        bin_result23, bin_mod23 = divmod(bin_result22, 2)
        bin_result24, bin_mod24 = divmod(bin_result23, 2)

        bin_mod_values = [bin_mod24, bin_mod23, bin_mod22, bin_mod21, bin_mod20, bin_mod19, bin_mod18, bin_mod17, bin_mod16, bin_mod15, bin_mod14, bin_mod13, bin_mod12, bin_mod11, bin_mod10, bin_mod9, bin_mod8, bin_mod7, bin_mod6, bin_mod5, bin_mod4, bin_mod3, bin_mod2, bin_mod1, bin_mod0]
        bin_binary = np.transpose(bin_mod_values)
        return bin_binary
    
    def dec_to_bin26(self, dec_num):
        self.dec_num = dec_num.copy()
        bin_result0, bin_mod0 = divmod(self.dec_num, 2)
        bin_result1, bin_mod1 = divmod(bin_result0, 2)
        bin_result2, bin_mod2 = divmod(bin_result1, 2)
        bin_result3, bin_mod3 = divmod(bin_result2, 2)
        bin_result4, bin_mod4 = divmod(bin_result3, 2)
        bin_result5, bin_mod5 = divmod(bin_result4, 2)
        bin_result6, bin_mod6 = divmod(bin_result5, 2)
        bin_result7, bin_mod7 = divmod(bin_result6, 2)
        bin_result8, bin_mod8 = divmod(bin_result7, 2)
        bin_result9, bin_mod9 = divmod(bin_result8, 2)
        bin_result10, bin_mod10 = divmod(bin_result9, 2)
        bin_result11, bin_mod11 = divmod(bin_result10, 2)
        bin_result12, bin_mod12 = divmod(bin_result11, 2)
        bin_result13, bin_mod13 = divmod(bin_result12, 2)
        bin_result14, bin_mod14 = divmod(bin_result13, 2)
        bin_result15, bin_mod15 = divmod(bin_result14, 2)
        bin_result16, bin_mod16 = divmod(bin_result15, 2)
        bin_result17, bin_mod17 = divmod(bin_result16, 2)
        bin_result18, bin_mod18 = divmod(bin_result17, 2)
        bin_result19, bin_mod19 = divmod(bin_result18, 2)
        bin_result20, bin_mod20 = divmod(bin_result19, 2)
        bin_result21, bin_mod21 = divmod(bin_result20, 2)
        bin_result22, bin_mod22 = divmod(bin_result21, 2)
        bin_result23, bin_mod23 = divmod(bin_result22, 2)
        bin_result24, bin_mod24 = divmod(bin_result23, 2)
        bin_result25, bin_mod25 = divmod(bin_result24, 2)

        bin_mod_values = [bin_mod25, bin_mod24, bin_mod23, bin_mod22, bin_mod21, bin_mod20, bin_mod19, bin_mod18, bin_mod17, bin_mod16, bin_mod15, bin_mod14, bin_mod13, bin_mod12, bin_mod11, bin_mod10, bin_mod9, bin_mod8, bin_mod7, bin_mod6, bin_mod5, bin_mod4, bin_mod3, bin_mod2, bin_mod1, bin_mod0]
        bin_binary = np.transpose(bin_mod_values)
        return bin_binary
    
    def dec_to_bin30(self, dec_num):
        self.dec_num = dec_num.copy()
        bin_result0, bin_mod0 = divmod(self.dec_num, 2)
        bin_result1, bin_mod1 = divmod(bin_result0, 2)
        bin_result2, bin_mod2 = divmod(bin_result1, 2)
        bin_result3, bin_mod3 = divmod(bin_result2, 2)
        bin_result4, bin_mod4 = divmod(bin_result3, 2)
        bin_result5, bin_mod5 = divmod(bin_result4, 2)
        bin_result6, bin_mod6 = divmod(bin_result5, 2)
        bin_result7, bin_mod7 = divmod(bin_result6, 2)
        bin_result8, bin_mod8 = divmod(bin_result7, 2)
        bin_result9, bin_mod9 = divmod(bin_result8, 2)
        bin_result10, bin_mod10 = divmod(bin_result9, 2)
        bin_result11, bin_mod11 = divmod(bin_result10, 2)
        bin_result12, bin_mod12 = divmod(bin_result11, 2)
        bin_result13, bin_mod13 = divmod(bin_result12, 2)
        bin_result14, bin_mod14 = divmod(bin_result13, 2)
        bin_result15, bin_mod15 = divmod(bin_result14, 2)
        bin_result16, bin_mod16 = divmod(bin_result15, 2)
        bin_result17, bin_mod17 = divmod(bin_result16, 2)
        bin_result18, bin_mod18 = divmod(bin_result17, 2)
        bin_result19, bin_mod19 = divmod(bin_result18, 2)
        bin_result20, bin_mod20 = divmod(bin_result19, 2)
        bin_result21, bin_mod21 = divmod(bin_result20, 2)
        bin_result22, bin_mod22 = divmod(bin_result21, 2)
        bin_result23, bin_mod23 = divmod(bin_result22, 2)
        bin_result24, bin_mod24 = divmod(bin_result23, 2)
        bin_result25, bin_mod25 = divmod(bin_result24, 2)
        
        bin_result26, bin_mod26 = divmod(bin_result25, 2)
        bin_result27, bin_mod27 = divmod(bin_result26, 2)
        bin_result28, bin_mod28 = divmod(bin_result27, 2)
        bin_result29, bin_mod29 = divmod(bin_result28, 2)

        bin_mod_values = [bin_mod29, bin_mod28, bin_mod27, bin_mod26, bin_mod25, bin_mod24, bin_mod23, bin_mod22, bin_mod21, bin_mod20, bin_mod19, bin_mod18, bin_mod17, bin_mod16, bin_mod15, bin_mod14, bin_mod13, bin_mod12, bin_mod11, bin_mod10, bin_mod9, bin_mod8, bin_mod7, bin_mod6, bin_mod5, bin_mod4, bin_mod3, bin_mod2, bin_mod1, bin_mod0]
        bin_binary = np.transpose(bin_mod_values)
        return bin_binary

    def dec_to_bin32(self, dec_num):
        self.dec_num = dec_num.copy()
        bin_result0, bin_mod0 = divmod(self.dec_num, 2)
        bin_result1, bin_mod1 = divmod(bin_result0, 2)
        bin_result2, bin_mod2 = divmod(bin_result1, 2)
        bin_result3, bin_mod3 = divmod(bin_result2, 2)
        bin_result4, bin_mod4 = divmod(bin_result3, 2)
        bin_result5, bin_mod5 = divmod(bin_result4, 2)
        bin_result6, bin_mod6 = divmod(bin_result5, 2)
        bin_result7, bin_mod7 = divmod(bin_result6, 2)
        bin_result8, bin_mod8 = divmod(bin_result7, 2)
        bin_result9, bin_mod9 = divmod(bin_result8, 2)
        bin_result10, bin_mod10 = divmod(bin_result9, 2)
        bin_result11, bin_mod11 = divmod(bin_result10, 2)
        bin_result12, bin_mod12 = divmod(bin_result11, 2)
        bin_result13, bin_mod13 = divmod(bin_result12, 2)
        bin_result14, bin_mod14 = divmod(bin_result13, 2)
        bin_result15, bin_mod15 = divmod(bin_result14, 2)
        bin_result16, bin_mod16 = divmod(bin_result15, 2)
        bin_result17, bin_mod17 = divmod(bin_result16, 2)
        bin_result18, bin_mod18 = divmod(bin_result17, 2)
        bin_result19, bin_mod19 = divmod(bin_result18, 2)
        bin_result20, bin_mod20 = divmod(bin_result19, 2)
        bin_result21, bin_mod21 = divmod(bin_result20, 2)
        bin_result22, bin_mod22 = divmod(bin_result21, 2)
        bin_result23, bin_mod23 = divmod(bin_result22, 2)
        bin_result24, bin_mod24 = divmod(bin_result23, 2)
        bin_result25, bin_mod25 = divmod(bin_result24, 2)
        
        bin_result26, bin_mod26 = divmod(bin_result25, 2)
        bin_result27, bin_mod27 = divmod(bin_result26, 2)
        bin_result28, bin_mod28 = divmod(bin_result27, 2)
        bin_result29, bin_mod29 = divmod(bin_result28, 2)
        bin_result30, bin_mod30 = divmod(bin_result29, 2)
        bin_result31, bin_mod31 = divmod(bin_result30, 2)

        bin_mod_values = [bin_mod31, bin_mod30, bin_mod29, bin_mod28, bin_mod27, bin_mod26, bin_mod25, bin_mod24, bin_mod23, bin_mod22, bin_mod21, bin_mod20, bin_mod19, bin_mod18, bin_mod17, bin_mod16, bin_mod15, bin_mod14, bin_mod13, bin_mod12, bin_mod11, bin_mod10, bin_mod9, bin_mod8, bin_mod7, bin_mod6, bin_mod5, bin_mod4, bin_mod3, bin_mod2, bin_mod1, bin_mod0]
        bin_binary = np.transpose(bin_mod_values)
        return bin_binary

    def generate_1bit(self):
        
        size = self.num
        dec_num_a = np.random.randint(0,2, size = self.num, dtype = np.uint8)
        
        a_result0, a_mod0 = divmod(dec_num_a, 2)

        a_mod_values = [a_mod0]
        
        a_binary = np.transpose(a_mod_values)

        return a_binary, dec_num_a



    def generate_4bit(self):
        
        size = self.num
        dec_num_a = np.random.randint(0,16, size = self.num, dtype = np.uint8)
        
        a_result0, a_mod0 = divmod(dec_num_a, 2)
        a_result1, a_mod1 = divmod(a_result0, 2)
        a_result2, a_mod2 = divmod(a_result1, 2)
        a_result3, a_mod3 = divmod(a_result2, 2)

        a_mod_values = [a_mod3, a_mod2, a_mod1, a_mod0]
        
        a_binary = np.transpose(a_mod_values)

        return a_binary, dec_num_a


    def generate_7bit(self):
         
        # dec_num_a = np.random.randint(96,160, size = self.num, dtype = np.uint8)
        dec_num_a = np.random.randint(0,127, size = self.num, dtype = np.uint8)
         
        a_result0, a_mod0 = divmod(dec_num_a, 2)
        a_result1, a_mod1 = divmod(a_result0, 2)
        a_result2, a_mod2 = divmod(a_result1, 2)
        a_result3, a_mod3 = divmod(a_result2, 2)
        a_result4, a_mod4 = divmod(a_result3, 2)
        a_result5, a_mod5 = divmod(a_result4, 2)
        a_result6, a_mod6 = divmod(a_result5, 2)
        
        
        a_mod_values = [a_mod6, a_mod5, a_mod4, a_mod3, a_mod2, a_mod1, a_mod0]
        a_binary = np.transpose(a_mod_values)

        return a_binary, dec_num_a


        


    def generate_8bit(self):
         
        dec_num_a = np.random.randint(80,160, size = self.num, dtype = np.uint8)
        # dec_num_a = np.random.randint(0,256, size = self.num, dtype = np.uint8)
         
        a_result0, a_mod0 = divmod(dec_num_a, 2)
        a_result1, a_mod1 = divmod(a_result0, 2)
        a_result2, a_mod2 = divmod(a_result1, 2)
        a_result3, a_mod3 = divmod(a_result2, 2)
        a_result4, a_mod4 = divmod(a_result3, 2)
        a_result5, a_mod5 = divmod(a_result4, 2)
        a_result6, a_mod6 = divmod(a_result5, 2)
        a_result7, a_mod7 = divmod(a_result6, 2)

             
        a_mod_values = [a_mod7, a_mod6, a_mod5, a_mod4, a_mod3, a_mod2, a_mod1, a_mod0]
        
        # a_binary = np.array(a_mod_values)
        # b_binary = np.array(b_mod_values)
        a_binary = np.transpose(a_mod_values)

        return a_binary, dec_num_a

    def generate_ran_8bit(self):
         
        size = self.num
        dec_num_a = np.random.randint(0,256, size = self.num, dtype = np.uint8)
        dec_num_b = np.random.randint(0,256, size = self.num, dtype = np.uint8)
         
        a_result0, a_mod0 = divmod(dec_num_a, 2)
        a_result1, a_mod1 = divmod(a_result0, 2)
        a_result2, a_mod2 = divmod(a_result1, 2)
        a_result3, a_mod3 = divmod(a_result2, 2)
        a_result4, a_mod4 = divmod(a_result3, 2)
        a_result5, a_mod5 = divmod(a_result4, 2)
        a_result6, a_mod6 = divmod(a_result5, 2)
        a_result7, a_mod7 = divmod(a_result6, 2)

        b_result0, b_mod0 = divmod(dec_num_b, 2)
        b_result1, b_mod1 = divmod(b_result0, 2)
        b_result2, b_mod2 = divmod(b_result1, 2)
        b_result3, b_mod3 = divmod(b_result2, 2)
        b_result4, b_mod4 = divmod(b_result3, 2)
        b_result5, b_mod5 = divmod(b_result4, 2)
        b_result6, b_mod6 = divmod(b_result5, 2)
        b_result7, b_mod7 = divmod(b_result6, 2)


             
        a_mod_values = [a_mod7, a_mod6, a_mod5, a_mod4, a_mod3, a_mod2, a_mod1, a_mod0]
        b_mod_values = [b_mod7, b_mod6, b_mod5, b_mod4, b_mod3, b_mod2, b_mod1, b_mod0]
        
        # a_binary = np.array(a_mod_values)
        # b_binary = np.array(b_mod_values)
        a_binary = np.transpose(a_mod_values)
        b_binary = np.transpose(b_mod_values)

        return a_binary, b_binary, dec_num_a, dec_num_b

    def generate_16bit(self):
         
        size = self.num
        
        # dec_num_c = np.arange(self.num)
        dec_num_c = np.random.randint(0,65535, size = self.num, dtype = np.uint16)
         
        c_result0, c_mod0 = divmod(dec_num_c, 2)
        c_result1, c_mod1 = divmod(c_result0, 2)
        c_result2, c_mod2 = divmod(c_result1, 2)
        c_result3, c_mod3 = divmod(c_result2, 2)
        c_result4, c_mod4 = divmod(c_result3, 2)
        c_result5, c_mod5 = divmod(c_result4, 2)
        c_result6, c_mod6 = divmod(c_result5, 2)
        c_result7, c_mod7 = divmod(c_result6, 2)
        c_result8, c_mod8 = divmod(c_result7, 2)
        c_result9, c_mod9 = divmod(c_result8, 2)
        c_result10, c_mod10 = divmod(c_result9, 2)
        c_result11, c_mod11 = divmod(c_result10, 2)
        c_result12, c_mod12 = divmod(c_result11, 2)
        c_result13, c_mod13 = divmod(c_result12, 2)
        c_result14, c_mod14 = divmod(c_result13, 2)
        c_result15, c_mod15 = divmod(c_result14, 2)
        # c_result16, c_mod16 = divmod(c_result15, 2)
        # test = np.transpose(a_mod0)

             
        c_mod_values = [c_mod15, c_mod14, c_mod13, c_mod12, c_mod11, c_mod10, c_mod9, c_mod8, c_mod7, c_mod6, c_mod5, c_mod4, c_mod3, c_mod2, c_mod1, c_mod0]
        c_binary = np.transpose(c_mod_values)

        # string 형태로 추출하는 binary
        # bin_num_a = [format(value, '08b') for value in dec_num_a]
        # bin_num_b = [format(value, '08b') for value in dec_num_b]

        return c_binary, dec_num_c
    def bin_to_dec(self, bin_num):
         
        dec_num = []
        # binary_str = ''.join(map(str, bin_num.flatten()))
        for row in bin_num:

            binary_str = ''.join(map(str,row))
            dec_num.append(int(binary_str, 2))
         
        return dec_num
    
    def sign_ctrl(self, bin_a, bin_b, bin_c):
        if self.mode == 'fp8':
            self.invert_pd = np.zero((bin_a.shape[0], 2), dtype=int)
            self.invert_c = bin_c[:, 0]
            self.invert_pd = [bin_a[:,0] ^ bin_b[:,0], 0]
            invert_c = np.transpose(np.array(self.invert_c))
            invert_pd=np.transpose(np.array(self.invert_pd))
            
            return invert_pd, invert_c
        elif self.mode == 'fp4':
            self.invert_pd = []
            self.invert_c = bin_c[:, 0]
            self.invert_pd = [bin_a[:,0] ^ bin_b[:,0], bin_a[:, 4] ^ bin_b[:, 4]]
            invert_c = np.transpose(np.array(self.invert_c))
            invert_pd=np.transpose(np.array(self.invert_pd))

            return invert_pd, invert_c
        elif self.mode == 'int2':
            self.invert_pd = []
            self.invert_c = bin_c[:, 0]
            self.invert_pd = [0,0]
            invert_c = np.transpose(np.array(self.invert_c))
            invert_pd=np.transpose(np.array(self.invert_pd))

            return invert_pd, invert_c
        else:
            print('mode is all mode')


    def add_2to1(self, carry, sum):
        self.carry = np.array(carry)
        self.sum = np.array(sum)
        
        # for i in range(self.carry.shape[0]):
            
          #  self.sum_result = self.carry[i] + self.sum[i]
        self.sum_result = self.carry + self.sum
         
        return self.sum_result


        #dec_num = np.zeros((self.num), dtype = np.uint8)
        #for i in range(self.num):
        #    dec_num[i] = int(''.join(map(str, bin_num[i])), 2)
        #return dec_num
    def generate_seq_num(self):
        # seq_num = np.arange(self.num)
         
        seq_num = np.arange(self.num, self.num+15)
        c_result0, c_mod0 = divmod(seq_num, 2)
        c_result1, c_mod1 = divmod(c_result0, 2)
        c_result2, c_mod2 = divmod(c_result1, 2)
        c_result3, c_mod3 = divmod(c_result2, 2)
        c_result4, c_mod4 = divmod(c_result3, 2)
        c_result5, c_mod5 = divmod(c_result4, 2)
        c_result6, c_mod6 = divmod(c_result5, 2)
        c_result7, c_mod7 = divmod(c_result6, 2)
        
        c_mod_values = [ c_mod7, c_mod6, c_mod5, c_mod4, c_mod3, c_mod2, c_mod1, c_mod0]
        c_binary = np.transpose(c_mod_values)
        
        return c_binary, seq_num

    def comparator(self, din_python, din_verilog):
        if din_python.shape[0] != din_verilog.shape[0] :
            print('Error: shift bit shape is not same!')
            exit()

        print("######################### Comparison start! #########################")
        for i in range(din_python.shape[0]):
            if din_python[i] != din_verilog[i]:
                print("Error: The value is not match!")
                print("-----------------------------------------------")
                print(f"Python: {din_python[i]}\n")
                print(f"Verilog: {din_verilog[i]}\n")
                print("")
                print("")
                print("")
                print("")
                print("")
        print("######################### Comparison finish! ########################")
        print("")
        print("")
        print("")
        print("")
        print("")


    def generate_real(self):
        # 127~0
        dec_num_a = np.random.randint(0,127, size = self.num, dtype = np.uint8)
        dec_num_b = np.random.randint(0,127, size = self.num, dtype = np.uint8)
        
    def extracting_man(self, bin_a, bin_b):
        if self.mode == 'fp8':
            half_a = bin_a[:, 4:]
            half_b = bin_b[:, 4:]
            
             
            half_zero_masking_a = np.concatenate((np.zeros((bin_a.shape[0], 4), dtype=int), half_a), axis=1)
            half_zero_masking_b = np.concatenate((np.zeros((bin_b.shape[0], 4), dtype=int), half_b), axis=1)
            


             
            # print(half_a)    
            # print(half_b)
            implicit_half_a= half_zero_masking_a
            implicit_half_b= half_zero_masking_b
            
            implicit_half_a[:][:,4] = 1
            implicit_half_b[:][:,4] = 1
            
            fp8_man_a = implicit_half_a
            fp8_man_b = implicit_half_b
            
             
            return fp8_man_a, fp8_man_b
        elif self.mode == 'fp4':
            # half_r_a = bin_a[:, 2:3]
            # half_l_a = bin_a[:, 6:7]
            # half_r_b = bin_b[:, 2:3]
            # half_l_b = bin_b[:, 6:7]
             
            self.bin_a = bin_a.copy()
            self.bin_b = bin_b.copy()

            self.bin_a[:][:,:2] = 0
            self.bin_a[:][:,4:6] = 0
            self.bin_b[:][:,:2] = 0
            self.bin_b[:][:,4:6] = 0

            zero_masking_a = self.bin_a
            zero_masking_b = self.bin_b

            zero_masking_a[:][:,2] = 1  # add implicit bit
            zero_masking_a[:][:,6] = 1  # add implicit bit
            zero_masking_b[:][:,2] = 1  # add implicit bit
            zero_masking_b[:][:,6] = 1  # add implicit bit
            fp4_man_a = zero_masking_a
            fp4_man_b = zero_masking_b
            return fp4_man_a, fp4_man_b

        elif self.mode == 'int2':

            self.bin_a = bin_a.copy()
            self.bin_b = bin_b.copy()
            self.bin_a[:][:,:2] = 0
            self.bin_a[:][:,4:6] = 0
            self.bin_b[:][:,:2] = 0
            self.bin_b[:][:,4:6] = 0

            int2_man_a = self.bin_a
            int2_man_b = self.bin_b
            return int2_man_a, int2_man_b
        elif self.mode == 'bf_int':
            self.bin_a = bin_a.copy()
            self.bin_b = bin_b.copy()
        else:
            print('Please select one of the options')

    def extracting_man_c(self, bin_c):
         
        half_c = bin_c[:, 8:]
         
        half_zero_masking_c = np.concatenate((np.zeros((bin_c.shape[0], 8), dtype=int), half_c), axis=1)
        implicit_half_c= half_zero_masking_c
        implicit_half_c[:][:,8] = 1
        fp8_man_c = implicit_half_c
         
        return fp8_man_c

    def extracting_exp(self, bin_a, bin_b):
        if self.mode == 'fp8':
            self.bin_a = bin_a.copy()
            self.bin_b = bin_b.copy()

            self.bin_a[:, 0] = 0
            self.bin_b[:, 0] = 0
            self.bin_a[:, 5:] = 0
            self.bin_b[:, 5:] = 0
            return self.bin_a, self.bin_b
            
        elif self.mode == 'fp4':
            self.bin_a = bin_a.copy()
            self.bin_b = bin_b.copy()
            
            self.bin_a[:, 0] = 0
            self.bin_b[:, 0] = 0
            self.bin_a[:, 3:5] = 0
            self.bin_b[:, 3:5] = 0
            self.bin_a[:, 7] = 0
            self.bin_b[:, 7] = 0
            
            # exp_a = bin_a[:, 1:3]
            # exp_b = bin_b[:, 1:3]
            return self.bin_a, self.bin_b
        else:
            return bin_a, bin_b





    def mult(self, man_a, man_b):
        self.man_a = man_a
        self.man_b = man_b
        self.data_num = man_a.shape[0]
        if self.mode == 'fp8':
            
            # partial product0
            pp0_0 = self.man_a[:][:,7] * self.man_b[:][:,7]
            pp0_1 = self.man_a[:][:,6] * self.man_b[:][:,7]
            pp0_2 = self.man_a[:][:,5] * self.man_b[:][:,7]
            pp0_3 = self.man_a[:][:,4] * self.man_b[:][:,7]
            pp0_0 = pp0_0[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp0_1 = pp0_1[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp0_2 = pp0_2[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp0_3 = pp0_3[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp0 = np.concatenate((pp0_3, pp0_2, pp0_1, pp0_0), axis=1)
            pp0 = np.concatenate((np.zeros((self.data_num, 4), dtype=int), pp0), axis=1)
            #  
            # partial product1
            pp1_0 = self.man_a[:][:,7] * self.man_b[:][:,6]
            pp1_1 = self.man_a[:][:,6] * self.man_b[:][:,6]
            pp1_2 = self.man_a[:][:,5] * self.man_b[:][:,6]
            pp1_3 = self.man_a[:][:,4] * self.man_b[:][:,6]
            pp1_0 = pp1_0[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp1_1 = pp1_1[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp1_2 = pp1_2[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp1_3 = pp1_3[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
             
            pp1 = np.concatenate((pp1_3, pp1_2, pp1_1, pp1_0), axis=1)
            pp1 = np.concatenate((np.zeros((self.data_num, 3), dtype=int), pp1, np.zeros((self.data_num,1),dtype=int)), axis=1)

            # partial product2
            pp2_0 = self.man_a[:][:,7] * self.man_b[:][:,5]
            pp2_1 = self.man_a[:][:,6] * self.man_b[:][:,5]
            pp2_2 = self.man_a[:][:,5] * self.man_b[:][:,5]
            pp2_3 = self.man_a[:][:,4] * self.man_b[:][:,5]
            pp2_0 = pp2_0[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp2_1 = pp2_1[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp2_2 = pp2_2[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp2_3 = pp2_3[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
             
            pp2 = np.concatenate((pp2_3, pp2_2, pp2_1, pp2_0), axis=1)
            pp2 = np.concatenate((np.zeros((self.data_num, 2), dtype=int), pp2, np.zeros((self.data_num,2),dtype=int)), axis=1)

            # partial product3
            pp3_0 = self.man_a[:][:,7] * self.man_b[:][:,4]
            pp3_1 = self.man_a[:][:,6] * self.man_b[:][:,4]
            pp3_2 = self.man_a[:][:,5] * self.man_b[:][:,4]
            pp3_3 = self.man_a[:][:,4] * self.man_b[:][:,4]
            pp3_0 = pp3_0[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp3_1 = pp3_1[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp3_2 = pp3_2[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp3_3 = pp3_3[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
             
            pp3 = np.concatenate((pp3_3, pp3_2, pp3_1, pp3_0), axis=1)
            pp3 = np.concatenate((np.zeros((self.data_num, 1), dtype=int), pp3, np.zeros((self.data_num,3),dtype=int)), axis=1)

             
            # carry save adder
            
            sum0 = np.zeros((self.data_num, 8), dtype=int)
            carry0_7b = np.zeros((self.data_num, 7), dtype=int)
            inter_x0 =  np.zeros((self.data_num, 8), dtype=int)
            inter_y0 = np.zeros((self.data_num, 8), dtype=int)
            inter_z0 = np.zeros((self.data_num, 8), dtype=int)
            sum_result = np.zeros((self.data_num, 8), dtype=int)
            carry_result = np.zeros((self.data_num, 8), dtype=int)
            

            # csa0
            inter_x0 = pp0 ^ pp1
            inter_y0 = inter_x0 & pp2
            inter_z0 = pp0 & pp1

            carry0_7b = inter_y0[:][:,1:] | inter_z0[:][:,1:]
            carry0 = np.concatenate((carry0_7b, np.zeros((self.data_num, 1), dtype=int)), axis=1)
            sum0 = inter_x0 ^ pp2
            
            #csa1
            inter_x1 = carry0 ^ sum0
            inter_y1 = inter_x1 & pp3
            inter_z1 = carry0 & sum0
             
            carry1_7b = inter_y1[:][:,1:] | inter_z1[:][:,1:]
            carry_result = np.concatenate((carry1_7b, np.zeros((self.data_num, 1), dtype=int)), axis=1)
            sum_result = inter_x1 ^ pp3

            return carry_result, sum_result





        elif self.mode == 'fp4' or self.mode == 'int2':
             
            # partial product0
            pp0_0 = self.man_a[:][:,7] * self.man_b[:][:,7]
            pp0_1 = self.man_a[:][:,6] * self.man_b[:][:,7]
            # pp0_2 = self.man_a[:][:,5] * self.man_b[:][:,7]
            # pp0_3 = self.man_a[:][:,4] * self.man_b[:][:,7]
            pp0_0 = pp0_0[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp0_1 = pp0_1[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            # pp0_2 = pp0_2[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            # pp0_3 = pp0_3[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
             
            # pp0 = np.concatenate((pp0_3, pp0_2, pp0_1, pp0_0), axis=1)
            pp0 = np.concatenate((pp0_1, pp0_0), axis=1)
            pp0 = np.concatenate((np.zeros((self.data_num, 6), dtype=int), pp0), axis=1)
            
            # partial product1
            pp1_0 = self.man_a[:][:,7] * self.man_b[:][:,6]
            pp1_1 = self.man_a[:][:,6] * self.man_b[:][:,6]
            # pp1_2 = self.man_a[:][:,5] * self.man_b[:][:,6]
            # pp1_3 = self.man_a[:][:,4] * self.man_b[:][:,6]
            pp1_0 = pp1_0[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp1_1 = pp1_1[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            # pp1_2 = pp1_2[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            # pp1_3 = pp1_3[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
             
            # pp1 = np.concatenate((pp1_3, pp1_2, pp1_1, pp0_0), axis=1)
            pp1 = np.concatenate((pp1_1, pp1_0), axis=1)
            pp1 = np.concatenate((np.zeros((self.data_num, 5), dtype=int), pp1, np.zeros((self.data_num,1),dtype=int)), axis=1)

            # partial product2
            # pp2_0 = self.man_a[:][:,3] * self.man_b[:][:,3]
            # pp2_1 = self.man_a[:][:,2] * self.man_b[:][:,3]
            # pp2_2 = self.man_a[:][:,1] * self.man_b[:][:,3]
            # pp2_3 = self.man_a[:][:,0] * self.man_b[:][:,3]
            pp2_2 = self.man_a[:][:,3] * self.man_b[:][:,3]
            pp2_3 = self.man_a[:][:,2] * self.man_b[:][:,3]
            
            # pp2_0 = pp2_0[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            # pp2_1 = pp2_1[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp2_2 = pp2_2[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp2_3 = pp2_3[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
             
            # pp2 = np.concatenate((pp2_3, pp2_2, pp2_1, pp2_0), axis=1)
            pp2 = np.concatenate((pp2_3, pp2_2), axis=1)
            pp2 = np.concatenate((np.zeros((self.data_num, 2), dtype=int), pp2, np.zeros((self.data_num,4),dtype=int)), axis=1)

            # partial product3
            # pp3_0 = self.man_a[:][:,3] * self.man_b[:][:,2]
            # pp3_1 = self.man_a[:][:,2] * self.man_b[:][:,2]
            # pp3_2 = self.man_a[:][:,1] * self.man_b[:][:,2]
            # pp3_3 = self.man_a[:][:,0] * self.man_b[:][:,2]
            pp3_2 = self.man_a[:][:,3] * self.man_b[:][:,2]
            pp3_3 = self.man_a[:][:,2] * self.man_b[:][:,2]
            # pp3_0 = pp3_0[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            # pp3_1 = pp3_1[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp3_2 = pp3_2[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
            pp3_3 = pp3_3[:, None]  # 1차원 배열을 2차원 열 벡터로 변환
             
            # pp3 = np.concatenate((pp3_3, pp3_2, pp3_1, pp3_0), axis=1)
            pp3 = np.concatenate((pp3_3, pp3_2), axis=1)
            pp3 = np.concatenate((np.zeros((self.data_num, 1), dtype=int), pp3, np.zeros((self.data_num,5),dtype=int)), axis=1)
             
            # carry save adder
            sum0 = np.zeros((self.data_num, 8), dtype=int)
            carry0_7b = np.zeros((self.data_num, 7), dtype=int)
            inter_x0 =  np.zeros((self.data_num, 8), dtype=int)
            inter_y0 = np.zeros((self.data_num, 8), dtype=int)
            inter_z0 = np.zeros((self.data_num, 8), dtype=int)
            sum_result = np.zeros((self.data_num, 8), dtype=int)
            carry_result = np.zeros((self.data_num, 8), dtype=int)

            # csa0
            inter_x0 = pp0 ^ pp1
            inter_y0 = inter_x0 & pp2
            inter_z0 = pp0 & pp1

            carry0_7b = inter_y0[:][:,1:] | inter_z0[:][:,1:]
            carry0 = np.concatenate((carry0_7b, np.zeros((self.data_num, 1), dtype=int)), axis=1)
            sum0 = inter_x0 ^ pp2 # 여기까지 문제 없음
             
            # csa1
            inter_x1 = carry0 ^ sum0
            inter_y1 = inter_x1 & pp3
            inter_z1 = carry0 & sum0
             
            carry1_7b = inter_y1[:][:,1:] | inter_z1[:][:,1:]
            carry_result = np.concatenate((carry1_7b, np.zeros((self.data_num, 1), dtype=int)), axis=1)
            sum_result = inter_x1 ^ pp3

            return carry_result, sum_result
        
    def writing_txt_no_spacing(self, write_path, in_data, fmt = '%d', delimiter = ''):
        self.in_data = in_data
        self.write_path = write_path
        self.fmt = fmt
        self.delimiter = delimiter
        np.savetxt(write_path, in_data, fmt =fmt, delimiter = delimiter)
        print('writing complete')
    
    def writing_txt_no_spacing_hex(self, write_path, in_data, fmt = '%s', delimiter = ''):
        self.in_data = in_data
        self.write_path = write_path
        self.fmt = fmt
        self.delimiter = delimiter
        np.savetxt(write_path, in_data, fmt =fmt, delimiter = delimiter)
        # np.savetxt(write_path, in_data, fmt ='%04s', delimiter = delimiter)
        print('writing complete')
        # np.savetxt('output.txt', X, fmt='%04X')

    def writing_txt_with_spacing(self, write_path, in_data, fmt = '%d'):
        self.in_data = in_data
        self.write_path = write_path
        self.fmt = fmt
        np.savetxt(write_path, in_data, fmt =fmt)
        print('writing complete')

    def simulation_params(self, file_path, parameter_name, parameter_value):
        self.file_path = file_path
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

        with open(file_path, 'w') as f:
            f.write(f"parameter {parameter_name} = {parameter_value};\n")
        
    def input_processing(self, bin_a, bin_b):
        if self.mode == 'bf_int':
            chunk = int(self.num/4)
            self.bin_a = bin_a.copy()
            self.bin_b = bin_b.copy()
            
            bin_sign_a = self.bin_a[:, :1]
            #####################################################################################
            # sign도 chunk로 4그룹씩 나누어서 만들어주기(20240331)
            bin_sign_a0 = np.zeros((self.num, 1), dtype=int)
            bin_sign_a1 = np.zeros((self.num, 1), dtype=int)
            bin_sign_a2 = np.zeros((self.num, 1), dtype=int)
            bin_sign_a3 = np.zeros((self.num, 1), dtype=int)

            for i in range(chunk):
                bin_sign_a0[4*i]   = bin_sign_a[4*i]
                bin_sign_a0[4*i+1] = bin_sign_a[4*i]
                bin_sign_a0[4*i+2] = bin_sign_a[4*i]
                bin_sign_a0[4*i+3] = bin_sign_a[4*i]

                bin_sign_a1[4*i]   = bin_sign_a[4*i+1]
                bin_sign_a1[4*i+1] = bin_sign_a[4*i+1]
                bin_sign_a1[4*i+2] = bin_sign_a[4*i+1]
                bin_sign_a1[4*i+3] = bin_sign_a[4*i+1]

                bin_sign_a2[4*i]   = bin_sign_a[4*i+2]
                bin_sign_a2[4*i+1] = bin_sign_a[4*i+2]
                bin_sign_a2[4*i+2] = bin_sign_a[4*i+2]
                bin_sign_a2[4*i+3] = bin_sign_a[4*i+2]

                bin_sign_a3[4*i]   = bin_sign_a[4*i+3]
                bin_sign_a3[4*i+1] = bin_sign_a[4*i+3]
                bin_sign_a3[4*i+2] = bin_sign_a[4*i+3]
                bin_sign_a3[4*i+3] = bin_sign_a[4*i+3]

            bin_sign_b3 = self.bin_b[:, :1]
            bin_sign_b2 = self.bin_b[:, 4:5]
            bin_sign_b1 = self.bin_b[:, 8:9]
            bin_sign_b0 = self.bin_b[:, 12:13]

            bin_sign_pd0 = bin_sign_a0 ^ bin_sign_b0
            bin_sign_pd1 = bin_sign_a1 ^ bin_sign_b1
            bin_sign_pd2 = bin_sign_a2 ^ bin_sign_b2
            bin_sign_pd3 = bin_sign_a3 ^ bin_sign_b3

            bin_sign_pd = np.concatenate((bin_sign_pd3, bin_sign_pd2, bin_sign_pd1, bin_sign_pd0), axis = 1)
            
            ######################################################################################
            # Sign Extracting Logic
            # bin_sign_a = self.bin_a[:, :1]
             
            #bin_sign_b = np.concatenate((self.bin_b[:, 0:1], self.bin_b[:, 4:5], self.bin_b[:, 8:9], self.bin_b[:, 12:13]),  axis = 1)
            
            # bin_sign_b = np.concatenate((self.bin_b[:,12:13], self.bin_b[:,8:9], self.bin_b[:,4:5], self.bin_b[:,0:1]),  axis = 1)
            #bin_sign_pd = bin_sign_a ^ bin_sign_b
             


            # Exponent Extracting Logic
            bin_exp_a = self.bin_a[:, 1:9]
            # bin_exp_b = bin_b[:, 1:9]
            dec_exp_a = np.array(self.bin_to_dec(bin_exp_a)).reshape(bin_a.shape[0], 1)
            bias = [0, 1, 1, 1, 1, 1, 1, 1]
            bin_exp_b = np.tile(bias, (bin_a.shape[0],1))
            dec_exp_b = np.array(self.bin_to_dec(bin_exp_b)).reshape(bin_a.shape[0], 1)
            # dec_exp_b = np.array(self.bin_to_dec(bin_exp_b)).reshape(bin_b.shape[0], 1)
            dec_exp_pd = dec_exp_a + dec_exp_b - 127
            reduced_dec_exp_pd = dec_exp_pd[:self.num]
            bin_exp_pd = np.array(self.dec_to_bin8(reduced_dec_exp_pd)).reshape(self.num, 8)

            # Mantissa Extracting Logic
            bin_implicit_bit = np.ones((self.num, 1), dtype = int)
             
            bin_man_a = np.concatenate((bin_implicit_bit, self.bin_a[:, 9:]), axis = 1)
             
            ##############################################################################################
            # 여기부터 수정해줘야함(20240330)
            chunk = int(self.num/4)
            bin_man_a0 = np.zeros((self.num, 8), dtype = int)
            bin_man_a1 = np.zeros((self.num, 8), dtype = int)
            bin_man_a2 = np.zeros((self.num, 8), dtype = int)
            bin_man_a3 = np.zeros((self.num, 8), dtype = int)
            for i in range(chunk):

                bin_man_a0[4*i]   = bin_man_a[4*i]
                bin_man_a0[4*i+1] = bin_man_a[4*i]
                bin_man_a0[4*i+2] = bin_man_a[4*i]
                bin_man_a0[4*i+3] = bin_man_a[4*i]

                bin_man_a1[4*i]   = bin_man_a[4*i+1]
                bin_man_a1[4*i+1] = bin_man_a[4*i+1]
                bin_man_a1[4*i+2] = bin_man_a[4*i+1]
                bin_man_a1[4*i+3] = bin_man_a[4*i+1]

                bin_man_a2[4*i]   = bin_man_a[4*i+2]
                bin_man_a2[4*i+1] = bin_man_a[4*i+2]
                bin_man_a2[4*i+2] = bin_man_a[4*i+2]
                bin_man_a2[4*i+3] = bin_man_a[4*i+2]

                bin_man_a3[4*i]   = bin_man_a[4*i+3]
                bin_man_a3[4*i+1] = bin_man_a[4*i+3]
                bin_man_a3[4*i+2] = bin_man_a[4*i+3]
                bin_man_a3[4*i+3] = bin_man_a[4*i+3]
            # 이어서 여기도
                
             
            bin_man3_b = self.bin_b[:, 1:4]
            bin_man2_b = self.bin_b[:, 5:8]
            bin_man1_b = self.bin_b[:, 9:12]
            bin_man0_b = self.bin_b[:, 13:]
            dec_man_a =  np.array(self.bin_to_dec(bin_man_a)).reshape(self.num, 1)
             
            dec_man0_b = np.array(self.bin_to_dec(bin_man0_b)).reshape(self.num, 1)
            dec_man1_b = np.array(self.bin_to_dec(bin_man1_b)).reshape(self.num, 1)
            dec_man2_b = np.array(self.bin_to_dec(bin_man2_b)).reshape(self.num, 1)
            dec_man3_b = np.array(self.bin_to_dec(bin_man3_b)).reshape(self.num, 1)

            # dec_man_b = np.concatenate((dec_man0_b, dec_man1_b, dec_man2_b, dec_man3_b), axis = 1)
            dec_man_b = np.concatenate((dec_man3_b, dec_man2_b, dec_man1_b, dec_man0_b), axis = 1)
             

            #########################################
            # overflow flag
            ovf_flag = np.zeros((self.epoch, 1), dtype = int)
            for i in range(self.epoch):
                if np.any(dec_exp_pd[32*i:32*(i+1)] > 255):
                    ovf_flag[i] = 1
                else:
                    ovf_flag[i] = 0
            #########################################
             
            udf_flag = np.where(reduced_dec_exp_pd < 0, 1, 0)
             
            return bin_sign_pd, reduced_dec_exp_pd, bin_man_a, dec_man_a, dec_man_b, ovf_flag, udf_flag
        elif self.mode == 'bf_bf':
            print('bf_bf mode')
            chunk = int(self.num/4)
            self.bin_a = bin_a.copy()
            self.bin_b = bin_b.copy()
            #####################################################################################
            # Sign Extracting Logic

            bin_sign_a = self.bin_a[:, :1]
            #####################################################################################
            # sign도 chunk로 4그룹씩 나누어서 만들어주기(20240331)


            bin_sign_b = self.bin_b[:, :1]

            bin_sign_pd0 = np.zeros((self.num, 1),dtype = int)
            bin_sign_pd1 = np.zeros((self.num, 1),dtype = int)
            bin_sign_pd2 = np.zeros((self.num, 1),dtype = int)
            bin_sign_pd3 = bin_sign_a ^ bin_sign_b

            bin_sign_pd = np.concatenate((bin_sign_pd3, bin_sign_pd2, bin_sign_pd1, bin_sign_pd0), axis = 1)
            ######################################################################################
            # EXP Extracting Logic
            bin_exp_a = self.bin_a[:, 1:9]
            bin_exp_b = self.bin_b[:, 1:9]

            dec_exp_a = np.array(self.bin_to_dec(bin_exp_a)).reshape(bin_a.shape[0], 1)
            dec_exp_b = np.array(self.bin_to_dec(bin_exp_b)).reshape(bin_b.shape[0], 1)

            dec_exp_pd = dec_exp_a + dec_exp_b - 127

            ######################################################################################
            # Mantissa Extracting Logic
            bin_implicit_bit = np.ones((self.num, 1), dtype = int)
             
            bin_man_a = np.concatenate((bin_implicit_bit, self.bin_a[:, 9:]), axis = 1)
            bin_man_b = np.concatenate((bin_implicit_bit, self.bin_b[:, 9:]), axis = 1)

            dec_man_a = np.array(self.bin_to_dec(bin_man_a)).reshape(self.num, 1)
            dec_man_b = np.array(self.bin_to_dec(bin_man_b)).reshape(self.num, 1)

            ovf_flag = np.zeros((self.epoch, 1), dtype = int)
            for i in range(self.epoch):
                if np.any(dec_exp_pd[32*i:32*(i+1)] > 255):
                    ovf_flag[i] = 1
                else:
                    ovf_flag[i] = 0
            #########################################
             
            udf_flag = np.where(dec_exp_pd < 0, 1, 0)


             
            return bin_sign_pd, dec_exp_pd, bin_man_a, bin_man_b, dec_man_a, dec_man_b, ovf_flag, udf_flag
        
        elif self.mode == 'fp_fp':
            chunk = int(self.num/4)
            self.bin_a = bin_a.copy()
            self.bin_b = bin_b.copy()
            #####################################################################################
            # Sign Extracting Logic

            bin_sign_a = self.bin_a[:, :1]
            #####################################################################################
            # sign도 chunk로 4그룹씩 나누어서 만들어주기(20240331)


            bin_sign_b = self.bin_b[:, :1]

            bin_sign_pd0 = np.zeros((self.num, 1),dtype = int)
            bin_sign_pd1 = np.zeros((self.num, 1),dtype = int)
            bin_sign_pd2 = np.zeros((self.num, 1),dtype = int)
            bin_sign_pd3 = bin_sign_a ^ bin_sign_b

            bin_sign_pd = np.concatenate((bin_sign_pd3, bin_sign_pd2, bin_sign_pd1, bin_sign_pd0), axis = 1)
            ######################################################################################
            # EXP Extracting Logic
            bin_exp_a = self.bin_a[:, 1:6]
            bin_exp_b = self.bin_b[:, 1:6]

            dec_exp_a = np.array(self.bin_to_dec(bin_exp_a)).reshape(bin_a.shape[0], 1)
            dec_exp_b = np.array(self.bin_to_dec(bin_exp_b)).reshape(bin_b.shape[0], 1)

            dec_exp_pd = dec_exp_a + dec_exp_b - 15

            ######################################################################################
            # Mantissa Extracting Logic
            bin_implicit_bit = np.ones((self.num, 1), dtype = int)
             
            bin_man_a = np.concatenate((bin_implicit_bit, self.bin_a[:, 6:]), axis = 1)
            bin_man_b = np.concatenate((bin_implicit_bit, self.bin_b[:, 6:]), axis = 1)

            dec_man_a = np.array(self.bin_to_dec(bin_man_a)).reshape(self.num, 1)
            dec_man_b = np.array(self.bin_to_dec(bin_man_b)).reshape(self.num, 1)

            ovf_flag = np.zeros((self.epoch, 1), dtype = int)
            for i in range(self.epoch):
                if np.any(dec_exp_pd[32*i:32*(i+1)] > 31):
                    ovf_flag[i] = 1
                else:
                    ovf_flag[i] = 0
            #########################################
             
            udf_flag = np.where(dec_exp_pd < 0, 1, 0)


             
            return bin_sign_pd, dec_exp_pd, bin_man_a, bin_man_b, dec_man_a, dec_man_b, ovf_flag, udf_flag
        elif self.mode == 'fp_int':
            chunk = int(self.num/4)
            self.bin_a = bin_a.copy()
            self.bin_b = bin_b.copy()
            
            bin_sign_a = self.bin_a[:, :1]
            #####################################################################################
            # sign도 chunk로 4그룹씩 나누어서 만들어주기(20240331)
            bin_sign_a0 = np.zeros((self.num, 1), dtype=int)
            bin_sign_a1 = np.zeros((self.num, 1), dtype=int)
            bin_sign_a2 = np.zeros((self.num, 1), dtype=int)
            bin_sign_a3 = np.zeros((self.num, 1), dtype=int)

            for i in range(chunk):
                bin_sign_a0[4*i]   = bin_sign_a[4*i]
                bin_sign_a0[4*i+1] = bin_sign_a[4*i]
                bin_sign_a0[4*i+2] = bin_sign_a[4*i]
                bin_sign_a0[4*i+3] = bin_sign_a[4*i]

                bin_sign_a1[4*i]   = bin_sign_a[4*i+1]
                bin_sign_a1[4*i+1] = bin_sign_a[4*i+1]
                bin_sign_a1[4*i+2] = bin_sign_a[4*i+1]
                bin_sign_a1[4*i+3] = bin_sign_a[4*i+1]

                bin_sign_a2[4*i]   = bin_sign_a[4*i+2]
                bin_sign_a2[4*i+1] = bin_sign_a[4*i+2]
                bin_sign_a2[4*i+2] = bin_sign_a[4*i+2]
                bin_sign_a2[4*i+3] = bin_sign_a[4*i+2]

                bin_sign_a3[4*i]   = bin_sign_a[4*i+3]
                bin_sign_a3[4*i+1] = bin_sign_a[4*i+3]
                bin_sign_a3[4*i+2] = bin_sign_a[4*i+3]
                bin_sign_a3[4*i+3] = bin_sign_a[4*i+3]

            bin_sign_b3 = self.bin_b[:, :1]
            bin_sign_b2 = self.bin_b[:, 4:5]
            bin_sign_b1 = self.bin_b[:, 8:9]
            bin_sign_b0 = self.bin_b[:, 12:13]

            bin_sign_pd0 = bin_sign_a0 ^ bin_sign_b0
            bin_sign_pd1 = bin_sign_a1 ^ bin_sign_b1
            bin_sign_pd2 = bin_sign_a2 ^ bin_sign_b2
            bin_sign_pd3 = bin_sign_a3 ^ bin_sign_b3

            bin_sign_pd = np.concatenate((bin_sign_pd3, bin_sign_pd2, bin_sign_pd1, bin_sign_pd0), axis = 1)
            
            ######################################################################################
            # Sign Extracting Logic
            # bin_sign_a = self.bin_a[:, :1]
             
            #bin_sign_b = np.concatenate((self.bin_b[:, 0:1], self.bin_b[:, 4:5], self.bin_b[:, 8:9], self.bin_b[:, 12:13]),  axis = 1)
            
            # bin_sign_b = np.concatenate((self.bin_b[:,12:13], self.bin_b[:,8:9], self.bin_b[:,4:5], self.bin_b[:,0:1]),  axis = 1)
            #bin_sign_pd = bin_sign_a ^ bin_sign_b
             


            # Exponent Extracting Logic
            # bin_exp_a = self.bin_a[:, 1:9]
            bin_exp_a = self.bin_a[:, 1:6]
            # bin_exp_b = bin_b[:, 1:9]
            dec_exp_a = np.array(self.bin_to_dec(bin_exp_a)).reshape(bin_a.shape[0], 1)
            bias = [0, 1, 1, 1, 1]
            bin_exp_b = np.tile(bias, (bin_a.shape[0],1))
            dec_exp_b = np.array(self.bin_to_dec(bin_exp_b)).reshape(bin_a.shape[0], 1)
            # dec_exp_b = np.array(self.bin_to_dec(bin_exp_b)).reshape(bin_b.shape[0], 1)
            dec_exp_pd = dec_exp_a + dec_exp_b - 15
            reduced_dec_exp_pd = dec_exp_pd[:self.num]
            bin_exp_pd = np.array(self.dec_to_bin5(reduced_dec_exp_pd)).reshape(self.num, 5)

            # Mantissa Extracting Logic
            bin_implicit_bit = np.ones((self.num, 1), dtype = int)
             
            # bin_man_a = np.concatenate((bin_implicit_bit, self.bin_a[:, 9:]), axis = 1)
            bin_man_a = np.concatenate((bin_implicit_bit, self.bin_a[:, 6:]), axis = 1)
             
            ##############################################################################################
            # 여기부터 수정해줘야함(20240330)
            chunk = int(self.num/4)
            bin_man_a0 = np.zeros((self.num, 11), dtype = int)
            bin_man_a1 = np.zeros((self.num, 11), dtype = int)
            bin_man_a2 = np.zeros((self.num, 11), dtype = int)
            bin_man_a3 = np.zeros((self.num, 11), dtype = int)
            for i in range(chunk):

                bin_man_a0[4*i]   = bin_man_a[4*i]
                bin_man_a0[4*i+1] = bin_man_a[4*i]
                bin_man_a0[4*i+2] = bin_man_a[4*i]
                bin_man_a0[4*i+3] = bin_man_a[4*i]

                bin_man_a1[4*i]   = bin_man_a[4*i+1]
                bin_man_a1[4*i+1] = bin_man_a[4*i+1]
                bin_man_a1[4*i+2] = bin_man_a[4*i+1]
                bin_man_a1[4*i+3] = bin_man_a[4*i+1]

                bin_man_a2[4*i]   = bin_man_a[4*i+2]
                bin_man_a2[4*i+1] = bin_man_a[4*i+2]
                bin_man_a2[4*i+2] = bin_man_a[4*i+2]
                bin_man_a2[4*i+3] = bin_man_a[4*i+2]

                bin_man_a3[4*i]   = bin_man_a[4*i+3]
                bin_man_a3[4*i+1] = bin_man_a[4*i+3]
                bin_man_a3[4*i+2] = bin_man_a[4*i+3]
                bin_man_a3[4*i+3] = bin_man_a[4*i+3]
            # 이어서 여기도
                
             
            bin_man3_b = self.bin_b[:, 1:4]
            bin_man2_b = self.bin_b[:, 5:8]
            bin_man1_b = self.bin_b[:, 9:12]
            bin_man0_b = self.bin_b[:, 13:]
            dec_man_a =  np.array(self.bin_to_dec(bin_man_a)).reshape(self.num, 1)
             
            dec_man0_b = np.array(self.bin_to_dec(bin_man0_b)).reshape(self.num, 1)
            dec_man1_b = np.array(self.bin_to_dec(bin_man1_b)).reshape(self.num, 1)
            dec_man2_b = np.array(self.bin_to_dec(bin_man2_b)).reshape(self.num, 1)
            dec_man3_b = np.array(self.bin_to_dec(bin_man3_b)).reshape(self.num, 1)

            # dec_man_b = np.concatenate((dec_man0_b, dec_man1_b, dec_man2_b, dec_man3_b), axis = 1)
            dec_man_b = np.concatenate((dec_man3_b, dec_man2_b, dec_man1_b, dec_man0_b), axis = 1)
             

            #########################################
            # overflow flag
            ovf_flag = np.zeros((self.epoch, 1), dtype = int)
            for i in range(self.epoch):
                if np.any(dec_exp_pd[32*i:32*(i+1)] > 31):
                    ovf_flag[i] = 1
                else:
                    ovf_flag[i] = 0
            #########################################
             
            udf_flag = np.where(reduced_dec_exp_pd < 0, 1, 0)
             
            return bin_sign_pd, reduced_dec_exp_pd, bin_man_a, dec_man_a, dec_man_b, ovf_flag, udf_flag
        
    def exp_comparator(self, dec_exp_pd, udf_flag):
        if self.mode == 'bf_int':
            print('bf_int mode exp_comparator')
             
            self.dec_exp_pd = dec_exp_pd.copy()
            self.udf_flag = udf_flag.copy()
            max_exp = []
            for i in range(0, self.dec_exp_pd.shape[0], 32):
                
                max_exp_in_chunck = np.max(self.dec_exp_pd[i:i+32])
                max_exp.append(max_exp_in_chunck)
            max_exp = np.array(max_exp).reshape(-1, 1)
            
            expanded_max_exp = np.zeros((self.num,1), dtype = int)
            for i in range(self.epoch):
                expanded_max_exp[i*32:(i+1)*32] = max_exp[i]
            
             


            # max_exp = np.max(self.dec_exp_pd)
             
            dec_temp_shift_bit = np.where(self.udf_flag == 1, 15, expanded_max_exp - self.dec_exp_pd)
            oor_flag = np.where(dec_temp_shift_bit > 15, 1, 0)
            dec_shift_bit = np.where(dec_temp_shift_bit > 15, 15, dec_temp_shift_bit) # 이거 oor flag = 1일 때, shift bit = 15로 할까, 16으로 할까
            bin_shift_bit = np.array(self.dec_to_bin4(dec_shift_bit)).reshape(self.num, 4)
             
            return oor_flag, bin_shift_bit, dec_shift_bit, max_exp
            
        elif self.mode == 'bf_bf':
            print('bf_bf mode exp_comparator')
            self.dec_exp_pd = dec_exp_pd.copy()
            self.udf_flag = udf_flag.copy()
            max_exp = []
            for i in range(0, self.dec_exp_pd.shape[0], 32):
                
                max_exp_in_chunk = np.max(self.dec_exp_pd[i:i+32])
                max_exp.append(max_exp_in_chunk)

            max_exp = np.array(max_exp).reshape(-1,1)

            expanded_max_exp = np.zeros((self.num, 1), dtype = int)
            for i in range(self.epoch):
                expanded_max_exp[i*32:(i+1)*32] = max_exp[i]

            dec_temp_shift_bit = np.where(self.udf_flag == 1, 15, expanded_max_exp - self.dec_exp_pd)
            oor_flag = np.where(dec_temp_shift_bit > 15, 1, 0)
            dec_shift_bit = np.where(dec_temp_shift_bit > 15, 15, dec_temp_shift_bit) # 이거 oor flag = 1일 때, shift bit = 15로 할까, 16으로 할까
            bin_shift_bit = np.array(self.dec_to_bin4(dec_shift_bit)).reshape(self.num, 4)
             
            return oor_flag, bin_shift_bit, dec_shift_bit, max_exp
        
        elif self.mode == 'fp_fp':
            print('fp_fp mode exp_comparator')
            self.dec_exp_pd = dec_exp_pd.copy()
            self.udf_flag = udf_flag.copy()
            max_exp = []
            for i in range(0, self.dec_exp_pd.shape[0], 32):
                
                max_exp_in_chunk = np.max(self.dec_exp_pd[i:i+32])
                max_exp.append(max_exp_in_chunk)

            max_exp = np.array(max_exp).reshape(-1,1)

            expanded_max_exp = np.zeros((self.num, 1), dtype = int)
            for i in range(self.epoch):
                expanded_max_exp[i*32:(i+1)*32] = max_exp[i]

            dec_temp_shift_bit = np.where(self.udf_flag == 1, 15, expanded_max_exp - self.dec_exp_pd)
            oor_flag = np.where(dec_temp_shift_bit > 15, 1, 0)
            dec_shift_bit = np.where(dec_temp_shift_bit > 15, 15, dec_temp_shift_bit) # 이거 oor flag = 1일 때, shift bit = 15로 할까, 16으로 할까
            bin_shift_bit = np.array(self.dec_to_bin4(dec_shift_bit)).reshape(self.num, 4)
            # pdb.set_trace()
            return oor_flag, bin_shift_bit, dec_shift_bit, max_exp
        
        elif self.mode == 'fp_int':
            print('fp_int mode exp_comparator')
             
            self.dec_exp_pd = dec_exp_pd.copy()
            self.udf_flag = udf_flag.copy()
            max_exp = []
            for i in range(0, self.dec_exp_pd.shape[0], 32):
                
                max_exp_in_chunck = np.max(self.dec_exp_pd[i:i+32])
                max_exp.append(max_exp_in_chunck)
            max_exp = np.array(max_exp).reshape(-1, 1)
            
            expanded_max_exp = np.zeros((self.num,1), dtype = int)
            for i in range(self.epoch):
                expanded_max_exp[i*32:(i+1)*32] = max_exp[i]

            # max_exp = np.max(self.dec_exp_pd)
             
            dec_temp_shift_bit = np.where(self.udf_flag == 1, 15, expanded_max_exp - self.dec_exp_pd)
            oor_flag = np.where(dec_temp_shift_bit > 15, 1, 0)
            dec_shift_bit = np.where(dec_temp_shift_bit > 15, 15, dec_temp_shift_bit) # 이거 oor flag = 1일 때, shift bit = 15로 할까, 16으로 할까
            bin_shift_bit = np.array(self.dec_to_bin4(dec_shift_bit)).reshape(self.num, 4)
             
            return oor_flag, bin_shift_bit, dec_shift_bit, max_exp

    def grid_fma(self, bin_sign_pd, dec_man_a, dec_man_b, oor_flag, dec_shift_bit):
        if self.mode == 'bf_int':
            print('bf_int mode grid_fma')
            #######################################################################
            # 20240331 (Logic 수정된거 반영위한 코드 수정 test)

            bin_sign_pd3 = bin_sign_pd[:, 0:1]
            bin_sign_pd2 = bin_sign_pd[:, 1:2]
            bin_sign_pd1 = bin_sign_pd[:, 2:3]
            bin_sign_pd0 = bin_sign_pd[:, 3:4]

            dec_man_a0 = np.zeros((self.num, 1), dtype=int)
            dec_man_a1 = np.zeros((self.num, 1), dtype=int)
            dec_man_a2 = np.zeros((self.num, 1), dtype=int)
            dec_man_a3 = np.zeros((self.num, 1), dtype=int)

            dec_shift_bit0 = np.zeros((self.num, 1), dtype = int)
            dec_shift_bit1 = np.zeros((self.num, 1), dtype = int)
            dec_shift_bit2 = np.zeros((self.num, 1), dtype = int)
            dec_shift_bit3 = np.zeros((self.num, 1), dtype = int)            

            oor_flag0 = np.zeros((self.num, 1), dtype = int)
            oor_flag1 = np.zeros((self.num, 1), dtype = int)
            oor_flag2 = np.zeros((self.num, 1), dtype = int)
            oor_flag3 = np.zeros((self.num, 1), dtype = int)

            dec_man_b3 = dec_man_b[:, 0:1]
            dec_man_b2 = dec_man_b[:, 1:2]
            dec_man_b1 = dec_man_b[:, 2:3]
            dec_man_b0 = dec_man_b[:, 3:4]


             
            chunk = int(self.num/4)
            for i in range(chunk):
                dec_man_a0[4*i]   = dec_man_a[4*i]
                dec_man_a0[4*i+1] = dec_man_a[4*i]
                dec_man_a0[4*i+2] = dec_man_a[4*i]
                dec_man_a0[4*i+3] = dec_man_a[4*i]

                dec_man_a1[4*i]   = dec_man_a[4*i+1]
                dec_man_a1[4*i+1] = dec_man_a[4*i+1]
                dec_man_a1[4*i+2] = dec_man_a[4*i+1]
                dec_man_a1[4*i+3] = dec_man_a[4*i+1]

                dec_man_a2[4*i]   = dec_man_a[4*i+2]
                dec_man_a2[4*i+1] = dec_man_a[4*i+2]
                dec_man_a2[4*i+2] = dec_man_a[4*i+2]
                dec_man_a2[4*i+3] = dec_man_a[4*i+2]

                dec_man_a3[4*i]   = dec_man_a[4*i+3]
                dec_man_a3[4*i+1] = dec_man_a[4*i+3]
                dec_man_a3[4*i+2] = dec_man_a[4*i+3]
                dec_man_a3[4*i+3] = dec_man_a[4*i+3]

                # dec_Shift_bit
                dec_shift_bit0[4*i]   = dec_shift_bit[4*i]
                dec_shift_bit0[4*i+1] = dec_shift_bit[4*i]
                dec_shift_bit0[4*i+2] = dec_shift_bit[4*i]
                dec_shift_bit0[4*i+3] = dec_shift_bit[4*i]

                dec_shift_bit1[4*i]   = dec_shift_bit[4*i+1]
                dec_shift_bit1[4*i+1] = dec_shift_bit[4*i+1]
                dec_shift_bit1[4*i+2] = dec_shift_bit[4*i+1]
                dec_shift_bit1[4*i+3] = dec_shift_bit[4*i+1]

                dec_shift_bit2[4*i]   = dec_shift_bit[4*i+2]
                dec_shift_bit2[4*i+1] = dec_shift_bit[4*i+2]
                dec_shift_bit2[4*i+2] = dec_shift_bit[4*i+2]
                dec_shift_bit2[4*i+3] = dec_shift_bit[4*i+2]

                dec_shift_bit3[4*i]   = dec_shift_bit[4*i+3]
                dec_shift_bit3[4*i+1] = dec_shift_bit[4*i+3]
                dec_shift_bit3[4*i+2] = dec_shift_bit[4*i+3]
                dec_shift_bit3[4*i+3] = dec_shift_bit[4*i+3]

                # oor_Flag
                oor_flag0[4*i]   = oor_flag[4*i]
                oor_flag0[4*i+1] = oor_flag[4*i]
                oor_flag0[4*i+2] = oor_flag[4*i]
                oor_flag0[4*i+3] = oor_flag[4*i]

                oor_flag1[4*i]   = oor_flag[4*i+1]
                oor_flag1[4*i+1] = oor_flag[4*i+1]
                oor_flag1[4*i+2] = oor_flag[4*i+1]
                oor_flag1[4*i+3] = oor_flag[4*i+1]

                oor_flag2[4*i]   = oor_flag[4*i+2]
                oor_flag2[4*i+1] = oor_flag[4*i+2]
                oor_flag2[4*i+2] = oor_flag[4*i+2]
                oor_flag2[4*i+3] = oor_flag[4*i+2]

                oor_flag3[4*i]   = oor_flag[4*i+3]
                oor_flag3[4*i+1] = oor_flag[4*i+3]
                oor_flag3[4*i+2] = oor_flag[4*i+3]
                oor_flag3[4*i+3] = oor_flag[4*i+3]


            
            dec_mult0 = dec_man_a0 * dec_man_b0
            dec_mult1 = dec_man_a1 * dec_man_b1
            dec_mult2 = dec_man_a2 * dec_man_b2
            dec_mult3 = dec_man_a3 * dec_man_b3

            # dec_pad_mult0 = dec_mult0 << 5
            # dec_pad_mult1 = dec_mult1 << 5
            # dec_pad_mult2 = dec_mult2 << 5
            # dec_pad_mult3 = dec_mult3 << 5
            dec_pad_mult0 = dec_mult0 << 8
            dec_pad_mult1 = dec_mult1 << 8
            dec_pad_mult2 = dec_mult2 << 8
            dec_pad_mult3 = dec_mult3 << 8

            # dec_pad_mult0 = dec_mult0 << 4
            # dec_pad_mult1 = dec_mult1 << 4
            # dec_pad_mult2 = dec_mult2 << 4
            # dec_pad_mult3 = dec_mult3 << 4

            dec_shift0 = dec_pad_mult0 >> dec_shift_bit0
            dec_shift1 = dec_pad_mult1 >> dec_shift_bit1
            dec_shift2 = dec_pad_mult2 >> dec_shift_bit2
            dec_shift3 = dec_pad_mult3 >> dec_shift_bit3

            dec_complement0 = np.where(bin_sign_pd0 == 1, -dec_shift0, dec_shift0)
            dec_complement1 = np.where(bin_sign_pd1 == 1, -dec_shift1, dec_shift1)
            dec_complement2 = np.where(bin_sign_pd2 == 1, -dec_shift2, dec_shift2)
            dec_complement3 = np.where(bin_sign_pd3 == 1, -dec_shift3, dec_shift3)

            dec_oor_check0 = np.where(oor_flag0 == 1, 0, dec_complement0)
            dec_oor_check1 = np.where(oor_flag1 == 1, 0, dec_complement1)
            dec_oor_check2 = np.where(oor_flag2 == 1, 0, dec_complement2)
            dec_oor_check3 = np.where(oor_flag3 == 1, 0, dec_complement3)
            
            dec_oor_check = np.concatenate((dec_oor_check3, dec_oor_check2, dec_oor_check1, dec_oor_check0), axis = 1)

            dec_dout_fma_grid = np.zeros((self.num, 1), dtype = int)
            dec_second_sum = np.zeros((self.num, 1), dtype = int)

            for i in range(self.num):
                dec_dout_fma_grid[i] = np.sum(dec_oor_check[i])
                dec_second_sum[i] = np.sum(dec_oor_check0[i] + dec_oor_check1[i] + dec_oor_check2[i])
            
            
            
            # pdb.set_trace()
            dec_sum0 = np.zeros((self.epoch, 1), dtype = int)
            dec_sum1 = np.zeros((self.epoch, 1), dtype = int)
            dec_sum2 = np.zeros((self.epoch, 1), dtype = int)
            dec_sum3 = np.zeros((self.epoch, 1), dtype = int)

            dec_test_sum0 = np.zeros((self.epoch, 1), dtype = int)
            dec_test_sum1 = np.zeros((self.epoch, 1), dtype = int)
            dec_test_sum2 = np.zeros((self.epoch, 1), dtype = int)
            dec_test_sum3 = np.zeros((self.epoch, 1), dtype = int)

            for i in range(self.epoch):
                dec_sum0[i] = np.sum(dec_oor_check[32*i] + dec_oor_check[32*i+4] + dec_oor_check[32*i+8] + dec_oor_check[32*i+12] + dec_oor_check[32*i + 16] + dec_oor_check[32*i + 20] + dec_oor_check[32*i + 24] + dec_oor_check[32*i + 28]) 
                dec_sum1[i] = np.sum(dec_oor_check[32*i+1] + dec_oor_check[32*i+5] + dec_oor_check[32*i+9] + dec_oor_check[32*i+13] + dec_oor_check[32*i + 17] + dec_oor_check[32*i + 21] + dec_oor_check[32*i + 25] + dec_oor_check[32*i + 29])    
                dec_sum2[i] = np.sum(dec_oor_check[32*i+2] + dec_oor_check[32*i+6] + dec_oor_check[32*i+10] + dec_oor_check[32*i+14] + dec_oor_check[32*i + 18] + dec_oor_check[32*i + 22] + dec_oor_check[32*i + 26] + dec_oor_check[32*i + 30])
                dec_sum3[i] = np.sum(dec_oor_check[32*i+3] + dec_oor_check[32*i+7] + dec_oor_check[32*i+11] + dec_oor_check[32*i+15] + dec_oor_check[32*i + 19] + dec_oor_check[32*i + 23] + dec_oor_check[32*i + 27] + dec_oor_check[32*i + 31])
            

            for i in range(self.epoch):
                dec_test_sum0[i] = np.sum(dec_dout_fma_grid[32*i] + dec_dout_fma_grid[32*i+4] + dec_dout_fma_grid[32*i+8] + dec_dout_fma_grid[32*i+12] + dec_dout_fma_grid[32*i + 16] + dec_dout_fma_grid[32*i + 20] + dec_dout_fma_grid[32*i + 24] + dec_dout_fma_grid[32*i + 28])    
                dec_test_sum1[i] = np.sum(dec_dout_fma_grid[32*i+1] + dec_dout_fma_grid[32*i+5] + dec_dout_fma_grid[32*i+9] + dec_dout_fma_grid[32*i+13] + dec_dout_fma_grid[32*i + 17] + dec_dout_fma_grid[32*i + 21] + dec_dout_fma_grid[32*i + 25] + dec_dout_fma_grid[32*i + 29])  
                dec_test_sum2[i] = np.sum(dec_dout_fma_grid[32*i+2] + dec_dout_fma_grid[32*i+6] + dec_dout_fma_grid[32*i+10] + dec_dout_fma_grid[32*i+14] + dec_dout_fma_grid[32*i + 18] + dec_dout_fma_grid[32*i + 22] + dec_dout_fma_grid[32*i + 26] + dec_dout_fma_grid[32*i + 30]) 
                dec_test_sum3[i] = np.sum(dec_dout_fma_grid[32*i+3] + dec_dout_fma_grid[32*i+7] + dec_dout_fma_grid[32*i+11] + dec_dout_fma_grid[32*i+15] + dec_dout_fma_grid[32*i + 19] + dec_dout_fma_grid[32*i + 23] + dec_dout_fma_grid[32*i + 27] + dec_dout_fma_grid[32*i + 31]) 
            
            dec_sum_int64 = np.concatenate((dec_sum3, dec_sum2, dec_sum1, dec_sum0), axis = 1)
            dec_test_sum = np.concatenate((dec_test_sum3, dec_test_sum2, dec_test_sum1, dec_test_sum0), axis = 1)
            # pdb.set_trace() 

            # oor_flag까지 하고 summation까지 끝나면, 이 밑에 겹치는 부분은 주석 처리해주기
            #######################################################################
                
            # dec_mult = dec_man_a * dec_man_b
            # dec_mult0 = dec_mult[:, 0:1]
            # dec_mult1 = dec_mult[:, 1:2]
            # dec_mult2 = dec_mult[:, 2:3]
            # dec_mult3 = dec_mult[:, 3:4]
             
            
            
            # bin_sign0_pd = bin_sign_pd[:,0:1]
            # bin_sign1_pd = bin_sign_pd[:,1:2]
            # bin_sign2_pd = bin_sign_pd[:,2:3]
            # bin_sign3_pd = bin_sign_pd[:,3:4]
# 
            # # add 5bit pre_shift pad bit
            # dec_pad_mult = dec_mult << 5
            # dec_pad_mult0 = dec_mult[:, 0:1] << 5
            # dec_pad_mult1 = dec_mult[:, 1:2] << 5
            # dec_pad_mult2 = dec_mult[:, 2:3] << 5
            # dec_pad_mult3 = dec_mult[:, 3:4] << 5
# 
            # dec_complement0 = np.where(bin_sign0_pd == 1, -dec_pad_mult0, dec_pad_mult0)
            # dec_complement1 = np.where(bin_sign1_pd == 1, -dec_pad_mult1, dec_pad_mult0)
            # dec_complement2 = np.where(bin_sign2_pd == 1, -dec_pad_mult2, dec_pad_mult0)
            # dec_complement3 = np.where(bin_sign3_pd == 1, -dec_pad_mult3, dec_pad_mult0)
# 
            # 
# 
# 
            # # dec_invert = np.where(bin_sign_pd == 1, ~dec_mult, dec_mult)
            # dec_invert = np.where(bin_sign_pd == 1, ~dec_pad_mult, dec_pad_mult)
            # 
            # dec_invert_int16 = dec_invert.astype(np.int16)
            # dec_invert_uint16 = dec_invert.astype(np.uint16)
            # 
            # #bin_mult0 = self.dec_to_bin16(dec_mult0)
            # #bin_mult1 = self.dec_to_bin16(dec_mult1)
            # #bin_mult2 = self.dec_to_bin16(dec_mult2)
            # #bin_mult3 = self.dec_to_bin16(dec_mult3)
## 
            # # bin_complement0 = np.where(bin_sign_pd)
# 
            # 
            # # dec_complement = np.where(bin_sign_pd == 1, -dec_mult, dec_mult)
            # 
            # # dec_shift = dec_complement >> 1
            # # dec_shift = dec_invert >> dec_shift_bit
            # dec_shift = dec_invert_int16 >> dec_shift_bit
# 
            # dec_shift_int64 = dec_invert >> dec_shift_bit
            # dec_complement_int64 = np.where(bin_sign_pd == 1, dec_shift_int64 + 1, dec_shift_int64)
            # dec_oor_check_int64 = np.where(oor_flag == 1, 0, dec_complement_int64)
            # dec_sum_int64 = np.zeros((self.epoch, 4), dtype = int)
            # 
            # for i in range(self.epoch):
            #     # 이 값 사용해줄 것
            #     dec_sum_int64[i] = np.sum(dec_oor_check_int64[i*32:(i+1)*32], axis = 0)
            # 
            # dec_complement = np.where(bin_sign_pd == 1, dec_shift + 1, dec_shift)
            # dec_oor_check = np.where(oor_flag == 1, 0, dec_complement)            
            # dec_sum = np.zeros((self.epoch, 4), dtype = int)
            # for i in range(self.epoch):
            #     dec_sum[i] = np.sum(dec_oor_check[i*32:(i+1)*32], axis =0)



            return dec_sum_int64
        elif self.mode == 'bf_bf' :
            print('bf_bf mode grid_fma')
            dec_mult = dec_man_a * dec_man_b
            
            # dec_pad_mult = dec_mult << 5
            dec_pad_mult = dec_mult << 3


            dec_shift = dec_pad_mult >> dec_shift_bit
            
            dec_complement = np.where(bin_sign_pd[:,0:1] == 1, -dec_shift, dec_shift)
            

            dec_oor_check = np.where(oor_flag == 1, 0, dec_complement)
            
            dec_sum0_8_to_1 = np.zeros((self.epoch, 1), dtype = int)
            dec_sum1_8_to_1 = np.zeros((self.epoch, 1), dtype = int)
            dec_sum2_8_to_1 = np.zeros((self.epoch, 1), dtype = int)
            dec_sum3_8_to_1 = np.zeros((self.epoch, 1), dtype = int)
             
            for i in range(self.epoch):
                
                dec_sum0_8_to_1[i] = np.sum(dec_oor_check[32*i] + dec_oor_check[32*i+4] + dec_oor_check[32*i+8] + dec_oor_check[32*i+12] + dec_oor_check[32*i + 16] + dec_oor_check[32*i + 20] + dec_oor_check[32*i + 24] + dec_oor_check[32*i + 28])  
                dec_sum1_8_to_1[i] = np.sum(dec_oor_check[32*i+1] + dec_oor_check[32*i+5] + dec_oor_check[32*i+9] + dec_oor_check[32*i+13] + dec_oor_check[32*i + 17] + dec_oor_check[32*i + 21] + dec_oor_check[32*i + 25] + dec_oor_check[32*i + 29])    
                dec_sum2_8_to_1[i] = np.sum(dec_oor_check[32*i+2] + dec_oor_check[32*i+6] + dec_oor_check[32*i+10] + dec_oor_check[32*i+14] + dec_oor_check[32*i + 18] + dec_oor_check[32*i + 22] + dec_oor_check[32*i + 26] + dec_oor_check[32*i + 30])   
                dec_sum3_8_to_1[i] = np.sum(dec_oor_check[32*i+3] + dec_oor_check[32*i+7] + dec_oor_check[32*i+11] + dec_oor_check[32*i+15] + dec_oor_check[32*i + 19] + dec_oor_check[32*i + 23] + dec_oor_check[32*i + 27] + dec_oor_check[32*i + 31])   



            # pdb.set_trace()
             
            dec_sum = np.zeros((self.epoch, 1), dtype = int)
            for i in range(self.epoch):
                dec_sum[i] = np.sum(dec_oor_check[i*32:(i+1)*32])
            # pdb.set_trace()
            return dec_sum
        
        elif self.mode == 'fp_fp' :
            print('fp_fp mode grid_fma')
            dec_mult = dec_man_a * dec_man_b

            # dec_pad_mult = dec_mult << 5
            # dec_pad_mult = dec_mult << 3
            dec_pad_mult = dec_mult << 1

            # pdb.set_trace()
            dec_shift = dec_pad_mult >> dec_shift_bit
            
            dec_complement = np.where(bin_sign_pd[:,0:1] == 1, -dec_shift, dec_shift)
            

            dec_oor_check = np.where(oor_flag == 1, 0, dec_complement)
            
            dec_sum0_8_to_1 = np.zeros((self.epoch, 1), dtype = int)
            dec_sum1_8_to_1 = np.zeros((self.epoch, 1), dtype = int)
            dec_sum2_8_to_1 = np.zeros((self.epoch, 1), dtype = int)
            dec_sum3_8_to_1 = np.zeros((self.epoch, 1), dtype = int)
             
            for i in range(self.epoch):
                
                dec_sum0_8_to_1[i] = np.sum(dec_oor_check[32*i] + dec_oor_check[32*i+4] + dec_oor_check[32*i+8] + dec_oor_check[32*i+12] + dec_oor_check[32*i + 16] + dec_oor_check[32*i + 20] + dec_oor_check[32*i + 24] + dec_oor_check[32*i + 28])  
                dec_sum1_8_to_1[i] = np.sum(dec_oor_check[32*i+1] + dec_oor_check[32*i+5] + dec_oor_check[32*i+9] + dec_oor_check[32*i+13] + dec_oor_check[32*i + 17] + dec_oor_check[32*i + 21] + dec_oor_check[32*i + 25] + dec_oor_check[32*i + 29])    
                dec_sum2_8_to_1[i] = np.sum(dec_oor_check[32*i+2] + dec_oor_check[32*i+6] + dec_oor_check[32*i+10] + dec_oor_check[32*i+14] + dec_oor_check[32*i + 18] + dec_oor_check[32*i + 22] + dec_oor_check[32*i + 26] + dec_oor_check[32*i + 30])   
                dec_sum3_8_to_1[i] = np.sum(dec_oor_check[32*i+3] + dec_oor_check[32*i+7] + dec_oor_check[32*i+11] + dec_oor_check[32*i+15] + dec_oor_check[32*i + 19] + dec_oor_check[32*i + 23] + dec_oor_check[32*i + 27] + dec_oor_check[32*i + 31])   



            # pdb.set_trace()
             
            dec_sum = np.zeros((self.epoch, 1), dtype = int)
            for i in range(self.epoch):
                dec_sum[i] = np.sum(dec_oor_check[i*32:(i+1)*32])
            # pdb.set_trace()
            return dec_sum
        
        elif self.mode == 'fp_int':
            print('fp_int mode grid_fma')
            #######################################################################
            # 20240331 (Logic 수정된거 반영위한 코드 수정 test)

            bin_sign_pd3 = bin_sign_pd[:, 0:1]
            bin_sign_pd2 = bin_sign_pd[:, 1:2]
            bin_sign_pd1 = bin_sign_pd[:, 2:3]
            bin_sign_pd0 = bin_sign_pd[:, 3:4]

            dec_man_a0 = np.zeros((self.num, 1), dtype=int)
            dec_man_a1 = np.zeros((self.num, 1), dtype=int)
            dec_man_a2 = np.zeros((self.num, 1), dtype=int)
            dec_man_a3 = np.zeros((self.num, 1), dtype=int)

            dec_shift_bit0 = np.zeros((self.num, 1), dtype = int)
            dec_shift_bit1 = np.zeros((self.num, 1), dtype = int)
            dec_shift_bit2 = np.zeros((self.num, 1), dtype = int)
            dec_shift_bit3 = np.zeros((self.num, 1), dtype = int)            

            oor_flag0 = np.zeros((self.num, 1), dtype = int)
            oor_flag1 = np.zeros((self.num, 1), dtype = int)
            oor_flag2 = np.zeros((self.num, 1), dtype = int)
            oor_flag3 = np.zeros((self.num, 1), dtype = int)

            dec_man_b3 = dec_man_b[:, 0:1]
            dec_man_b2 = dec_man_b[:, 1:2]
            dec_man_b1 = dec_man_b[:, 2:3]
            dec_man_b0 = dec_man_b[:, 3:4]


             
            chunk = int(self.num/4)
            for i in range(chunk):
                dec_man_a0[4*i]   = dec_man_a[4*i]
                dec_man_a0[4*i+1] = dec_man_a[4*i]
                dec_man_a0[4*i+2] = dec_man_a[4*i]
                dec_man_a0[4*i+3] = dec_man_a[4*i]

                dec_man_a1[4*i]   = dec_man_a[4*i+1]
                dec_man_a1[4*i+1] = dec_man_a[4*i+1]
                dec_man_a1[4*i+2] = dec_man_a[4*i+1]
                dec_man_a1[4*i+3] = dec_man_a[4*i+1]

                dec_man_a2[4*i]   = dec_man_a[4*i+2]
                dec_man_a2[4*i+1] = dec_man_a[4*i+2]
                dec_man_a2[4*i+2] = dec_man_a[4*i+2]
                dec_man_a2[4*i+3] = dec_man_a[4*i+2]

                dec_man_a3[4*i]   = dec_man_a[4*i+3]
                dec_man_a3[4*i+1] = dec_man_a[4*i+3]
                dec_man_a3[4*i+2] = dec_man_a[4*i+3]
                dec_man_a3[4*i+3] = dec_man_a[4*i+3]

                # dec_Shift_bit
                dec_shift_bit0[4*i]   = dec_shift_bit[4*i]
                dec_shift_bit0[4*i+1] = dec_shift_bit[4*i]
                dec_shift_bit0[4*i+2] = dec_shift_bit[4*i]
                dec_shift_bit0[4*i+3] = dec_shift_bit[4*i]

                dec_shift_bit1[4*i]   = dec_shift_bit[4*i+1]
                dec_shift_bit1[4*i+1] = dec_shift_bit[4*i+1]
                dec_shift_bit1[4*i+2] = dec_shift_bit[4*i+1]
                dec_shift_bit1[4*i+3] = dec_shift_bit[4*i+1]

                dec_shift_bit2[4*i]   = dec_shift_bit[4*i+2]
                dec_shift_bit2[4*i+1] = dec_shift_bit[4*i+2]
                dec_shift_bit2[4*i+2] = dec_shift_bit[4*i+2]
                dec_shift_bit2[4*i+3] = dec_shift_bit[4*i+2]

                dec_shift_bit3[4*i]   = dec_shift_bit[4*i+3]
                dec_shift_bit3[4*i+1] = dec_shift_bit[4*i+3]
                dec_shift_bit3[4*i+2] = dec_shift_bit[4*i+3]
                dec_shift_bit3[4*i+3] = dec_shift_bit[4*i+3]

                # oor_Flag
                oor_flag0[4*i]   = oor_flag[4*i]
                oor_flag0[4*i+1] = oor_flag[4*i]
                oor_flag0[4*i+2] = oor_flag[4*i]
                oor_flag0[4*i+3] = oor_flag[4*i]

                oor_flag1[4*i]   = oor_flag[4*i+1]
                oor_flag1[4*i+1] = oor_flag[4*i+1]
                oor_flag1[4*i+2] = oor_flag[4*i+1]
                oor_flag1[4*i+3] = oor_flag[4*i+1]

                oor_flag2[4*i]   = oor_flag[4*i+2]
                oor_flag2[4*i+1] = oor_flag[4*i+2]
                oor_flag2[4*i+2] = oor_flag[4*i+2]
                oor_flag2[4*i+3] = oor_flag[4*i+2]

                oor_flag3[4*i]   = oor_flag[4*i+3]
                oor_flag3[4*i+1] = oor_flag[4*i+3]
                oor_flag3[4*i+2] = oor_flag[4*i+3]
                oor_flag3[4*i+3] = oor_flag[4*i+3]


            
            dec_mult0 = dec_man_a0 * dec_man_b0
            dec_mult1 = dec_man_a1 * dec_man_b1
            dec_mult2 = dec_man_a2 * dec_man_b2
            dec_mult3 = dec_man_a3 * dec_man_b3
            ########################################################################
            # PAD_BIT_TEST!!!!! ####################################################
            # pad_bit = 5
            # dec_pad_mult0 = dec_mult0 << 5
            # dec_pad_mult1 = dec_mult1 << 5
            # dec_pad_mult2 = dec_mult2 << 5
            # dec_pad_mult3 = dec_mult3 << 5
            # pad_bit = 6
            dec_pad_mult0 = dec_mult0 << 6
            dec_pad_mult1 = dec_mult1 << 6
            dec_pad_mult2 = dec_mult2 << 6
            dec_pad_mult3 = dec_mult3 << 6
            # pad_bit = 7
            # dec_pad_mult0 = dec_mult0 << 7
            # dec_pad_mult1 = dec_mult1 << 7
            # dec_pad_mult2 = dec_mult2 << 7
            # dec_pad_mult3 = dec_mult3 << 7
            # pad_bit = 8
            # dec_pad_mult0 = dec_mult0 << 8
            # dec_pad_mult1 = dec_mult1 << 8
            # dec_pad_mult2 = dec_mult2 << 8
            # dec_pad_mult3 = dec_mult3 << 8
            # pad_bit = 9
            # dec_pad_mult0 = dec_mult0 << 9
            # dec_pad_mult1 = dec_mult1 << 9
            # dec_pad_mult2 = dec_mult2 << 9
            # dec_pad_mult3 = dec_mult3 << 9
            # pad_bit = 10
            # dec_pad_mult0 = dec_mult0 << 10
            # dec_pad_mult1 = dec_mult1 << 10
            # dec_pad_mult2 = dec_mult2 << 10
            # dec_pad_mult3 = dec_mult3 << 10
            # pad_bit = 12
            # dec_pad_mult0 = dec_mult0 << 12
            # dec_pad_mult1 = dec_mult1 << 12
            # dec_pad_mult2 = dec_mult2 << 12
            # dec_pad_mult3 = dec_mult3 << 12
            # pad_bit = 13
            # dec_pad_mult0 = dec_mult0 << 13
            # dec_pad_mult1 = dec_mult1 << 13
            # dec_pad_mult2 = dec_mult2 << 13
            # dec_pad_mult3 = dec_mult3 << 13
            # pad_bit = 14
            # dec_pad_mult0 = dec_mult0 << 14
            # dec_pad_mult1 = dec_mult1 << 14
            # dec_pad_mult2 = dec_mult2 << 14
            # dec_pad_mult3 = dec_mult3 << 14
            # pad_bit = 15
            # dec_pad_mult0 = dec_mult0 << 15
            # dec_pad_mult1 = dec_mult1 << 15
            # dec_pad_mult2 = dec_mult2 << 15
            # dec_pad_mult3 = dec_mult3 << 15
            ########################################################################
            ########################################################################
            # pdb.set_trace()

            dec_shift0 = dec_pad_mult0 >> dec_shift_bit0
            dec_shift1 = dec_pad_mult1 >> dec_shift_bit1
            dec_shift2 = dec_pad_mult2 >> dec_shift_bit2
            dec_shift3 = dec_pad_mult3 >> dec_shift_bit3

            dec_complement0 = np.where(bin_sign_pd0 == 1, -dec_shift0, dec_shift0)
            dec_complement1 = np.where(bin_sign_pd1 == 1, -dec_shift1, dec_shift1)
            dec_complement2 = np.where(bin_sign_pd2 == 1, -dec_shift2, dec_shift2)
            dec_complement3 = np.where(bin_sign_pd3 == 1, -dec_shift3, dec_shift3)

            dec_oor_check0 = np.where(oor_flag0 == 1, 0, dec_complement0)
            dec_oor_check1 = np.where(oor_flag1 == 1, 0, dec_complement1)
            dec_oor_check2 = np.where(oor_flag2 == 1, 0, dec_complement2)
            dec_oor_check3 = np.where(oor_flag3 == 1, 0, dec_complement3)
            
            dec_oor_check = np.concatenate((dec_oor_check3, dec_oor_check2, dec_oor_check1, dec_oor_check0), axis = 1)
            # dec_oor_check는 각 group에서 r_sfhit만 나온 녀석들
            dec_dout_fma_grid = np.zeros((self.num, 1), dtype = int)
            dec_second_sum = np.zeros((self.num, 1), dtype = int)

            for i in range(self.num):
                dec_dout_fma_grid[i] = np.sum(dec_oor_check[i])
                dec_second_sum[i] = np.sum(dec_oor_check0[i] + dec_oor_check1[i] + dec_oor_check2[i])
            
            
            
            # pdb.set_trace()
            dec_sum0 = np.zeros((self.epoch, 1), dtype = int)
            dec_sum1 = np.zeros((self.epoch, 1), dtype = int)
            dec_sum2 = np.zeros((self.epoch, 1), dtype = int)
            dec_sum3 = np.zeros((self.epoch, 1), dtype = int)

            dec_test_sum0 = np.zeros((self.epoch, 1), dtype = int)
            dec_test_sum1 = np.zeros((self.epoch, 1), dtype = int)
            dec_test_sum2 = np.zeros((self.epoch, 1), dtype = int)
            dec_test_sum3 = np.zeros((self.epoch, 1), dtype = int)

            for i in range(self.epoch):
                dec_sum0[i] = np.sum(dec_oor_check[32*i] + dec_oor_check[32*i+4] + dec_oor_check[32*i+8] + dec_oor_check[32*i+12] + dec_oor_check[32*i + 16] + dec_oor_check[32*i + 20] + dec_oor_check[32*i + 24] + dec_oor_check[32*i + 28]) 
                dec_sum1[i] = np.sum(dec_oor_check[32*i+1] + dec_oor_check[32*i+5] + dec_oor_check[32*i+9] + dec_oor_check[32*i+13] + dec_oor_check[32*i + 17] + dec_oor_check[32*i + 21] + dec_oor_check[32*i + 25] + dec_oor_check[32*i + 29])    
                dec_sum2[i] = np.sum(dec_oor_check[32*i+2] + dec_oor_check[32*i+6] + dec_oor_check[32*i+10] + dec_oor_check[32*i+14] + dec_oor_check[32*i + 18] + dec_oor_check[32*i + 22] + dec_oor_check[32*i + 26] + dec_oor_check[32*i + 30])
                dec_sum3[i] = np.sum(dec_oor_check[32*i+3] + dec_oor_check[32*i+7] + dec_oor_check[32*i+11] + dec_oor_check[32*i+15] + dec_oor_check[32*i + 19] + dec_oor_check[32*i + 23] + dec_oor_check[32*i + 27] + dec_oor_check[32*i + 31])
            

            for i in range(self.epoch):
                dec_test_sum0[i] = np.sum(dec_dout_fma_grid[32*i] + dec_dout_fma_grid[32*i+4] + dec_dout_fma_grid[32*i+8] + dec_dout_fma_grid[32*i+12] + dec_dout_fma_grid[32*i + 16] + dec_dout_fma_grid[32*i + 20] + dec_dout_fma_grid[32*i + 24] + dec_dout_fma_grid[32*i + 28])    
                dec_test_sum1[i] = np.sum(dec_dout_fma_grid[32*i+1] + dec_dout_fma_grid[32*i+5] + dec_dout_fma_grid[32*i+9] + dec_dout_fma_grid[32*i+13] + dec_dout_fma_grid[32*i + 17] + dec_dout_fma_grid[32*i + 21] + dec_dout_fma_grid[32*i + 25] + dec_dout_fma_grid[32*i + 29])  
                dec_test_sum2[i] = np.sum(dec_dout_fma_grid[32*i+2] + dec_dout_fma_grid[32*i+6] + dec_dout_fma_grid[32*i+10] + dec_dout_fma_grid[32*i+14] + dec_dout_fma_grid[32*i + 18] + dec_dout_fma_grid[32*i + 22] + dec_dout_fma_grid[32*i + 26] + dec_dout_fma_grid[32*i + 30]) 
                dec_test_sum3[i] = np.sum(dec_dout_fma_grid[32*i+3] + dec_dout_fma_grid[32*i+7] + dec_dout_fma_grid[32*i+11] + dec_dout_fma_grid[32*i+15] + dec_dout_fma_grid[32*i + 19] + dec_dout_fma_grid[32*i + 23] + dec_dout_fma_grid[32*i + 27] + dec_dout_fma_grid[32*i + 31]) 
            
            dec_sum_int64 = np.concatenate((dec_sum3, dec_sum2, dec_sum1, dec_sum0), axis = 1)
            dec_test_sum = np.concatenate((dec_test_sum3, dec_test_sum2, dec_test_sum1, dec_test_sum0), axis = 1)
            # pdb.set_trace() 

            # dec_sum_int64는 add_8_to_1 통과한 녀석


            return dec_sum_int64
        

    def complement(self, dec_sum):
        # I think this function is only extract final_sign bit
        if self.mode == 'bf_int':
            print('bf_int mode complement')
            bin_sign_final = np.where(dec_sum >= 0, 0, 1)
            dec_complement = np.where(bin_sign_final == 1, -dec_sum, dec_sum)

             
            return bin_sign_final, dec_complement
        elif self.mode == 'bf_bf':
            print('bf_bf mode complement')
            bin_sign_final = np.where(dec_sum >= 0, 0, 1)
            dec_complement = np.where(bin_sign_final == 1, -dec_sum, dec_sum)
            
            return bin_sign_final, dec_complement
        
        elif self.mode == 'fp_fp':
            print('fp_fp mode complement')
            bin_sign_final = np.where(dec_sum >= 0, 0, 1)
            dec_complement = np.where(bin_sign_final == 1, -dec_sum, dec_sum)
            
            return bin_sign_final, dec_complement
        
        elif self.mode == 'fp_int':
            print('fp_int mode complement')
            bin_sign_final = np.where(dec_sum >= 0, 0, 1)
            dec_complement = np.where(bin_sign_final == 1, -dec_sum, dec_sum)
        
            return bin_sign_final, dec_complement
        
    def pre_norm(self, dec_complement):
        if self.mode == 'bf_int':
            print('bf_int mode pre_norm')
            dec_complement0 = dec_complement[:, 0:1]
            dec_complement1 = dec_complement[:, 1:2]
            dec_complement2 = dec_complement[:, 2:3]
            dec_complement3 = dec_complement[:, 3:]
            bin_complement0 = np.array(self.dec_to_bin25(dec_complement0)).reshape(-1, 25)
            bin_complement1 = np.array(self.dec_to_bin25(dec_complement1)).reshape(-1, 25)
            bin_complement2 = np.array(self.dec_to_bin25(dec_complement2)).reshape(-1, 25)
            bin_complement3 = np.array(self.dec_to_bin25(dec_complement3)).reshape(-1, 25)

            bin_pre_norm0 = np.zeros((self.epoch, 16), dtype = int)
            bin_pre_norm1 = np.zeros((self.epoch, 16), dtype = int)
            bin_pre_norm2 = np.zeros((self.epoch, 16), dtype = int)
            bin_pre_norm3 = np.zeros((self.epoch, 16), dtype = int)

            dec_pre_norm_exp0 = np.zeros((self.epoch, 1), dtype = int)
            dec_pre_norm_exp1 = np.zeros((self.epoch, 1), dtype = int)
            dec_pre_norm_exp2 = np.zeros((self.epoch, 1), dtype = int)
            dec_pre_norm_exp3 = np.zeros((self.epoch, 1), dtype = int)

            for i in range(self.epoch):
                # bin_pre_norm0_w = []
                if bin_complement0[i][4] == 1:
                    bin_pre_norm0[i] = bin_complement0[i][4:20]
                    dec_pre_norm_exp0[i] = 8
                elif bin_complement0[i][5] == 1:
                    bin_pre_norm0[i] = bin_complement0[i][5:21]
                    dec_pre_norm_exp0[i] = 7
                elif bin_complement0[i][6] == 1:
                    bin_pre_norm0[i] = bin_complement0[i][6:22]
                    dec_pre_norm_exp0[i] = 6
                elif bin_complement0[i][7] == 1:
                    bin_pre_norm0[i] = bin_complement0[i][7:23]
                    dec_pre_norm_exp0[i] = 5
                elif bin_complement0[i][8] == 1:
                    bin_pre_norm0[i] = bin_complement0[i][8:24]
                    dec_pre_norm_exp0[i] = 4
                else:
                    bin_pre_norm0[i] = bin_complement0[i][9:25]
                    dec_pre_norm_exp0[i] = 3
            
            for i in range(self.epoch):
                if bin_complement1[i][4] == 1:
                    bin_pre_norm1[i] = bin_complement1[i][4:20]
                    dec_pre_norm_exp1[i] = 8
                elif bin_complement1[i][5] == 1:
                    bin_pre_norm1[i] = bin_complement1[i][5:21]
                    dec_pre_norm_exp1[i] = 7
                elif bin_complement1[i][6] == 1:
                    bin_pre_norm1[i] = bin_complement1[i][6:22]
                    dec_pre_norm_exp1[i] = 6
                elif bin_complement1[i][7] == 1:
                    bin_pre_norm1[i] = bin_complement1[i][7:23]
                    dec_pre_norm_exp1[i] = 5
                elif bin_complement1[i][8] == 1:
                    bin_pre_norm1[i] = bin_complement1[i][8:24]
                    dec_pre_norm_exp1[i] = 4
                else:
                    bin_pre_norm1[i] = bin_complement1[i][9:25]
                    dec_pre_norm_exp1[i] = 3
                
            
            for i in range(self.epoch):
                if bin_complement2[i][4] == 1:
                    bin_pre_norm2[i] = bin_complement2[i][4:20]
                    dec_pre_norm_exp2[i] = 8
                elif bin_complement2[i][5] == 1:
                    bin_pre_norm2[i] = bin_complement2[i][5:21]
                    dec_pre_norm_exp2[i] = 7
                elif bin_complement2[i][6] == 1:
                    bin_pre_norm2[i] = bin_complement2[i][6:22]
                    dec_pre_norm_exp2[i] = 6
                elif bin_complement2[i][7] == 1:
                    bin_pre_norm2[i] = bin_complement2[i][7:23]
                    dec_pre_norm_exp2[i] = 5
                elif bin_complement2[i][8] == 1:
                    bin_pre_norm2[i] = bin_complement2[i][8:24]
                    dec_pre_norm_exp2[i] = 4
                else:
                    bin_pre_norm2[i] = bin_complement2[i][9:25]
                    dec_pre_norm_exp2[i] = 3
                
            for i in range(self.epoch):
                if bin_complement3[i][4] == 1:
                    bin_pre_norm3[i] = bin_complement3[i][4:20]
                    dec_pre_norm_exp3[i] = 8
                elif bin_complement3[i][5] == 1:
                    bin_pre_norm3[i] = bin_complement3[i][5:21]
                    dec_pre_norm_exp3[i] = 7
                elif bin_complement3[i][6] == 1:
                    bin_pre_norm3[i] = bin_complement3[i][6:22]
                    dec_pre_norm_exp3[i] = 6
                elif bin_complement3[i][7] == 1:
                    bin_pre_norm3[i] = bin_complement3[i][7:23]
                    dec_pre_norm_exp3[i] = 5
                elif bin_complement3[i][8] == 1:
                    bin_pre_norm3[i] = bin_complement3[i][8:24]
                    dec_pre_norm_exp3[i] = 4
                else:
                    bin_pre_norm3[i] = bin_complement3[i][9:25]
                    dec_pre_norm_exp3[i] = 3
            
            dec_pre_norm0 = np.array(self.bin_to_dec(bin_pre_norm0)).reshape(-1, 1)
            dec_pre_norm1 = np.array(self.bin_to_dec(bin_pre_norm1)).reshape(-1, 1)
            dec_pre_norm2 = np.array(self.bin_to_dec(bin_pre_norm2)).reshape(-1, 1)
            dec_pre_norm3 = np.array(self.bin_to_dec(bin_pre_norm3)).reshape(-1, 1)

            dec_pre_norm = np.concatenate((dec_pre_norm0, dec_pre_norm1, dec_pre_norm2, dec_pre_norm3), axis = 1)

            dec_pre_norm_exp = np.concatenate((dec_pre_norm_exp0, dec_pre_norm_exp1, dec_pre_norm_exp2, dec_pre_norm_exp3), axis = 1)
            

            return dec_pre_norm, bin_pre_norm0, bin_pre_norm1, bin_pre_norm2, bin_pre_norm3, dec_pre_norm_exp
                
            
            
    # def norm(self, dec_pre_norm, bin_pre_norm0, bin_pre_norm1, bin_pre_norm2, bin_pre_norm3):
    def norm(self, dec_complement):
        if self.mode == 'bf_int':
            print('bf_int mode norm')
            
            dec_complement3 = dec_complement[:, 0:1]
            dec_complement2 = dec_complement[:, 1:2]
            dec_complement1 = dec_complement[:, 2:3]
            dec_complement0 = dec_complement[:, 3:]

            bin_complement3 = np.array(self.dec_to_bin24(dec_complement3)).reshape(-1, 24)
            bin_complement2 = np.array(self.dec_to_bin24(dec_complement2)).reshape(-1, 24)
            bin_complement1 = np.array(self.dec_to_bin24(dec_complement1)).reshape(-1, 24)
            bin_complement0 = np.array(self.dec_to_bin24(dec_complement0)).reshape(-1, 24)

            


            # dec_norm = dec_pre_norm - 15
            # bin_norm0 = np.zeros((self.epoch, 16), dtype = int)
            # bin_norm1 = np.zeros((self.epoch, 16), dtype = int)
            # bin_norm2 = np.zeros((self.epoch, 16), dtype = int)
            # bin_norm3 = np.zeros((self.epoch, 16), dtype = int)
            bin_norm0 = np.zeros((self.epoch, 24), dtype = int)
            bin_norm1 = np.zeros((self.epoch, 24), dtype = int)
            bin_norm2 = np.zeros((self.epoch, 24), dtype = int)
            bin_norm3 = np.zeros((self.epoch, 24), dtype = int)

            dec_norm_exp0 = np.zeros((self.epoch, 1), dtype = int)
            dec_norm_exp1 = np.zeros((self.epoch, 1), dtype = int)
            dec_norm_exp2 = np.zeros((self.epoch, 1), dtype = int)
            dec_norm_exp3 = np.zeros((self.epoch, 1), dtype = int)

            # test = np.concatenate((np.array(bin_pre_norm0[0][1:]).reshape(1,-1), np.zeros((1, 1), dtype = int)), axis = -1)
            for i in range(self.epoch):
                if bin_complement0[i][0] == 1:
                    bin_norm0[i] = bin_complement0[i]
                    dec_norm_exp0[i] = 0
                elif bin_complement0[i][1] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][1:]).reshape(1,-1), np.zeros((1, 1), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 1
                elif bin_complement0[i][2] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][2:]).reshape(1,-1), np.zeros((1, 2), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 2
                elif bin_complement0[i][3] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][3:]).reshape(1,-1), np.zeros((1, 3), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 3
                elif bin_complement0[i][4] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][4:]).reshape(1,-1), np.zeros((1, 4), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 4
                elif bin_complement0[i][5] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][5:]).reshape(1,-1), np.zeros((1, 5), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 5
                elif bin_complement0[i][6] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][6:]).reshape(1,-1), np.zeros((1, 6), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 6
                elif bin_complement0[i][7] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][7:]).reshape(1,-1), np.zeros((1, 7), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 7
                elif bin_complement0[i][8] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][8:]).reshape(1,-1), np.zeros((1, 8), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 8
                elif bin_complement0[i][9] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][9:]).reshape(1,-1), np.zeros((1, 9), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 9
                elif bin_complement0[i][10] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][10:]).reshape(1,-1), np.zeros((1, 10), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 10
                elif bin_complement0[i][11] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][11:]).reshape(1,-1), np.zeros((1, 11), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 11
                elif bin_complement0[i][12] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][12:]).reshape(1,-1), np.zeros((1, 12), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 12
                elif bin_complement0[i][13] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][13:]).reshape(1,-1), np.zeros((1, 13), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 13
                elif bin_complement0[i][14] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][14:]).reshape(1,-1), np.zeros((1, 14), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 14
                elif bin_complement0[i][15] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][15:]).reshape(1,-1), np.zeros((1, 15), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 15
                elif bin_complement0[i][16] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][16:]).reshape(1,-1), np.zeros((1, 16), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 16   
                elif bin_complement0[i][17] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][17:]).reshape(1,-1), np.zeros((1, 17), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 17
                elif bin_complement0[i][18] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][18:]).reshape(1,-1), np.zeros((1, 18), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 18
                elif bin_complement0[i][19] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][19:]).reshape(1,-1), np.zeros((1, 19), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 19
                elif bin_complement0[i][20] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][20:]).reshape(1,-1), np.zeros((1, 20), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 20
                elif bin_complement0[i][21] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][21:]).reshape(1,-1), np.zeros((1, 21), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 21
                elif bin_complement0[i][22] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][22:]).reshape(1,-1), np.zeros((1, 22), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 22
                elif bin_complement0[i][23] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][23:]).reshape(1,-1), np.zeros((1, 23), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 23
                elif bin_complement0[i][24] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][24:]).reshape(1,-1), np.zeros((1, 24), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 24
                else:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][25:]).reshape(1,-1), np.zeros((1, 25), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 25            

            for i in range(self.epoch):
                if bin_complement1[i][0] == 1:
                    bin_norm1[i] = bin_complement1[i]
                    dec_norm_exp1[i] = 0
                elif bin_complement1[i][1] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][1:]).reshape(1,-1), np.zeros((1, 1), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 1
                elif bin_complement1[i][2] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][2:]).reshape(1,-1), np.zeros((1, 2), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 2
                elif bin_complement1[i][3] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][3:]).reshape(1,-1), np.zeros((1, 3), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 3
                elif bin_complement1[i][4] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][4:]).reshape(1,-1), np.zeros((1, 4), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 4
                elif bin_complement1[i][5] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][5:]).reshape(1,-1), np.zeros((1, 5), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 5
                elif bin_complement1[i][6] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][6:]).reshape(1,-1), np.zeros((1, 6), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 6
                elif bin_complement1[i][7] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][7:]).reshape(1,-1), np.zeros((1, 7), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 7
                elif bin_complement1[i][8] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][8:]).reshape(1,-1), np.zeros((1, 8), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 8
                elif bin_complement1[i][9] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][9:]).reshape(1,-1), np.zeros((1, 9), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 9
                elif bin_complement1[i][10] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][10:]).reshape(1,-1), np.zeros((1, 10), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 10
                elif bin_complement1[i][11] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][11:]).reshape(1,-1), np.zeros((1, 11), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 11
                elif bin_complement1[i][12] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][12:]).reshape(1,-1), np.zeros((1, 12), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 12
                elif bin_complement1[i][13] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][13:]).reshape(1,-1), np.zeros((1, 13), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 13
                elif bin_complement1[i][14] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][14:]).reshape(1,-1), np.zeros((1, 14), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 14
                elif bin_complement1[i][15] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][15:]).reshape(1,-1), np.zeros((1, 15), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 15
                elif bin_complement1[i][16] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][16:]).reshape(1,-1), np.zeros((1, 16), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 16
                elif bin_complement1[i][17] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][17:]).reshape(1,-1), np.zeros((1, 17), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 17
                elif bin_complement1[i][18] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][18:]).reshape(1,-1), np.zeros((1, 18), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 18
                elif bin_complement1[i][19] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][19:]).reshape(1,-1), np.zeros((1, 19), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 19
                elif bin_complement1[i][20] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][20:]).reshape(1,-1), np.zeros((1, 20), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 20
                elif bin_complement1[i][21] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][21:]).reshape(1,-1), np.zeros((1, 21), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 21
                elif bin_complement1[i][22] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][22:]).reshape(1,-1), np.zeros((1, 22), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 22
                elif bin_complement1[i][23] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][23:]).reshape(1,-1), np.zeros((1, 23), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 23
                elif bin_complement1[i][24] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][24:]).reshape(1,-1), np.zeros((1, 24), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 24
                else:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][25:]).reshape(1,-1), np.zeros((1, 25), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 25



            for i in range(self.epoch):
                if bin_complement2[i][0] == 1:
                    bin_norm2[i] = bin_complement2[i]
                    dec_norm_exp2[i] = 0
                elif bin_complement2[i][1] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][1:]).reshape(1,-1), np.zeros((1, 1), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 1
                elif bin_complement2[i][2] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][2:]).reshape(1,-1), np.zeros((1, 2), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 2
                elif bin_complement2[i][3] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][3:]).reshape(1,-1), np.zeros((1, 3), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 3
                elif bin_complement2[i][4] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][4:]).reshape(1,-1), np.zeros((1, 4), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 4
                elif bin_complement2[i][5] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][5:]).reshape(1,-1), np.zeros((1, 5), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 5
                elif bin_complement2[i][6] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][6:]).reshape(1,-1), np.zeros((1, 6), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 6
                elif bin_complement2[i][7] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][7:]).reshape(1,-1), np.zeros((1, 7), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 7
                elif bin_complement2[i][8] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][8:]).reshape(1,-1), np.zeros((1, 8), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 8
                elif bin_complement2[i][9] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][9:]).reshape(1,-1), np.zeros((1, 9), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 9
                elif bin_complement2[i][10] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][10:]).reshape(1,-1), np.zeros((1, 10), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 10
                elif bin_complement2[i][11] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][11:]).reshape(1,-1), np.zeros((1, 11), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 11
                elif bin_complement2[i][12] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][12:]).reshape(1,-1), np.zeros((1, 12), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 12
                elif bin_complement2[i][13] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][13:]).reshape(1,-1), np.zeros((1, 13), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 13
                elif bin_complement2[i][14] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][14:]).reshape(1,-1), np.zeros((1, 14), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 14
                elif bin_complement2[i][15] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][15:]).reshape(1,-1), np.zeros((1, 15), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 15
                elif bin_complement2[i][16] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][16:]).reshape(1,-1), np.zeros((1, 16), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 16
                elif bin_complement2[i][17] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][17:]).reshape(1,-1), np.zeros((1, 17), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 17
                elif bin_complement2[i][18] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][18:]).reshape(1,-1), np.zeros((1, 18), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 18
                elif bin_complement2[i][19] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][19:]).reshape(1,-1), np.zeros((1, 19), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 19
                elif bin_complement2[i][20] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][20:]).reshape(1,-1), np.zeros((1, 20), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 20
                elif bin_complement2[i][21] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][21:]).reshape(1,-1), np.zeros((1, 21), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 21
                elif bin_complement2[i][22] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][22:]).reshape(1,-1), np.zeros((1, 22), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 22
                elif bin_complement2[i][23] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][23:]).reshape(1,-1), np.zeros((1, 23), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 23
                elif bin_complement2[i][24] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][24:]).reshape(1,-1), np.zeros((1, 24), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 24
                else:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][25:]).reshape(1,-1), np.zeros((1, 25), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 25
                

                # Todo)
                


            for i in range(self.epoch):
                if bin_complement3[i][0] == 1:
                    bin_norm3[i] = bin_complement3[i]
                    dec_norm_exp3[i] = 0
                elif bin_complement3[i][1] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][1:]).reshape(1,-1), np.zeros((1, 1), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 1
                elif bin_complement3[i][2] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][2:]).reshape(1,-1), np.zeros((1, 2), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 2
                elif bin_complement3[i][3] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][3:]).reshape(1,-1), np.zeros((1, 3), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 3
                elif bin_complement3[i][4] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][4:]).reshape(1,-1), np.zeros((1, 4), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 4
                elif bin_complement3[i][5] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][5:]).reshape(1,-1), np.zeros((1, 5), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 5
                elif bin_complement3[i][6] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][6:]).reshape(1,-1), np.zeros((1, 6), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 6
                elif bin_complement3[i][7] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][7:]).reshape(1,-1), np.zeros((1, 7), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 7
                elif bin_complement3[i][8] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][8:]).reshape(1,-1), np.zeros((1, 8), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 8
                elif bin_complement3[i][9] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][9:]).reshape(1,-1), np.zeros((1, 9), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 9
                elif bin_complement3[i][10] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][10:]).reshape(1,-1), np.zeros((1, 10), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 10
                elif bin_complement3[i][11] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][11:]).reshape(1,-1), np.zeros((1, 11), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 11
                elif bin_complement3[i][12] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][12:]).reshape(1,-1), np.zeros((1, 12), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 12
                elif bin_complement3[i][13] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][13:]).reshape(1,-1), np.zeros((1, 13), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 13
                elif bin_complement3[i][14] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][14:]).reshape(1,-1), np.zeros((1, 14), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 14
                elif bin_complement3[i][15] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][15:]).reshape(1,-1), np.zeros((1, 15), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 15
                elif bin_complement3[i][16] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][16:]).reshape(1,-1), np.zeros((1, 16), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 16
                elif bin_complement3[i][17] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][17:]).reshape(1,-1), np.zeros((1, 17), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 17
                elif bin_complement3[i][18] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][18:]).reshape(1,-1), np.zeros((1, 18), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 18
                elif bin_complement3[i][19] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][19:]).reshape(1,-1), np.zeros((1, 19), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 19
                elif bin_complement3[i][20] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][20:]).reshape(1,-1), np.zeros((1, 20), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 20
                elif bin_complement3[i][21] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][21:]).reshape(1,-1), np.zeros((1, 21), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 21
                elif bin_complement3[i][22] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][22:]).reshape(1,-1), np.zeros((1, 22), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 22
                elif bin_complement3[i][23] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][23:]).reshape(1,-1), np.zeros((1, 23), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 23
                elif bin_complement3[i][24] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][24:]).reshape(1,-1), np.zeros((1, 24), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 24

             

            dec_norm_exp = np.concatenate((dec_norm_exp0, dec_norm_exp1, dec_norm_exp2, dec_norm_exp3), axis = 1)

            return dec_norm_exp, bin_norm0, bin_norm1, bin_norm2, bin_norm3
        
        elif self.mode == 'bf_bf':
            print('bf_bf mode round')
            dec_complement0 = dec_complement

            bin_complement0 = np.array(self.dec_to_bin26(dec_complement0)).reshape(-1, 26)

             


            # dec_norm = dec_pre_norm - 15
            # bin_norm0 = np.zeros((self.epoch, 16), dtype = int)
            # bin_norm1 = np.zeros((self.epoch, 16), dtype = int)
            # bin_norm2 = np.zeros((self.epoch, 16), dtype = int)
            # bin_norm3 = np.zeros((self.epoch, 16), dtype = int)
            bin_norm0 = np.zeros((self.epoch, 26), dtype = int)

            dec_norm_exp0 = np.zeros((self.epoch, 1), dtype = int)


            for i in range(self.epoch):
                if bin_complement0[i][0] == 1:
                    bin_norm0[i] = bin_complement0[i]
                    dec_norm_exp0[i] = 0
                elif bin_complement0[i][1] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][1:]).reshape(1,-1), np.zeros((1, 1), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 1
                elif bin_complement0[i][2] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][2:]).reshape(1,-1), np.zeros((1, 2), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 2
                elif bin_complement0[i][3] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][3:]).reshape(1,-1), np.zeros((1, 3), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 3
                elif bin_complement0[i][4] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][4:]).reshape(1,-1), np.zeros((1, 4), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 4
                elif bin_complement0[i][5] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][5:]).reshape(1,-1), np.zeros((1, 5), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 5
                elif bin_complement0[i][6] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][6:]).reshape(1,-1), np.zeros((1, 6), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 6
                elif bin_complement0[i][7] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][7:]).reshape(1,-1), np.zeros((1, 7), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 7
                elif bin_complement0[i][8] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][8:]).reshape(1,-1), np.zeros((1, 8), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 8
                elif bin_complement0[i][9] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][9:]).reshape(1,-1), np.zeros((1, 9), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 9
                elif bin_complement0[i][10] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][10:]).reshape(1,-1), np.zeros((1, 10), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 10
                elif bin_complement0[i][11] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][11:]).reshape(1,-1), np.zeros((1, 11), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 11
                elif bin_complement0[i][12] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][12:]).reshape(1,-1), np.zeros((1, 12), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 12
                elif bin_complement0[i][13] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][13:]).reshape(1,-1), np.zeros((1, 13), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 13
                elif bin_complement0[i][14] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][14:]).reshape(1,-1), np.zeros((1, 14), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 14
                elif bin_complement0[i][15] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][15:]).reshape(1,-1), np.zeros((1, 15), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 15
                elif bin_complement0[i][16] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][16:]).reshape(1,-1), np.zeros((1, 16), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 16   
                elif bin_complement0[i][17] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][17:]).reshape(1,-1), np.zeros((1, 17), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 17
                elif bin_complement0[i][18] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][18:]).reshape(1,-1), np.zeros((1, 18), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 18
                elif bin_complement0[i][19] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][19:]).reshape(1,-1), np.zeros((1, 19), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 19
                elif bin_complement0[i][20] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][20:]).reshape(1,-1), np.zeros((1, 20), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 20
                elif bin_complement0[i][21] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][21:]).reshape(1,-1), np.zeros((1, 21), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 21
                elif bin_complement0[i][22] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][22:]).reshape(1,-1), np.zeros((1, 22), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 22
                elif bin_complement0[i][23] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][23:]).reshape(1,-1), np.zeros((1, 23), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 23
                elif bin_complement0[i][24] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][24:]).reshape(1,-1), np.zeros((1, 24), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 24
                elif bin_complement0[i][25] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][25:]).reshape(1,-1), np.zeros((1, 25), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 25            
                else:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][26:]).reshape(1,-1), np.zeros((1, 26), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 26

             
            return dec_norm_exp0, bin_norm0

        elif self.mode == 'fp_fp':
            print('fp_fp mode round')
            dec_complement0 = dec_complement

            bin_complement0 = np.array(self.dec_to_bin32(dec_complement0)).reshape(-1, 32)

             


            # dec_norm = dec_pre_norm - 15
            # bin_norm0 = np.zeros((self.epoch, 16), dtype = int)
            # bin_norm1 = np.zeros((self.epoch, 16), dtype = int)
            # bin_norm2 = np.zeros((self.epoch, 16), dtype = int)
            # bin_norm3 = np.zeros((self.epoch, 16), dtype = int)
            bin_norm0 = np.zeros((self.epoch, 32), dtype = int)

            dec_norm_exp0 = np.zeros((self.epoch, 1), dtype = int)


            for i in range(self.epoch):
                if bin_complement0[i][0] == 1:
                    bin_norm0[i] = bin_complement0[i]
                    dec_norm_exp0[i] = 0
                elif bin_complement0[i][1] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][1:]).reshape(1,-1), np.zeros((1, 1), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 1
                elif bin_complement0[i][2] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][2:]).reshape(1,-1), np.zeros((1, 2), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 2
                elif bin_complement0[i][3] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][3:]).reshape(1,-1), np.zeros((1, 3), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 3
                elif bin_complement0[i][4] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][4:]).reshape(1,-1), np.zeros((1, 4), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 4
                elif bin_complement0[i][5] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][5:]).reshape(1,-1), np.zeros((1, 5), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 5
                elif bin_complement0[i][6] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][6:]).reshape(1,-1), np.zeros((1, 6), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 6
                elif bin_complement0[i][7] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][7:]).reshape(1,-1), np.zeros((1, 7), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 7
                elif bin_complement0[i][8] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][8:]).reshape(1,-1), np.zeros((1, 8), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 8
                elif bin_complement0[i][9] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][9:]).reshape(1,-1), np.zeros((1, 9), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 9
                elif bin_complement0[i][10] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][10:]).reshape(1,-1), np.zeros((1, 10), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 10
                elif bin_complement0[i][11] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][11:]).reshape(1,-1), np.zeros((1, 11), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 11
                elif bin_complement0[i][12] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][12:]).reshape(1,-1), np.zeros((1, 12), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 12
                elif bin_complement0[i][13] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][13:]).reshape(1,-1), np.zeros((1, 13), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 13
                elif bin_complement0[i][14] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][14:]).reshape(1,-1), np.zeros((1, 14), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 14
                elif bin_complement0[i][15] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][15:]).reshape(1,-1), np.zeros((1, 15), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 15
                elif bin_complement0[i][16] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][16:]).reshape(1,-1), np.zeros((1, 16), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 16   
                elif bin_complement0[i][17] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][17:]).reshape(1,-1), np.zeros((1, 17), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 17
                elif bin_complement0[i][18] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][18:]).reshape(1,-1), np.zeros((1, 18), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 18
                elif bin_complement0[i][19] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][19:]).reshape(1,-1), np.zeros((1, 19), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 19
                elif bin_complement0[i][20] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][20:]).reshape(1,-1), np.zeros((1, 20), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 20
                elif bin_complement0[i][21] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][21:]).reshape(1,-1), np.zeros((1, 21), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 21
                elif bin_complement0[i][22] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][22:]).reshape(1,-1), np.zeros((1, 22), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 22
                elif bin_complement0[i][23] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][23:]).reshape(1,-1), np.zeros((1, 23), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 23
                elif bin_complement0[i][24] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][24:]).reshape(1,-1), np.zeros((1, 24), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 24
                elif bin_complement0[i][25] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][25:]).reshape(1,-1), np.zeros((1, 25), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 25            
                elif bin_complement0[i][26] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][26:]).reshape(1,-1), np.zeros((1, 26), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 26
                elif bin_complement0[i][27] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][27:]).reshape(1,-1), np.zeros((1, 27), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 27
                elif bin_complement0[i][28] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][28:]).reshape(1,-1), np.zeros((1, 28), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 28
                elif bin_complement0[i][29] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][29:]).reshape(1,-1), np.zeros((1, 29), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 29
                elif bin_complement0[i][30] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][30:]).reshape(1,-1), np.zeros((1, 30), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 30
                elif bin_complement0[i][31] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][31:]).reshape(1,-1), np.zeros((1, 31), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 31
                else:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][32:]).reshape(1,-1), np.zeros((1, 32), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 32


             
            return dec_norm_exp0, bin_norm0
        
        elif self.mode == 'fp_int':
            print('fp_int mode norm')
            
            dec_complement3 = dec_complement[:, 0:1]
            dec_complement2 = dec_complement[:, 1:2]
            dec_complement1 = dec_complement[:, 2:3]
            dec_complement0 = dec_complement[:, 3:]

            bin_complement3 = np.array(self.dec_to_bin30(dec_complement3)).reshape(-1, 30)
            bin_complement2 = np.array(self.dec_to_bin30(dec_complement2)).reshape(-1, 30)
            bin_complement1 = np.array(self.dec_to_bin30(dec_complement1)).reshape(-1, 30)
            bin_complement0 = np.array(self.dec_to_bin30(dec_complement0)).reshape(-1, 30)

       
            bin_norm0 = np.zeros((self.epoch, 30), dtype = int)
            bin_norm1 = np.zeros((self.epoch, 30), dtype = int)
            bin_norm2 = np.zeros((self.epoch, 30), dtype = int)
            bin_norm3 = np.zeros((self.epoch, 30), dtype = int)

            dec_norm_exp0 = np.zeros((self.epoch, 1), dtype = int)
            dec_norm_exp1 = np.zeros((self.epoch, 1), dtype = int)
            dec_norm_exp2 = np.zeros((self.epoch, 1), dtype = int)
            dec_norm_exp3 = np.zeros((self.epoch, 1), dtype = int)

            # test = np.concatenate((np.array(bin_pre_norm0[0][1:]).reshape(1,-1), np.zeros((1, 1), dtype = int)), axis = -1)
            for i in range(self.epoch):
                if bin_complement0[i][0] == 1:
                    bin_norm0[i] = bin_complement0[i]
                    dec_norm_exp0[i] = 0
                elif bin_complement0[i][1] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][1:]).reshape(1,-1), np.zeros((1, 1), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 1
                elif bin_complement0[i][2] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][2:]).reshape(1,-1), np.zeros((1, 2), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 2
                elif bin_complement0[i][3] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][3:]).reshape(1,-1), np.zeros((1, 3), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 3
                elif bin_complement0[i][4] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][4:]).reshape(1,-1), np.zeros((1, 4), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 4
                elif bin_complement0[i][5] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][5:]).reshape(1,-1), np.zeros((1, 5), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 5
                elif bin_complement0[i][6] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][6:]).reshape(1,-1), np.zeros((1, 6), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 6
                elif bin_complement0[i][7] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][7:]).reshape(1,-1), np.zeros((1, 7), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 7
                elif bin_complement0[i][8] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][8:]).reshape(1,-1), np.zeros((1, 8), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 8
                elif bin_complement0[i][9] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][9:]).reshape(1,-1), np.zeros((1, 9), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 9
                elif bin_complement0[i][10] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][10:]).reshape(1,-1), np.zeros((1, 10), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 10
                elif bin_complement0[i][11] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][11:]).reshape(1,-1), np.zeros((1, 11), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 11
                elif bin_complement0[i][12] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][12:]).reshape(1,-1), np.zeros((1, 12), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 12
                elif bin_complement0[i][13] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][13:]).reshape(1,-1), np.zeros((1, 13), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 13
                elif bin_complement0[i][14] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][14:]).reshape(1,-1), np.zeros((1, 14), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 14
                elif bin_complement0[i][15] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][15:]).reshape(1,-1), np.zeros((1, 15), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 15
                elif bin_complement0[i][16] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][16:]).reshape(1,-1), np.zeros((1, 16), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 16   
                elif bin_complement0[i][17] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][17:]).reshape(1,-1), np.zeros((1, 17), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 17
                elif bin_complement0[i][18] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][18:]).reshape(1,-1), np.zeros((1, 18), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 18
                elif bin_complement0[i][19] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][19:]).reshape(1,-1), np.zeros((1, 19), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 19
                elif bin_complement0[i][20] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][20:]).reshape(1,-1), np.zeros((1, 20), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 20
                elif bin_complement0[i][21] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][21:]).reshape(1,-1), np.zeros((1, 21), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 21
                elif bin_complement0[i][22] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][22:]).reshape(1,-1), np.zeros((1, 22), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 22
                elif bin_complement0[i][23] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][23:]).reshape(1,-1), np.zeros((1, 23), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 23
                elif bin_complement0[i][24] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][24:]).reshape(1,-1), np.zeros((1, 24), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 24
                elif bin_complement0[i][25] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][25:]).reshape(1,-1), np.zeros((1, 25), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 25        
                elif bin_complement0[i][26] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][26:]).reshape(1,-1), np.zeros((1, 26), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 26
                elif bin_complement0[i][27] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][27:]).reshape(1,-1), np.zeros((1, 27), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 27
                elif bin_complement0[i][28] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][28:]).reshape(1,-1), np.zeros((1, 28), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 28
                elif bin_complement0[i][29] == 1:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][29:]).reshape(1,-1), np.zeros((1, 29), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 29
                else:
                    bin_norm0[i] = np.concatenate((np.array(bin_complement0[i][30:]).reshape(1,-1), np.zeros((1, 30), dtype = int)), axis = -1)
                    dec_norm_exp0[i] = 30    

            for i in range(self.epoch):
                if bin_complement1[i][0] == 1:
                    bin_norm1[i] = bin_complement1[i]
                    dec_norm_exp1[i] = 0
                elif bin_complement1[i][1] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][1:]).reshape(1,-1), np.zeros((1, 1), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 1
                elif bin_complement1[i][2] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][2:]).reshape(1,-1), np.zeros((1, 2), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 2
                elif bin_complement1[i][3] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][3:]).reshape(1,-1), np.zeros((1, 3), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 3
                elif bin_complement1[i][4] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][4:]).reshape(1,-1), np.zeros((1, 4), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 4
                elif bin_complement1[i][5] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][5:]).reshape(1,-1), np.zeros((1, 5), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 5
                elif bin_complement1[i][6] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][6:]).reshape(1,-1), np.zeros((1, 6), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 6
                elif bin_complement1[i][7] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][7:]).reshape(1,-1), np.zeros((1, 7), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 7
                elif bin_complement1[i][8] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][8:]).reshape(1,-1), np.zeros((1, 8), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 8
                elif bin_complement1[i][9] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][9:]).reshape(1,-1), np.zeros((1, 9), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 9
                elif bin_complement1[i][10] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][10:]).reshape(1,-1), np.zeros((1, 10), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 10
                elif bin_complement1[i][11] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][11:]).reshape(1,-1), np.zeros((1, 11), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 11
                elif bin_complement1[i][12] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][12:]).reshape(1,-1), np.zeros((1, 12), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 12
                elif bin_complement1[i][13] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][13:]).reshape(1,-1), np.zeros((1, 13), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 13
                elif bin_complement1[i][14] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][14:]).reshape(1,-1), np.zeros((1, 14), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 14
                elif bin_complement1[i][15] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][15:]).reshape(1,-1), np.zeros((1, 15), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 15
                elif bin_complement1[i][16] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][16:]).reshape(1,-1), np.zeros((1, 16), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 16
                elif bin_complement1[i][17] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][17:]).reshape(1,-1), np.zeros((1, 17), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 17
                elif bin_complement1[i][18] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][18:]).reshape(1,-1), np.zeros((1, 18), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 18
                elif bin_complement1[i][19] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][19:]).reshape(1,-1), np.zeros((1, 19), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 19
                elif bin_complement1[i][20] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][20:]).reshape(1,-1), np.zeros((1, 20), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 20
                elif bin_complement1[i][21] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][21:]).reshape(1,-1), np.zeros((1, 21), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 21
                elif bin_complement1[i][22] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][22:]).reshape(1,-1), np.zeros((1, 22), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 22
                elif bin_complement1[i][23] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][23:]).reshape(1,-1), np.zeros((1, 23), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 23
                elif bin_complement1[i][24] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][24:]).reshape(1,-1), np.zeros((1, 24), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 24
                elif bin_complement1[i][25] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][25:]).reshape(1,-1), np.zeros((1, 25), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 25
                elif bin_complement1[i][26] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][26:]).reshape(1,-1), np.zeros((1, 26), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 26
                elif bin_complement1[i][27] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][27:]).reshape(1,-1), np.zeros((1, 27), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 27
                elif bin_complement1[i][28] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][28:]).reshape(1,-1), np.zeros((1, 28), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 28
                elif bin_complement1[i][29] == 1:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][29:]).reshape(1,-1), np.zeros((1, 29), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 29
                else:
                    bin_norm1[i] = np.concatenate((np.array(bin_complement1[i][30:]).reshape(1,-1), np.zeros((1, 30), dtype = int)), axis = -1)
                    dec_norm_exp1[i] = 30


            for i in range(self.epoch):
                if bin_complement2[i][0] == 1:
                    bin_norm2[i] = bin_complement2[i]
                    dec_norm_exp2[i] = 0
                elif bin_complement2[i][1] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][1:]).reshape(1,-1), np.zeros((1, 1), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 1
                elif bin_complement2[i][2] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][2:]).reshape(1,-1), np.zeros((1, 2), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 2
                elif bin_complement2[i][3] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][3:]).reshape(1,-1), np.zeros((1, 3), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 3
                elif bin_complement2[i][4] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][4:]).reshape(1,-1), np.zeros((1, 4), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 4
                elif bin_complement2[i][5] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][5:]).reshape(1,-1), np.zeros((1, 5), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 5
                elif bin_complement2[i][6] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][6:]).reshape(1,-1), np.zeros((1, 6), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 6
                elif bin_complement2[i][7] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][7:]).reshape(1,-1), np.zeros((1, 7), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 7
                elif bin_complement2[i][8] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][8:]).reshape(1,-1), np.zeros((1, 8), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 8
                elif bin_complement2[i][9] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][9:]).reshape(1,-1), np.zeros((1, 9), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 9
                elif bin_complement2[i][10] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][10:]).reshape(1,-1), np.zeros((1, 10), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 10
                elif bin_complement2[i][11] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][11:]).reshape(1,-1), np.zeros((1, 11), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 11
                elif bin_complement2[i][12] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][12:]).reshape(1,-1), np.zeros((1, 12), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 12
                elif bin_complement2[i][13] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][13:]).reshape(1,-1), np.zeros((1, 13), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 13
                elif bin_complement2[i][14] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][14:]).reshape(1,-1), np.zeros((1, 14), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 14
                elif bin_complement2[i][15] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][15:]).reshape(1,-1), np.zeros((1, 15), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 15
                elif bin_complement2[i][16] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][16:]).reshape(1,-1), np.zeros((1, 16), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 16
                elif bin_complement2[i][17] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][17:]).reshape(1,-1), np.zeros((1, 17), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 17
                elif bin_complement2[i][18] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][18:]).reshape(1,-1), np.zeros((1, 18), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 18
                elif bin_complement2[i][19] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][19:]).reshape(1,-1), np.zeros((1, 19), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 19
                elif bin_complement2[i][20] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][20:]).reshape(1,-1), np.zeros((1, 20), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 20
                elif bin_complement2[i][21] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][21:]).reshape(1,-1), np.zeros((1, 21), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 21
                elif bin_complement2[i][22] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][22:]).reshape(1,-1), np.zeros((1, 22), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 22
                elif bin_complement2[i][23] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][23:]).reshape(1,-1), np.zeros((1, 23), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 23
                elif bin_complement2[i][24] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][24:]).reshape(1,-1), np.zeros((1, 24), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 24
                elif bin_complement2[i][25] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][25:]).reshape(1,-1), np.zeros((1, 25), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 25
                elif bin_complement2[i][26] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][26:]).reshape(1,-1), np.zeros((1, 26), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 26
                elif bin_complement2[i][27] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][27:]).reshape(1,-1), np.zeros((1, 27), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 27
                elif bin_complement2[i][28] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][28:]).reshape(1,-1), np.zeros((1, 28), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 28
                elif bin_complement2[i][29] == 1:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][29:]).reshape(1,-1), np.zeros((1, 29), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 29
                else:
                    bin_norm2[i] = np.concatenate((np.array(bin_complement2[i][30:]).reshape(1,-1), np.zeros((1, 30), dtype = int)), axis = -1)
                    dec_norm_exp2[i] = 30
                

            for i in range(self.epoch):
                if bin_complement3[i][0] == 1:
                    bin_norm3[i] = bin_complement3[i]
                    dec_norm_exp3[i] = 0
                elif bin_complement3[i][1] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][1:]).reshape(1,-1), np.zeros((1, 1), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 1
                elif bin_complement3[i][2] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][2:]).reshape(1,-1), np.zeros((1, 2), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 2
                elif bin_complement3[i][3] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][3:]).reshape(1,-1), np.zeros((1, 3), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 3
                elif bin_complement3[i][4] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][4:]).reshape(1,-1), np.zeros((1, 4), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 4
                elif bin_complement3[i][5] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][5:]).reshape(1,-1), np.zeros((1, 5), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 5
                elif bin_complement3[i][6] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][6:]).reshape(1,-1), np.zeros((1, 6), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 6
                elif bin_complement3[i][7] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][7:]).reshape(1,-1), np.zeros((1, 7), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 7
                elif bin_complement3[i][8] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][8:]).reshape(1,-1), np.zeros((1, 8), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 8
                elif bin_complement3[i][9] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][9:]).reshape(1,-1), np.zeros((1, 9), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 9
                elif bin_complement3[i][10] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][10:]).reshape(1,-1), np.zeros((1, 10), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 10
                elif bin_complement3[i][11] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][11:]).reshape(1,-1), np.zeros((1, 11), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 11
                elif bin_complement3[i][12] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][12:]).reshape(1,-1), np.zeros((1, 12), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 12
                elif bin_complement3[i][13] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][13:]).reshape(1,-1), np.zeros((1, 13), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 13
                elif bin_complement3[i][14] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][14:]).reshape(1,-1), np.zeros((1, 14), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 14
                elif bin_complement3[i][15] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][15:]).reshape(1,-1), np.zeros((1, 15), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 15
                elif bin_complement3[i][16] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][16:]).reshape(1,-1), np.zeros((1, 16), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 16
                elif bin_complement3[i][17] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][17:]).reshape(1,-1), np.zeros((1, 17), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 17
                elif bin_complement3[i][18] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][18:]).reshape(1,-1), np.zeros((1, 18), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 18
                elif bin_complement3[i][19] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][19:]).reshape(1,-1), np.zeros((1, 19), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 19
                elif bin_complement3[i][20] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][20:]).reshape(1,-1), np.zeros((1, 20), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 20
                elif bin_complement3[i][21] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][21:]).reshape(1,-1), np.zeros((1, 21), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 21
                elif bin_complement3[i][22] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][22:]).reshape(1,-1), np.zeros((1, 22), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 22
                elif bin_complement3[i][23] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][23:]).reshape(1,-1), np.zeros((1, 23), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 23
                elif bin_complement3[i][24] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][24:]).reshape(1,-1), np.zeros((1, 24), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 24
                elif bin_complement3[i][25] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][25:]).reshape(1,-1), np.zeros((1, 25), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 25
                elif bin_complement3[i][26] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][26:]).reshape(1,-1), np.zeros((1, 26), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 26
                elif bin_complement3[i][27] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][27:]).reshape(1,-1), np.zeros((1, 27), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 27
                elif bin_complement3[i][28] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][28:]).reshape(1,-1), np.zeros((1, 28), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 28
                elif bin_complement3[i][29] == 1:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][29:]).reshape(1,-1), np.zeros((1, 29), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 29
                else:
                    bin_norm3[i] = np.concatenate((np.array(bin_complement3[i][30:]).reshape(1,-1), np.zeros((1, 30), dtype = int)), axis = -1)
                    dec_norm_exp3[i] = 30

            dec_norm_exp = np.concatenate((dec_norm_exp0, dec_norm_exp1, dec_norm_exp2, dec_norm_exp3), axis = 1)

            return dec_norm_exp, bin_norm0, bin_norm1, bin_norm2, bin_norm3

    def round(self, bin_norm0, bin_norm1, bin_norm2, bin_norm3):
        if self.mode == 'bf_int':
            print('bf_int mode round')
             
            L0 = bin_norm0[:, 7:8]
            R0 = bin_norm0[:, 8:9]
            S0 = bin_norm0[:, 9:10] | bin_norm0[:, 10:11] | bin_norm0[:, 11:12] | bin_norm0[:, 12:13] | bin_norm0[:, 13:14] | bin_norm0[:, 14:15] | bin_norm0[:, 15:16] | bin_norm0[:, 16:17] | bin_norm0[:, 17:18] | bin_norm0[:, 18:19] | bin_norm0[:, 19:20] | bin_norm0[:, 20:21] | bin_norm0[:, 21:22] | bin_norm0[:, 22:23] | bin_norm0[:, 23:24] \
                #| bin_norm0[:, 24:25] | bin_norm0[:, 25:26]
            round0 = R0 & (S0 | L0)

            L1 = bin_norm1[:, 7:8]
            R1 = bin_norm1[:, 8:9]
            S1 = bin_norm1[:, 9:10] | bin_norm1[:, 10:11] | bin_norm1[:, 11:12] | bin_norm1[:, 12:13] | bin_norm1[:, 13:14] | bin_norm1[:, 14:15] | bin_norm1[:, 15:16] | bin_norm1[:, 16:17] | bin_norm1[:, 17:18] | bin_norm1[:, 18:19] | bin_norm1[:, 19:20] | bin_norm1[:, 20:21] | bin_norm1[:, 21:22] | bin_norm1[:, 22:23] | bin_norm1[:, 23:24] \
                #| bin_norm1[:, 24:25] | bin_norm1[:, 25:26]
            round1 = R1 & (S1 | L1)

            L2 = bin_norm2[:, 7:8]
            R2 = bin_norm2[:, 8:9]
            S2 = bin_norm2[:, 9:10] | bin_norm2[:, 10:11] | bin_norm2[:, 11:12] | bin_norm2[:, 12:13] | bin_norm2[:, 13:14] | bin_norm2[:, 14:15] | bin_norm2[:, 15:16] | bin_norm2[:, 16:17] | bin_norm2[:, 17:18] | bin_norm2[:, 18:19] | bin_norm2[:, 19:20] | bin_norm2[:, 20:21] | bin_norm2[:, 21:22] | bin_norm2[:, 22:23] | bin_norm2[:, 23:24] \
                #| bin_norm2[:, 24:25] | bin_norm2[:, 25:26]
            round2 = R2 & (S2 | L2)

            L3 = bin_norm3[:, 7:8]
            R3 = bin_norm3[:, 8:9]
            S3 = bin_norm3[:, 9:10] | bin_norm3[:, 10:11] | bin_norm3[:, 11:12] | bin_norm3[:, 12:13] | bin_norm3[:, 13:14] | bin_norm3[:, 14:15] | bin_norm3[:, 15:16] | bin_norm3[:, 16:17] | bin_norm3[:, 17:18] | bin_norm3[:, 18:19] | bin_norm3[:, 19:20] | bin_norm3[:, 20:21] | bin_norm3[:, 21:22] | bin_norm3[:, 22:23] | bin_norm3[:, 23:24] \
                #| bin_norm3[:, 24:25] | bin_norm3[:, 25:26]
            round3 = R3 & (S3 | L3)

            bin_norm0 = np.concatenate((np.zeros((self.epoch,1), dtype = int), np.array(bin_norm0[:,0:8]).reshape(self.epoch, -1)), axis = -1)
            bin_norm1 = np.concatenate((np.zeros((self.epoch,1), dtype = int), np.array(bin_norm1[:,0:8]).reshape(self.epoch, -1)), axis = -1)
            bin_norm2 = np.concatenate((np.zeros((self.epoch,1), dtype = int), np.array(bin_norm2[:,0:8]).reshape(self.epoch, -1)), axis = -1)
            bin_norm3 = np.concatenate((np.zeros((self.epoch,1), dtype = int), np.array(bin_norm3[:,0:8]).reshape(self.epoch, -1)), axis = -1)

            dec_round0 = np.where(round0 == 1, np.array(self.bin_to_dec(bin_norm0)).reshape(-1, 1) + 1, np.array(self.bin_to_dec(bin_norm0)).reshape(-1, 1))
            dec_round1 = np.where(round1 == 1, np.array(self.bin_to_dec(bin_norm1)).reshape(-1, 1) + 1, np.array(self.bin_to_dec(bin_norm1)).reshape(-1, 1))
            dec_round2 = np.where(round2 == 1, np.array(self.bin_to_dec(bin_norm2)).reshape(-1, 1) + 1, np.array(self.bin_to_dec(bin_norm2)).reshape(-1, 1))
            dec_round3 = np.where(round3 == 1, np.array(self.bin_to_dec(bin_norm3)).reshape(-1, 1) + 1, np.array(self.bin_to_dec(bin_norm3)).reshape(-1, 1))
             
            dec_round = np.concatenate((dec_round0, dec_round1, dec_round2, dec_round3), axis = 1)

            return dec_round, dec_round0, dec_round1, dec_round2, dec_round3
        
        elif self.mode == 'bf_bf':
            print('bf_bf mode round')

            L0 = bin_norm0[:, 7:8]
            R0 = bin_norm0[:, 8:9]
            S0 = bin_norm0[:, 9:10] | bin_norm0[:, 10:11] | bin_norm0[:, 11:12] | bin_norm0[:, 12:13] | bin_norm0[:, 13:14] | bin_norm0[:, 14:15] | bin_norm0[:, 15:16] | bin_norm0[:, 16:17] | bin_norm0[:, 17:18] | bin_norm0[:, 18:19] | bin_norm0[:, 19:20] | bin_norm0[:, 20:21] | bin_norm0[:, 21:22] | bin_norm0[:, 22:23] | bin_norm0[:, 23:24] \
                | bin_norm0[:, 24:25] | bin_norm0[:, 25:26]
            round0 = R0 & (S0 | L0)

            bin_norm0 = np.concatenate((np.zeros((self.epoch,1), dtype = int), np.array(bin_norm0[:,0:8]).reshape(self.epoch, -1)), axis = -1)
            dec_round0 = np.where(round0 == 1, np.array(self.bin_to_dec(bin_norm0)).reshape(-1, 1) + 1, np.array(self.bin_to_dec(bin_norm0)).reshape(-1, 1))
             
            return dec_round0
    
        elif self.mode == 'fp_fp':
            print('bf_bf mode round')

            L0 = bin_norm0[:, 10:11]
            R0 = bin_norm0[:, 11:12]
            S0 = bin_norm0[:, 13:14] | bin_norm0[:, 14:15] | bin_norm0[:, 15:16] | bin_norm0[:, 16:17] | bin_norm0[:, 17:18] | bin_norm0[:, 18:19] | bin_norm0[:, 19:20] | bin_norm0[:, 20:21] | bin_norm0[:, 21:22] | bin_norm0[:, 22:23] | bin_norm0[:, 23:24] \
                | bin_norm0[:, 24:25] | bin_norm0[:, 25:26] | bin_norm0[:, 26:27] | bin_norm0[:, 27:28] | bin_norm0[:, 28:29] | bin_norm0[:, 29:30] | bin_norm0[:, 30:31] | bin_norm0[:, 31:32]
            round0 = R0 & (S0 | L0)

            bin_norm0 = np.concatenate((np.zeros((self.epoch,1), dtype = int), np.array(bin_norm0[:,0:11]).reshape(self.epoch, -1)), axis = -1)
            dec_round0 = np.where(round0 == 1, np.array(self.bin_to_dec(bin_norm0)).reshape(-1, 1) + 1, np.array(self.bin_to_dec(bin_norm0)).reshape(-1, 1))
             
            return dec_round0
        
        elif self.mode == 'fp_int':
            print('fp_int mode round')
             
            L0 = bin_norm0[:, 10:11]
            R0 = bin_norm0[:, 11:12]
            S0 = bin_norm0[:, 12:13] | bin_norm0[:, 13:14] | bin_norm0[:, 14:15] | bin_norm0[:, 15:16] | bin_norm0[:, 16:17] | bin_norm0[:, 17:18] | bin_norm0[:, 18:19] | bin_norm0[:, 19:20] | bin_norm0[:, 20:21] | bin_norm0[:, 21:22] | bin_norm0[:, 22:23] | bin_norm0[:, 23:24] \
                | bin_norm0[:, 24:25] | bin_norm0[:, 25:26] | bin_norm0[:, 26:27] | bin_norm0[:, 27:28] | bin_norm0[:, 28:29] | bin_norm0[:, 29:30] 
            round0 = R0 & (S0 | L0)

            L1 = bin_norm1[:, 10:11]
            R1 = bin_norm1[:, 11:12]
            S1 = bin_norm1[:, 12:13] | bin_norm1[:, 13:14] | bin_norm1[:, 14:15] | bin_norm1[:, 15:16] | bin_norm1[:, 16:17] | bin_norm1[:, 17:18] | bin_norm1[:, 18:19] | bin_norm1[:, 19:20] | bin_norm1[:, 20:21] | bin_norm1[:, 21:22] | bin_norm1[:, 22:23] | bin_norm1[:, 23:24] \
                | bin_norm1[:, 24:25] | bin_norm1[:, 25:26] | bin_norm1[:, 26:27] | bin_norm1[:, 27:28] | bin_norm1[:, 28:29] | bin_norm1[:, 29:30]
            round1 = R1 & (S1 | L1)

            L2 = bin_norm2[:, 10:11]
            R2 = bin_norm2[:, 11:12]
            S2 = bin_norm2[:, 12:13] | bin_norm2[:, 13:14] | bin_norm2[:, 14:15] | bin_norm2[:, 15:16] | bin_norm2[:, 16:17] | bin_norm2[:, 17:18] | bin_norm2[:, 18:19] | bin_norm2[:, 19:20] | bin_norm2[:, 20:21] | bin_norm2[:, 21:22] | bin_norm2[:, 22:23] | bin_norm2[:, 23:24] \
                | bin_norm2[:, 24:25] | bin_norm2[:, 25:26] | bin_norm2[:, 26:27] | bin_norm2[:, 27:28] | bin_norm2[:, 28:29] | bin_norm2[:, 29:30]
            round2 = R2 & (S2 | L2)

            L3 = bin_norm3[:, 10:11]
            R3 = bin_norm3[:, 11:12]
            S3 = bin_norm3[:, 12:13] | bin_norm3[:, 13:14] | bin_norm3[:, 14:15] | bin_norm3[:, 15:16] | bin_norm3[:, 16:17] | bin_norm3[:, 17:18] | bin_norm3[:, 18:19] | bin_norm3[:, 19:20] | bin_norm3[:, 20:21] | bin_norm3[:, 21:22] | bin_norm3[:, 22:23] | bin_norm3[:, 23:24] \
                | bin_norm3[:, 24:25] | bin_norm3[:, 25:26] | bin_norm3[:, 26:27] | bin_norm3[:, 27:28] | bin_norm3[:, 28:29] | bin_norm3[:, 29:30]
            round3 = R3 & (S3 | L3)

            bin_norm0 = np.concatenate((np.zeros((self.epoch,1), dtype = int), np.array(bin_norm0[:,0:11]).reshape(self.epoch, -1)), axis = -1)
            bin_norm1 = np.concatenate((np.zeros((self.epoch,1), dtype = int), np.array(bin_norm1[:,0:11]).reshape(self.epoch, -1)), axis = -1)
            bin_norm2 = np.concatenate((np.zeros((self.epoch,1), dtype = int), np.array(bin_norm2[:,0:11]).reshape(self.epoch, -1)), axis = -1)
            bin_norm3 = np.concatenate((np.zeros((self.epoch,1), dtype = int), np.array(bin_norm3[:,0:11]).reshape(self.epoch, -1)), axis = -1)

            dec_round0 = np.where(round0 == 1, np.array(self.bin_to_dec(bin_norm0)).reshape(-1, 1) + 1, np.array(self.bin_to_dec(bin_norm0)).reshape(-1, 1))
            dec_round1 = np.where(round1 == 1, np.array(self.bin_to_dec(bin_norm1)).reshape(-1, 1) + 1, np.array(self.bin_to_dec(bin_norm1)).reshape(-1, 1))
            dec_round2 = np.where(round2 == 1, np.array(self.bin_to_dec(bin_norm2)).reshape(-1, 1) + 1, np.array(self.bin_to_dec(bin_norm2)).reshape(-1, 1))
            dec_round3 = np.where(round3 == 1, np.array(self.bin_to_dec(bin_norm3)).reshape(-1, 1) + 1, np.array(self.bin_to_dec(bin_norm3)).reshape(-1, 1))
             
            dec_round = np.concatenate((dec_round0, dec_round1, dec_round2, dec_round3), axis = 1)

            return dec_round, dec_round0, dec_round1, dec_round2, dec_round3
            

