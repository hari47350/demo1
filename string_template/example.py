from string import Template
s = Template('$who likes $what')
print(s.substitute(who='suresh', what='ram'))


# # example 2
from string import Template

d = dict(who='suresh')

print(Template('Give $who $$100').substitute(d))

# helper function
import string

s = "   hello   world   python "
print(string.capwords(s))

