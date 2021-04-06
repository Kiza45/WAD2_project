$(document).ready(
    $('#like_btn').click(function(){
    var pageID;
    pageID = $(this).attr('data-pageid');

    $.get('/hashtagtube/like_video/',
          {'page_id': pageID},
          function(data){
              $('#like_count').html(data);
            //  $(buttonID).hide(); //dunno if we should hide the button
          })
    });

    $('#dislike_btn').click(function(){
    var pageID;
    pageID = $(this).attr('data-pageid');

    $.get('/hashtagtube/dislike_video/',
          {'page_id': pageID},
          function(data){
              $('#dislike_count').html(data);
            //  $(buttonID).hide(); //dunno if we should hide the button
          })
    });

    $('#love_btn').click(function(){
    var pageID;
    pageID = $(this).attr('data-pageid');

    $.get('/hashtagtube/love_video/',
          {'page_id': pageID},
          function(data){
              $('#love_count').html(data);
            //  $(buttonID).hide(); //dunno if we should hide the button
          })
    });

    $('#haha_btn').click(function(){
    var pageID;
    pageID = $(this).attr('data-pageid');

    $.get('/hashtagtube/haha_video/',
          {'page_id': pageID},
          function(data){
              $('#haha_count').html(data);
            //  $(buttonID).hide(); //dunno if we should hide the button
          })
    });

    $('#submit_comment_btn').click(function(){
      //get the id of a videopage
      var pageID;
      pageID = $(this).attr('data-pageid');

      //call the appropriate view
      $.get('/hashtagtube/submit_comment/',
            {'page_id': pageID},
            //append a new comment to the comments element of the html(is it the right way)
            function(data){
              $('#comments').append(data);
            })
    })

//need to correct when templates done
//    $('#follow').click(function(){
//    $.get('/hashtagtube/haha_video/',
//          {'page_id': pageID},
//          function(data){
//              $('#haha_count').html(data);
            //  $(buttonID).hide(); //dunno if we should hide the button
//          })
//    });
);
