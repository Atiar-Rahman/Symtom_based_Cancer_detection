from django import forms

class TailwindFormMixin:
    default_classes = (
        "w-full border border-gray-300 rounded-md px-4 py-2 "
        "focus:outline-none focus:ring-2 focus:ring-rose-500"
    )

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            widget = field.widget
            placeholder = f"Enter {field.label.lower()}" if field.label else ""

            if isinstance(widget, (forms.TextInput, forms.NumberInput, forms.EmailInput)):
                widget.attrs.update({
                    "class": self.default_classes,
                    "placeholder": placeholder,
                })

            elif isinstance(widget, forms.Textarea):
                widget.attrs.update({
                    "class": f"{self.default_classes} resize-none",
                    "placeholder": placeholder,
                    "rows": 4,
                })

            elif isinstance(widget, forms.Select):
                widget.attrs.update({
                    "class": f"{self.default_classes} bg-white"
                })

            elif isinstance(widget, forms.CheckboxInput):
                widget.attrs.update({
                    "class": "form-checkbox text-rose-600 rounded focus:ring-rose-500"
                })

            elif isinstance(widget, forms.CheckboxSelectMultiple):
                widget.attrs.update({
                    "class": "space-y-2"
                })

            elif isinstance(widget, forms.SelectDateWidget):
                widget.attrs.update({
                    "class": "border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-rose-500"
                })

            else:
                widget.attrs.update({
                    "class": self.default_classes
                })
