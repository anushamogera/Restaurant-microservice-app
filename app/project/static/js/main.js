$(document).ready(function(){
	$.ajax({
		url: 'http://localhost:81/Menus/all_resturant',
		type: "get",
		dataType: 'json',
		success: function (response) {
			$.each(response['response'], function (key, val) {
			   	$('.resturant-filter-box').append('<label class="checkbox"> \
					<input type="checkbox" class="filter-by-resturant" value="'+val+'">'+val+' \
				</label>');
			});
		}
	});

	$.ajax({
		url: 'http://localhost:81/Menus/all_category',
		type: "get",
		dataType: 'json',
		success: function (response) {
			$.each(response['response'], function (key, val) {
			    $('.category-filter-box').append('<label class="checkbox"> \
					<input type="checkbox" class="filter-by-category" value="'+val+'">'+val+' \
				</label>');
			});
		}
	});

	$.ajax({
		url: 'http://localhost:81/Menus/',
		type: "get",
		dataType: 'json',
		success: function (response) {
			$.each(response['response'], function (key, val) {
			        $('.hotels-list').append('<div class="list-box clearfix"> \
						<div class="pull-left-lg pull-left-md"></div> \
						<div class="pull-left-lg pull-left-md list-box-info"> \
						<h5 class="list-box-info-title"><a href="#">'+val['name']+'</a></h5> \
						<p class="list-unstyled list-inline list-box-info-tags"> '+val['description']+'</p> \
						<ul class="list-unstyled list-inline list-box-info-links"> \
							<li><i class="fa fa-tag"></i> <a href="#">'+val['resturant']+'</a></li> \
							<li><i class="fa fa-info-circle"></i> <a href="#">'+val['type']+'</a></li> \
							<li><i class="fa fa-asterisk"></i> <a href="#">'+val['category']+'</a></li> \
						</ul> \
						</div> \
						<div class="pull-right-lg pull-right-md right-col text-right text-center-sm text-center-xs"> \
							<h6 class="sub-title">'+val['price']+' €</h6> \
							<a href="#" class="btn btn-secondary animation"> Compare <i class="fa fa-chevron-right"></i></a> \
						</div> \
					</div>');
			    });
		}
	});

	$('body').on('keydown','#search-txt-box',function(event){
		if(event.keyCode==13){
			event.preventDefault();
			var value = $(this).val();
			var url ="http://localhost:81/Menus/search/"+value;
			$.ajax({
				url: url,
		    	type: "get",
		    	dataType: 'json',
		    	success: function (response) {
		    		$('.hotels-list').empty();
		    		$.each(response['response'], function (key, val) {
			        	$('.hotels-list').append('<div class="list-box clearfix"> \
							<div class="pull-left-lg pull-left-md"></div> \
							<div class="pull-left-lg pull-left-md list-box-info"> \
							<h5 class="list-box-info-title"><a href="#">'+val['name']+'</a></h5> \
							<p class="list-unstyled list-inline list-box-info-tags"> '+val['description']+'</p> \
							<ul class="list-unstyled list-inline list-box-info-links"> \
								<li><i class="fa fa-tag"></i> <a href="#">'+val['resturant']+'</a></li> \
								<li><i class="fa fa-info-circle"></i> <a href="#">'+val['type']+'</a></li> \
								<li><i class="fa fa-asterisk"></i> <a href="#">'+val['category']+'</a></li> \
							</ul> \
							</div> \
							<div class="pull-right-lg pull-right-md right-col text-right text-center-sm text-center-xs"> \
								<h6 class="sub-title">'+val['price']+' €</h6> \
								<a href="#" class="btn btn-secondary animation"> Compare <i class="fa fa-chevron-right"></i></a> \
							</div> \
						</div>');
			    	});
		    	}
			});
		}
	});

	$('body').on('click','#search-btn-box',function(event){
			event.preventDefault();
			var value = $(this).val();
			var url ="http://localhost:81/Menus/search/"+value;
			$.ajax({
				url: url,
		    	type: "get",
		    	dataType: 'json',
		    	success: function (response) {
		    		$('.hotels-list').empty();
		    		$.each(response['response'], function (key, val) {
			        	$('.hotels-list').append('<div class="list-box clearfix"> \
							<div class="pull-left-lg pull-left-md"></div> \
							<div class="pull-left-lg pull-left-md list-box-info"> \
							<h5 class="list-box-info-title"><a href="#">'+val['name']+'</a></h5> \
							<p class="list-unstyled list-inline list-box-info-tags"> '+val['description']+'</p> \
							<ul class="list-unstyled list-inline list-box-info-links"> \
								<li><i class="fa fa-tag"></i> <a href="#">'+val['resturant']+'</a></li> \
								<li><i class="fa fa-info-circle"></i> <a href="#">'+val['type']+'</a></li> \
								<li><i class="fa fa-asterisk"></i> <a href="#">'+val['category']+'</a></li> \
							</ul> \
							</div> \
							<div class="pull-right-lg pull-right-md right-col text-right text-center-sm text-center-xs"> \
								<h6 class="sub-title">'+val['price']+' €</h6> \
								<a href="#" class="btn btn-secondary animation"> Compare <i class="fa fa-chevron-right"></i></a> \
							</div> \
						</div>');
			    	});
		    	}
			});
	});

	 

	$('body').on('change','#sort_by',function(){
		var value = $(this).val();
		var url ="http://localhost:81/Menus/?order_by="+value;
		$.ajax({
			url: url,
		    type: "get",
		    dataType: 'json',
		    success: function (response) {
		    	$('.hotels-list').empty();
		    	$.each(response['response'], function (key, val) {
			        $('.hotels-list').append('<div class="list-box clearfix"> \
						<div class="pull-left-lg pull-left-md"></div> \
						<div class="pull-left-lg pull-left-md list-box-info"> \
						<h5 class="list-box-info-title"><a href="#">'+val['name']+'</a></h5> \
						<p class="list-unstyled list-inline list-box-info-tags"> '+val['description']+'</p> \
						<ul class="list-unstyled list-inline list-box-info-links"> \
							<li><i class="fa fa-tag"></i> <a href="#">'+val['resturant']+'</a></li> \
							<li><i class="fa fa-info-circle"></i> <a href="#">'+val['type']+'</a></li> \
							<li><i class="fa fa-asterisk"></i> <a href="#">'+val['category']+'</a></li> \
						</ul> \
						</div> \
						<div class="pull-right-lg pull-right-md right-col text-right text-center-sm text-center-xs"> \
							<h6 class="sub-title">'+val['price']+' €</h6> \
							<a href="#" class="btn btn-secondary animation"> Compare <i class="fa fa-chevron-right"></i></a> \
						</div> \
					</div>');
			    });
		    }
		});
	});


	$('body').on('click','.filter-by-type',function(){
		var value = $(this).val();
		$(".filter-by-type").attr("checked", false); //uncheck all checkboxes
  		$(this).attr("checked", true);  //check the clicked one
		var url =''
		if(value == 'all'){
			url ="http://localhost:81/Menus/";
		}else if(value == 'website'){
			url ="http://localhost:81/Menus/?search=type,like,"+value;
		}else if(value == 'pdf'){
			url ="http://localhost:81/Menus/?search=type,like,"+value;
		}
		$.ajax({
			url: url,
		    type: "get",
		    dataType: 'json',
		    success: function (response) {
		    	$('.hotels-list').empty();
		    	$.each(response['response'], function (key, val) {
			        $('.hotels-list').append('<div class="list-box clearfix"> \
						<div class="pull-left-lg pull-left-md"></div> \
						<div class="pull-left-lg pull-left-md list-box-info"> \
						<h5 class="list-box-info-title"><a href="#">'+val['name']+'</a></h5> \
						<p class="list-unstyled list-inline list-box-info-tags"> '+val['description']+'</p> \
						<ul class="list-unstyled list-inline list-box-info-links"> \
							<li><i class="fa fa-tag"></i> <a href="#">'+val['resturant']+'</a></li> \
							<li><i class="fa fa-info-circle"></i> <a href="#">'+val['type']+'</a></li> \
							<li><i class="fa fa-asterisk"></i> <a href="#">'+val['category']+'</a></li> \
						</ul> \
						</div> \
						<div class="pull-right-lg pull-right-md right-col text-right text-center-sm text-center-xs"> \
							<h6 class="sub-title">'+val['price']+' €</h6> \
							<a href="#" class="btn btn-secondary animation"> Compare <i class="fa fa-chevron-right"></i></a> \
						</div> \
					</div>');
			    });
		    }
		});
	});

	$('body').on('click','.filter-by-resturant',function(){
		var value = $(this).val();
		$(".filter-by-resturant").attr("checked", false); //uncheck all checkboxes
  		$(this).attr("checked", true);  //check the clicked one
		var url =''
		if(value == 'all'){
			url ="http://localhost:81/Menus/";
		}else{
			url ="http://localhost:81/Menus/?search=resturant,like,"+value;
		}
		$.ajax({
			url: url,
		    type: "get",
		    dataType: 'json',
		    success: function (response) {
		    	$('.hotels-list').empty();
		    	$.each(response['response'], function (key, val) {
			        $('.hotels-list').append('<div class="list-box clearfix"> \
						<div class="pull-left-lg pull-left-md"></div> \
						<div class="pull-left-lg pull-left-md list-box-info"> \
						<h5 class="list-box-info-title"><a href="#">'+val['name']+'</a></h5> \
						<p class="list-unstyled list-inline list-box-info-tags"> '+val['description']+'</p> \
						<ul class="list-unstyled list-inline list-box-info-links"> \
							<li><i class="fa fa-tag"></i> <a href="#">'+val['resturant']+'</a></li> \
							<li><i class="fa fa-info-circle"></i> <a href="#">'+val['type']+'</a></li> \
							<li><i class="fa fa-asterisk"></i> <a href="#">'+val['category']+'</a></li> \
						</ul> \
						</div> \
						<div class="pull-right-lg pull-right-md right-col text-right text-center-sm text-center-xs"> \
							<h6 class="sub-title">'+val['price']+' €</h6> \
							<a href="#" class="btn btn-secondary animation"> Compare <i class="fa fa-chevron-right"></i></a> \
						</div> \
					</div>');
			    });
		    }
		});
	});

	$('body').on('click','.filter-by-category',function(){
		var value = $(this).val();
		$(".filter-by-category").attr("checked", false); //uncheck all checkboxes
  		$(this).attr("checked", true);  //check the clicked one
		var url =''
		if(value == 'all'){
			url ="http://localhost:81/Menus/";
		}else{
			url ="http://localhost:81/Menus/?search=category,like,"+value;
		}
		$.ajax({
			url: url,
		    type: "get",
		    dataType: 'json',
		    success: function (response) {
		    	$('.hotels-list').empty();
		    	$.each(response['response'], function (key, val) {
			        $('.hotels-list').append('<div class="list-box clearfix"> \
						<div class="pull-left-lg pull-left-md"></div> \
						<div class="pull-left-lg pull-left-md list-box-info"> \
						<h5 class="list-box-info-title"><a href="#">'+val['name']+'</a></h5> \
						<p class="list-unstyled list-inline list-box-info-tags"> '+val['description']+'</p> \
						<ul class="list-unstyled list-inline list-box-info-links"> \
							<li><i class="fa fa-tag"></i> <a href="#">'+val['resturant']+'</a></li> \
							<li><i class="fa fa-info-circle"></i> <a href="#">'+val['type']+'</a></li> \
							<li><i class="fa fa-asterisk"></i> <a href="#">'+val['category']+'</a></li> \
						</ul> \
						</div> \
						<div class="pull-right-lg pull-right-md right-col text-right text-center-sm text-center-xs"> \
							<h6 class="sub-title">'+val['price']+' €</h6> \
							<a href="#" class="btn btn-secondary animation"> Compare <i class="fa fa-chevron-right"></i></a> \
						</div> \
					</div>');
			    });
		    }
		});
	});

	$('body').on('click','.compare-me',function(){
		var value = $(this).attr('data-name');
		var url =url ="http://localhost:81/Menus/?search=name,like,"+value;
		$.ajax({
			url: url,
		    type: "get",
		    dataType: 'json',
		    success: function (response) {
		    	$('.hotels-list').empty();
		    	$.each(response['response'], function (key, val) {
			        $('.hotels-list').append('<div class="list-box clearfix"> \
						<div class="pull-left-lg pull-left-md"></div> \
						<div class="pull-left-lg pull-left-md list-box-info"> \
						<h5 class="list-box-info-title"><a href="#">'+val['name']+'</a></h5> \
						<p class="list-unstyled list-inline list-box-info-tags"> '+val['description']+'</p> \
						<ul class="list-unstyled list-inline list-box-info-links"> \
							<li><i class="fa fa-tag"></i> <a href="#">'+val['resturant']+'</a></li> \
							<li><i class="fa fa-info-circle"></i> <a href="#">'+val['type']+'</a></li> \
							<li><i class="fa fa-asterisk"></i> <a href="#">'+val['category']+'</a></li> \
						</ul> \
						</div> \
						<div class="pull-right-lg pull-right-md right-col text-right text-center-sm text-center-xs"> \
							<h6 class="sub-title">'+val['price']+' €</h6> \
							<a href="#" class="btn btn-secondary animation"> Compare <i class="fa fa-chevron-right"></i></a> \
						</div> \
					</div>');
			    });
		    }
		});
	});

});