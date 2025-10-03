# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Member(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		active: DF.Check
		project: DF.Link
		role: DF.Literal["Owner", "PM", "Engineer", "Supervisor", "QC"]
		user: DF.Link
	# end: auto-generated types
	pass
