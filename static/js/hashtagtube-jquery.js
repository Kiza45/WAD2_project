$(document).ready(function() {
//when user clicks follow button-change colour and id,
//once followed, user can then unfollow aanother user
    $('#follow').click(function(){
        $(this).css('color', 'grey');
        //when unfollowing, change button's id and text to unfollow-next available state
        $(this).removeAttr('id').attr('id', 'unfollow');
        $(this).text('Unfollow');
    });

//if user follows another user, the only thing they can do is unfollow them
//hence id and text unfollow
    $('#unfollow').click(function(){
        $(this).css('color', 'red');
        //when unfollowing, change button's id and text to follow-next available state
        $(this).removeAttr('id').attr('id', 'follow');
        $(this).text('Follow');
    });

//when users clicks a react button, it appears as clicked
//by the background changing to grey
    $('.reaction').click(function(){
      //obtain rection's id to manipulate the right button
        var react_type = '#'+$(this).attr('id');
        $(react_type).toggle(function(){
          //when reaction is clicked, batton changed to a shadow/darker background
            $(this).css('background', 'grey');
        }, function(){
          //when we clicked a clicked reaction, button is changed to original(no background) state
            $(this).css('background', 'none');
        });
    });
});
