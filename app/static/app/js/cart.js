var updateBtns = document.getElementsByClassName("update-cart");

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('product id:', productId," action:",action);
        
        if(user === "AnonymousUser"){
            console.log('user not logged in ');
        }else{
            console.log('user logged in: ',user);
        }
    })
}
