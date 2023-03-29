#json
import json
d={
   'course_name':'Python',
    'fees':15000
}
f=json.dumps(d)
print(f)
print(type(f))