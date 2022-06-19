from py2neo.ogm import Model, Property, RelatedTo
from neo4j.neo4j_database import Neo4jDatabase
from model.BC_output import BC,BCModel

class BCInstance(Model):
  name = Property()
  based_on= Property()
  narrower = RelatedTo('BCInstance', "BC_NARROWER")

  @classmethod
  def find_bc(cls, name):
    results = []
    db = Neo4jDatabase()
    query = """
    MATCH path1=(bcp:BC_INSTANCE)
    WHERE NOT ()-[:BC_NARROWER]->(bcp) AND bcp.name contains '%s'
    OPTIONAL MATCH path2=(bcp)-[r:BC_NARROWER]->(bcc:BC_INSTANCE)
    WITH path1, path2, apoc.path.combine(path1, path2) as path
    WITH collect(path) AS paths
    CALL apoc.convert.toTree(paths)
    YIELD value
     RETURN value
    """ % (name)
    items = db.graph().run(query).data()
    for item in items:
     x = dict(item['value'])
     results.append(BC(**x))
    return results
  
  @classmethod
  def list_bcs(cls):
    results = []
    db = Neo4jDatabase()
    query = """
    MATCH path1=(bcp:BC_INSTANCE)
    WHERE NOT ()-[:BC_NARROWER]->(bcp)
    OPTIONAL MATCH path2=(bcp)-[r:BC_NARROWER]->(bcc:BC_INSTANCE)
    WITH path1, path2, apoc.path.combine(path1, path2) as path
    WITH collect(path) AS paths
    CALL apoc.convert.toTree(paths)
    YIELD value
     RETURN value 
    """
    items = db.graph().run(query).data()
    for item in items:
     x = dict(item['value'])
     results.append(BC(**x))
    return results
  
