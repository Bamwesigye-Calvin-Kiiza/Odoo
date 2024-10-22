from odoo import api,models, fields
from PIL import Image
from io import BytesIO
import base64

class NationalIDApplication(models.Model):
    _name = 'national.id.application'
    _description = 'National ID Application'
    _inherit = ['mail.thread']

    applicant_name = fields.Char(string='Applicant Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    national_id_number = fields.Char(string='National ID Number', required=True)
    place_of_birth = fields.Char(string='Place of Birth', required=True)
    contact_number = fields.Char(string='Contact Number', required=True)
    photo = fields.Binary(string='Applicant Photo', attachment=True, required=True)
    lc_reference_letter = fields.Binary(string='LC Reference Letter', attachment=True, required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('stage_1', 'Stage 1 Approval'),
        ('stage_2', 'Stage 2 Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft', track_visibility='onchange')

    approved_by_stage_1 = fields.Many2one('res.users', string='Stage 1 Approved By')
    approved_by_stage_2 = fields.Many2one('res.users', string='Stage 2 Approved By')

    def action_stage_1_approval(self):
        self.write({
            'state': 'stage_1',
            'approved_by_stage_1': self.env.user.id
        })
        self.message_post(body=f"Stage 1 approved by {self.env.user.name}")

    def action_stage_2_approval(self):
        if self.state == 'stage_1':
            self.write({
                'state': 'stage_2',
                'approved_by_stage_2': self.env.user.id
            })
            self.message_post(body=f"Stage 2 approved by {self.env.user.name}")

    def action_final_approval(self):
        if self.state == 'stage_2':
            self.write({'state': 'approved'})
            self.message_post(body=f"Final approval granted by {self.env.user.name}")

    def action_reject(self):
        self.write({'state': 'rejected'})
        self.message_post(body=f"Application rejected by {self.env.user.name}")

    def _resize_image(self, image_data, size=(100, 100)):
        """Resizes the given image to the specified size"""
        # Decode the image
        image = Image.open(BytesIO(base64.b64decode(image_data)))

        # Resize the image to passport size (600x600)
        image = image.resize(size)

        # Convert it back to base64 for saving in Odoo Binary field
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        resized_image = base64.b64encode(buffer.getvalue())

        return resized_image

    @api.model
    def create(self, vals):
        """Override create to resize photo before saving"""
        if vals.get('photo'):
            vals['photo'] = self._resize_image(vals['photo'])
        return super(NationalIDApplication, self).create(vals)
