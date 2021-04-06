$(document).ready(function() {
//when user clicks follow button-change colour and id,
//now user can unfollow this other user
    $('#follow').click(function(){
        $(this).css('color', 'grey');
        $(this).removeAttr('id').attr('id', 'unfollow');
        $(this).text('Unfollow');
    });
    //adjust colors when know which colors used
    $('#unfollow').click(function(){
        $(this).css('color', 'red');
        $(this).removeAttr('id').attr('id', 'follow');
        $(this).text('Unfollow');
    });

//when users clicks a react button, it appears as clicked
//by the background changing to grey
    $('.reaction').click(function(){
      //obtain rection's id to manipulate the right button
        var react_type = '#'+$(this).attr('id');
        $(react_type).toggle(function(){
            $(this).css('background', 'grey');
        }, function(){
            $(this).css('background', 'none');
        });
    });
});
