$(document).ready(
    $('.react_btn').click(function(){
    var pageID;
    pageID = $(this).attr('data-pageid');

    var buttonID;
    buttonID = '#'+$(this).attr('id');
    var buttonCount = buttonID+'_count'

    $.get('/hashtagtube/react_video/',
          {'page_id': pageID},
          function(data){
              $(buttonCount).html(data);
              $(buttonID).hide();
          })
    });
);
