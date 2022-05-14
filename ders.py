#Task1

n1 = 15
n2 = 13
#print('%s + %s = %s' % (n1, n2, n1+n2))

#Task 2

userData = [
    {
        'debt': 12543,
        'payed': 341.346742,
        'payed_percent': 0.027214122777644904,
        'card_number': '5326-6644-1234-6432',
        'first_name': 'Akif',
        'last_name': 'Serifov',
        'father_name': 'Elekber',
    }
]
prprint(("""Hormetli {0[0][first_name]:.1}. {0[0][father_name]:.1}. {0[0][last_name]}, sizin {0[0][card_number]:*<16.9} nomreli
kredit kartiniza {0[0][payed]}AZN odenis edildi. 
Umumi {0[0][debt]:,}AZN teskil eden borcunuzdan mebleg silinmisdir.""").format(userData))




