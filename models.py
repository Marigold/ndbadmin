# This is sample models
# Note Meta() class inside model - it is define form fields for CRUD
# and templates for list/new/edit/delete operations.
# Default templates located inside /templates/admin/
# To subclass template: create a folder inside /templates/admin/
# with model name lowercase.

from google.appengine.ext import ndb

from admin import fields


class Item(ndb.Model):
    """
    Sample item model
    """
    name = ndb.StringProperty()
    description = ndb.TextProperty()

    def __unicode__(self):
    	return self.name

    def __str__(self):
    	return self.__unicode__()

    # this is where Admin CRUD form lives
    class Meta():
        def __init__(self):
            self.fields = [
                fields.TextField("name", "Name", required=True),
                fields.BigTextField("description", "Description")
            ]



class Order(ndb.Model):
	"""
	More complex mdoel
	"""
	item = ndb.KeyProperty(Item)
	is_payed = ndb.BooleanProperty()
	date_added = ndb.DateProperty()
	customer = ndb.StringProperty()
	memo = ndb.TextProperty()
	def __unicode__(self):
		return "%s ordered %s" % (self.date_added.strftime("%d %M %Y"), self.item.get())

	class Meta():
		def __init__(self):
			self.fields = [
            	fields.KeyField("item", "Item", required=True,
                    query=Item.query()),
            	fields.DateField("date_added", "Date", required=True),
            	fields.CheckboxField("is_payed", "Payed"),
                fields.TextField("customer", "Customer", required=True),
                fields.BigTextField("memo", "Memo")
            ]