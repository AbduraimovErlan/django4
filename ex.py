from jinja2 import Template

name = "федор"
tm = Template("привет{% name %}")
msg = tm.render(name=name)
print(msg)