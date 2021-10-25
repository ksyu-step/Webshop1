$(document).ready(function() {

    $('.add-to-cart-btn').click(function() {
        //
        let productId = $(this).prev().val();
        let userId = $(this).prev().prev().val();
        //
        if (userId == 'None') {
            alert('Нужно авторизоваться для использования корзины')
            window.location = '/account/entry';
        } else {
            let uid = userId;
            let pid = productId;
            $.ajax({
                url: '/orders/ajax_cart',
                data: `uid=${uid}&pid=${pid}`,
                success: function (result) {
                    alert('Товар  успешно добавлен в корзину');
                    $('#count').text(result.count);
                    $('#amount').text(`Колличество товаров: ${result.count} шт`);
                    $('#cost').text(`Общая стоимость: ${result.cost} uah`);
                }
            });
        }
    });
});