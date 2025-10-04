# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Task(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		actual_quantity: DF.Float
		assignee: DF.Link | None
		category: DF.Link
		notes: DF.SmallText | None
		planned_quantity: DF.Float
		project: DF.Link
		task_name: DF.Data
		unit: DF.Literal["m2", "m3", "t\u1ea5n", "b\u1ed9", "kg", "litre", "piece"]
	# end: auto-generated types
	pass
