/*
* This script customizes the list view for the Agency DocType.
*/

frappe.listview_settings['Agency'] = {
  // The `get_indicator` function is used to set the color of the
  // status indicator on each row in the list view.
  get_indicator: function(doc) {
    // The doc object represents a single row in the list view.
    // We check for a "falsy" value of `is_active` to determine if it's inactive.
    // This handles cases where `is_active` might be `0`, `false`, `null`, or `undefined`.
    if (!doc.is_active) {
      return [__("Inactive"), "red", "is_active,=,0"];
    }
    // If the document is active (truthy), we return a green indicator.
    return [__("Active"), "green", "is_active,=,1"];
  }
};