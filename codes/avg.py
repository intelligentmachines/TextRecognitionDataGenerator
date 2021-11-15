words = {'ঠিকানা': 359, 'বাসা': 1000, 'হোল্ডিং': 116, 'ডাকঘর': 103, 'রক্তের': 551, 'গ্রুপ': 4074, 
'মেয়াদ': 0, 'উত্তীর্ণের': 10, 'তারিখ': 4184, 'প্রদানের': 1861, 'গ্রাম': 4233, 'রাস্তা': 1794}
nums = {'০': 716066, '১': 929692, '২': 575696, '৩': 258137, '৪': 240221, '৫': 263046, '৬': 237923, '৭': 240844, '৮': 264406, '৯': 513899}
chars = {'/': 32535, ':': 163277, ',': 1040046, '-': 346231}

len = 70528
for word in chars.keys():
    print(f'{word} : {chars[word]/len}')