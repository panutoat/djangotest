var addButton = document.querySelector('.add-button');
var popupContainer = document.getElementById('popup-container');
var closeButton = document.querySelector('.close');

addButton.addEventListener('click', function() {
    popupContainer.style.display = 'block'; 
});

closeButton.addEventListener('click', function() {
    popupContainer.style.display = 'none'; 
});

window.addEventListener('click', function(event) {
    if (event.target == popupContainer) {
        popupContainer.style.display = 'none'; 
    }
});



function openEditPopup(productCode, productName, productType, amount) {
    document.getElementById('edit-product-code').value = productCode;
    document.getElementById('edit-product-name').value = productName;
    document.getElementById('edit-product-type').value = productType;
    document.getElementById('edit-amount').value = amount;

    var editPopupContainer = document.getElementById('edit-popup-container');
    editPopupContainer.style.display = 'block';

    var closeButton = editPopupContainer.querySelector('.close');
    closeButton.addEventListener('click', function() {
        editPopupContainer.style.display = 'none';
    });
   
    
}