from io import open


def convert(amount, home_currency, location_currency):        #function for getting the amount,home and location currency
    from web_utility import load_page

    def ignore_characters_at_beginning(index_character, all_other_string):     #funtion definition for removing the text before
        ignore_commence = all_other_string.find(index_character)
        if ignore_commence == -1:
            return ''
        ignore_commence += len(index_character)
        return all_other_string[ignore_commence:]

    def ignore_space(all_strings):                                   #function definition for removing the space before
        ignore_begin = all_strings.find('<')
        ignore_exit = all_strings.find('>') + 1
        return all_strings[:ignore_begin] + all_strings[ignore_exit:]

    currency_url = 'https://www.google.com/finance/converter?a={}&from={}&to={}' #getting the url of the google finance converter
    url_string = currency_url.format(amount, home_currency, location_currency)

    http_url = load_page(url_string)
    if not http_url:
        return -1

    info_text = ignore_characters_at_beginning('converter_result>', http_url)       #remove text before url
    if not info_text:
        return -1

    info_text = ignore_space(info_text)                                             #remove space before url
    amount_after_conversion_text = ignore_characters_at_beginning(" = ", info_text)

    if not amount_after_conversion_text:
        return -1

    end_amount = amount_after_conversion_text.find(' ')                             #final amount after currency conversion
    return float(amount_after_conversion_text[:end_amount])


def get_details(country_name):                               # getting the country details
    outfile = open('currency_details.txt', encoding='utf-8')
    for line in outfile:
        string = [string for string in line.strip().split(',')] # separator is comma ,
        if string[0] == country_name:
            outfile.close()
            return tuple(string)                             #getting the details in tuples
    outfile.close()
    return ()


all_info_country = {}                           #getting all the details in a set


def get_all_details(country_name):               #function definition to retrive country details
    info = get_details(country_name)
    all_info_country[country_name] = info
    return all_info_country




if __name__ == '__main__':
    def currency_conversion(amount, home, location):          #currency conversion test function
        amount_after_conversion = convert(amount, home, location)
        details = "{}->{}".format(home,location)
        print_conversion_test('valid conversion', amount, details, amount_after_conversion)

        real_amount = convert(amount_after_conversion, home, location)   #original amount
        info = "{}->{}".format(home, location)
        print_conversion_test('valid conversion reverse',amount_after_conversion, info, real_amount)


    def print_conversion_test(type, amount, info, result):                 #print functiin for test currency conversion
        text = "{:>40} {:>40,.2f} {:^40} {:<40,.2f}".format(type, amount, info, result)
        print(text)


    print_conversion_test('invalid conversion', 1, 'AUD->AUD', convert(1, 'AUD', 'AUD'))            #prints invalid conversion
    print_conversion_test('invalid conversion', 1, 'JPY->ABC', convert(1, 'JPY', 'ABC'))
    print_conversion_test('invalid conversion', 1, 'ABC->USD', convert(1, 'ABC', 'USD'))
    print_conversion_test('invalid conversion', 1, 'SGD->SGD', convert(1, 'SGD', 'SGD'))

    currency_conversion(10.95, "AUD", "JPY")
    currency_conversion(10.95, "AUD", "BGN")
    currency_conversion(200.15, "BGN", "JPY")
    currency_conversion(100, "JPY", "USD")
    currency_conversion(19.99, "USD", "BGN")
    currency_conversion(19.99, "USD", "AUD")
    currency_conversion(10.95,"USD","SGD")
    currency_conversion(200.15,"SGD","AUD")


    print()


    def print_details_test(type, info, result):
        text = "{:>40} {:<40} {}".format(type, info, result)
        print(text)


    print_details_test('invalid details', 'XYZ land', get_details("XYZ land"))
    print_details_test('invalid details', 'French', get_details("French"))


    print_details_test('valid details', 'Australia', get_details("Australia"))
    print_details_test('valid details', 'China', get_details("China"))
    print_details_test('valid details', 'India', get_details("India"))
    print_details_test('valid details', 'Japan', get_details("Japan"))
    print_details_test('valid details', 'Hong Kong', get_details("Hong Kong"))
    print_details_test('valid details', 'Singapore', get_details("Singapore"))

