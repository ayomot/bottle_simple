$(function() {
	//classがadd-starの要素がクリックされた時の処理
	$('.add-star').click(function(){
		var $this = $(this);
		var post_id = $this.attr('data-post-id');
		$.ajax({
			url: '/star/'+post_id,
			dataType: 'json',
			success: function(data) {
				$this.text(data['star_count']);
			},
			error: function(data){
				alert('失敗しました');
			}
		});
	});
});
