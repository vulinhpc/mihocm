# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Category(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		category_name: DF.Data
		notes: DF.SmallText | None
		planned_end: DF.Date | None
		planned_start: DF.Date | None
		progress_weight: DF.Float
		project: DF.Link
	# end: auto-generated types
	pass
