from odoo import http
from odoo.http import request

class NationalIDApplicationController(http.Controller):
    @http.route('/submit_national_id_application', type='http', auth="public", methods=['POST'], website=True)
    def submit_application(self, **post):
        photo = post.get('photo')
        lc_reference_letter = post.get('lc_reference_letter')

        # Create a new national ID application record
        request.env['national.id.application'].sudo().create({
            'applicant_name': post.get('applicant_name'),
            'date_of_birth': post.get('date_of_birth'),
            'place_of_birth': post.get('place_of_birth'),
            'contact_number': post.get('contact_number'),
            'national_id_number': post.get('national_id_number'),
            'photo': photo.read(),
            'lc_reference_letter': lc_reference_letter.read()
        })

        return request.render('national_id.application_success')
