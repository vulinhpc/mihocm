# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Project(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address: DF.SmallText | None
		client_name: DF.Data | None
		client_phone: DF.Data | None
		cover_image: DF.AttachImage
		description: DF.TextEditor | None
		end_date: DF.Date | None
		location_map: DF.Data | None
		project_code: DF.Data | None
		project_name: DF.Data
		scale: DF.Data | None
		show_client_phone: DF.Check
		start_date: DF.Date | None
		status: DF.Literal["Draft", "In Progress", "Paused", "Completed"]
	# end: auto-generated types
	pass
