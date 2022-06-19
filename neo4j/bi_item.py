from py2neo.ogm import Model, Property, RelatedTo

class BCItem(Model):
  name = Property()
  collect= Property()
  enabled= Property() 