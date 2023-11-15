from SERPENT24 import SERPENT24
import math
alpha = [0x00000000, 0xE19FCF13, 0x6B973726, 0x8A08F835,
	     0xD6876E4C, 0x3718A15F, 0xBD10596A, 0x5C8F9679,
	     0x05A7DC98, 0xE438138B, 0x6E30EBBE, 0x8FAF24AD,
    	 0xD320B2D4, 0x32BF7DC7, 0xB8B785F2, 0x59284AE1,
     	 0x0AE71199, 0xEB78DE8A, 0x617026BF, 0x80EFE9AC,
 	 	 0xDC607FD5, 0x3DFFB0C6, 0xB7F748F3, 0x566887E0,
	 	 0x0F40CD01, 0xEEDF0212, 0x64D7FA27, 0x85483534,
	 	 0xD9C7A34D, 0x38586C5E, 0xB250946B, 0x53CF5B78,
	 	 0x1467229B, 0xF5F8ED88, 0x7FF015BD, 0x9E6FDAAE,
	 	 0xC2E04CD7, 0x237F83C4, 0xA9777BF1, 0x48E8B4E2,
	 	 0x11C0FE03, 0xF05F3110, 0x7A57C925, 0x9BC80636,
	 	 0xC747904F, 0x26D85F5C, 0xACD0A769, 0x4D4F687A,
	 	 0x1E803302, 0xFF1FFC11, 0x75170424, 0x9488CB37,
	 	 0xC8075D4E, 0x2998925D, 0xA3906A68, 0x420FA57B,
	 	 0x1B27EF9A, 0xFAB82089, 0x70B0D8BC, 0x912F17AF,
	 	 0xCDA081D6, 0x2C3F4EC5, 0xA637B6F0, 0x47A879E3,
	 	 0x28CE449F, 0xC9518B8C, 0x435973B9, 0xA2C6BCAA,
	 	 0xFE492AD3, 0x1FD6E5C0, 0x95DE1DF5, 0x7441D2E6,
	 	 0x2D699807, 0xCCF65714, 0x46FEAF21, 0xA7616032,
	 	 0xFBEEF64B, 0x1A713958, 0x9079C16D, 0x71E60E7E,
	 	 0x22295506, 0xC3B69A15, 0x49BE6220, 0xA821AD33,
	 	 0xF4AE3B4A, 0x1531F459, 0x9F390C6C, 0x7EA6C37F,
	 	 0x278E899E, 0xC611468D, 0x4C19BEB8, 0xAD8671AB,
	 	 0xF109E7D2, 0x109628C1, 0x9A9ED0F4, 0x7B011FE7,
	 	 0x3CA96604, 0xDD36A917, 0x573E5122, 0xB6A19E31,
	 	 0xEA2E0848, 0x0BB1C75B, 0x81B93F6E, 0x6026F07D,
	 	 0x390EBA9C, 0xD891758F, 0x52998DBA, 0xB30642A9,
	 	 0xEF89D4D0, 0x0E161BC3, 0x841EE3F6, 0x65812CE5,
	 	 0x364E779D, 0xD7D1B88E, 0x5DD940BB, 0xBC468FA8,
	 	 0xE0C919D1, 0x0156D6C2, 0x8B5E2EF7, 0x6AC1E1E4,
	 	 0x33E9AB05, 0xD2766416, 0x587E9C23, 0xB9E15330,
	 	 0xE56EC549, 0x04F10A5A, 0x8EF9F26F, 0x6F663D7C,
	 	 0x50358897, 0xB1AA4784, 0x3BA2BFB1, 0xDA3D70A2,
	 	 0x86B2E6DB, 0x672D29C8, 0xED25D1FD, 0x0CBA1EEE,
	 	 0x5592540F, 0xB40D9B1C, 0x3E056329, 0xDF9AAC3A,
	 	 0x83153A43, 0x628AF550, 0xE8820D65, 0x091DC276,
	 	 0x5AD2990E, 0xBB4D561D, 0x3145AE28, 0xD0DA613B,
	 	 0x8C55F742, 0x6DCA3851, 0xE7C2C064, 0x065D0F77,
	 	 0x5F754596, 0xBEEA8A85, 0x34E272B0, 0xD57DBDA3,
	 	 0x89F22BDA, 0x686DE4C9, 0xE2651CFC, 0x03FAD3EF,
	 	 0x4452AA0C, 0xA5CD651F, 0x2FC59D2A, 0xCE5A5239,
	 	 0x92D5C440, 0x734A0B53, 0xF942F366, 0x18DD3C75,
	 	 0x41F57694, 0xA06AB987, 0x2A6241B2, 0xCBFD8EA1,
	 	 0x977218D8, 0x76EDD7CB, 0xFCE52FFE, 0x1D7AE0ED,
	 	 0x4EB5BB95, 0xAF2A7486, 0x25228CB3, 0xC4BD43A0,
	 	 0x9832D5D9, 0x79AD1ACA, 0xF3A5E2FF, 0x123A2DEC,
	 	 0x4B12670D, 0xAA8DA81E, 0x2085502B, 0xC11A9F38,
	 	 0x9D950941, 0x7C0AC652, 0xF6023E67, 0x179DF174,
	 	 0x78FBCC08, 0x9964031B, 0x136CFB2E, 0xF2F3343D,
	 	 0xAE7CA244, 0x4FE36D57, 0xC5EB9562, 0x24745A71,
	 	 0x7D5C1090, 0x9CC3DF83, 0x16CB27B6, 0xF754E8A5,
	 	 0xABDB7EDC, 0x4A44B1CF, 0xC04C49FA, 0x21D386E9,
	 	 0x721CDD91, 0x93831282, 0x198BEAB7, 0xF81425A4,
	 	 0xA49BB3DD, 0x45047CCE, 0xCF0C84FB, 0x2E934BE8,
	 	 0x77BB0109, 0x9624CE1A, 0x1C2C362F, 0xFDB3F93C,
	 	 0xA13C6F45, 0x40A3A056, 0xCAAB5863, 0x2B349770,
	 	 0x6C9CEE93, 0x8D032180, 0x070BD9B5, 0xE69416A6,
	 	 0xBA1B80DF, 0x5B844FCC, 0xD18CB7F9, 0x301378EA,
	 	 0x693B320B, 0x88A4FD18, 0x02AC052D, 0xE333CA3E,
	 	 0xBFBC5C47, 0x5E239354, 0xD42B6B61, 0x35B4A472,
	 	 0x667BFF0A, 0x87E43019, 0x0DECC82C, 0xEC73073F,
	 	 0xB0FC9146, 0x51635E55, 0xDB6BA660, 0x3AF46973,
	 	 0x63DC2392, 0x8243EC81, 0x084B14B4, 0xE9D4DBA7,
	 	 0xB55B4DDE, 0x54C482CD, 0xDECC7AF8, 0x3F53B5EB]

