frappe.ui.form.on('Test Data Item', 'submit_data', function(frm, cdt, cdn){

	var d = new frappe.ui.Dialog({
					title: __('Email Digest: '),
					width: 800
	});
	$(d.body).html("<div>Successfully Done</div>");
	d.show();
})