# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DailyProgressLog(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.mihocm.doctype.daily_log_photo.daily_log_photo import DailyLogPhoto
		from frappe.mihocm.doctype.daily_progress_log_task.daily_progress_log_task import DailyProgressLogTask
		from frappe.types import DF

		category: DF.Link
		date: DF.Date
		description: DF.TextEditor
		photos: DF.Table[DailyLogPhoto]
		project: DF.Link
		qc_comment: DF.SmallText | None
		qc_rating: DF.Literal["Pass", "Fail", "1", "2", "3", "4", "5"]
		shift: DF.Literal["Morning", "Afternoon", "Night"]
		status: DF.Literal["Draft", "Pending Supervisor", "Approved", "Finalized by QC"]
		task: DF.Table[DailyProgressLogTask]
	# end: auto-generated types
	pass