ialpha =[0x00000000, 0x180F40CD, 0x301E8033, 0x2811C0FE,
	 	 0x603CA966, 0x7833E9AB, 0x50222955, 0x482D6998,
	 	 0xC078FBCC, 0xD877BB01, 0xF0667BFF, 0xE8693B32,
	 	 0xA04452AA, 0xB84B1267, 0x905AD299, 0x88559254,
	 	 0x29F05F31, 0x31FF1FFC, 0x19EEDF02, 0x01E19FCF,
	 	 0x49CCF657, 0x51C3B69A, 0x79D27664, 0x61DD36A9,
	 	 0xE988A4FD, 0xF187E430, 0xD99624CE, 0xC1996403,
	 	 0x89B40D9B, 0x91BB4D56, 0xB9AA8DA8, 0xA1A5CD65,
	 	 0x5249BE62, 0x4A46FEAF, 0x62573E51, 0x7A587E9C,
	 	 0x32751704, 0x2A7A57C9, 0x026B9737, 0x1A64D7FA,
	 	 0x923145AE, 0x8A3E0563, 0xA22FC59D, 0xBA208550,
	 	 0xF20DECC8, 0xEA02AC05, 0xC2136CFB, 0xDA1C2C36,
	 	 0x7BB9E153, 0x63B6A19E, 0x4BA76160, 0x53A821AD,
	 	 0x1B854835, 0x038A08F8, 0x2B9BC806, 0x339488CB,
	 	 0xBBC11A9F, 0xA3CE5A52, 0x8BDF9AAC, 0x93D0DA61,
	 	 0xDBFDB3F9, 0xC3F2F334, 0xEBE333CA, 0xF3EC7307,
	 	 0xA492D5C4, 0xBC9D9509, 0x948C55F7, 0x8C83153A,
	 	 0xC4AE7CA2, 0xDCA13C6F, 0xF4B0FC91, 0xECBFBC5C,
	 	 0x64EA2E08, 0x7CE56EC5, 0x54F4AE3B, 0x4CFBEEF6,
	 	 0x04D6876E, 0x1CD9C7A3, 0x34C8075D, 0x2CC74790,
	 	 0x8D628AF5, 0x956DCA38, 0xBD7C0AC6, 0xA5734A0B,
	 	 0xED5E2393, 0xF551635E, 0xDD40A3A0, 0xC54FE36D,
	 	 0x4D1A7139, 0x551531F4, 0x7D04F10A, 0x650BB1C7,
	 	 0x2D26D85F, 0x35299892, 0x1D38586C, 0x053718A1,
	 	 0xF6DB6BA6, 0xEED42B6B, 0xC6C5EB95, 0xDECAAB58,
	 	 0x96E7C2C0, 0x8EE8820D, 0xA6F942F3, 0xBEF6023E,
	 	 0x36A3906A, 0x2EACD0A7, 0x06BD1059, 0x1EB25094,
	 	 0x569F390C, 0x4E9079C1, 0x6681B93F, 0x7E8EF9F2,
	 	 0xDF2B3497, 0xC724745A, 0xEF35B4A4, 0xF73AF469,
	 	 0xBF179DF1, 0xA718DD3C, 0x8F091DC2, 0x97065D0F,
	 	 0x1F53CF5B, 0x075C8F96, 0x2F4D4F68, 0x37420FA5,
	 	 0x7F6F663D, 0x676026F0, 0x4F71E60E, 0x577EA6C3,
	 	 0xE18D0321, 0xF98243EC, 0xD1938312, 0xC99CC3DF,
	 	 0x81B1AA47, 0x99BEEA8A, 0xB1AF2A74, 0xA9A06AB9,
	 	 0x21F5F8ED, 0x39FAB820, 0x11EB78DE, 0x09E43813,
	 	 0x41C9518B, 0x59C61146, 0x71D7D1B8, 0x69D89175,
	 	 0xC87D5C10, 0xD0721CDD, 0xF863DC23, 0xE06C9CEE,
	 	 0xA841F576, 0xB04EB5BB, 0x985F7545, 0x80503588,
	 	 0x0805A7DC, 0x100AE711, 0x381B27EF, 0x20146722,
	 	 0x68390EBA, 0x70364E77, 0x58278E89, 0x4028CE44,
	 	 0xB3C4BD43, 0xABCBFD8E, 0x83DA3D70, 0x9BD57DBD,
	 	 0xD3F81425, 0xCBF754E8, 0xE3E69416, 0xFBE9D4DB,
	 	 0x73BC468F, 0x6BB30642, 0x43A2C6BC, 0x5BAD8671,
	 	 0x1380EFE9, 0x0B8FAF24, 0x239E6FDA, 0x3B912F17,
	 	 0x9A34E272, 0x823BA2BF, 0xAA2A6241, 0xB225228C,
	 	 0xFA084B14, 0xE2070BD9, 0xCA16CB27, 0xD2198BEA,
	 	 0x5A4C19BE, 0x42435973, 0x6A52998D, 0x725DD940,
	 	 0x3A70B0D8, 0x227FF015, 0x0A6E30EB, 0x12617026,
	 	 0x451FD6E5, 0x5D109628, 0x750156D6, 0x6D0E161B,
	 	 0x25237F83, 0x3D2C3F4E, 0x153DFFB0, 0x0D32BF7D,
	 	 0x85672D29, 0x9D686DE4, 0xB579AD1A, 0xAD76EDD7,
	 	 0xE55B844F, 0xFD54C482, 0xD545047C, 0xCD4A44B1,
	 	 0x6CEF89D4, 0x74E0C919, 0x5CF109E7, 0x44FE492A,
	 	 0x0CD320B2, 0x14DC607F, 0x3CCDA081, 0x24C2E04C,
	 	 0xAC977218, 0xB49832D5, 0x9C89F22B, 0x8486B2E6,
	 	 0xCCABDB7E, 0xD4A49BB3, 0xFCB55B4D, 0xE4BA1B80,
	 	 0x17566887, 0x0F59284A, 0x2748E8B4, 0x3F47A879,
	 	 0x776AC1E1, 0x6F65812C, 0x477441D2, 0x5F7B011F,
	 	 0xD72E934B, 0xCF21D386, 0xE7301378, 0xFF3F53B5,
	 	 0xB7123A2D, 0xAF1D7AE0, 0x870CBA1E, 0x9F03FAD3,
	 	 0x3EA637B6, 0x26A9777B, 0x0EB8B785, 0x16B7F748,
	 	 0x5E9A9ED0, 0x4695DE1D, 0x6E841EE3, 0x768B5E2E,
	 	 0xFEDECC7A, 0xE6D18CB7, 0xCEC04C49, 0xD6CF0C84,
	 	 0x9EE2651C, 0x86ED25D1, 0xAEFCE52F, 0xB6F3A5E2]
