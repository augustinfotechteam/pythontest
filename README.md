# python test

1) You have two files. Each files has a list of other files. How will you write a script which will print only the files names in the first file but not the second.
Comments:
We have developed script testscript1.py Since there was not mentioned how to consider which file is first one. We have considered it based on file modify date. 
We have attached video as well for reference. So know you how it works.


2)  Find subdomain in a domain using regex. Test on regex101.com or similar https://blog.microsoft.com/test.html (blog), https://www.blog.microsoft.com/test/test (blog is the answer - www is not considered), https://www.microsoft.com (no subdomain)
Comments:
Here is a regular expression for the same. 
Regular Expression: https?:\/\/[www]*\.?([^www][\w]+)\.[^co][\w]+\..*

We have tested it with following test cases.
https://www.bb.microsoft.com
https://www.blog.microsoft.com/test/test
https://www.microsoft.com/
https://www.blog123.microsoft.com/test/test
https://www.blog123.microsoft.uk
https://www.blog123.microsoft.io
https://123blog.microsoft.co/test/test
https://nikhilesh.com/
https://doc.google.com/document/d/
https://www.microsoft.co.in/
https://microsoft.co.uk/


