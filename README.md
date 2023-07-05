# Misk's JSP Opportunities Availability Checker

For short it just sends GET requests to the site to get all information about the job shadowing, and then I just check whatever appeals to me so the code can check their availability instead, as automation is better, and also spending time coding is better than doing manual labor, I'm doing good for people who's after automation, I suppose.

</br>

## To get your bearer auth
Ctrl+Shift+I, Network tab, and capture any request, from there scroll down until you see "Authorization:" with some text after it, select it all and then paste it, and make sure to read any code before executing it, as many Python scripts do include malicious lines.

![Result after selecting and including your authorization's:](https://github.com/Developer-Incoming/Misk-Shadowing-Program-Opportunities-Checker/assets/56730075/d4a97044-0eec-450f-a901-ca3ef438da88)

</br>
</br>

## To change opportunities from riyadh to something else
First, [Check this line of code](https://github.com/Developer-Incoming/Misk-Shadowing-Program-Opportunities-Checker/blob/main/main.py#L69), and change it to your city of choice, options are (probably case sensitive, so ctrl+c&v it exactly in **English**):
- الباحة  : `bahah`
- الجوف  : `jowf`
- الحدود الشمالية  : `northern-borders`
- الرياض  : `riyadh`
- القصيم  : `qassim`
- المدينة المنورة  : `medina`
- المنطقة الشرقية  : `eastern-province`
- تبوك  : `tabuk`
- جازان  : `jazan`
- حائل  : `hail`
- عسير  : `asir`
- مكة المكرمة  : `makkah`
- نجران  : `najran`


So, from *`https://api.jsp.elham.training/api/students/opportunities/fields/riyadh`* to *`https://api.jsp.elham.training/api/students/opportunities/fields/makkah`* as an example.

*As a fun little project for you, make it so the user inputs the city he wants instead of hardcoding it, as I forgot to implement it. And I'm now too busy celebrating my victory*

</br>
</br>

Forgot to mention you need some built-in Python 3.11.3's modules, and an extenal library called [Keyboard](https://pypi.org/project/keyboard/), to stop the program so it prints the logs if enabled, edit the code to your liking if you have trust issues or paranoid, we care less to some extent.


### **Update: it worked and after over 12 hours of continuous request per second got an IT opportunity available, surprisingly it was only 1.**
