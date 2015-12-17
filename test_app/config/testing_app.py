from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "page",
					"name": "zpl_print-1",
					"label": _("Print ZPL"),
					"description": _("Print ZPL."),
				},
			]
		},
	]
