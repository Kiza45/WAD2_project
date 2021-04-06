$(document).ready(
  //function updating the like count for the video on button click
    $('#like_btn').click(function(){
    //get id of the videopage
    var pageID;
    pageID = $(this).attr('data-pageid');

    //call apropriate view function and update the like count
    $.get('/hashtagtube/like_video/',
          {'page_id': pageID},
          function(data){
              $('#like_count').html(data);
          })
    });

//function updating the dislike count for the video on button click
    $('#dislike_btn').click(function(){
    //get id of the videopage
    var pageID;
    pageID = $(this).attr('data-pageid');

    //call apropriate view function and update the dislike count
    $.get('/hashtagtube/dislike_video/',
          {'page_id': pageID},
          function(data){
              $('#dislike_count').html(data);
          })
    });

//function updating the love count for the video on button click
    $('#love_btn').click(function(){
    //get id of the videopage
    var pageID;
    pageID = $(this).attr('data-pageid');

    //call apropriate view function and update the love count
    $.get('/hashtagtube/love_video/',
          {'page_id': pageID},
          function(data){
              $('#love_count').html(data);
          })
    });

//function updating the haha count for the video on button click
    $('#haha_btn').click(function(){
    //get id of the videopage
    var pageID;
    pageID = $(this).attr('data-pageid');

    //call apropriate view function and update the haha count
    $.get('/hashtagtube/haha_video/',
          {'page_id': pageID},
          function(data){
              $('#haha_count').html(data);

          })
    });

//submit the comment to the video without a page reloading
    $('#submit_comment_btn').click(function(){
      //get the id of a videopage
      var pageID;
      pageID = $(this).attr('data-pageid');

      //call the appropriate view and inform the user comment has been added
      $.get('/hashtagtube/submit_comment/',
            {'page_id': pageID},
            function(data){
              alert('Comment successfully added.');
            })
    })

//letting user follow another user profile
    $('#follow').click(function(){
      //obtain id of the user profile a user wants to follow
        var userID;
        userID = $(this).attr('data-userprofileid');

        //call the appropriate view and inform the user they have successfully followed
        //another user
        $.get('/hashtagtube/follow_unfollow/',
              {'user_profile_id': userID},
              function(data){
                alert('You successfully followed this account.');
              })
    })

//letting user unfollow another user profile
    $('#unfollow').click(function(){
      //obtain id of the user profile a user wants to follow
        var userID;
        userID = $(this).attr('data-userprofileid');

        //call the appropriate view and inform the user they have successfully followed
        //another user
        $.get('/hashtagtube/follow_unfollow/',
              {'user_profile_id': userID},
              function(data){
                alert('You successfully unfollowed this account.');
              })
    })
);