window = 0xFFFFFFFF
M = 0x54655307
class SOSEMANUK:
    def __init__(self, key, initVec) -> None:
        self.S = []
        self.R = []
        # Run SERPENT key schedule
        init = SERPENT24(key)
        # IV injection
        lis = init.run(initVec)
        # Pass initial value to S and R vector.
        self.S.extend([lis[23][3],lis[23][2],lis[23][1],lis[23][0], # S1, S2, S3, S4 = Y24-3, Y24-2, Y24-1, Y24-0
                       lis[17][1], lis[17][3],                      # S5, S6 = Y18-1, Y18-3
                       lis[11][3],lis[11][2],lis[11][1],lis[11][0]])# S7, S8, S9, S10 = Y12-3, Y12-2, Y12-1, Y12-0
        
        self.R.extend([lis[17][0], lis[17][2]]) # R1, R2 = Y18-0, Y18-2

    def mul_a(self, x):  #thực hiện phép nhân
        x = ((x<<8)& window) ^ alpha[x>>24]
        return x
    
    def div_a(self, x): #thực hiện phép chia
        x = (x>>8) ^ ialpha[x & 0xFF]
        return x
    
    def LFSR(self): #Linear Feedback Shift Register
		#Sử dụng các giá trị trong vector S để thực hiện phép XOR và các phép nhân, chia trên trường hữu hạn.
        s = self.S[9]^self.div_a(self.S[3])^self.mul_a(self.S[0])
        ret = self.S.pop(0)
        self.S.append(s)
        return ret
    
    def FSM(self):
		#Sử dụng giá trị trong vector R để quyết định giá trị đầu vào của FSM, sau đó thực hiện một số phép toán để cập nhật vector R và trả về giá trị đầu ra.
        if (self.R[0]&0b1) == 1:
            mux = self.S[1]
        else:
            mux = self.S[1] ^ self.S[8]
        r1 = (self.R[1] + mux)%int(math.pow(2,32))
        r2 = SERPENT24.ROTL(SERPENT24,(self.R[0]*M)%int(math.pow(2,32)), 7)
        self.R[0] = r1
        self.R[1] = r2

        return ((self.S[9]+r1)%int(math.pow(2,32)))^r2
    
    def run(self):
        f_list =[]
        s_list =[]
        string = ""
        for _ in range(4):
            f_list.append(self.FSM())
            s_list.append(self.LFSR())

        for i in range(4):
            f_list[i] = SERPENT24.SboxExec(SERPENT24,f_list[i], 2) ^ s_list[i]

        for i in range(4):
            string += self.byte2bin(f_list[3-i])

        return string
    def byte2bin(self, int): # Bien doi 32 bit word (int) thanh string 32 binary
        string = ""
        for i in range(32):
            x = 0b00000001 << (31 - i)
            x = x & int
            x = x >> (31 - i)
            string += str(x)
        return string