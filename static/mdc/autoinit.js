'use strict';

(() => {
  mdc.autoInit();
  const setSliderHiddenField = (evt) => {
    const hidden = evt.currentTarget.querySelector('input[type="hidden"]');
    hidden.value = evt.detail.value;
  };
  for (const el of document.querySelectorAll('[data-mdc-auto-init]')) {
    switch (el.dataset.mdcAutoInit) {
      case 'MDCCheckbox':
        if (el.parentNode.MDCFormField) {
          el.parentNode.MDCFormField.input = el.MDCCheckbox;
        }
        break;
      case 'MDCRadio':
        if (el.parentNode.MDCFormField) {
          el.parentNode.MDCFormField.input = el.MDCRadio;
        }
        break;
      case 'MDCSlider':
        if (el.querySelector('input[type="hidden"]')) {
          el.addEventListener('MDCSlider:input', setSliderHiddenField, false);
        }
        break;
      // no default
    }
  }
})();
