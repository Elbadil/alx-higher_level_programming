// adds a <li> element to a list when the user clicks on the tag DIV#add_item

$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const itemsList = $('UL.my_list');
    itemsList.append('<li>Item</li>');
  });
});
