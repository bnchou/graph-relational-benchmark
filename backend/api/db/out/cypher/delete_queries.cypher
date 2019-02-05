// DETACH Keyword deletes the Node specified
// It also deletes all relationships to and from that Node

MATCH (c: Company {name: 'Test'})
DETACH DELETE c;