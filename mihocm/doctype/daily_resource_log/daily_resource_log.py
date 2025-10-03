# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DailyResourceLog(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.mihocm.doctype.daily_resource_log_issue.daily_resource_log_issue import DailyResourceLogIssue
		from frappe.types import DF

		actual_quantity: DF.Float
		category: DF.Link
		date: DF.Date
		issues: DF.Table[DailyResourceLogIssue]
		labor_count: DF.Int
		machine_hours: DF.Float
		machine_type: DF.Data | None
		material_quantity: DF.Float
		material_type: DF.Data | None
		notes: DF.SmallText | None
		project: DF.Link
		task: DF.Link
		weather: DF.Literal["N\u1eafng", "M\u01b0a", "Kh\u00e1c"]
	# end: auto-generated types
	pass
